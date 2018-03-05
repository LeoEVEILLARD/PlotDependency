
########### find header files
import os
import sys
from ForHeaders import *
from ForCMake   import *



OK= False
while OK != True:
    if   (sys.version_info[0] == 2): # python 2
        choice = raw_input("Please enter CMake or headers : ")
    elif (sys.version_info[0] == 3): # python 3
        choice =     input("Please enter CMake or headers : ")
    else:
        print("Seriously man, on what computer are you running this script ?")

    if(choice == "CMake" or choice == "headers"):
        OK = True
    else:
        print("please quick enter 'CMake' of 'headers', we've got a lot of stuff to do ")



dir = "./testDir2"
OK= False
while OK != True:
    if   (sys.version_info[0] == 2): # python 2
        dir = raw_input("Please enter a path : ")
    elif (sys.version_info[0] == 3): # python 3
        dir =     input("Please enter a path : ")
    else:
        print("Seriously man, on what computer are you running this script ?")
    OK = True
    #toDo : path exist check


ListHeaders          = [];
dictExternDependency = {}
dictInternDependency = {}

if __name__ == "__main__":

    print("######### début phase de recherche des headers.")
    

    
    if   choice == "headers":
        ListHeaders, dictExternDependency , dictInternDependency = FindHeaders(dir)
    elif choice  == "CMake":
        ListHeaders, dictExternDependency , dictInternDependency = FindCMakeLists(dir)



    print("\nlist of header : \n", *ListHeaders, sep='\n- ')

    print("######### fin phase de recherche des headers.")

    ########### regex on file to find dependency

    print("######### début phase de regex des headers.")
    
    if   choice == "headers":
        dictExternDependency , dictInternDependency = GrepHeadersContent(ListHeaders,  dictExternDependency , dictInternDependency)
    elif choice  == "CMake":
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
