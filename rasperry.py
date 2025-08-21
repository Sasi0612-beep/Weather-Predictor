#recursion from 1 to n and from n to 1
# n=int(input("Enter the number : "))
# def recurssion(n):
#     if n==0:
#         return
#     else:
#         print(n)
#         recurssion(n-1)
    
# recurssion(5)
# def even_numbers(n):
#     if n==0:
#         return
#     if n%2==0:
#         print(n)
#     even_numbers(n-1)
        
# even_numbers(31)
class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs_scheduling(processes):
    time = 0
    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time
        process.waiting_time = time - process.arrival_time
        time += process.burst_time
        process.completion_time = time
        process.turnaround_time = process.completion_time - process.arrival_time

    return processes

# Example usage
processes = [Process(1, 0, 4), Process(2, 1, 3), Process(3, 2, 1)]
scheduled_processes = fcfs_scheduling(processes)

for process in scheduled_processes:
    print(f"Process {process.id}: Waiting Time = {process.waiting_time}, Turnaround Time = {process.turnaround_time}")

        
    
        
        

