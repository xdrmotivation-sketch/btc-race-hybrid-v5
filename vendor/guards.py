"""Order guards the entrypoint calls before an order goes out.

Kept tiny on purpose: the replay punishes any order the market would refuse,
so every spend passes through these checks first.
"""


def usable_cash(state, reserve_frac=0.0):
    """Cash the bot may spend, holding `reserve_frac` of it back."""
    cash = int(state.cash or 0)
    keep = int(cash * max(0.0, min(1.0, float(reserve_frac))))
    return cash - keep


def has_position(state, symbol):
    """True when a positive position in `symbol` is held."""
    held = state.positions.get(symbol)
    return held is not None and held.qty > 0
