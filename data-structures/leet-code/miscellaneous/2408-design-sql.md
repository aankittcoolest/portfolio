## Design SQL
- Ref: https://leetcode.com/problems/design-sql/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency


### Approach
```py
class SQL:

    dict = {}
    names = List[str]
    columns = List[int]

    def __init__(self, names: List[str], columns: List[int]):
        self.names = names
        for name in self.names:
            self.dict[name] = []
        self.columns = columns

    def insertRow(self, name: str, row: List[str]) -> None:
        row.append(False)
        self.dict[name].append(row)

    def deleteRow(self, name: str, rowId: int) -> None:
        rowId = rowId - 1
        row = self.dict[name][rowId]
        row[len(row)-1] = True

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        rowId = rowId - 1
        columnId = columnId - 1
        return self.dict[name][rowId][columnId]
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)
```