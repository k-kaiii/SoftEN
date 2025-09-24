class Solution:
    def search(self, arr: list[int], target: int) -> int:
        n = len(arr)
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m] == target:
                return m
            
            elif arr[m] < target:
                l = m + 1

            else:
                r = m - 1

        return -1
    
def main():
    arr = [15, 25, 30, 50, 60, 100]
    target = 100
    solution = Solution()
    result = solution.search(arr, target)
    print(result)

if __name__ == '__main__':
    main()