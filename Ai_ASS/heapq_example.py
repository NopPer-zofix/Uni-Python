import heapq

heap = []
counter = 0

# Tuples are compared from left to right:
# first value, then second value, then counter if needed.
heapq.heappush(heap, (7, 3, counter, "A"))
counter += 1

heapq.heappush(heap, (7, 2, counter, "B"))
counter += 1

heapq.heappush(heap, (7, 2, counter, "C"))
counter += 1

heapq.heappush(heap, (5, 9, counter, "D"))
counter += 1

while heap:
    first, second, order, item = heapq.heappop(heap)
    print(first, second, order, item)