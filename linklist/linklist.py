
#A program to count number of nodes in a singly linked circular list


#creating node
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

#creating class for linkedlist
class LinkedList:

    def __init__(self):
        self.head = None


#a function to add elements to the list we created

    def push_to_list(self, newElement):
        newNode = Node(newElement)
        
        if(self.head == None):
            
            self.head = newNode
            newNode.next = self.head
            return
    
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
                
            temp.next = newNode
            newNode.next = self.head
    

    #A function to count nodes in the list

    def countNodes(self):
        temp = self.head

        i = 0

        if (temp !=None):

            i += 1

            temp = temp.next
        
        while (temp !=self.head):

            i += 1

            temp = temp.next
        
        return i



#Printing the data put in the list

    def PrintList(self):

        temp = self.head
        
        if(temp != None):
            
            print("The list contains:", end=" ")
            
            while (True):
                
                print(temp.data, end=" ")
                
                temp = temp.next
                
                if(temp == self.head):
                    break
                    
            print()
        
        else:
            
            print("The list is empty.")

# testing the code                  

MyList = LinkedList()

#Adding some elements in the list.
MyList.push_to_list(2)
MyList.push_to_list(5)
MyList.push_to_list(10)
MyList.push_to_list(17)
MyList.push_to_list(20)



#Displaying the elements in the list.
MyList.PrintList()


#The number of nodes in the list

print( "Number of nodes in the list is: ", MyList.countNodes())

