
########### find header files
import os

print("######### début phase de recherche des headers.")

dir = "./testDir"

ListHeaders = [];
dictExternDependency = {}
dictInternDependency = {}

for root, dir, files in os.walk(dir):
    for file in files:
        if file.endswith(".h") or file.endswith(".hpp") or file.endswith(".hxx"):
            print("Header trouvé :", os.path.join(root,file))
            ListHeaders.append(os.path.join(root,file))
            dictExternDependency[file] = [];
            dictInternDependency[file] = [];

print("\nlist of header : \n", *ListHeaders, sep='\n- ')


print("######### fin phase de recherche des headers.")

########### regex on file to find dependency

print("######### début phase de regex des headers.")

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
                if name.endswith(".h"): dictInternDependency[os.path.basename(header)].append(name);
                #print("dependance interne trouvée : ", name)

#print("######### fin phase de regex des headers.")

########### plot dependency in graph

#print("######### début phase de graphe.")
import pygraphviz as pgv

graph = pgv.AGraph()

for header, listDependency in dictInternDependency.items():
    for dependency in listDependency:
        graph.add_edge(header, dependency)

graph.layout('dot')
graph.draw('graph.png')

#print("######### fin phase de graphe.")
