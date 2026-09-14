#!/usr/bin/env python3
# Generate docs/components.md from the source: one entry per exported function, with
# the doc comment above it and the props record declared above that. Run from the
# package root after editing a component's comment or props:
#   python3 scripts/gen_components.py
import re
out = ["# Components\n", "One entry per component: what it is, then its props record as declared. The doc\ncomment is the one in the source, so the two cannot drift.\n"]
groups = [("buttons", "Buttons and links"), ("surfaces", "Surfaces and labels"), ("forms", "Forms"),
          ("feedback", "Feedback"), ("overlays", "Overlays"), ("data", "Data display"), ("motion", "Motion")]
for f, title in groups:
    s = open(f"src/{f}.chuks").read()
    out.append(f"\n## {title}\n")
    for m in re.finditer(r'(export dataType (\w+) \{.*?\n\}\n)?/\*\*(.*?)\*/\nexport function (\w+)\(', s, re.S):
        props, doc, fn = m.group(1), m.group(3), m.group(4)
        doc = "\n".join(l.strip().lstrip("*").rstrip() for l in doc.strip().splitlines()).strip()
        doc = doc.replace("\n ", "\n")
        out.append(f"\n### {fn}\n\n{doc}\n")
        if props: out.append("\n```chuks\n" + props.strip() + "\n```\n")
open("docs/components.md", "w").write("".join(out))
print(sum(1 for l in out if l.startswith("\n### ")), "components")
