# Backtest Quality Checklist

A backtest is a simulation of what would have happened. The gap between simulation and reality is where most quant strategies fail. This checklist systematically identifies every way a backtest can flatter a strategy that won't work live.

Simons: "The system tells us what to do. When it's wrong, we try to understand why."

---

## Section 1: Data Integrity

### 1.1 Survivorship Bias
**Definition:** Using only the assets that exist today, excluding those that failed, merged, or were delisted.
**Effect:** Inflates returns by 1–3%/year for equity strategies. Results look better than live trading will.

- [ ] Dataset confirmed to include delisted, bankrupt, and acquired entities?
- [ ] For index strategies: historical constituency data used (not current members)?
- [ ] Point-in-time data used for any fundamental inputs?

**Survivorship bias risk:** None / Low (< 0.5%/yr) / Medium (0.5–2%/yr) / High (> 2%/yr)

### 1.2 Look-Ahead Bias
**Definition:** Using information in the simulation that was not available at the decision time.
**Effect:** Can produce unrealistically high Sharpe ratios; strategy will fail immediately in live trading.

**Common sources:**
- Using end-of-day prices for intraday decisions
- Using restated financial data (as-of-today) instead of as-reported-at-the-time
- Using index membership that was announced after the trade date
- Using earnings announcements before market hours when the trade executes at open

**Checklist:**
- [ ] All decisions use data available at decision time, with realistic lags
- [ ] Financial data uses "as-reported" not "as-restated" figures
- [ ] Price data is end-of-day (or intraday with correct timestamps)
- [ ] Corporate actions (splits, dividends) handled with correct dates

**Look-ahead bias risk:** None / Suspected / Confirmed

### 1.3 Data Vendor Quality
- [ ] Price data cross-checked against secondary source for major outliers?
- [ ] Dividend/split adjustments applied consistently (forward vs. backward adjusting)?
- [ ] Currency conversions use correct dates and rates?
- [ ] Trading halt periods handled (returns during halts are illiquid and non-representative)?

---

## Section 2: Overfitting Detection

### 2.1 Parameters vs. Observations Ratio
A rough heuristic: you need at least 10–20 independent observations per free parameter to avoid overfitting.

```
N_parameters = number of optimized or "chosen" variables
N_independent = effective independent observations (see Signal Validation Audit)

Ratio = N_independent / N_parameters
Target: > 20
Marginal: 10–20
Overfitting likely: < 10
```

**N_parameters:** ___
**N_independent:** ___
**Ratio:** ___

### 2.2 Parameter Sensitivity Test
If the strategy has parameters (lookback window, threshold, etc.), test performance across a range:

| Parameter Value | Sharpe | Max DD | Annual Return |
|----------------|--------|--------|--------------|
| [−30% from chosen] | | | |
| [−15% from chosen] | | | |
| [Chosen value] | | | |
| [+15% from chosen] | | | |
| [+30% from chosen] | | | |

**Is performance concentrated around the chosen value (peaked), or stable across the range (flat)?**
- Flat/stable: good. The chosen value isn't being data-mined.
- Peaked: bad. The strategy is overfit to this specific parameter combination.

**Parameter sensitivity assessment:** Stable / Marginally peaked / Peaked (overfit)

### 2.3 Out-of-Sample Decay Ratio
```
In-sample Sharpe:       ___
Out-of-sample Sharpe:   ___
Decay ratio:            ___  [OOS / IS]

Interpretation:
  > 0.8: minimal overfitting
  0.5–0.8: moderate overfitting, typical for data-driven strategies
  0.3–0.5: significant overfitting; reduce position size
  < 0.3: severe overfitting; do not trade
```

### 2.4 The "How Many Strategies Did You Try?" Test
Before this strategy was selected, how many alternative specifications were evaluated?

| Search dimension | Variants tested |
|-----------------|----------------|
| Signal type | |
| Lookback periods | |
| Universe filters | |
| Entry/exit conditions | |
| Position sizing rules | |
| **Total combinations explored** | |

Apply Bonferroni correction: if N combinations were tested, the true significance threshold is 0.05/N.

**Expected false positives at p<0.05:** ___ (= N × 0.05)
**Does this strategy's p-value survive Bonferroni correction?** Y/N

---

## Section 3: Execution Realism

### 3.1 Transaction Cost Model
Most backtests underestimate real-world trading costs. Use the most conservative assumption.

| Cost Component | Assumption Used | Is it Realistic? |
|---------------|----------------|-----------------|
| Bid-ask spread | ___ bps | Y/N |
| Brokerage commission | ___ bps | Y/N |
| Market impact (price slippage) | ___ bps | Y/N |
| Short borrow cost (if applicable) | ___% /year | Y/N |
| Margin cost (if leveraged) | ___% /year | Y/N |
| **Total round-trip cost** | ___ bps | |

