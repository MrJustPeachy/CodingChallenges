data = [int(n) for n in input().strip().split()]

test_cases = data[0]
totalTime = data[1]

tasks = [int(n) for n in input().strip().split()]

tasksCompleted = 0

for task in tasks:
    totalTime -= task

    if totalTime >= 0:
        tasksCompleted += 1

print(tasksCompleted)