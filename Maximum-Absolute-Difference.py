class Solution:
    # @param A : list of integers
    # @return an integer
     def maxArr(self, A):

        positive = []
        negative = []
        for i in range(len(A)):
            positive.append(A[i] + i )
            negative.append(A[i] - i)

        answer1 = abs(max(positive) - min(positive))
        answer2 = abs(max(negative) - min (negative))

        return max(answer1, answer2)