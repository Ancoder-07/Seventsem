
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

"""
// Job Sequencing with Deadlines using Greedy Method

#include <iostream>
#include <string>
using namespace std;

const int MAX = 100;

string jobId[MAX];
int deadline[MAX];
int profit[MAX];

string slots[MAX];   // empty string "" means the slot is empty

int main() {

    int n;
    cout << "Enter number of jobs: ";
    cin >> n;

    // Input jobs
    for (int i = 0; i < n; i++) {
        cout << "Enter job ID: ";
        cin >> jobId[i];
        cout << "Enter deadline: ";
        cin >> deadline[i];
        cout << "Enter profit: ";
        cin >> profit[i];
    }

    // Sort jobs according to profit in descending order (bubble sort)
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (profit[j] < profit[j + 1]) {
                swap(jobId[j], jobId[j + 1]);
                swap(deadline[j], deadline[j + 1]);
                swap(profit[j], profit[j + 1]);
            }
        }
    }

    // Find maximum deadline
    int maxDeadline = deadline[0];
    for (int i = 1; i < n; i++) {
        if (deadline[i] > maxDeadline)
            maxDeadline = deadline[i];
    }

    int totalProfit = 0;

    // Schedule jobs
    for (int i = 0; i < n; i++) {

        // Find an empty slot before deadline
        for (int j = deadline[i] - 1; j >= 0; j--) {

            if (slots[j] == "") {
                slots[j] = jobId[i];
                totalProfit += profit[i];
                break;
            }
        }
    }

    // Display result
    cout << "\nSelected Jobs:" << endl;

    for (int i = 0; i < maxDeadline; i++) {
        if (slots[i] != "")
            cout << "Slot " << i + 1 << " : " << slots[i] << endl;
    }

    cout << "Maximum Profit: " << totalProfit << endl;

    return 0;
}
"""