class Solution:
    def kSmallestPairs(self, num1, num2, k):
        if not num1 or not num2 or k == 0:
            return []

        n1, n2 = len(num1), len(num2)
        heap = []

        for i in range(min(k, n1)):
            heapq.heappush(heap, (num1[i] + num2[0], i, 0))

        result = []
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([num1[i], num2[j]])
            if j + 1 < n2:
                heapq.heappush(heap, (num1[i] + num2[j + 1], i, j + 1))

        return result
