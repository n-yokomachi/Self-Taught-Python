def do(func):
    func()

def thanks():
    print("ありがとう")

def hi():
    print("やあ！")
    
condition = 1
if condition == 1:
    do(thanks)
else:
    do(hi)