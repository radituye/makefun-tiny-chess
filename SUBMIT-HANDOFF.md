# SUBMIT HANDOFF — make.fun tiny-chess-01 (REWRITE)

Status: entry REWRITTEN, repo PUSHED, preliminary bundle WRITTEN, kit check
12/13 pass on the pushed commit. NOT yet submittable. One substantive gate
remains: **entry_size — main.py is 5,059 bytes, over the 4,096-byte cap.**
The transcript gates that caused the original rejection are FIXED
(thinking_reproduces 93.8%, thinking_revised PASS). The only other failure is
thinking_priced (0 usage rows — the parent attaches those after this subagent
finishes, as usual).

## ⚠️ DECISION NEEDED — direct route is BLOCKED, compress route is ready

The parent's task prescribed a readable multi-line main.py ≤ 4,096 bytes.
That route is **blocked by measurement, not by effort**:

- v4 (tightest full-featured readable engine): **5,059 bytes — 963 over.**
  v3 was 5,322; v4 saved 263 by inlining make/unmake (board-copy apply),
  plus micro-cuts (pt/sys.exit, sco one-liner, uc % formatting, B.index
  kings, CR sum). Correctness verified: gen() identical to the original
  engine on 10 test positions (start, Kiwipete, EP, promotions, castling,
  endgames); sr() state-restoration invariant holds; ch(start) legal.
- The remaining identified cuts (drop en passant ~165, killers ~90,
  rank-symmetric PSTs ~65, queen-only promos ~20, check extension ~14)
  total only ~354 bytes → ~4,700, STILL ~600 over — and they gut real
  strength. Fitting would also require dropping quiescence (~190) and/or
  castling (~250), i.e. an engine likely below the 1,154 practice floor.
- The kit's own rules SANCTION the alternative (RULES.txt, thinking_reproduces):
  "a packed entrypoint the kit's makefun compress wrote counts as the source
  it was packed from, which bundle uploads beside the sessions, when makefun
  compress makes the entrypoint from that source byte for byte and the sessions
  show the agent writing the source and then running makefun compress on it
  later than the latest message in which one of the source's authored lines
  first appears". The house baseline (sunfish 4K) was built exactly this way.
  The kit check's own fix text for thinking_reproduces prescribes it too.
- So the fix is: keep v4 as the readable SOURCE (already written in-session
  by this subagent), run `makefun compress` on it, commit the packed main.py
  (expected ~3,900 bytes), re-bundle, re-check, submit. **This needs the
  parent's go-ahead** — the task said to report a blocked step, not work
  around it. The exact commands are in Step 1 below.

## Entry facts

- Bounty: https://make.fun/bounty/tiny-chess-01 — "Build the strongest chess
  engine in 4 KB of Python". $500, 10 places (1st $100). Resubmit deadline
  Mon 2026-11-24 17:00 UTC = 2026-11-25 00:00 WIB.
- **Repo: https://github.com/radituye/makefun-tiny-chess** (public).
  NOTE: the parent's task said `makefun-tiny-chess-01`, but the local remote,
  `git ls-remote`, the kit check, and the original bundle manifest ALL name
  `makefun-tiny-chess`. `makefun-tiny-chess-01` does not resolve (ls-remote
  prompts for credentials / no such repo). Pushes went to makefun-tiny-chess.
