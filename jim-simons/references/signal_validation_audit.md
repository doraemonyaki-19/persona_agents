# Signal Validation Audit

Simons: "We search through historical data looking for anomalous patterns that we would not expect to occur at random."

A signal is a repeatable, statistically demonstrable relationship between observable inputs and future returns. This audit is the gate between "interesting pattern I found" and "tradeable edge." Most patterns fail this audit. That is the correct outcome — false positives destroy capital.

---

## Stage 0: Pre-Audit — Define the Signal Precisely

Before any testing, write the signal definition in one sentence that could be handed to a programmer:

**Signal definition:**
> "When [observable condition X] is true at time T, the [asset/instrument] tends to [return direction] over the next [N periods] by [magnitude range], with [holding period]."

**Example (acceptable):**
> "When a US equity's trailing 12-month return ranks in the top decile of its sector, AND the most recent quarterly earnings surprise was positive, the stock tends to outperform its sector median by 0.8–1.2% over the next 21 calendar days."

**Example (not acceptable):**
> "Momentum works."

**Your signal definition:** _______

---

## Stage 1: Data Audit

*"A signal built on dirty data is worthless. And dangerous."*

### 1.1 Data Source
- Source: _______
- Provider: _______
- Last updated: _______
- Coverage: _______ instruments × _______ years

### 1.2 Survivorship Bias Check
- [ ] Does the dataset include delisted, bankrupt, and acquired companies?
- [ ] If testing on an index (e.g., S&P 500), does it use the *historical* constituents or the *current* constituents?
- [ ] What % of the test universe has been replaced since the start of the backtest period?

**Survivorship bias severity:** None / Low / Medium / High
If Medium or High: quantify the expected bias on reported returns: +___% (typically 1–3%/year for equity datasets)

### 1.3 Look-Ahead Bias Check
For each data input used in the signal:
| Data Input | Publication Lag | Used With Correct Lag? |
|-----------|----------------|----------------------|
| Earnings data | 1–45 days after quarter end | Y/N |
| Index constituents | Announced before effective | Y/N |
| Analyst estimates | Real-time vs. point-in-time | Y/N |
| Price data | End-of-day vs. intraday | Y/N |
| Fundamental data | As-reported vs. restated | Y/N |

**Look-ahead bias present?** Yes / No / Uncertain
If uncertain: rebuild the signal using a point-in-time database.

### 1.4 Data Quality Checks
- [ ] Price data adjusted for splits and dividends
- [ ] Outliers investigated (returns > 3σ are real or data errors?)
- [ ] Missing data handled consistently (fill-forward, drop, interpolate — which method and why?)
- [ ] Currency and timezone normalization applied

---

## Stage 2: Statistical Significance

### 2.1 Sample Size Assessment
```
N_observations = total signal events in backtest
N_independent = N_observations / autocorrelation_adjustment

Autocorrelation adjustment:
  For daily signals: positions held H days → N_independent ≈ N / H
  For monthly signals: overlap of 11/12 months → N_independent ≈ N / 12
```

| Metric | Value |
|--------|-------|
| Total signal events | |
| Average holding period (days) | |
| Estimated independent observations | |
| Minimum required for 95% confidence (≈30) | 30 |
| Minimum required for robust inference (≈100) | 100 |

**Is the sample size sufficient?** Yes / Marginal / No

### 2.2 T-Statistic Calculation
```
t = (mean_return − 0) / (std_return / √N_independent)

For a two-sided test at 95% confidence: t > 1.96
For a two-sided test at 99% confidence: t > 2.58
```

| Metric | Value |
|--------|-------|
| Mean return per signal event | ___% |
| Std dev of returns | ___% |
| N_independent | |
| t-statistic | |
| p-value (two-sided) | |
| Passes 95% threshold? | Y/N |
| Passes 99% threshold? | Y/N |

### 2.3 Newey-West Standard Errors
Standard errors are typically understated when returns are autocorrelated. Use Newey-West correction with lag = holding period.

```
NW-adjusted SE = SE × correction_factor
Correction factor ≈ √(1 + 2 × Σ autocorrelation(lag k) for k=1 to H)
```

**NW-adjusted t-statistic:** _______
**Still significant after correction?** Y/N

---

## Stage 3: Out-of-Sample Validation

*The in-sample period is for discovery. The out-of-sample period is for validation.*

### 3.1 Train/Test Split
- In-sample period (for development): _______ to _______
- Out-of-sample period (held out, touched once): _______ to _______
- Split ratio: ___% in-sample / ___% out-of-sample

**Rule:** The out-of-sample period is used exactly ONCE. If you look at it to improve the signal, it is no longer out-of-sample. A new holdout must be designated.

### 3.2 Out-of-Sample Performance

