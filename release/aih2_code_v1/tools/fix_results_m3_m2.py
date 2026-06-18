#!/usr/bin/env python3
"""Apply M3 (CI framing) and M2 (associational caveat) fixes to results.tex."""
import sys

path = 'paper/sections/results.tex'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

OLD = (
    r"The" + "\n"
    r"physico-chemical regime label explains almost none of it:" + "\n"
    r"$R^2_{\texttt{system\_class}}\!=\!0.018$ (cluster-bootstrap 95\,\% CI $[0.015\,0.373]$)." + "\n"
)

# Use find/replace approach on just the key phrase
OLD_PHRASE = "physico-chemical regime label explains almost none of it:\n"
NEW_PHRASE = (
    "physico-chemical regime label explains "
    r"$R^2_{\texttt{system\_class}}\!=\!0.018$" + "\n"
    r"(cluster-bootstrap 95\,\% CI $[0.015\,,\,0.373]$); the point estimate is low, but the" + "\n"
    r"wide interval (upper bound $\approx\!37\,\%$) reflects the limited corpus ($n\!=\!31$" + "\n"
    "studies) and does not exclude moderate regime effects.\n"
)

# Check if old phrase exists
if OLD_PHRASE not in text:
    print("ERROR: OLD_PHRASE not found in text")
    sys.exit(1)

# Step 1: Replace the "almost none" opening
text = text.replace(OLD_PHRASE, NEW_PHRASE, 1)

# Step 2: Remove the now-redundant original CI line
REDUNDANT = r"$R^2_{\texttt{system\_class}}\!=\!0.018$ (cluster-bootstrap 95\,\% CI $[0.015\,,\,0.373]$)." + "\n"
# That line won't exist now, but the original CI line was:
OLD_CI_LINE = r"$R^2_{\texttt{system\_class}}\!=\!0.018$ (cluster-bootstrap 95\,\% CI $[0.015,\,0.373]$)." + "\n"
if OLD_CI_LINE in text:
    text = text.replace(OLD_CI_LINE, "", 1)
    print("Removed redundant original CI line")

# Step 3: Add associational caveat after the 33% figure
OLD_TEMP = (
    r"(CI $[0.030,\,0.676]$); studies using a self-heating protocol report higher mean yields" + "\n"
)
NEW_TEMP = (
    "(CI $[0.030,\\,0.676]$; associational: temperature-control is a study-level attribute\n"
    "that may partly reflect unmeasured laboratory-level differences co-varying with\n"
    "protocol choice). Studies using a self-heating protocol report higher mean yields\n"
)
if OLD_TEMP in text:
    text = text.replace(OLD_TEMP, NEW_TEMP, 1)
    print("Applied M2 caveat")
else:
    print("WARNING: M2 pattern not found")

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Done. Verify results.tex manually.")
