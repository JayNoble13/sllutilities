class Node():
    def init(self,value):
        self.value=value
        self.next=None

class SLL():
    def init(self, head):
        self.head=head

    def contains(value):
        if Node(value)==None:
            print("False")
            return False
        else:
            print("True")
            return True

    def add_front(self, value):
        temp=self.head
        self.head=Node(value)
        self.head.next=temp
        return self

# display list
    def display(self):
        runner=self.head
        count=1
        while(runner):
            print(f"this is your {count} node, it contains value {runner.value}")
            count +=1
            runner= runner.next
        return self


# length
    def length(self):
        runner=self.head
        count =0
        while(runner):
            count+=1
            runner=runner.next
        print(count)
        return count
