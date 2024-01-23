TOC = """
```
%s
```
"""

with open("rawtext.md", encoding="utf-8") as f:
    text=f.read()

textlines=text.split("\n")
toclist=[]
for i, line in enumerate(textlines):
    if line.startswith("SECTION"):
        
        splitline=line.split(" - ")
        sectext=f"{splitline[0].split(' ')[1]}. {splitline[1].title()}"
        newline=f"**{sectext}**"
        toclist.append(sectext)
    elif line.startswith("PREAMBLE"):
        newline="**Preamble**"
        toclist.append("Preamble")
    else:
        continue
    textlines[i]=newline

finaltext="\n".join(textlines)

with open("template.txt") as f:
    templatetext=f.read()

finaltoc=TOC %("\n".join(toclist))

def clean_text(*args):
    cleanedtext=f"{templatetext %(args)}\n\n{finaltoc}\n{finaltext}\n\n---\n\nProvince of British Columbia"
    print(cleanedtext)
    with open("rawtext.md", 'w', encoding="utf-8") as f:
        f.write(cleanedtext) 

clean_text("42", "https://docs.google.com/document/d/18Elgcdqv1U_5bVWq9tax8tRp4Uhw2kFVso9JDHSlksw/edit", "Legislative Subpoena Compliance & Enforcement Bylaw of 2022", "2nd", "35")