| Metric | In-Sample | Out-of-Sample | Ratio (OOS/IS) |
|--------|-----------|--------------|----------------|
| Mean return per event | | | |
| Sharpe ratio | | | |
| Hit rate | | | |
| Max drawdown | | | |

**Acceptable degradation:** OOS/IS ratio of 0.5–0.8 is normal (some overfitting expected).
**Concerning degradation:** OOS/IS ratio < 0.3 suggests significant overfitting.
**Signal potentially overfit:** OOS/IS ratio < 0.0 (signal inverted out-of-sample).

**Out-of-sample verdict:** Validates / Marginal / Fails

### 3.3 Walk-Forward Validation
More robust than a single train/test split. Roll the training window forward:

| Window | Training Period | Test Period | OOS Return | OOS Sharpe |
|--------|----------------|-------------|-----------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Is performance consistent across windows, or concentrated in specific periods?**
_______

---

## Stage 4: Multiple Comparisons Correction

*"If you test 1,000 signals at p<0.05, expect 50 false positives."*

### 4.1 Search Process Disclosure
- How many signal variants were tested before this specification was chosen? ___
- How many parameters were optimized? ___
- Were any parameters "tuned" by looking at their effect on returns? Y/N

### 4.2 False Discovery Rate Correction

**Bonferroni correction** (conservative):
```
Adjusted p-value threshold = 0.05 / N_tests_run
Required t-statistic for significance ≈ t(adjusted_p, N_independent)
```

If 100 variants tested: adjusted threshold = 0.0005, required t ≈ 3.5

**Benjamini-Hochberg correction** (less conservative):
```
Sort all p-values: p(1) ≤ p(2) ≤ ... ≤ p(m)
Find largest k such that p(k) ≤ (k/m) × 0.05
All hypotheses 1..k are considered discoveries
```

**Number of variants tested:** ___
**Adjusted significance threshold (Bonferroni):** ___
**Signal t-statistic:** ___
**Passes corrected threshold?** Y/N

### 4.3 The "Simulated p-Hacking" Test
Generate 1,000 random signals with the same structure (frequency, holding period, universe) but random entry criteria. What % achieve the same t-statistic as your signal?

**Random signal percentile rank:** ___% [should be > 95th percentile to be meaningful]

---

## Stage 5: Economic Mechanism

*"We don't need to know why it works. But we should have a plausible reason why it might persist."*

### 5.1 Mechanism Hypothesis
Write one paragraph explaining why this pattern might persist:
- Is it a behavioral bias? Which one?
- Is it a structural constraint? (who is forced to trade on the other side?)
- Is it a microstructure effect? (what creates the predictability?)
- Is it a risk factor? (if so, is it alpha or just beta in disguise?)

**Mechanism hypothesis:** _______

### 5.2 Arbitrage Resistance
If the signal is real, why hasn't it been arbitraged away?
- [ ] Capacity constraint: works only at small scale
- [ ] Institutional constraint: index funds / passive cannot act on it
- [ ] Behavioral persistence: the bias that creates it is deeply human and won't disappear
- [ ] Information barrier: data required is expensive or hard to process
- [ ] Liquidity constraint: trading the signal incurs prohibitive market impact

**Arbitrage resistance assessment:** _______

---

## Stage 6: Capacity and Transaction Cost Analysis

### 6.1 Transaction Costs

```
Gross Sharpe (pre-cost): ___
Transaction cost per trade: ___ bps (spread + commission + market impact)
Trade frequency: ___ trades/year
Annual cost drag: ___ bps = ___% annualized

Net Sharpe (post-cost): ___
```

**Does the signal survive realistic transaction costs?** Y/N

### 6.2 Capacity Estimate
```
Max position size without moving market = ADV × ___% (typically 5–20%)
Positions per day = ___
Max daily capital deployed = ___
Annual turnover = ___x
Max strategy AUM before returns decay = $___M
```

---

## Final Verdict

| Test | Result | Pass? |
|------|--------|-------|
| Data quality (no survivorship/look-ahead) | | |
| Statistical significance (t > 2.0) | | |
| Sufficient independent observations (N > 100) | | |
| Out-of-sample validates (OOS/IS > 0.4) | | |
| Walk-forward consistent | | |
| Passes multiple-comparison correction | | |
| Plausible economic mechanism | | |
| Survives transaction costs | | |
| Adequate capacity | | |

**Signals passing all 9 gates: proceed to portfolio integration.**
**Signals failing 1–2 gates: investigate the failures before small-scale live testing.**
**Signals failing 3+ gates: discard. Do not trade. Document why it failed.**

**Final verdict:** APPROVED / CONDITIONAL / REJECTED
**Reason:** _______
