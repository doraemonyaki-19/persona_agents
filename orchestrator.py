"""
Board Meeting Orchestrator for Personas.

Convenes a virtual board meeting by loading persona SKILL.md files and
reference materials, gathering live market data, and producing a structured
board meeting transcript in board_meetings/.

Usage:
  python orchestrator.py "Evaluate NVDA ahead of Q1 earnings"
  python orchestrator.py "Should we add gold to the portfolio?" --roster buffett,munger,simons
  python orchestrator.py "Review TimesFM paper trade results" --chair feynman
  python orchestrator.py list                    # list all personas
  python orchestrator.py meetings                # list past meetings

The orchestrator produces a prompt package (system prompt + persona
definitions + research context + topic) that can be fed to Claude or
another LLM to generate the board meeting transcript.
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# ── Persona registry ─────────────────────────────────────────────────────

PERSONAS = {
  "buffett":     {"dir": "warren-buffett",      "name": "Warren Buffett",      "role": "Chair (default)"},
  "munger":      {"dir": "charlie-munger",       "name": "Charlie Munger",      "role": "Vice Chair"},
  "burry":       {"dir": "michael-burry",        "name": "Michael Burry",       "role": "Contrarian Forensics"},
  "simons":      {"dir": "jim-simons",           "name": "Jim Simons",          "role": "Quantitative Analysis"},
  "feynman":     {"dir": "richard-feynman",      "name": "Richard Feynman",     "role": "First Principles"},
  "kurzweil":    {"dir": "ray-kurzweil",         "name": "Ray Kurzweil",        "role": "Exponential Trends"},
  "stephenson":  {"dir": "neal-stephenson",      "name": "Neal Stephenson",     "role": "Infrastructure & Geopolitics"},
  "oppenheimer": {"dir": "robert-oppenheimer",   "name": "Robert Oppenheimer",  "role": "Tail Risk & Moral Weight"},
  "brin":        {"dir": "david-brin",           "name": "David Brin",          "role": "Transparency & Accountability"},
  "jobs":        {"dir": "steve-jobs",           "name": "Steve Jobs",          "role": "Product & Experience"},
}

DEFAULT_ROSTER = list(PERSONAS.keys())


def load_persona(key: str) -> dict:
  """Load a persona's SKILL.md and reference files."""
  info = PERSONAS[key]
  persona_dir = ROOT / info["dir"]
  skill_path = persona_dir / "SKILL.md"
  refs_dir = persona_dir / "references"

  result = {
    "key": key,
    "name": info["name"],
    "role": info["role"],
    "skill": "",
    "references": {},
  }

  if skill_path.exists():
    result["skill"] = skill_path.read_text(encoding="utf-8")

  if refs_dir.is_dir():
    for ref_file in sorted(refs_dir.glob("*.md")):
      result["references"][ref_file.name] = ref_file.read_text(encoding="utf-8")

  return result


def build_roster_section(personas: list[dict]) -> str:
  """Build the roster block for the prompt."""
  lines = ["## Board Roster\n"]
  for p in personas:
    ref_list = ", ".join(p["references"].keys()) if p["references"] else "none"
    lines.append(f"- **{p['name']}** ({p['role']}) — refs: {ref_list}")
  return "\n".join(lines)


def build_persona_definitions(personas: list[dict]) -> str:
  """Build full persona definition blocks."""
  sections = []
  for p in personas:
    sections.append(f"# === {p['name']} ({p['role']}) ===\n")
    sections.append(p["skill"])
    sections.append("")
    for ref_name, ref_content in p["references"].items():
      sections.append(f"## Reference: {ref_name}\n")
      sections.append(ref_content)
      sections.append("")
  return "\n".join(sections)


