import os

def FindHeaders(dir):

    ListHeaders          = [];
    dictExternDependency = {}
    dictInternDependency = {}
    for root, dir, files in os.walk(dir):
        for file in files:
            if file.endswith(".h") or file.endswith(".hpp") or file.endswith(".hxx"):
                print("Header trouvé :", os.path.join(root,file))
                ListHeaders.append(os.path.join(root,file))
                dictExternDependency[file] = [];
                dictInternDependency[file] = [];

    return ListHeaders, dictExternDependency , dictInternDependency


def GrepHeadersContent(ListHeaders,  dictExternDependency , dictInternDependency):

    for header in ListHeaders:
        #print("on analyse le header", header)
        F = open(header,'r')
        #print(F)
        for line in F:
            if line.startswith("#include"):
                if '<' in line:
                    name = line[line.find("<")+1:line.find(">")];
                    dictExternDependency[os.path.basename(header)].append(name);
                #print("dependance externe trouvée : ", name)
                elif '"' in line:
                    name = line.split('"')[1];
                    #print(os.path.basename(header))
                    if name.endswith(".h"): dictInternDependency[os.path.basename(header)].append(name); #exclude cpp
    #print("dependance interne trouvée : ", name)
    return dictExternDependency , dictInternDependency
