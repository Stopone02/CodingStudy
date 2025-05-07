import heapq
import sys

n = int(sys.stdin.readline())

lHeap = []
rHeap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(lHeap) == len(rHeap):
        heapq.heappush(lHeap, -num) # -num : rootnode가 제일 큰 MaxHeap을 만들기 위함
    else:
        heapq.heappush(rHeap, num)

    if len(rHeap) != 0:
        if (-lHeap[0] > rHeap[0]):
            num1 = heapq.heappop(lHeap)
            num2 = heapq.heappop(rHeap)
            heapq.heappush(lHeap, -num2)
            heapq.heappush(rHeap, -num1)

    print(-lHeap[0])