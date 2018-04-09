info = [int(n) for n in input().strip().split()]

taskLength = sorted([int(n) for n in input().strip().split()])
workTime = sorted([int(n) for n in input().strip().split()])
taskLength = taskLength[:len(workTime)]
workableTimes = []

for i in reversed(range(len(workTime))):
    if i < len(taskLength):
        if workTime[i] < taskLength[i]:
            workTime.pop(0)
            taskLength.pop()
        else:
            workableTimes.append(i)

print(len(workableTimes))
