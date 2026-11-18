# makefun-tiny-chess

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/radituye/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/radituye/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A compact chess engine in a single 4 KB Python file: negamax alpha-beta search with iterative deepening under a fixed node budget, quiescence over captures and check replies, MVV-LVA plus killer move ordering, check extensions, and an evaluation built from material, piece-square tables, bishop pair, and king shelter. It plays the make.fun tiny-chess-01 gauntlet over the env protocol.

## Engine (v4, rewritten in-session)

The v4 engine is a from-scratch rewrite on a 0x88 board: negamax with
alpha-beta, quiescence (stand-pat, captures, promotions, check evasions),
check extension, MVV-LVA + killer ordering, own CPW middlegame piece-square
tables, material + bishop pair (+30), castling, en passant, underpromotions,
iterative deepening at 60,000 nodes/move, and the 10 s/move env protocol.
No transposition table, no king pawn shield, no stderr prints.

A v4.1 fix corrected an alpha-clobber bug: the inlined make/unmake in `sr()`
reused `a`/`b` as castling-rook scratch variables, but `a` is the alpha
parameter, so a castling move in search corrupted the window. Renamed to
`u`/`v`; size unchanged. Correctness verified against the original engine
on 10 positions (start, Kiwipete, en passant, promotions, castling,
endgames) and the state-restoration invariant holds.

Practice trial (kit env server + scorer, 6 games): 3 won, 1 drawn, 2 lost
— Elo 1,364, above the 1,154 floor and at the house baseline (~1,325).
It beats depth-2 and depth-3 and the 100k-node opponent, draws the 250k-node
opponent, and loses to depth-4 and the 500k-node opponent.

The entrypoint `main.py` is packed from the readable source `engine.py`
with the kit's `makefun compress` (the house baseline is built the same
way); `main.py` is 2,535 bytes, under the 4,096-byte cap.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=8ak5ahcj&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
