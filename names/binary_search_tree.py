class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  
        # check if empty
        # if empty put node here @ root
        # else if new node < node.value, go left
        #  if >= go right, insert(value)
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)

            else:
                self.left.insert(value)
        else: 
            # >=
            if not self.right:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # at start, self will be root
        # compare target against self
        # 
        # when searching fo False: we know we need to go in 1 direction
        # but there's nothing in the left or right direction

        if target == self.value:
            return True
        if target < self.value:
            # go left
            if not self.left:
                return False
            return self.left.contains(target)

        else:
            # go right
            if not self.right:
                return False
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # if there's a right
        if self.right:
            return self.right.get_max()
        else:
            # return root
            return self.value


    # Class Notes

    # def iterative_get_max(self):
    # current_max = self.value 

    # current = self
    # # traverse our structure
    # while current is not None:
    #     if current.value > current_max:
    #         current_max = current.value
    #     # update our current_max variable if we see a larger value 
    #     current = current.right

    # return current_max


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Class Notes
    # def iterative_for_each(self, fn):
    # stack = [] 

    # # add the root node
    # stack.append(self)

    # # loop so long as the stack still has elements 
    # while len(stack) > 0:
    #     current = stack.pop()
    #     if current.right:
    #         stack.append(current.right)
    #     if current.left:
    #         stack.append(current.left)

    #     fn(current.value)