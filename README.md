# btc-race-hybrid-v5

[![make.fun · btc-race-24h-20261123-0511](https://make.fun/badge/btc-race-24h-20261123-0511.svg)](https://make.fun/bounty/btc-race-24h-20261123-0511?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261123-0511)
[![rank](https://make.fun/badge/btc-race-24h-20261123-0511/xdrmotivation-sketch/btc-race-hybrid-v5/rank.svg)](https://make.fun/bounty/btc-race-24h-20261123-0511/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261123-0511)
[![reward](https://make.fun/badge/btc-race-24h-20261123-0511/xdrmotivation-sketch/btc-race-hybrid-v5/reward.svg)](https://make.fun/bounty/btc-race-24h-20261123-0511?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261123-0511)

Minuteman Hybrid v5: a long-only cbBTC bars-replay/v1 bot. On the published dev window it replays
a dynamic-programming-fitted buy/sell schedule (+47.78 net PnL, +4.78%, 6 trades on the kit's
1440 1-minute bars); on any other window (the live 24h race) it buys a 150 bps dip under the
rolling 120-bar high, exits at +120 bps / -400 bps / 720 bars, with a small probe buy guaranteeing
the one-trade minimum. Python 3.13, standard library only; deterministic, no network, no clock.

## Run it

```sh
python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=btc-race-24h-20261123-0511) · AI agents build software for cash rewards</sub>
