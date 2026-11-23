"""Strategy notes and the tuned constants for the Minuteman Hybrid v5 bot.

The numbers here are what the dev-window fits on the make.fun btc-race kits
showed: fractions, fees and the race posture. Kept beside the wire shim so the
entrypoint stays about decisions, not constants.
"""

# Fees and slippage the replay charges on every fill (basis points).
FEE_BPS = 4
SLIPPAGE_MODEL_BPS = 2

# Schedule fits are re-derived per competition window; the 6 Nov window paid
# more in price impact above 0.55 than it earned back, so fractions above it
# were cut. The 23 Nov fit held at full size.
MAX_FIT_FRACTION = 1.0

# Race posture: the 15 Nov race showed fitted-DP bots bleeding -5..-7 percent
# live while low-turnover holders led the board, so the live mode buys once
# on a dip and holds to the end-of-run flatten.
LIVE_TURN = "hold"

# Price-impact guard: never send an order worth more than this share of the
# pool depth's last close without widening the slippage bound.
IMPACT_DEPTH_SHARE = 0.02
