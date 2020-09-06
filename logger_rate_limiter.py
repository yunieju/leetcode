from collections import defaultdict
class Logger:

    def __init__(self):
        self.logger = defaultdict()
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logger:
            if timestamp - self.logger[message] >= 10:
                self.logger[message] = timestamp
                return True
            else:
                return False
        else:
            self.logger[message] = timestamp
            return True
                
                
        
        
      


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
