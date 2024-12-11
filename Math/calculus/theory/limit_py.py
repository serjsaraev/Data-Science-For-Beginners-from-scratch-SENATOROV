"""Limit in python."""

import sympy as sp

n_ = sp.symbols("n")
f_ = (n_**2 + 3 * n_ - 5) / (3 * n_**2 - n_ + 6)
limit = sp.limit(f_, n_, sp.oo)
limit

n_ = sp.symbols("n")
f_ = (sp.sqrt(n_) * sp.sin(n_)) / ((2 * n_) + 6)
limit = sp.limit(f_, n_, sp.oo)
limit

n_ = sp.symbols("n")
f_ = (sp.sqrt(n_)) / (n_)
limit = sp.limit(f_, n_, sp.oo)
limit

n_ = sp.symbols("n")
f_ = sp.sqrt(n_ + 1) - sp.sqrt(n_)
limit = sp.limit(f_, n_, sp.oo)
limit
