import os
import time
import enchant

import re


d = enchant.Dict("en_US")
print  d.suggest("enalbe")


a=set()
a.add("11")
a.add("11")

print  "11" in a

# if re.match('^[a-zA-Z]+$', "helo"):
#     print 11

