import re

batRegex=re.compile(r'Bat(man|mobile|copter)')

mo=batRegex.search("Batman flew the Batcopter since he crashed the Batmobile")

print(mo.group())
print(mo.group(1))


qualityRegex=re.compile(r'(108|72|48)0')
do=qualityRegex.search("dark knight rises 720px")

print(do.group())
print(do.group(1))
