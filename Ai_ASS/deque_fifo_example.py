from collections import deque

q = deque()

q.append("A")
q.append("B")
q.append("C")

print(q.popleft())   # A
print(q.popleft())   # B
print(q.popleft())   # C