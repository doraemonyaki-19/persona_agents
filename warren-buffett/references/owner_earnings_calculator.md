# Owner Earnings Calculator

Source: Buffett, 1986 Berkshire Annual Letter. The definitive measure of what a business earns for its owners — distinct from accounting earnings.

---

## Formula

```
Owner Earnings =
  Net Income
  + Depreciation & Amortization
  + Other non-cash charges (e.g., stock-based comp if truly non-economic)
  − Maintenance Capex (estimated)
  − Additional Working Capital required for growth (if any)
```

**Maintenance Capex** = capex required to maintain the existing competitive position at current volume. NOT total reported capex (which includes growth capex). This is the hardest number to pin down — management rarely discloses it separately.

**Estimating Maintenance Capex:**
- For asset-light businesses: often ≈ D&A × 0.5–0.8
- For asset-heavy businesses: ask management; cross-check with capex during recession years (when growth was zero)
- Sanity check: over 10 years, cumulative capex should roughly match cumulative D&A if growth was modest

---

## Worksheet

### Step 1: Collect 5-Year Averages (reduces single-year noise)

| Line Item | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 5Y Avg |
|-----------|--------|--------|--------|--------|--------|--------|
| Net Income | | | | | | |
| + D&A | | | | | | |
| − Maintenance Capex (est.) | | | | | | |
| − ΔWorking Capital | | | | | | |
| **= Owner Earnings** | | | | | | |

### Step 2: Normalize for Unusual Items

Remove or adjust:
- [ ] Litigation settlements (one-time)
- [ ] Restructuring charges
- [ ] Impairment charges (unless recurring = a business problem)
- [ ] Gain/loss on asset sales
- [ ] Mark-to-market swings (unrealized)
- [ ] Tax rate changes or one-time tax events
- [ ] Acquisition-related amortization (add back — not a real cash cost)

**Normalized Owner Earnings = $_______**

### Step 3: Yield and Valuation

```
Owner Earnings Yield = Normalized Owner Earnings / Market Cap
Implied P/OE Multiple = Market Cap / Normalized Owner Earnings

At current price, what growth rate is required to justify the multiple?
  Required growth ≈ (Discount Rate − Owner Earnings Yield)
  Use 10-year Treasury + 5–7% equity risk premium as discount rate
```

| | Value |
|--|--|
| Market Cap | |
| Normalized Owner Earnings | |
| Owner Earnings Yield | |
| P/OE Multiple | |
| 10Y Treasury Rate | |
| Discount Rate (used) | |
| Required growth to justify price | |
| My base case growth estimate | |
| Margin of safety (base − required) | |

### Step 4: Intrinsic Value Estimate

Simple DCF on owner earnings (Buffett's preferred approach: no terminal multiple, just perpetuity):

```
Intrinsic Value = Owner Earnings × (1 + g) / (r − g)

  g = sustainable long-term growth rate (conservative: GDP ≈ 2–3%)
  r = required return (10–12% for equities)
```

**Bear case** (g = 0%): IV = OE / r = $______
**Base case** (g = 3%): IV = OE × 1.03 / (r − 0.03) = $______
**Bull case** (g = 5%): IV = OE × 1.05 / (r − 0.05) = $______

**Current Price: $______**
**Margin of Safety vs. Base Case: ______%**

Buffett rule of thumb: require at least 25–30% margin of safety before buying.

---

## Common Mistakes

- **Using reported capex as maintenance capex** — overstates the true maintenance burden for growing businesses; understates it for declining ones
- **Using 1-year net income** — single year earnings are volatile; always normalize over a cycle
- **Ignoring working capital changes** — fast-growing businesses consume significant working capital; this is a real cash cost
- **Treating stock-based compensation as truly non-cash** — employees are real economic claimants; SBC should generally be treated as a cash expense
- **Applying a terminal multiple** — Buffett prefers not to assume a sale price; value as a perpetuity instead

---

## WebFetch Usage

To pull financial data for this calculation:
- SEC 10-K: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={ticker}&type=10-K`
- Cash flow statement (primary source for D&A, capex, working capital)
- Look for management commentary on "maintenance vs. growth capex" in MD&A section
