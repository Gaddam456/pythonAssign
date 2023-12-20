class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)  == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("queue id empty")
            return -1
        
    def size(self):
        return len(self.items)
    

    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            print("queue id empty")
            return -1
    def output(self):
        return self.items


def isValidParenthesis(s):
    q = Queue()
    stropen = ""
    strclose = ""
    for i in s:
        if i in "([{":
            stropen += i
        elif i in ")]}":
            strclose += i
    strclose = strclose[::-1] # reversed(strclose)
    stropen += strclose
    for i in stropen:
        if i in "([{":
            q.enqueue(i)
        elif i in ")]}":
            if q.isEmpty():
                return False
            top = q.dequeue() # [
            if (i == ")" and top != "(") or (i == "]" and top != "[") or (i == "}" and top != "{"):
                return False
    return q.isEmpty()
    
print(isValidParenthesis("([)]"))  # --> False queue --> true
print(isValidParenthesis("([{}])")) # --> True ([{)]}  stack --> false
print(isValidParenthesis("({]})")) # --> False