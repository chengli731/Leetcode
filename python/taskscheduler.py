class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        len_task = len(tasks)
        d = {x:tasks.count(x) for x in tasks}
        highest = max(d.values())
        maxfrequency = len([k for k, v in d.items() if v == highest])
        interval = (highest-1)*(n-maxfrequency+1)+highest*maxfrequency 
        if interval>= len_task:
            return interval
        else:
            return len_task
