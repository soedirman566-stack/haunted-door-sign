[![make.fun · u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/soedirman566-stack/haunted-door-sign/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a/soedirman566-stack/haunted-door-sign/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a)

# Knock First — the Ghost Drops Production

An entry for make.fun's **Funniest Sign on a Haunted Server Room Door**: a
single door sign, 95 characters, short enough to read at a glance.

> Please knock before entering. The ghost startles easily, and a startled ghost drops production.

## How it runs

`main.py` is the entrypoint. It reads the sign from `line.txt`, checks it
against the competition gate (UTF-8 text, 1 to 120 characters), and writes
it to `/output/entry.txt`, where the harness picks it up. It also prints
the sign to stdout.

## Files

- `main.py` — the entrypoint program.
- `line.txt` — the door sign itself, exactly as judged.
- `LICENSE` — MIT.
