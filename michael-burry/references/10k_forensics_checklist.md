# 10-K Forensics Checklist

Burry: "I read a lot of 10-Ks, 10-Qs, and proxies. I make lots of notes as I read. I don't think any edge comes from talking to management."

This checklist guides a systematic read of SEC filings with an adversarial mindset. Assume the numbers are presented in the most favorable light management can legally get away with. Your job is to find what's buried.

---

## Pre-Read Setup

**Filing to read:** 10-K (annual) + last 2 10-Qs (quarterly) + DEF 14A (proxy)
**Tools needed:** At minimum 3 years of annual filings to spot trends
**Reading order:** Read footnotes and MD&A *before* the financial statements

**Sources:**
- SEC EDGAR full-text search: `https://efts.sec.gov/LATEST/search-index?q="{company}"&dateRange=custom`
- EDGAR filing index: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={ticker}&type=10-K`

---

## Part 1: Revenue Quality

### Revenue Recognition Red Flags
- [ ] Has the company changed its revenue recognition policy in the last 3 years?
- [ ] Is revenue recognized at "point in time" or "over time" — and has this changed?
- [ ] Are there "bill-and-hold" arrangements? (revenue recognized before delivery)
- [ ] Channel stuffing indicators: revenue growing faster than distributor inventory drawdowns?
- [ ] Are returns/allowances growing as a % of gross revenue?

**Deferred Revenue Trend:**
| Year | Deferred Revenue ($M) | Change YoY |
|------|----------------------|------------|
| Y-2 | | |
| Y-1 | | |
| LTM | | |

Deferred revenue growing = good (customers paying in advance). Declining = potential revenue pull-forward.

**Days Sales Outstanding (DSO) Trend:**
```
DSO = (Accounts Receivable / Revenue) × 365
```
| Year | Revenue | AR | DSO | YoY Change |
|------|---------|-----|-----|-----------|
| Y-2 | | | | |
| Y-1 | | | | |
| LTM | | | | |

**Red flag:** DSO rising faster than revenue growth = customers paying slower = potential collection issues or channel stuffing.

---

## Part 2: Expense Quality

### Cost Capitalization
- [ ] Is the company capitalizing expenses that should be expensed? (software development, marketing, "subscriber acquisition costs")
- [ ] Has the amortization period for capitalized costs changed? (lengthening = inflating earnings)
- [ ] What % of total costs are capitalized vs. expensed? Has this ratio changed?

### Non-GAAP Adjustments
List every non-GAAP adjustment in the most recent earnings release:

| Adjustment | Amount ($M) | Recurring or one-time? | Legitimate? |
|-----------|------------|----------------------|-------------|
| Stock-based compensation | | Recurring | Questionable |
| Restructuring charges | | | |
| Acquisition-related amortization | | | |
| Other | | | |

**True earnings = GAAP Net Income − [SBC] − [other recurring "one-time" charges]**

**Burry rule:** If restructuring charges appear in 3+ consecutive years, they are not "one-time."

---

## Part 3: Balance Sheet Forensics

### Goodwill
```
Goodwill as % of total assets = ____%
Goodwill as % of equity = ____%
```
- [ ] Has goodwill been impaired? If yes: when, why, how much?
- [ ] Is goodwill growing through acquisitions while organic ROIC is declining?
- [ ] Does the management explanation for acquisition prices reconcile with actual post-acquisition performance?

**Red flag:** Goodwill > 30% of total assets with no impairments over 10 years = likely over-optimistic acquisition assumptions.

### Off-Balance-Sheet Items
- [ ] Operating lease obligations (now on-balance-sheet post-ASC 842, but check pre-2019 filings)
- [ ] Variable interest entities (VIEs) — are they consolidated? Should they be?
- [ ] Take-or-pay contracts: unconditional purchase obligations in footnotes
- [ ] Pension obligations: funded status, discount rate assumptions
- [ ] Contingent liabilities: litigation, environmental, regulatory

**Total off-balance-sheet obligations:** $______
**As % of reported total debt:** ____%

### Pension / OPEB Red Flags
- [ ] Discount rate assumption: ___% [>6% is aggressive in current rate environment]
- [ ] Expected return on plan assets: ___% [>7.5% is aggressive]
- [ ] Funded status: $___M [negative = underfunded]
- [ ] Has the company made any "catch-up" contributions? When?

---

## Part 4: Cash Flow Forensics

### FCF Reconstruction
```
Reported Operating Cash Flow:          $______
− Growth capex (est.):                 $______
+ Adjustments for working capital games: $______
= True Free Cash Flow:                 $______

