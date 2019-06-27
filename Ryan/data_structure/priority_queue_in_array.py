# https://www.geeksforgeeks.org/priority-queue-in-python/
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, val):
        self.queue.append((val))

    def pop(self):
        self.queue.sort()
        del self.queue[-1]
    def pop1(self):
        max_ind=0
        if not self.queue:
            return []
        max_value=self.queue[0]
        for i in range(len(self.queue)):
            if self.queue[i]>=max_value:
                max_value=self.queue[i]
                max_ind=i
        temp=self.queue[max_ind]
        del self.queue[max_ind]
        return temp

    def __str__(self):
        return " ".join([str(i) for i in self.queue])


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.pop1()
    print("empty pq", pq, "pop1 is ", pq.pop1())
    pq.push(3)
    pq.push(2)
    pq.push(4)
    pq.push(3)
    print(pq)
    pq.pop1()
    print(pq)