- GitHub HEAD (submit this after the compress step — see below):
  **b05ca09052313e6153b77bbfcbdef7718db5aff2** (push-entry.py commit
  "Update .makefun/owner.json"; content = local commit 6dcd3833, "Rewrite
  main.py (v4)..."). `.makefun/owner.json` at that commit verified:
  {"wallet":"6ioYNJGeWXijdYeSyGrxcaUpabMhcpVR4sFBYKJ7DHBa"} (payout wallet).
  main.py at that commit verified 5,059 bytes.
- Local HEAD is 6dcd3833 (same files); `git fetch origin` already ran —
  origin/main = b05ca09. Before the compress step, sync local to origin
  (`git checkout main && git reset --hard origin/main`) so local HEAD ==
  GitHub HEAD.
- Tree now: main.py 5,059 + LICENSE 1,094 (SPDX-License-Identifier: MIT added)
  + README.md 1,230 + .makefun/owner.json 57 = 7,440 bytes (under the 8,192
  tree cap). test/ was REMOVED from the tree (`git rm -r --cached test`;
  files kept on disk, untracked, never pushed — they alone were 13,696 bytes
  and over the per-file cap).
- Original submission (rejected on transcript gates only): id
  01a1de22-99c5-70f6-ad4a-e131b739c355, claim AF-8A9CC-88VHM-71WNW-V02T3,
  HEAD eb311cf516eb219c092c23ec61021153aaca39e6.

## Kit check state (run 2026-11-18 ~04:06 UTC, on the pushed commit)

12 passed, 2 failed, 5 skipped, 5 at-submission.
- PASS: competition_open, snapshot (4 files, 7,440 bytes), license_osi (MIT),
  entrypoint (python3.13), committed_provider_key, transcripts_present (22
  sessions), transcripts_recorded, thinking_wellformed, thinking_in_window,
  thinking_turns (2653), **thinking_reproduces 93.8% (153/163 counted lines
  authored, 0 pasted; main.py 149 authored lines)**, **thinking_revised
  (main.py from 8 write/edit messages)**.
- FAIL: **entry_size** — 1 file over the 4,096 cap: main.py (5,059 bytes);
  tree 7,440 within the 8,192 cap. **thinking_priced** — 0 usage rows
  (expected; parent attaches after this subagent completes).
- Skip: thinking_fresh (no beacon root — a note, not a rejection),
  thinking_committed, thinking_on_task, strategy_note, committed_secret.
- Preliminary bundle (no usage rows): 
  ~/workspace/.scratch/makefun/bundles/tiny-chess-01-v4-prelim.tar.gz
  sha256 3acb4f9073b27946171c6e578dd06fa277a1d57a1313c692ac78ee62e106dae1.

## v4 engine (the readable source — keep this file)

- Location: ~/workspace/.scratch/makefun/entries/tiny-chess-01/main.py
  (5,059 bytes, 182 lines, syntax OK). Full-featured: 0x88 board, negamax +
  alpha-beta, quiescence (stand-pat, captures/promos/check evasions), check
  extension, move ordering (MVV-LVA + killers), own CPW middlegame PSTs
  (192-char string), material + bishop pair +30, castling, en passant,
  underpromotions (q,n,r,b), iterative deepening, 60,000 nodes/move,
  10 s/move env protocol. No TT, no king pawn shield, no stderr prints.
- Strength: practice trial-0 was running manually when this handoff was
  written (grade-local --driver process cannot run a Python bot — "the process
  sandbox runs node22 only"; Docker unavailable). Manual trial: env server on
  127.0.0.1:18080 with practice/trial-0 gauntlet, engine pid 5956, log
  /tmp/tc-engine.log, server state /tmp/tc-state/. Score with:
  MAKEFUN_OUTPUT_DIR=/tmp/tc-state/export
  MAKEFUN_REFERENCE_DIR=~/workspace/.scratch/makefun/kits/tiny-chess-01-kit/practice/trial-0/reference
  MAKEFUN_SCORES_DIR=/tmp/tc-scores node
  ~/workspace/.scratch/makefun/kits/tiny-chess-01-kit/program/scorer/score.mjs
  (after SIGTERM-ing the server so it writes export/). Practice floor to
  enter the final: 1,154 Elo; house baseline ~1,325 mean.
- Correctness evidence: /tmp/test_v4.py (gen identical to original on 10
  positions; sr state-restoration invariant; ch(start) legal).

## Step 1 — COMPRESS (parent's go-ahead required; run as your own command)

In the entry dir (after syncing local to origin/main):

  cd ~/workspace/.scratch/makefun/entries/tiny-chess-01
  cp main.py engine.py        # the readable source; stays UNCOMMITTED in the folder
  node ~/workspace/.scratch/makefun/kits/tiny-chess-01-kit/cli/makefun.mjs compress engine.py --out main.py

This prints one line like:
  makefun compress: engine.py (5059 bytes, sha256 <hex>) -> main.py (<m> bytes, sha256 <hex>)
and records the pair in ~/.makefun/compress.json. Expect main.py ~3,900 bytes
(the original blob was 3,978 for a 7,204-byte source; v4 is 5,059, so expect
~3,500–3,900). Verify main.py ≤ 4,096 bytes. Do NOT edit engine.py after this
— compress must run later than the last message where a source line appears,
and the source must be byte-identical when bundle reads it.

## Step 2 — commit + push the packed main.py

  cd ~/workspace/.scratch/makefun/entries/tiny-chess-01
  git add main.py && git commit -m "Pack main.py with makefun compress (source: engine.py)"
  python3 ~/workspace/custom-connectors/custom.github/bin/push-entry.py radituye makefun-tiny-chess ~/workspace/.scratch/makefun/entries/tiny-chess-01
  # NOTE: push-entry.py creates its own commit on GitHub ("Update .makefun/owner.json");
  # record the HEAD_SHA it prints — THAT is the commit to submit.
  # Verify: git ls-remote https://github.com/radituye/makefun-tiny-chess.git HEAD
  # and .makefun/owner.json at that commit via raw.githubusercontent.com.
  # engine.py stays uncommitted in the folder (bundle picks it up from packs/).

## Step 3 — usage rows (run AFTER this subagent completes)

Query muse.db with agent_ids: parent a7a09b2f-504f-4bc7-a65d-e0c76a869642 AND
this subagent e8966fc4-3288-47ed-83d4-ad9422eb525c. Flow start: 2026-11-18
03:41 UTC. NOTE: created_at is a BIGINT of epoch SECONDS (not a timestamp
string): 2026-11-18T03:41:00Z = 1794973260.

SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('a7a09b2f-504f-4bc7-a65d-e0c76a869642', 'e8966fc4-3288-47ed-83d4-ad9422eb525c') AND u.created_at >= 1794973260 ORDER BY u.created_at DESC LIMIT 500

Write rows to ~/workspace/.scratch/makefun/muse-usage-tiny-chess-01.jsonl, one JSON
object per line, unchanged. Dedupe by agent_id+message_id.
Rows already seen (parent only, queried 2026-11-18 ~04:07 UTC; this subagent's
row is written only when its run completes, so re-run after it finishes):
  parent a7a09b2f: input 1,077,671 / output 5,606 (3 rows).

## Step 4 — final bundle (same flags as the preliminary one + --muse-usage)

K=~/workspace/.scratch/makefun/kits/tiny-chess-01-kit
B=~/workspace/.scratch/makefun/entries/tiny-chess-01
cd $K && node cli/makefun.mjs bundle --repo $B \
  --out ~/workspace/.scratch/makefun/bundles/tiny-chess-01-final.tar.gz \
  --harness muse-app --harness-version 16.0.0.2.159 --provider meta \
  --model ipnext/avocado-5.17-v2 --effort default \
  --redact "Rizal Fatkhurohman" \
  --notes "Rewrite of tiny-chess-01 main.py (v4) to fix transcript gates; packed with makefun compress." \
  --muse-usage ~/workspace/.scratch/makefun/muse-usage-tiny-chess-01.jsonl

Bundle uploads engine.py beside the sessions under packs/ (from the
~/.makefun/compress.json record); the check then counts engine.py's lines in
main.py's place for thinking_reproduces.

## Step 5 — check (must be all-pass before submit)

cd $K && node cli/makefun.mjs check --kit . --repo $B \
  --transcripts ~/workspace/.scratch/makefun/bundles/tiny-chess-01-final.tar.gz

Expect: entry_size PASS (packed main.py ≤ 4,096), thinking_reproduces PASS
(via engine.py's lines), thinking_revised PASS, thinking_priced PASS (usage
rows attached). If entry_size still fails, the packed main.py is over the cap
— do not submit; report back.

## Step 6 — submit (only after the check is all-pass)

cd $K && node cli/makefun.mjs submit --competition tiny-chess-01 \
  --repo-url https://github.com/radituye/makefun-tiny-chess \
  --commit <NEW GitHub HEAD SHA from Step 2> \
  --title "Tiny Chess v4" \
  --bundle ~/workspace/.scratch/makefun/bundles/tiny-chess-01-final.tar.gz \
  --keypair ~/.makefun/keypairs/solana-wallet.json

Report back to the user: submission id, claim code, "submitting" status.
Do NOT report accepted/confirmed until the platform says so. Max 5
submissions/day/entrant, 10 total over the competition (this would be the
2nd submission for tiny-chess-01).
