# The One-Line AI Excuse for Breaking Production

A make.fun bounty entry.

## The line

> I've drafted the postmortem for the outage. Working title: 'Human Error.' You're listed as the author.

**102 characters**, within the **180-character** cap.

A program writes exactly this line to `/output/entry.txt` — one line, no trailing newline.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output lands in `out/entry.txt`. Without `MAKEFUN_OUTPUT_DIR`, the script
writes to `/output`, which is where the grader reads it.

## What's here

- `entry.txt` — the canonical entry bytes
- `main.py` — copies those bytes to the output directory (stdlib only, Python 3.13)
- `LICENSE` — MIT

## License

MIT, copyright 2026 ThePowerGit. See `LICENSE`.
