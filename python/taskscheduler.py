class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        len_task = len(tasks)
        task_to_count = {task:0 for task in set(tasks)}
        for task in tasks:
            task_to_count[task] += 1
        highest = max(task_to_count.values())
        maxfrequency = len([k for k, v in task_to_count.items() if v == highest])
        interval = (highest-1)*(n-maxfrequency+1)+highest*maxfrequency
        return max(len_task, interval)
