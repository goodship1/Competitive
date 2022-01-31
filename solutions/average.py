class Solution:
    def average(self, salary: List[int]) -> float:
        min_remove = min(salary)
        max_remove =  max(salary)
        result = []
        del salary[salary.index(min_remove)]
        del salary[salary.index(max_remove)]
        return sum(salary)/len(salary)
