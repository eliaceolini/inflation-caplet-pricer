
# Inflation-Linked Caplet Pricer

This repository implements a Monte Carlo pricing engine for zero-coupon inflation caplets.

The model simulates inflation index paths under a lognormal process, corrects the simulated terminal values using Moment Matching to align with a deterministic inflation curve, and computes the payoff of an inflation caplet.

## Features

- Monte Carlo simulation of inflation index paths
- Moment Matching correction to match target expected inflation
- Payoff calculation for zero-coupon inflation caplet
- Configurable strike, maturity, and inflation parameters

## Installation

```bash
pip install numpy
```

## Usage

```python
from caplet_pricer import price_inflation_caplet

price = price_inflation_caplet(
    strike=0.02,
    maturity=3.0,
    n_paths=10000,
    mu=0.02,
    sigma=0.01,
    I0=100.0,
    discount_factor=0.95,
    target_mean=1.06  # target 6% inflation over 3 years
)

print(f"Caplet Price: {price:.6f}")
```

## Parameters

- `strike`: caplet strike (e.g. 0.02 for 2%)
- `maturity`: maturity in years
- `n_paths`: number of Monte Carlo paths
- `mu`: drift of inflation process
- `sigma`: volatility of inflation
- `I0`: initial inflation index value
- `discount_factor`: present value discount factor for maturity
- `target_mean`: optional target mean inflation multiplier for Moment Matching

## License

MIT
