import re
phoneRegex=re.compile(r'(\(\d\d\d\)-)?(\()?\d\d\d(\))?-(\()?\d\d\d\d(\))?')
mo=phoneRegex.search("my phone is (444-4444)")
print(mo.group())
print(mo.group(1))