import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency = defaultdict(int)
        for task in tasks:
            task_frequency[task] += 1

        max_heap = []
        for task in task_frequency:
            heapq.heappush(max_heap,(task_frequency[task]*-1, task))

        cycles = 0
        while max_heap:
            new_tasks = []
            #we can execute n+1 tasks because the first task needs to wait for n seconds
            for i in range(n+1):
                if max_heap: 
                    task = heapq.heappop(max_heap)
                    new_tasks.append(task)
                    
            for task in new_tasks:
                task_freq = task[0] + 1
                task_name = task[1]
                if task_freq < 0:
                    heapq.heappush(max_heap, (task_freq, task_name))
            cycles += len(new_tasks) if not max_heap else n+1
                
        return cycles


