import os

def FindCMakeLists(dir):
    
    ListHeaders          = [];
    dictExternDependency = {}
    dictInternDependency = {}
    for root, dir, files in os.walk(dir):
        for file in files:
            #print("DEBUG ###################################### : ", file)
            if file == "CMakeLists.txt":
                #print("CMakeLists.txt trouvé :", os.path.join(root,file))
                ListHeaders.append(os.path.join(root,file))


    return ListHeaders, dictExternDependency , dictInternDependency


def GrepCMakeContent(ListHeaders,  dictExternDependency , dictInternDependency):
    regEx_FindName       = "name"
    regEx_FindDependency = "target_link_libraries"
    for header in ListHeaders:
        #print("on analyse le header", header)
        F = open(header,'r')
        #print(F)
        name = "pastrouve" #case we dont find name
        for line in F:
            print("grep file : ", header)
            print(line)
            if regEx_FindName in line: #name
               name = line[line.find("(")+1:line.find(")")];
               dictExternDependency[name] = [];
               dictInternDependency[name] = [];
               print("nom trouvé : ", name)
            elif regEx_FindDependency in line: #dep
               dep = line[line.find("(")+1:line.find(")")];
               print("dep trouvée : ", dep)
                
        if name != "pastrouve":
               dictExternDependency[name] = [];
               dictInternDependency[name] = [];
               dictInternDependency[name].append(dep);
    #print("dependance interne trouvée : ", name)
    return dictExternDependency , dictInternDependency
