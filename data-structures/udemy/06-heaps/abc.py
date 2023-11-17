


## Here we will implement heap methods

class Heap:
    def __init__(self,size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

def sizeOfHeap(rootNode):
    if not rootNode:
        return

    return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1,rootNode.heapSize+1,1):
        print(rootNode.customList[i])

def heapifyInsert(rootNode, index, heapType):
    parentIndex = index//2
    if index <=1:
        return

    if heapType == "Min":
        # if current element is less than parent, do swapping
        if rootNode.customList[index] <  rootNode.cutomList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        # heapify whole tree after insertion
        heapifyInsert(rootNode,parentIndex,heapType)
    elif heapType == "Max":
        # if current element is greater than parent, do swapping
        if rootNode.customList[index] >  rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        # heapify whole tree after insertion
        heapifyInsert(rootNode,parentIndex,heapType)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Heap is already full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyInsert(rootNode,rootNode.heapSize,heapType)


newHeap = Heap(5)
insertNode(newHeap,4, "Max")
insertNode(newHeap,5, "Max")
insertNode(newHeap,2, "Max")
insertNode(newHeap,1, "Max")

levelOrderTraversal(newHeap)
