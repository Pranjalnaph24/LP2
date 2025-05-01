# Assignment-A3.IV (Job Scheduling)

class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling():
    n = int(input("Enter the number of jobs you want to enter: "))
    jobs = []

    print("Enter the details of the jobs: ")
    for i in range(n):
        print(f"Job {i + 1} :")
        job_id = int(input("Enter the ID of the job: "))
        deadline = int(input("Enter the deadline of the job: "))
        profit = int(input("Enter the profit of the job: "))
        jobs.append(Job(job_id, deadline, profit))

    # Sort jobs by decreasing profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)
    slots = [0] * (max_deadline + 1)

    total_profit = 0

    for job in jobs:
        # Try to schedule the job in the latest possible slot
        for i in range(job.deadline, 0, -1):
            if slots[i] == 0:
                slots[i] = job.id
                total_profit += job.profit
                break

    print("Scheduled Jobs:", end=" ")
    for i in range(1, len(slots)):
        if slots[i] != 0:
            print(slots[i], end=" ")

    print(f"\nTotal Profit: {total_profit}")

# Run the function
job_scheduling()
