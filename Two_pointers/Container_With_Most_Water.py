class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            best = max(best, area)

            if height[l] <= height[r]:
                l += 1   # parede esquerda é menor, move ela
            else:
                r -= 1   # parede direita é menor, move ela

        return best