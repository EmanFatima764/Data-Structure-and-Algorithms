# from typying import List
class MinStack:
    # create a new stack 
    # add value and minimum valu
    
    def __init__(self):
        self.items=[]

    def push(self, val: int) -> None:
         
        if len(self.items)==0:
            self.items.append([val,val])
        else:
            mini=min(self.items[-1][1],val)
            self.items.append([val,mini])
    def pop(self) -> None:
        self.items.pop()
    def top(self) -> int:
        return self.items[-1][0]
        

    def getMin(self) -> int:
        if len(self.items)==0:
            return 0
        return self.items[-1][1]
        


# Your MinStack object will be instantiated and called as such:
if __name__=="__main__":

    obj = MinStack()
    obj.push(8)
    obj.push(7)
    obj.push(4)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_4)
    