def build_system_prompt(topic: str, chair: str, personas: list[dict],
                        context: str = "") -> str:
  """Build the complete system prompt for the board meeting."""
  today = datetime.date.today().strftime("%B %d, %Y")
  chair_name = next((p["name"] for p in personas if p["key"] == chair),
                    personas[0]["name"])
  roster_names = ", ".join(p["name"] for p in personas)

  prompt = textwrap.dedent(f"""\
    # Board Meeting — {today}

    **Topic:** {topic}
    **Chair:** {chair_name}
    **Present:** {roster_names}

    ## Instructions

    You are orchestrating a board meeting among the personas listed below.
    Generate a structured transcript where each persona speaks in character,
    applying their specific analytical framework and referencing their tools
    (checklists, calculators, etc.) where relevant.

    Rules:
    1. Every persona MUST use <thinking> tags with a <biographical_anchor>
       before delivering their analysis. This is mandatory, not optional.
    2. The Chair opens the meeting with the topic framing and key facts.
    3. Each persona must speak at least once. Do not silently drop anyone.
    4. Personas should directly challenge, agree with, or build on each
       other's points — this is a debate, not a series of monologues.
    5. All numeric claims must be grounded in the research context provided.
       Do NOT fabricate financial data. If data is missing, say so.
    6. The meeting should conclude with:
       a. A summary of areas of agreement
       b. A summary of unresolved disagreements
       c. Concrete action items or next steps
    7. Use the persona's actual tone and style — Buffett is folksy, Munger
       is blunt, Burry is terse, Simons is mathematical, Feynman is
       plainspoken, etc.

    ## Format

    ```
    # Board Meeting: [Title]

    **Date:** {today}
    **Topic:** {topic}
    **Chair:** {chair_name}
    **Present:** {roster_names}

    ---

    **{chair_name.upper()}:**
    <thinking>
    <biographical_anchor>...</biographical_anchor>
    ...
    </thinking>

    [Opening remarks and framing]

    **[NEXT PERSONA]:**
    <thinking>
    <biographical_anchor>...</biographical_anchor>
    ...
    </thinking>

    [Response]

    ... [continue for all personas] ...

    ---

    ## Summary & Action Items

    ### Areas of Agreement
    - ...

    ### Unresolved Disagreements
    - ...

    ### Action Items
    - ...

    ---

    ## Sources
    - [url1]
    - [url2]
    ```
  """)

  if context:
    prompt += f"\n## Research Context\n\n{context}\n"

  prompt += f"\n{build_roster_section(personas)}\n"

  return prompt


def slugify(text: str) -> str:
  """Convert topic text to a filename slug."""
  text = text.lower().strip()
  text = re.sub(r"[^a-z0-9\s-]", "", text)
  text = re.sub(r"[\s-]+", "_", text)
  return text[:60]


def cmd_run(args):
  """Generate a board meeting prompt package."""
  topic = args.topic

  # Parse roster
  if args.roster:
    roster_keys = [k.strip().lower() for k in args.roster.split(",")]
    for k in roster_keys:
      if k not in PERSONAS:
        print(f"ERROR: Unknown persona '{k}'. Available: {', '.join(PERSONAS.keys())}")
        sys.exit(1)
  else:
    roster_keys = DEFAULT_ROSTER

  # Parse chair
  chair = args.chair or roster_keys[0]
  if chair not in roster_keys:
    roster_keys.insert(0, chair)

  # Load personas
  print(f"Loading {len(roster_keys)} personas...")
  personas = []
  for k in roster_keys:
    p = load_persona(k)
    personas.append(p)
    n_refs = len(p["references"])
    print(f"  {p['name']:.<30} SKILL.md + {n_refs} references")

  # Build context placeholder (user can pipe in research)
  context = ""
  if args.context_file:
    ctx_path = Path(args.context_file)
    if ctx_path.exists():
      context = ctx_path.read_text(encoding="utf-8")
      print(f"Loaded context from {ctx_path} ({len(context)} chars)")
    else:
      print(f"WARNING: Context file {ctx_path} not found, proceeding without.")

  # Build the prompt
  system_prompt = build_system_prompt(topic, chair, personas, context)
  persona_defs = build_persona_definitions(personas)

  # Output
  today = datetime.date.today().isoformat()
  slug = slugify(topic)
  out_dir = ROOT / "board_meetings"
  out_dir.mkdir(exist_ok=True)

  if args.output == "prompt":
    # Write the full prompt package to a file for manual use
    prompt_path = out_dir / f"{slug}_{today}_prompt.md"
    full_prompt = system_prompt + "\n---\n\n" + persona_defs
    prompt_path.write_text(full_prompt, encoding="utf-8")
    print(f"\nPrompt package saved to: {prompt_path}")
    print(f"Total size: {len(full_prompt):,} chars")
    print(f"\nTo run the meeting, feed this prompt to Claude with:")
    print(f'  cat "{prompt_path}" | claude --print')

  elif args.output == "json":
    # Write structured JSON for programmatic use
    json_path = out_dir / f"{slug}_{today}_prompt.json"
    package = {
      "date": today,
      "topic": topic,
      "chair": chair,
      "roster": roster_keys,
      "system_prompt": system_prompt,
      "persona_definitions": {p["key"]: {
        "name": p["name"],
        "role": p["role"],
        "skill": p["skill"],
        "references": p["references"],
      } for p in personas},
      "context": context,
    }
    json_path.write_text(json.dumps(package, indent=2, ensure_ascii=False),
                         encoding="utf-8")
    print(f"\nJSON prompt package saved to: {json_path}")

  elif args.output == "stdout":
    # Print to stdout for piping
    full_prompt = system_prompt + "\n---\n\n" + persona_defs
    print(full_prompt)

  # Print summary
  if args.output != "stdout":
    print(f"\n{'=' * 60}")
    print(f"Board Meeting: {topic}")
    print(f"Date: {today}")
    print(f"Chair: {next(p['name'] for p in personas if p['key'] == chair)}")
    print(f"Roster: {', '.join(p['name'] for p in personas)}")
    print(f"{'=' * 60}")


