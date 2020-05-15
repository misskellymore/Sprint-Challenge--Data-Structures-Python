class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest_node = None
        self.next_oldest = None
        self.ring = []


    # When the ring buffer is full and a 
    # new element is inserted, the oldest 
    # element in the ring buffer is overwritten 
    # with the newest element

    # When the ring buffer is full and a new 
    # element is inserted, the oldest element in 
    # the ring buffer is overwritten with the newest 
    # element

    def append(self, item):
        # if there's no oldest item
        # set to zero and append
        if self.oldest_node is None:
            self.oldest_node = 0
            return self.ring.append(item)
        
        # if the items do exisit 
        # and of the length of the ring +1 is less than cap   
        
        elif len(self.ring) + 1 <= self.capacity:
            # set the next_oldest to 1
            self.next_oldest = 1
            # and append ring
            return self.ring.append(item)

        else:
            # set the oldest node in the ring to item            
            self.ring[self.oldest_node] = item            
            self.oldest_node += 1
            # if its greater than capacity
            if self.oldest_node + 1 > self.capacity:
                # poof
                self.oldest_node = 0

        

    def get(self):
        return self.ring