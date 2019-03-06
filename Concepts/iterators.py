class Remote():
    def __init__(self,channels):
        self.channels = channels
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index > len(self.channels):
            raise StopIteration

        return self.channels[self.index]


channels = ["HBO","Star Movies","CNN","Star World"]
tv = Remote(channels)
for i in range(len(channels)):
    print (tv.__next__())