FCF vs. Net Income ratio: ______x [should be close to 1.0 for quality businesses]
```

**Working Capital Trend:**
```
Working Capital = Current Assets − Current Liabilities
(or more precisely: AR + Inventory − AP)
```
| Year | AR | Inventory | AP | Net WC | WC/Revenue |
|------|-----|-----------|-----|--------|-----------|
| Y-2 | | | | | |
| Y-1 | | | | | |
| LTM | | | | | |

**Red flag:** Working capital growing as % of revenue = capital efficiency declining.

### Cash Flow Quality Ratio
```
CFO / Net Income = ____x
[Target: > 0.9x; < 0.7x for 2+ consecutive years = earnings quality concern]
```

---

## Part 5: Management and Governance Red Flags

### Proxy Statement (DEF 14A) Review
- [ ] CEO total compensation vs. FCF per share: is pay aligned with value creation?
- [ ] Are performance metrics in compensation based on easily manipulated figures (EPS, adjusted EBITDA)?
- [ ] Has the compensation committee repriced or extended underwater stock options?
- [ ] Related-party transactions: any deals between the company and entities controlled by executives?
- [ ] Board independence: what % of directors are truly independent? Are any former employees?

### Insider Transactions (Form 4)
```
Source: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={ticker}&type=4
```
- 3-year insider buy/sell ratio: ___ buys / ___ sells
- [ ] Are insiders selling aggressively while making bullish statements?
- [ ] Any unusual clustering of sales (all selling at same time)?
- [ ] Did any large insider sales precede bad news announcements?

### Auditor
- [ ] Has the auditor changed in the last 5 years? Why?
- [ ] Any "going concern" qualifications in audit opinion?
- [ ] Any "material weakness" disclosures in internal controls?
- [ ] Are audit fees growing faster than revenue? (may indicate complexity / problems)

---

## Part 6: Footnote Mining

The most important section of the 10-K. Read every footnote.

**Priority footnotes:**
1. **Revenue recognition policy** — how exactly is revenue recorded?
2. **Segment reporting** — is a struggling segment being hidden in aggregation?
3. **Debt terms** — covenants, cross-default provisions, maturity schedule
4. **Commitments and contingencies** — lawsuits, environmental, regulatory
5. **Subsequent events** — anything material happened after the reporting date?
6. **Stock-based compensation** — grant volume, vesting terms, Black-Scholes assumptions
7. **Income taxes** — effective tax rate trend, deferred tax asset/liability, valuation allowances

**Burry's "cockroach theory":** When you find one problem footnote, keep reading. They cluster.

**Footnotes flagged during this read:**
| Footnote | Issue | Materiality (H/M/L) |
|---------|-------|---------------------|
| | | |
| | | |

---

## Part 7: Disclosure Quality Assessment

- [ ] Has management provided less granular disclosure compared to prior years? (consolidating segments, reducing tables)
- [ ] Are the same metrics disclosed consistently year over year?
- [ ] Does the MD&A use the same language as the press release (copy-paste)? Or does it add genuine insight?
- [ ] Does management address the obvious investor concerns, or avoid them?
- [ ] Is the 10-K longer and more complex than peers with similar businesses?

---

## Summary: Red Flag Tally

| Category | Flags Found | Severity (H/M/L) |
|----------|------------|------------------|
| Revenue quality | | |
| Expense quality / non-GAAP | | |
| Balance sheet (goodwill, off-B/S) | | |
| Cash flow quality | | |
| Management / governance | | |
| Footnotes | | |
| Disclosure quality | | |
| **Total** | | |

**Thesis impact:**
- 0–2 flags, all Low: Normal business complexity. Proceed with standard analysis.
- 3–5 flags, mixed: Elevated scrutiny required. Validate each flag before committing.
- 6+ flags or any High: Serious quality concern. Either short thesis or avoid entirely.

**Burry rule:** If you found something that surprised you, there is almost certainly more. Keep reading.
