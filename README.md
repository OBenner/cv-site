# omiagkov@prod:~$

Personal site of **Oleg Miagkov** — tech lead data engineer · high-load data platforms · fintech.

The whole site is a terminal. You type commands — it answers.

```
omiagkov@prod:~$ whoami
oleg miagkov · tech lead data engineer
high-load data platforms · fintech · 8+ years
team & tech lead · java · scala · go · python
location: russia · remote-friendly
status: open to interesting projects ✓

omiagkov@prod:~$ help
whoami · about · cv · cat stack.txt · ls projects/ · contact · sudo hire
```

## features

- **interactive shell** — command history (`↑`/`↓`), tab completion, fish-style ghost autosuggestions while typing
- **`cat stack.txt`** — draws an interactive iceberg of the stack right in the terminal: BI is the visible tip, everything that holds it is below the waterline (click a depth, the sonar reports)
- **`cv`** — renders a minimalist resume timeline inline + a downloadable pdf
- **clickable everything** — project folders in `ls`, contacts, hint chips
- **easter eggs** — quite a few. trust your muscle memory: type what you would type in a real shell
- **zero dependencies** — one html file, vanilla js, no frameworks, no build step

## structure

| path | what |
|---|---|
| `index.html` | the site — everything lives in this one file |
| `cv.pdf` | resume, generated — do not edit by hand |

## run locally

```bash
open index.html
```

That's it. No install, no build.



`// © 2026 oleg miagkov · mrobenner@gmail.com`