**Market impact model used:**
- [ ] None (unrealistic)
- [ ] Fixed bps per trade (simple but often sufficient for low-frequency)
- [ ] Square root model: impact ∝ √(trade size / ADV) × volatility (more realistic)
- [ ] Almgren-Chriss or similar (institutional grade)

**Gross Sharpe:** ___
**Net Sharpe (after all costs):** ___
**Cost drag as % of gross return:** ___%

### 3.2 Fill Assumptions
- [ ] Trades execute at close price (realistic for close-to-close strategies)
- [ ] Trades execute at open price with appropriate slippage (for open-gap strategies)
- [ ] Partial fills modeled for illiquid names?
- [ ] Large orders use VWAP or TWAP execution model?

### 3.3 Short-selling Constraints
If strategy involves short positions:
- [ ] Short availability checked (hard-to-borrow names excluded or penalized)?
- [ ] Borrow cost loaded by security (not a flat rate)?
- [ ] Forced buy-ins modeled (especially for small-cap shorts)?

---

## Section 4: Risk and Drawdown Analysis

### 4.1 Drawdown Profile
```
Maximum drawdown (MDD): ___%
Time to recovery: ___ months
Average drawdown: ___%
Longest drawdown duration: ___ months
```

**Is the MDD consistent with what you'd expect given the Sharpe ratio?**
For a Sharpe of 1.0, expected MDD ≈ 20–30% over 10 years.
If MDD is much lower: may indicate look-ahead bias or over-smoothed returns.

### 4.2 Tail Risk / Fat Tails
```
Skewness of returns: ___  [negative = left-tail / crash risk]
Excess kurtosis: ___      [> 0 = fat tails]
Worst 1% monthly returns: ___%
Worst month ever: ___%
```

**Is the strategy negatively skewed?** (Selling insurance — looks great until it doesn't)
If yes: the Sharpe ratio overstates risk-adjusted returns. Reduce effective Sharpe by 20–40%.

### 4.3 Crisis Period Performance
Test the strategy in known stress periods:

| Period | Strategy Return | Benchmark Return | Comments |
|--------|----------------|-----------------|----------|
| Aug–Oct 1998 (LTCM) | | | |
| Mar 2000–Oct 2002 (dot-com) | | | |
| Sep–Dec 2008 (GFC) | | | |
| Mar 2020 (COVID crash) | | | |
| 2022 rate-rise | | | |

**Does the strategy protect capital in crises, or amplify losses?**
Strategy with crisis amplification requires lower steady-state leverage.

---

## Section 5: Regime Analysis

### 5.1 Performance by Volatility Regime
| VIX Regime | Strategy Sharpe | Comments |
|-----------|----------------|----------|
| Low vol (VIX < 15) | | |
| Medium vol (VIX 15–25) | | |
| High vol (VIX > 25) | | |

**Is the edge concentrated in one regime?** If so, be cautious when that regime changes.

### 5.2 Performance by Market Direction
| Market Regime | Strategy Return | Market Return |
|--------------|----------------|--------------|
| Strong up (>15%/yr) | | |
| Moderate up (5–15%) | | |
| Flat (±5%) | | |
| Moderate down (−5 to −15%) | | |
| Strong down (<−15%) | | |

**Beta to market:** ___ [target for market-neutral strategy: < 0.1]
**Is alpha genuine or correlated beta?**

### 5.3 Decay Analysis
Is the strategy's edge eroding over time?

| 5-year period | Sharpe | Annual Alpha |
|--------------|--------|-------------|
| [Earliest 5yr] | | |
| [Mid 5yr] | | |
| [Recent 5yr] | | |

**Trend:** Improving / Stable / Declining
If declining: estimate when the edge reaches zero, and whether it's still worth trading today.

---

## Summary Scorecard

| Section | Issues Found | Severity | Adj. to Reported Sharpe |
|---------|-------------|----------|------------------------|
| Data integrity | | | −___ |
| Overfitting | | | −___ |
| Execution realism | | | −___ |
| Tail risk / crisis | | | −___ |
| Regime dependency | | | −___ |

**Reported backtest Sharpe:** ___
**Realistic live-trading Sharpe estimate:** ___
**Confidence interval:** (___,  ___)

**Recommendation:**
- Live Sharpe > 1.0: Trade at target allocation
- Live Sharpe 0.5–1.0: Trade at 50% allocation pending live validation
- Live Sharpe 0.2–0.5: Paper trade for 6 months; track closely
- Live Sharpe < 0.2: Do not trade; revise or discard
