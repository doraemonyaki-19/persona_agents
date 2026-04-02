# Multiple Comparisons Correction Guide

Simons: "We don't hire people who know about markets. We hire people who are good scientists."

Good scientists know that testing many hypotheses on the same dataset inflates the false positive rate. This is the multiple comparisons problem — the source of most spurious "discoveries" in quantitative finance. This guide explains when and how to correct for it.

---

## The Problem

If you test a single signal at p < 0.05 and it passes, you have a 5% chance of a false positive (assuming the null hypothesis is true).

If you test **20 independent signals** at p < 0.05, the probability that **at least one** is a false positive is:
```
P(at least one false positive) = 1 − (1 − 0.05)^20 = 1 − 0.95^20 ≈ 64%
```

In practice, quant researchers test hundreds or thousands of variations. Without correction, "significant" findings are mostly noise.

**The quant finance specific problem:** Strategies are often selected by showing them to a portfolio manager who can see the backtest. Every strategy shown is a test. Every rejected strategy was also a test. The denominator is almost never disclosed.

---

## Method 1: Bonferroni Correction (Conservative)

**When to use:** Small number of planned comparisons (N < 50), or when you need to be very sure about each individual result.

**Formula:**
```
Adjusted significance level = α / N
where α = 0.05 (family-wise error rate)
      N = number of hypotheses tested

Required t-statistic for N tests:
  N=1:   t > 1.96
  N=10:  t > 2.81
  N=50:  t > 3.29
  N=100: t > 3.48
  N=1000: t > 3.89
```

**Example:** You tested 50 signal variants. Your best signal has t = 2.9.
- Unadjusted: significant (t > 1.96) ✓
- Bonferroni-adjusted (threshold = 3.29): NOT significant ✗

**Limitation:** Overly conservative when tests are correlated (which they often are in finance). May reject too many true positives.

---

## Method 2: Benjamini-Hochberg (FDR Control)

**When to use:** Larger number of tests, correlated hypotheses, when you want to control the False Discovery Rate (FDR) rather than the family-wise error rate.

**Concept:** Controls the *expected proportion* of false positives among all discoveries, rather than controlling any single false positive.

**Procedure:**
```
1. Test N hypotheses, obtain p-values p(1) ≤ p(2) ≤ ... ≤ p(N)
2. Find the largest k such that: p(k) ≤ (k/N) × q
   where q = desired FDR (typically 0.05 or 0.10)
3. Reject hypotheses 1 through k (call them discoveries)
```

**Example with 20 signal variants, FDR = 0.10:**

| Rank | Signal | p-value | (k/N) × 0.10 | Reject? |
|------|--------|---------|--------------|---------|
| 1 | Momentum-12m | 0.002 | 0.005 | YES |
| 2 | Earnings surprise | 0.008 | 0.010 | YES |
| 3 | Short interest | 0.019 | 0.015 | NO ← stop here |
| ... | ... | ... | ... | NO |

**Interpretation:** Among the signals declared significant, at most 10% are expected to be false positives.

---

## Method 3: Bootstrap p-value Correction

**When to use:** When the return distribution is non-normal (fat tails, skewness), or when you want to account for the specific structure of your test universe.

**Procedure:**
```
1. Take your actual signal returns: r_1, r_2, ..., r_N
2. Generate 10,000 bootstrap samples by randomizing signal labels
   (assign the same returns to random time slots)
3. For each bootstrap sample, compute the t-statistic
4. Corrected p-value = fraction of bootstrap t-statistics exceeding your actual t-statistic
```

**Advantage:** Makes no distributional assumptions. Naturally accounts for autocorrelation and fat tails.

**Minimum bootstrap samples:** 10,000 for p-values down to 0.001; 100,000 for p-values down to 0.0001.

---

## Method 4: The Harvey-Liu-Zhu Framework (for Finance)

**Specifically designed for quant finance.** Harvey, Liu, and Zhu (2016) argued that given the number of factors published in academic finance (300+), a t-statistic of 2.0 is insufficient. They proposed minimum thresholds that account for the massive search effort in the field.

**Recommended t-statistic thresholds by era:**

