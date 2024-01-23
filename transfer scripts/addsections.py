import re

with open("rawtext.md", encoding="utf-8") as f: 
    text=f.read()

headers=re.sub(r"(^.*PREAMBLE|SECTION.*$)", r"\n\1", text)
matches=re.sub(r"(\([a-z]\)|(\(\d\))|(\((i|v|x|l|c|d|m)+\)))", r'\n**\1**', headers)
newlines=re.sub(r'($)', r'\\', matches, flags=re.MULTILINE)

with open("rawtext.md", 'w', encoding="utf-8") as d:
    d.write(newlines)

