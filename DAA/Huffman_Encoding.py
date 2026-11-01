
# Job Sequencing with Deadlines using Greedy Method

# Input number of jobs
n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    job_id = input("Enter job ID: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))

    jobs.append((job_id, deadline, profit))

# Sort jobs according to profit in descending order
jobs.sort(key=lambda x: x[2], reverse=True)

# Find maximum deadline
max_deadline = max(job[1] for job in jobs)

# Create slots
slots = [None] * max_deadline

total_profit = 0

# Schedule jobs
for job_id, deadline, profit in jobs:

    # Find an empty slot before deadline
    for j in range(min(deadline, max_deadline) - 1, -1, -1):

        if slots[j] is None:
            slots[j] = job_id
            total_profit += profit
            break

# Display result
print("\nSelected Jobs:")

for i in range(max_deadline):
    if slots[i] is not None:
        print("Slot", i + 1, ":", slots[i])

print("Maximum Profit:", total_profit)
