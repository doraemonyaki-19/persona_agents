# FCF Reconstruction Template

Burry: "Free cash flow is real; earnings are an opinion."

Reported earnings are the output of hundreds of accounting choices. Reported operating cash flow is better but still manipulable. This template reconstructs the truest possible measure of what the business generates for its owners, independent of accounting presentation.

---

## Step 1: Start with Reported Figures

Pull from the Cash Flow Statement (not the income statement):

| Item | Year -2 | Year -1 | LTM |
|------|---------|---------|-----|
| Net Income (GAAP) | | | |
| + D&A | | | |
| + Other non-cash (SBC, impairments, etc.) | | | |
| ± Change in Working Capital | | | |
| **= Cash from Operations (reported)** | | | |
| − Total Capex | | | |
| **= Reported Free Cash Flow** | | | |

---

## Step 2: Adjustments to Arrive at True Owner FCF

### 2a. Working Capital Normalization

Working capital changes are volatile and can be managed. Normalize by using average WC/Revenue ratio:

```
Normalized WC Change = (Target WC/Revenue − Current WC/Revenue) × Revenue

Target WC/Revenue = 3-year average (if no manipulation evidence)
                  = Industry median (if manipulation is suspected)
```

| Year | Reported ΔWC | Normalized ΔWC | Adjustment |
|------|-------------|---------------|-----------|
| Y-2 | | | |
| Y-1 | | | |
| LTM | | | |

### 2b. Capex Split: Maintenance vs. Growth

This is the hardest number. Methods:

**Method 1 — Management disclosure** (only if they explicitly break it out in MD&A):
- Maintenance capex (stated): $______
- Growth capex (stated): $______

**Method 2 — Recession year proxy** (most reliable):
- Find the year when revenue was flat or declining (growth ≈ 0)
- Capex in that year ≈ maintenance capex (no growth investment needed)
- Recession year capex: $______ (Year: ______)
- Adjust for inflation to current year: × ____

**Method 3 — D&A proxy** (rough):
- For asset-light businesses: Maintenance capex ≈ D&A × 0.5–0.7
- For asset-heavy businesses: Maintenance capex ≈ D&A × 0.9–1.1

**Method 4 — Gross PP&E growth** (accounting-based):
```
If all capex were maintenance: Gross PP&E would be flat (new capex replaces depreciated assets)
Growth capex ≈ ΔGross PP&E (after adjusting for disposals)
Maintenance capex ≈ Total capex − Growth capex
```

**Chosen method:** ______
**Estimated maintenance capex:** $______/year
**Growth capex (excluded from owner FCF):** $______/year

### 2c. Stock-Based Compensation Adjustment

SBC is real economic dilution even if non-cash. Two views:

**Conservative (Burry's preference):** treat SBC as a full cash expense
```
Adjusted FCF = FCF (after adding back SBC) − SBC expense
Net adjustment: $0 (SBC was already added back in CFO and should be subtracted)
```

**Moderate view:** SBC for options that are genuinely out-of-the-money can be excluded
```
Economic SBC ≈ in-the-money options + restricted stock grants × current price
```

**SBC as % of revenue:** ____%  [> 5% is high; > 10% is a real issue]
**Dilution from SBC (share count growth ex-buybacks):** ____%/year

### 2d. Capitalized Software / R&D Adjustment

If the company capitalizes software development costs:
```
Capitalized amount (from footnotes):     $______
Amortization of prior-period capitalized: $______
Net P&L benefit from capitalization:     $______ [adds to earnings, should be backed out]
```

True R&D expense = Cash R&D spending (reported) + Net capitalization benefit

### 2e. Pension Adjustment

If defined benefit pension plan exists:
```
Pension service cost (income statement):  $______
Pension cash contribution (cash flow):    $______
Adjustment needed:                        $______ [use cash if higher than service cost]
```

### 2f. One-Time Items (Evaluate Each Individually)

List every "one-time" charge in CFO over the last 3 years:

| Item | Year | Amount | Truly one-time? |
|------|------|--------|----------------|
| Restructuring | | | |
| Legal settlements | | | |
| Acquisition costs | | | |
| Other | | | |

**If "one-time" items appear 3+ years in a row: they are recurring.** Treat as ongoing.

---

## Step 3: Normalized Owner FCF

| Adjustment | Annual Amount |
|-----------|--------------|
| Reported CFO | |
| − True maintenance capex | |
| − SBC (if treating as cash expense) | |
| − Capitalized R&D net benefit | |
| ± Normalized WC adjustment | |
| ± Pension cash vs. service cost | |
| − Other recurring "one-time" items | |
| **= Normalized Owner FCF** | |

**5-year average Normalized Owner FCF:** $______
**Current market cap:** $______
**Owner FCF Yield:** ____%
**True P/FCF Multiple:** ___x

---

## Step 4: FCF Quality Score

| Metric | Value | Signal |
|--------|-------|--------|
| CFO / Net Income | ___x | [>0.9 = good; <0.7 = concern] |
| FCF Conversion (FCF / EBITDA) | ___% | [>50% = healthy] |
| FCF growth vs. Revenue growth | | [should be roughly equal or higher] |
| SBC as % of FCF | ___% | [>20% = material dilution] |
| Maintenance capex / D&A | ___x | [should be ~1.0 for stable businesses] |
| DSO trend | | [rising = concern] |
| WC / Revenue trend | | [rising = capital efficiency declining] |

**FCF Quality Rating:** High / Medium / Low

---

## Step 5: Variant Perception — Why Is the Market Wrong?

Burry's key question: if you've done all this work and found the business generates more (or less) FCF than the market believes, articulate the specific reason:

**Market believes:** $______ in FCF (implied by multiple × consensus earnings)
**True FCF:** $______ (your reconstruction)
**Gap:** $______ (___%)

**Why the gap exists:**
- [ ] Market using reported earnings, not normalizing for [specific item]
- [ ] Market unaware of [specific off-balance-sheet item]
- [ ] Consensus models using aggressive [revenue/cost] assumption
- [ ] Market capitulating on short-term headwinds that obscure normalized earning power
- [ ] Other: _______

**This gap closes when:**
_______

**Catalyst for repricing:**
_______
