class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        ans = []
        ans2 = []

        for i in nums:
            res[i] += 1

        ans = list(res.values())
        ans = sorted(ans, reverse = True)

        for n in ans:
            for key, v in res.items():
                if v == n and key not in ans2:
                    ans2.append(key)

        return ans2[:k]
