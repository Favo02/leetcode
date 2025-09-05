class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        n_even, n_odd = n // 2, n // 2 + (n % 2)
        m_even, m_odd = m // 2, m // 2 + (m % 2)
        return n_odd * m_even + m_odd * n_even