| Era | Minimum t-statistic | Rationale |
|-----|--------------------|----|
| Pre-1991 | 2.56 | Fewer strategies; less data-mining |
| 1991–2003 | 2.78 | Growing publication bias |
| Post-2003 | 3.00 | Massive proliferation of strategies tested |

**For proprietary trading (where the search is even broader):** t > 3.5 is a reasonable threshold.

---

## Practical Framework for Quant Signal Development

### Step 1: Pre-Register Your Tests
Before running any analysis, write down:
- The specific signal hypothesis
- The exact parameters (lookback, universe, holding period)
- The exact test to be run
- The significance threshold

Signals that are pre-registered have their stated p-values. Signals that are post-hoc selected do not.

### Step 2: Track All Tests Run
Maintain a signal log:

| Signal ID | Description | Params | t-stat | p-value | OOS result | Decision |
|-----------|-------------|--------|--------|---------|-----------|---------|
| S001 | 12m momentum | top decile | 3.2 | 0.001 | 2.8 | Test live |
| S002 | 3m momentum | top decile | 1.8 | 0.07 | n/a | Reject |
| S003 | 12m momentum | top quintile | 2.9 | 0.004 | | |
| ... | | | | | | |

**The number of rows in this table is your N for multiple comparison correction.**

### Step 3: Apply Correction
Using the full list of N tests run:

```
N_tests_run = ___
Bonferroni threshold = 0.05 / N = ___
Required t = scipy.stats.t.ppf(1 − 0.05/(2×N), df=N_independent)

Signals passing Bonferroni: ___
Signals passing BH at FDR=0.10: ___
```

### Step 4: Out-of-Sample Validation
For signals that pass statistical correction:
- Set aside a portion of data that was **never used** in development
- Test exactly once on this holdout
- If the signal fails on the holdout: it was a false discovery. Do not trade it.
- If the signal passes on the holdout: proceed to small-scale live testing

**Rule:** Once you look at the holdout data, it is no longer a holdout. Designate a new holdout period going forward.

---

## Quick Reference: Minimum t-Statistics by Search Intensity

| Search Intensity | N tested | Bonferroni threshold | Min t-stat |
|-----------------|---------|---------------------|-----------|
| Single hypothesis | 1 | 0.050 | 1.96 |
| Small study | 10 | 0.005 | 2.81 |
| Moderate search | 50 | 0.001 | 3.29 |
| Large search | 100 | 0.0005 | 3.48 |
| Systematic sweep | 500 | 0.0001 | 3.73 |
| Full factor zoo | 1000+ | <0.0001 | 3.89+ |

---

## Red Flags: Signs of Undisclosed Multiple Testing

- Reported strategy has t ≈ 2.0–2.5 (just barely significant)
- No disclosure of how many strategies were tested during development
- Parameters are oddly specific (e.g., "17-day lookback") without theoretical justification
- Strategy performance is sensitive to small parameter changes
- The "discovery" was made during an exploratory period, not a pre-registered test
- Multiple papers or presentations from the same group all report p ≈ 0.05

**Simons's rule of thumb:** If a quant researcher tells you they only tested one signal and it was significant, they are either lying or they had a very good prior. Both require further investigation.

---

## Worked Example

**Setup:** A researcher tested 200 signal variants on 20 years of US equity data.
The best signal achieved a t-statistic of 3.1 with p = 0.002.

**Unadjusted claim:** "Significant at the 0.1% level."

**Corrected analysis:**
```
N_tests = 200
Bonferroni threshold: p < 0.05/200 = 0.00025 → required t ≈ 3.72
Signal t = 3.1 → p ≈ 0.002 → FAILS Bonferroni

BH correction at FDR = 0.10:
  Rank this signal among all 200 p-values
  Expected discoveries at FDR=0.10: ~10 signals
  Does this signal fall below the BH threshold?  → [need full list to determine]

Bootstrap correction:
  Run 10,000 random shuffles → find what % achieve t > 3.1
  If 5%: genuine discovery. If 20%: noise.
```

**Conclusion:** The signal requires OOS validation before being considered tradeable. The unadjusted p-value overstates confidence by at least 40x.
