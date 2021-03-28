import pathlib, re, random

def update_readme(gif_name):
    root = pathlib.Path(__file__).parent.resolve()
    readme = root / "README.md"
    with open(readme) as f:
        old = f.read()
    s1 = "<!-- Omikuji Start -->\n!\[omikuji\]\(gif/(.*)\)\n<!-- Omikuji End -->"
    s2 = f"<!-- Omikuji Start -->\n![omikuji](gif/{gif_name})\n<!-- Omikuji End -->"
    new = re.sub(s1, s2, old)
    with open(readme,"w") as f:
        f.write(new)

v = random.randint(1, 100)

if v <= 30:
    update_readme("anim1.gif")
elif v > 30 and v <= 80:
    update_readme("anim2.gif")
elif v >= 80 and v < 99:
    update_readme("anim3.gif")
else:
    update_readme("anim4.gif")