def cmd_list(args):
  """List all available personas."""
  print(f"{'Key':<14} {'Name':<24} {'Role':<30} {'Refs':>4}")
  print("-" * 76)
  for key, info in PERSONAS.items():
    persona_dir = ROOT / info["dir"]
    refs_dir = persona_dir / "references"
    n_refs = len(list(refs_dir.glob("*.md"))) if refs_dir.is_dir() else 0
    skill_ok = "ok" if (persona_dir / "SKILL.md").exists() else "MISSING"
    print(f"{key:<14} {info['name']:<24} {info['role']:<30} {n_refs:>4}  [{skill_ok}]")


def cmd_meetings(args):
  """List past board meetings."""
  meetings_dir = ROOT / "board_meetings"
  if not meetings_dir.is_dir():
    print("No board_meetings/ directory found.")
    return

  files = sorted(meetings_dir.glob("*.md"))
  if not files:
    print("No board meetings found.")
    return

  print(f"{'File':<55} {'Size':>8}")
  print("-" * 65)
  for f in files:
    if f.name.endswith("_prompt.md"):
      continue  # skip prompt packages
    size = f.stat().st_size
    print(f"{f.name:<55} {size:>7,}")


def main():
  parser = argparse.ArgumentParser(
    description="Board Meeting Orchestrator for Personas",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent("""\
      Examples:
        python orchestrator.py "Evaluate NVDA ahead of Q1 earnings"
        python orchestrator.py "Review gold allocation" --roster buffett,munger,simons,burry
        python orchestrator.py "TimesFM paper trade review" --chair simons --output json
        python orchestrator.py list
        python orchestrator.py meetings
    """))

  subparsers = parser.add_subparsers(dest="command")

  # Default: run a meeting (also accessible without subcommand)
  p_run = subparsers.add_parser("run", help="Generate a board meeting prompt")
  p_run.add_argument("topic", help="The topic/question for the board meeting")
  p_run.add_argument("--roster", default=None,
                     help="Comma-separated persona keys (default: all 10)")
  p_run.add_argument("--chair", default=None,
                     help="Persona key for meeting chair (default: first in roster)")
  p_run.add_argument("--context-file", default=None,
                     help="Path to a file with research context to include")
  p_run.add_argument("--output", choices=["prompt", "json", "stdout"],
                     default="prompt",
                     help="Output format (default: prompt markdown file)")
  p_run.set_defaults(func=cmd_run)

  p_list = subparsers.add_parser("list", help="List available personas")
  p_list.set_defaults(func=cmd_list)

  p_meetings = subparsers.add_parser("meetings", help="List past board meetings")
  p_meetings.set_defaults(func=cmd_meetings)

  args = parser.parse_args()

  # Handle positional topic without subcommand
  if args.command is None:
    if len(sys.argv) > 1 and sys.argv[1] not in ("list", "meetings", "run", "-h", "--help"):
      # Treat first arg as topic for a quick run
      args.topic = sys.argv[1]
      args.roster = None
      args.chair = None
      args.context_file = None
      args.output = "prompt"
      cmd_run(args)
    else:
      parser.print_help()
    return

  args.func(args)


if __name__ == "__main__":
  main()
