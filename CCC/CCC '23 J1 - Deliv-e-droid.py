deli = int(input())
obs = int(input())
deli_point = deli * 50
obs_point = obs * 10
f = deli_point - obs_point
if deli > obs:
    print(f + 500)
else:
    print(f)
