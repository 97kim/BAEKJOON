a = input().split()

hour = int(a[0])
minute = int(a[1])

if minute < 45:
    hour = hour - 1
    minute = minute - 45 + 60
else:
    minute -= 45

if hour < 0:
    hour = 23

print(hour, minute)
