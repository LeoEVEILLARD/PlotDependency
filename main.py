
########### find header files
import os
from ForHeaders import *
from ForCMake   import *


dir = "./testDir2"

ListHeaders          = [];
dictExternDependency = {}
dictInternDependency = {}

if __name__ == "__main__":

    print("######### début phase de recherche des headers.")
    
    choice = "CMake"
    
    if   choice is "headers":
        ListHeaders, dictExternDependency , dictInternDependency = FindHeaders(dir)
    elif choice  is "CMake":
        ListHeaders, dictExternDependency , dictInternDependency = FindCMakeLists(dir)



    print("\nlist of header : \n", *ListHeaders, sep='\n- ')

    print("######### fin phase de recherche des headers.")

    ########### regex on file to find dependency

    print("######### début phase de regex des headers.")
    
    if   choice is "headers":
        dictExternDependency , dictInternDependency = GrepHeadersContent(ListHeaders,  dictExternDependency , dictInternDependency)
    elif choice  is "CMake":
        dictExternDependency , dictInternDependency = GrepCMakeContent(ListHeaders,  dictExternDependency , dictInternDependency)


    print("##########################DEBUG", dictInternDependency)
    print("######### fin phase de regex des headers.")

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
