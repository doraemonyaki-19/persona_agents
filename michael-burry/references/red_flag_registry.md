# Red Flag Registry

A curated list of warning patterns drawn from Burry's documented investment process and from post-mortems of major corporate failures he has studied or been involved with. Each flag is a trigger for deeper investigation — not necessarily a sell signal, but never to be ignored.

---

## Category 1: Earnings Quality Flags

### EQ-1: FCF / Net Income < 0.7 for 2+ consecutive years
Earnings that don't convert to cash are suspect. Possible causes: aggressive revenue recognition, capitalized expenses, working capital deterioration.
**Action:** Reconstruct FCF. Identify the specific divergence source.

### EQ-2: Non-GAAP adjustments > 20% of GAAP earnings
The gap between what management presents and what GAAP shows is a measure of how hard they're working to look better than reality.
**Action:** Classify every adjustment as recurring vs. one-time. Penalize recurring "one-time" charges.

### EQ-3: Restructuring charges in 3+ consecutive years
By definition, not one-time. A restructuring program that runs for years is either a permanent cost of the business model or a systematic earnings management tool.
**Action:** Capitalize and amortize, or treat as recurring operating expense.

### EQ-4: Stock-based compensation > 10% of revenue
At this level, SBC is a primary form of compensation, not an incidental benefit. GAAP earnings dramatically overstate true profitability.
**Action:** Deduct SBC from all earnings metrics as if it were cash compensation.

### EQ-5: Gross margin declining while volume grows
Normally, scale should preserve or expand gross margin. Declining gross margin at higher volume signals pricing pressure, input cost escalation, or mix shift toward lower-quality revenue.
**Action:** Disaggregate by product line/geography. Find which segment is deteriorating.

### EQ-6: Revenue growth from acquisitions masking organic decline
Companies nearing organic stagnation often accelerate acquisition activity to show revenue growth. Total revenue grows; organic revenue is flat or negative.
**Action:** Strip acquisitions from reported revenue. Calculate organic growth rate. If negative for 2+ years, the core business is in decline.

---

## Category 2: Balance Sheet Flags

### BS-1: Goodwill > 30% of total assets
Indicates serial acquirer paying large premiums. If goodwill is never impaired across a full business cycle, management is likely using optimistic assumptions in impairment tests.
**Action:** Compare goodwill to cumulative acquisition premiums paid. Assess whether acquired businesses earned their cost of capital post-acquisition.

### BS-2: Inventory / Revenue rising
Inventory growing faster than revenue = either build-up ahead of demand that may not materialize, or inability to sell at current prices (write-down risk ahead).
**Action:** Check inventory composition (raw materials vs. finished goods). Compare to competitor inventory ratios.

### BS-3: Accounts Receivable / Revenue rising (DSO expansion)
Customers paying slower = collection risk or channel stuffing. Burry specifically flagged this in pre-crisis mortgage servicer analysis.
**Action:** Check credit quality of the AR. Is the company extending payment terms to accelerate revenue recognition?

### BS-4: Off-balance-sheet obligations > 20% of reported debt
Operating leases, take-or-pay contracts, pension deficits, VIE liabilities — if these are material and excluded from leverage calculations, the reported debt/EBITDA is misleading.
**Action:** Add all identified off-balance-sheet obligations to reported debt. Recalculate leverage ratios.

### BS-5: Negative tangible book value
If goodwill and intangibles are stripped out and equity goes negative, the business has no asset-based floor to valuation. In a stress scenario, there is no asset base to protect the equity holder.
**Action:** Calculate tangible book value = Total equity − Goodwill − Other intangibles. If negative, understand why and whether it's sustainable.

### BS-6: Debt maturity concentration in < 2 years
Refinancing risk. If a large portion of debt matures soon and credit markets tighten or the company's credit quality deteriorates, refinancing may be impossible or punishingly expensive.
**Action:** Pull the full debt maturity schedule from footnotes. Map against projected FCF. Calculate the refinancing gap.

---

## Category 3: Revenue / Business Model Flags

### BM-1: Revenue concentrated in < 3 customers
Single-customer concentration creates binary outcomes. Loss of one customer could be existential.
**Action:** Check % of revenue from top customers (disclosed or estimable). Assess switching cost / contract length.

### BM-2: Subscription/recurring revenue % declining
For businesses valued on recurring revenue, any deterioration in this metric is a structural concern, not a one-quarter event.
**Action:** Track Net Revenue Retention and gross churn separately. Disaggregate new logo growth from existing customer expansion.

### BM-3: Unit economics degrading at scale
If customer acquisition cost (CAC) is rising while lifetime value (LTV) is flat or falling, the growth engine is running on subsidy, not genuine value creation.
**Action:** Reconstruct implied CAC and LTV from available disclosures (S&M spend per new customer, cohort retention).

