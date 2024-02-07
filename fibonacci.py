def catching_fibonacci():
    cache = {} # Порожній словник для кешування

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
         
    return fibonacci

# Приклад використання функції
fib = catching_fibonacci()
print(fib(10))
print(fib(15))