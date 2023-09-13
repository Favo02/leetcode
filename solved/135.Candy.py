class Solution(object):
  def candy(self, ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    N = len(ratings)
    print(ratings)
    candies = [1] * N

    for i in range(1, N):
      if ratings[i] > ratings[i-1]:
        candies[i] = candies[i-1]+1

    for i in range(N-2, -1, -1):
      if ratings[i] > ratings[i+1]:
        if not candies[i] > candies[i+1]:
          candies[i] = candies[i+1]+1
    
    print(candies)
    res = sum(candies)
    print(res)
    return res

Solution.candy(0, [1,0,2]) # 5
Solution.candy(0, [1,2,2]) # 4
Solution.candy(0, [1,3,2,2,1]) # 7
Solution.candy(0, [1,2,87,87,87,2,1]) # 13
Solution.candy(0, [1,3,4,5,2]) # 11

