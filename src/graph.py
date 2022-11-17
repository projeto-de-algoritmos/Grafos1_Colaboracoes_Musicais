from itertools import permutations 

class Graph:
    def __init__(self):
        self.graph = dict()

    def addEdge(self, node1, node2, edgeName):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append((node2, str(edgeName)))
        #self.graph[node2].append((node1, str(edgeName)))
        

    def printGraph(self):
        for source, destination in self.graph.items():
            print(f"{source}-->{destination}")


def main():
    g = Graph()

    with open("./filter/grafo_teste.txt") as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        edge, nodes = lines[i].replace("'", '').replace('"', '').split('|')
        nodesList = nodes.replace('\n', '').split(',')
        perm = permutations(nodesList, 2)

        for nodeCombination in list(perm):
            g.addEdge(nodeCombination[0], nodeCombination[1], edge)
    
    g.printGraph()
    
if __name__=="__main__":
    main()