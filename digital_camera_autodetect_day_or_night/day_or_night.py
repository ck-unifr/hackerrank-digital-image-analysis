#https://www.hackerrank.com/challenges/digital-camera-day-or-night/problem

# raw = raw_input().split(" ")
raw = input().split(" ")
sum_raw = 0

for i in range(len(raw)):
    line = raw[i].split(",")
    sum_raw += (int(line[0])+int(line[1])+int(line[2]))/3
sum_raw = sum_raw/len(raw)

if sum_raw < 80:
    print("night")
else:
    print("day")