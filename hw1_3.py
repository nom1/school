notice = "Please do not walk on the grass"
start = notice.index(" ")
end = notice.index("t")
x = notice[0:start]
stringLength = len(notice)
y = notice[end + 2:stringLength - 1]
print("x = " + x)
print("y = " + y)
print(x + y)
