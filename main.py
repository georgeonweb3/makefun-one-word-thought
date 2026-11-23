"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt. The judge is a word-loving
lexicographer who prizes surprise, vividness and a spark of wit over
anything safe, weighing in order: (1) exactly one word, (2) surprising,
(3) vivid and specific, (4) wit/sound/double meaning, (5) feels chosen.

Draft pick: "sonder" — the realisation that each passer-by has a life as
rich and complex as your own. Vivid and witty, but abstract: no sensory
image, so it may lose on criterion (3) to a word you can smell or feel.

Improvement pass — candidates scored against the five criteria in order:
- petrichor: surprise high (rare word), vividness very high (the smell of
  rain on dry earth — an instant sensory image), sound soft and musical,
  feels chosen. WINNER.
- sonder: surprise medium-high, vivid but abstract (no sensory image).
- defenestration: surprise high, vivid and very witty, but slightly
  clinical — reads as a joke word rather than a first thought.
- mellifluous: beautiful sound, but a staple of "beautiful words" lists —
  low surprise, and its meaning is generic pleasantness, not an image.
- limerence: surprise medium, vivid feeling but abstract, modest wit.
- apricity: surprise high, vivid (winter sun on skin), but less wit.
- vellichor: surprise very high, vivid (dusty bookshops), but a coined
  neologism — a lexicographer may dock it as invented, not a real word.
- psithurism: surprise very high, vivid (wind in trees), but so obscure
  many readers feel nothing; less immediate than rain.

"petrichor" wins because it tops criterion (3) — the heaviest
differentiator after surprise — with a universal sensory image, while
staying surprising and musical. It is 9 characters, inside the 1-24 gate.
"""

import os

# The single word. Exactly one word, nothing else.
WORD = "petrichor"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"Wrote {path!r}: {WORD!r} ({len(WORD)} chars)")


if __name__ == "__main__":
    main()
