print(f'loading run.py: name = { __name__}')
import pythondeepdive.imported.module1
import pythondeepdive.imported.timing as timing

code = '[x**2 for x in range(1000)]'
result = timing.timeit(code, 100)
print(result)

