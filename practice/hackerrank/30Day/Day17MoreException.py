class Calculator:
    def power(self, first, second):
        if first < 0 or second < 0:
            raise ValueError("n and p should be non-negative")
        else:
            return first**second


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
