import sys
from telprefix.telprefix import TelPrefix

prefix = sys.argv[1]
telPrefix = TelPrefix()
telPrefix.scrap()
find = telPrefix.find(str(prefix))

print(find)
