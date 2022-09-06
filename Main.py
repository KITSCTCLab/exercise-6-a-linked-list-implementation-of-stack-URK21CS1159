class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
        node = Node(data)  
        if(self.head == None):   
            self.head = node
        else:
            node.next = self.top  
            self.head = node    


  def pop(self) -> None:
    # Write your code here
        if(self.head == None):    
            return None
        else:
            node = self.head  
            self.head = node.next   
            node.next = None  
            data = node.value    
            del node   
            
            
  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  
       if(self.head == None):    
            return false
       else:
            temp = self.head  
            while(temp != None):   
                print(f'{temp.value}->',end = '')
                emp = temp.next 
            print()


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
