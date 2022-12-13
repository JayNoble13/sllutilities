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

    def display(self):
        runner=self.head
        count=1
        while(runner):
            print(f"this is your {count} node, it contains value {runner.value}")
            count +=1
            runner= runner.next
        return self

    def length(self):
        runner=self.head
        count =0
        while(runner):
            count+=1
            runner=runner.next
        print(count)
        return count

    def maxmove(self):
        runner= self.head
        max=runner.value
        while runner !=None:
            if max < runner:
                max=runner
            runner= runner.next
        print(self.head.value)
        return self

#
    def minmove(self):
        runner= self.head
        min=self.head.value
        while runner !=None:
            if min > runner.value:
                min=runner.value
            runner= runner.next
        print(self.head.value)
        return self

new_sll = SLL(Node(0))
new_sll.add_front(4).add_front(6).add_front(10).add_front(-5)
new_sll.contains()
new_sll.display()
new_sll.length()
new_sll.maxmove()
new_sll.display()
new_sll.minmove()
new_sll.display()