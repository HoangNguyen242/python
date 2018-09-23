def generate_num():
    num = 0
    while True:
        yield num
        num = num + 1

nums = generate_num()
print(type(nums))
for x in nums:
    print(x)
    if x > 4:
        break