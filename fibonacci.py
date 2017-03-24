_cache={}
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        '''
        #Looping, not recursive
        current=1
        previous=0
        for i in range(2,n+1):
            previous, current = current, current+previous
        return current
        '''

        #recursive without cache. 
        #return fibonacci(n-1)+fibonacci(n-2)

        #Recursive with cache

        if n not in _cache:
            _cache[n] = fibonacci(n-1)+fibonacci(n-2)
        return _cache[n]

    
if __name__ == "__main__":
    import time as t

    start=t.clock()
    print(fibonacci(6))
    print('Time - ', t.clock()-start)
    
    start=t.clock()
    print(fibonacci(10))
    print('Time - ', t.clock()-start)

    start=t.clock()
    print(fibonacci(340))
    print('Time - ', t.clock()-start)
'''
    start=t.clock()
    print(fibonacci(35))
    print('Time - ', t.clock()-start)

    start=t.clock()
    print(fibonacci(25))
    print('Time - ', t.clock()-start)

    start=t.clock()
    print(fibonacci(100))
    print('Time - ', t.clock()-start)
'''    
    
