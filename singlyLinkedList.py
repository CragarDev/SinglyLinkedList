# ***  Singly Linked Lists

"""

Objectives:

Learn how linked lists work
Learn more about pointers
Learn how to traverse through a linked list
Our class needs some methods! 

Let's start by adding a method that lets us add a node to the front of our list. 
We're going to take this slow.

Adding a Value to the Front

A common functionality of a list is to be able to add values, 

so let's add such a method to our class.

Just as we would pass in a value to a Python list's append method, 
our add_to_front method should accept a value to be added to the list:

"""


class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_to_front(self, val):
        # create a new node to hold the value and next
        new_node = SLNode(
            val
        )  # create a new instance of our Node class using the given value
        # set the next of the new node to the current head
        current_head = self.head  # save the current head in a variable
        # new_node.next = self.head

        new_node.next = (
            current_head  # SET the new node's next TO the list's current head
        )

        # set the list's head to our new node and set the next to the current head
        self.head = (
            new_node  # SET the list's head TO the node we created in the last step
        )
        self.length += 1
        return self  # return self to allow for chaining

    # This method won't require any input:
    def print_values(self):
        # We need to start at the front of our list, so let's create a pointer to our first node:
        runner = self.head  # a pointer to the list's first node

        # As long as the runner variable is pointing to a node:
        print()
        print("**********")
        while runner != None:  # iterating while runner is a node and not None
            # Let's print its value:
            print(runner.value)
            runner = runner.next  # set the runner to its neighbor
        print("**********  You have reached the end of the list")
        print()
        return self  # once the loop is done, return self to allow for chaining

    def add_to_back(self, val):
        # consider edge cases:
        if self.head == None:  # if the list is empty
            self.add_to_front(val)  # run the add_to_front method
            return self  # let's make sure the rest of this function doesn't happen if we add to the front

        # create a new node to hold the value and next
        new_node = SLNode(val)

        runner = self.head  # set an iterator to start at the front of the list

        while runner.next != None:  # iterate until the iterator doesn't have a neighbor
            runner = runner.next  # increment the runner to the next node in the list

        runner.next = new_node  # increment the runner to the next node in the list
        self.length += 1
        return self

    def search(self, val):
        runner = self.head
        while runner != None:
            if runner.value == val:
                return True
            runner = runner.next
        return False

    def remove_from_front(self):
        if self.head == None:
            return self
        self.head = self.head.next
        self.length -= 1
        return self

    def remove_from_back(self):
        if self.head == None:
            return self
        if self.head.next == None:
            self.remove_from_front()
            return self
        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        runner.next = None
        self.length -= 1
        return self

    def remove_val(self, val):
        if self.head == None:
            return self
        if self.head.value == val:
            self.remove_from_front()
            return self
        runner = self.head
        while runner.next != None:
            if runner.next.value == val:
                runner.next = runner.next.next
                self.length -= 1
                return self
            runner = runner.next
        return self

    def insert_at(self, val, n):
        if n > self.length:
            print(f"ERROR: {n} is greater than the length of the list")
            return self
        if n == 0:
            self.add_to_front(val)
            return self
        if n == self.length:
            self.add_to_back(val)
            return self
        runner = self.head
        for i in range(1, n):
            runner = runner.next
        new_node = SLNode(val)
        new_node.next = runner.next
        runner.next = new_node
        self.length += 1
        return self


"""
Take a moment to compare this functionality to appending a value to the front of an array. 
Hopefully you can see some of the benefits--no shifting necessary, 
no matter how many elements we have in our list!

* Traversing Through a List

Since this is pretty abstract, 
it might be helpful to have a function that goes through each node and prints its value. 
This is a great opportunity to learn how to traverse through a linked list. 
To iterate through an array, we used a for loop with an index as our iterator. 
However, since our linked list isn't indexed, 
we have to come up with a different iterator. 
We'll use a pointer that will, in a loop, point at each node.


* Traversing Through a List and Adding a Value to the End

Let's practice traversing one more time. 
If we want to add a new node anywhere in our list, 
it just needs to become a neighbor of an existing node. 
To become the last node in our list, 
the list's current last node needs to point to this new node.

"""


my_list = SLList()

my_list.add_to_front("Jim").add_to_front("Dwight").add_to_front("Andy")

my_list.print_values()


my_list2 = SLList()  # create a new instance of a list
my_list2.add_to_front("are").add_to_front("Linked lists").add_to_back(
    "fun!"
).print_values()  # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!
print(my_list2.search("fun!"))  # should return True
print(my_list.search("fun!"))  # should return False

print(my_list.length)  # should print 3
my_list.insert_at(
    "Michael", 2
).print_values()  # should print Jim, Dwight, Michael, Andy
my_list.remove_from_front().print_values()  # should print Dwight, Michael, Andy
my_list.insert_at("Pam", 2).print_values()  # should print Dwight, Michael, Andy, Pam
my_list.remove_from_back().print_values()  # should print Dwight, Michael, Andy
my_list.remove_val("Pam").print_values()


"""
If you're feeling discouraged, confused, or overwhelmed, don't worry. 
We guarantee you are not the only one. 
This is a really difficult concept to pick up the first time around. 
Just keep practicing and breaking down each step one line at a time. 
Try to figure out which parts don't make sense and then talk it out with a classmate, TA, or instructor.

Once you have a good grasp of this idea of nodes with pointers, 
you have the building blocks for building some other really neat data structures like binary search trees, tries, graphs, and more. 

As it's such a critical concept, practice and review the code above so that 
you are able to re-create the code demonstrated above without looking at the platform. 

Make sure you feel very comfortable with adding a new node, 
traversing through the linked list, etc. 
Once you can create both SList and Node without looking at the codes above, 
then move on to some of the additional challenges.


* Additional Challenges

These are challenging! 
Hop up to a whiteboard, grab a cohort mate if available, 
and try to work through these together.

    - remove_from_front(self) - remove the first node and return its value
    - remove_from_back(self) - remove the last node and return its value
    - remove_val(self, val) - remove the first node with the given value

Consider the following cases:

    - the node with the given value is the first node
    - the node with the given value is in the middle of the list
    - the node with the given value is the last node

    - insert_at(self, val, n) - insert a node with value val as the nth node in the list

Consider the following cases:
    - n is 0
    - n is the length of the list
    - n is between 0 and the length of the list

"""
