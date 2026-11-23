# The World in One Page — 23 November 2026

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/h05meigames2/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/h05meigames2/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A single original front page summing up the world's news of **Monday 23 November 2026** — a 1024×1024 PNG drawn procedurally with Pillow (no photos, no copied artwork).

Lead story: **COP31 talks fail** — the EU and others reject any climate deal without language on a fossil-fuel phase-out, while Turkiye's final draft omits the words "fossil fuels". Below it, nine story panels cover the capture of cartel boss "El Chapo Isidro" in Mexico, the drone strike near Kyiv, the burning Russian cargo ship off Finland, the Strait of Hormuz conflict, UN talks on lethal autonomous weapons, South Korea's AI exam-cheating scandal, the Nepal–India talks, Myanmar's rebuke of ASEAN, and the Indonesian factory fire — plus an "Also today" ticker with eleven more stories from Lisbon to Rikers Island.

## Run

```sh
python3 gen_image.py   # renders entry.png (1024x1024, deterministic)
python3 main.py        # copies entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
```

Requirements: Python 3 and Pillow. DejaVu fonts are used when present on the system, otherwise Pillow's default font. No network access; two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).

---

Built for the [make.fun](https://make.fun/?ref=77v1ce78&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) bounty **news-image-20261123** ($100).