### BM-4: Regulatory revenue > 30% of total
Revenue heavily dependent on government contracts, subsidies, or favorable regulation is fragile. Policy changes can eliminate it overnight.
**Action:** Scenario-test the business without the regulatory revenue/subsidy. Does it earn a positive return?

---

## Category 4: Management and Governance Flags

### MG-1: Insider selling > buying by 10:1 ratio (3-year basis)
Executives collectively selling far more than they're buying is a directional signal. They know the business better than any outside analyst.
**Action:** Decompose sales: planned (10b5-1 plans) vs. discretionary. Planned is less informative; discretionary is significant.

### MG-2: CEO/CFO turnover > once in 5 years
Frequent turnover, especially at the CFO level, suggests internal problems the board is managing.
**Action:** Research departure circumstances. "To pursue other opportunities" after < 3 years is a red flag phrase.

### MG-3: Auditor change without explanation
Auditor changes are unusual. The most common reasons: fee dispute (benign) or accounting disagreement (not benign).
**Action:** Read the 8-K filed when the auditor changed. Is there a disclosed disagreement? Check new auditor's reputation for leniency.

### MG-4: Compensation tied to non-FCF metrics
If executives are paid on revenue, EBITDA, adjusted EPS, or total shareholder return versus a peer group — all metrics that can be managed or gamed — incentives are misaligned.
**Action:** Read the compensation discussion in the proxy. What would a perfectly rational, self-interested CEO do to maximize their bonus? Does that align with long-term shareholder value?

### MG-5: Related-party transactions
Any business dealings between the company and entities controlled by executives or board members are conflicts of interest until proven otherwise.
**Action:** Read all related-party disclosures in the proxy and 10-K footnotes. Assess whether terms are arms-length.

---

## Category 5: Macro / Structural Flags (Burry's Systemic Risk Framework)

### SR-1: Valuation dependent on continued low interest rates
Businesses with no current earnings valued on long-dated DCFs are extremely sensitive to discount rate changes. A 2% rise in rates can cut intrinsic value by 30–50%.
**Action:** Stress-test the DCF with rates 200–300bps higher. If intrinsic value falls below current price, the business is implicitly a rates bet.

### SR-2: Asset prices disconnected from cash flow fundamentals
Burry's subprime insight: when prices rise because of credit availability rather than cash flow growth, the price rise is fragile. The credit can disappear; the fundamentals cannot.
**Action:** Calculate cash flow yield. Compare to historical norms. If the gap is explained only by "lower rates / multiple expansion," be skeptical of sustainability.

### SR-3: Passive flow distortion
Burry's 2019 thesis: passive index investing creates forced buyers regardless of price. Securities with high index weights become systematically overvalued relative to fundamentals.
**Action:** Check index weight. Is a significant portion of the float owned by passive vehicles? How does the stock behave around index rebalancing dates?

### SR-4: Leverage in the system, not just the company
Sometimes the risk is not on the company's balance sheet but in the hands of its customers, suppliers, or financing counterparties.
**Action:** Map the full ecosystem. Who is levered? What happens to this business if a key counterparty is forced to deleverage?

---

## Flag Tally and Severity Rating

| Flag ID | Description | Present? | Severity (H/M/L) | Investigated? |
|---------|-------------|----------|-----------------|---------------|
| EQ-1 | FCF/NI < 0.7 | | | |
| EQ-2 | Non-GAAP > 20% | | | |
| EQ-3 | Restructuring 3+ yrs | | | |
| EQ-4 | SBC > 10% revenue | | | |
| EQ-5 | Gross margin declining | | | |
| EQ-6 | Organic decline hidden | | | |
| BS-1 | Goodwill > 30% assets | | | |
| BS-2 | Inventory/Revenue rising | | | |
| BS-3 | DSO expansion | | | |
| BS-4 | Off-B/S > 20% debt | | | |
| BS-5 | Negative tangible BV | | | |
| BS-6 | Debt maturity < 2 yrs | | | |
| BM-1 | Customer concentration | | | |
| BM-2 | Recurring revenue declining | | | |
| BM-3 | Unit economics degrading | | | |
| BM-4 | Regulatory revenue > 30% | | | |
| MG-1 | Insider selling 10:1 | | | |
| MG-2 | Mgmt turnover > 1/5yr | | | |
| MG-3 | Auditor change | | | |
| MG-4 | Non-FCF compensation | | | |
| MG-5 | Related-party transactions | | | |
| SR-1 | Rates-dependent valuation | | | |
| SR-2 | Price/CF disconnect | | | |
| SR-3 | Passive flow distortion | | | |
| SR-4 | System leverage | | | |

**Total High flags:** ___
**Total Medium flags:** ___
**Total Low flags:** ___

**Decision threshold:**
- 0 High, ≤3 Medium: Normal due diligence. Proceed.
- 1–2 High, or >3 Medium: Elevated risk. Each High flag must be fully investigated and resolved before committing capital.
- 3+ High: Short thesis or hard pass. The probability of a negative surprise is too high for a long position.
