class Logger:

    def __init__(self):
        self.hash = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        next_timestamp = timestamp + 10
        if not message in self.hash:
            self.hash[message] = next_timestamp
            return True
        
        if timestamp < self.hash[message]:
            return False
        
        self.hash[message] = next_timestamp
        return True
            
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)