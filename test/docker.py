import os
import time
import enchant

import re

d = enchant.Dict("en_US")
d.add("func")
d.add("struct")

d.add("mv")

d.add("auth")
d.add("nil")

d.add('cAdvisor')
d.add("bool")
d.add("const")
d.add("unix")

d.add("blockquote")
d.add("html")

d.add("textarea")
d.add("tbody")
d.add("TODO")
d.add("kubelet")
d.add("tfoot")
d.add("CloudFlare")
d.add("SELinux")
d.add("Flocker")
d.add("ReadOnly")
d.add("repo")
d.add("iSCSI")
d.add("stdin")
d.add("finalizer")
d.add("http")
d.add("cgroups")
d.add("atEOF")
d.add("UUID")
d.add("passwd")
d.add("args")
d.add("chan")
d.add("backend")
d.add("filename")
d.add("golang")
d.add("sysctl")
d.add("kubenet")
d.add("portManager")
d.add("nsenter")
d.add("config")
d.add("podIP")
d.add("cniPlugin")
d.add("hostport")
d.add("vendorDir")
d.add("shaper")
d.add("boolean")
d.add("protobuf")
d.add("proto")
d.add("lookup")
d.add("langAliasType")
d.add("Matcher")
d.add("subtag")
d.add("langNoIndexOffset")
d.add("IsPrivateUse")
d.add("regionID")
d.add("ValueError")
d.add("stringSet")
d.add("isList")
d.add("haveRegion")
d.add("GOPATH")
d.add("endif")
d.add("ubuntu")






ok = set()
def eachFile(filepath):
    for root, dirs, files in os.walk(filepath):
#        print root
        for file in files:
            for line in open(os.path.join(root, file)):
                for i in line.split(" "):
                    if re.match('^[a-zA-Z]{5,20}$', i):
                        if d.check(i.strip("\r\n")):
                            continue
                        else:
                            ok.add(i)




eachFile("/home/tim/eclipse/workspace/src/github.com/docker/docker")


for i in ok:
    print i
