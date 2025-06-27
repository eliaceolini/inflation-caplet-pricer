
import numpy as np

def simulate_inflation_paths(
    T: float,
    n_paths: int,
    n_steps: int,
    mu: float,
    sigma: float,
    I0: float
) -> np.ndarray:
    dt = T / n_steps
    paths = np.zeros((n_paths, n_steps + 1))
    paths[:, 0] = I0
    for t in range(1, n_steps + 1):
        z = np.random.normal(size=n_paths)
        paths[:, t] = paths[:, t-1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)
    return paths

def apply_moment_matching(paths: np.ndarray, target_mean: float) -> np.ndarray:
    mean_at_T = np.mean(paths[:, -1])
    correction = target_mean / mean_at_T
    paths[:, -1] *= correction
    return paths

def price_inflation_caplet(
    strike: float,
    maturity: float,
    n_paths: int = 10000,
    n_steps: int = 120,
    mu: float = 0.02,
    sigma: float = 0.01,
    I0: float = 100.0,
    discount_factor: float = 0.95,
    target_mean: float = None
) -> float:
    paths = simulate_inflation_paths(maturity, n_paths, n_steps, mu, sigma, I0)
    if target_mean is not None:
        paths = apply_moment_matching(paths, target_mean)
    inflation_ratio = paths[:, -1] / I0 - 1.0
    payoff = np.maximum(inflation_ratio - strike, 0.0)
    return discount_factor * np.mean(payoff)

if __name__ == "__main__":
    price = price_inflation_caplet(
        strike=0.02,
        maturity=3.0,
        n_paths=10000,
        mu=0.02,
        sigma=0.01,
        I0=100.0,
        discount_factor=0.95,
        target_mean=1.06  # Example: target 6% inflation over 3 years
    )
    print(f"Caplet Price: {price:.6f}")
