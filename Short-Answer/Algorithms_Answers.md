#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
  a = 0 # O(1)
  while (a < n * n * n): # O(N)
    a = a + n * n 
```

The runtime complexity of this algorithm is O(N) because the only variable the algorithm depends on is N, and there is only one loop. A is a constant, so despite the amount of arithmetic occurring, since N is the only number that can fundamentally change the scope of the runtime, it is said to be O(N).

b)

```python
sum = 0 #O(1)
  for i in range(n): #O(N)
    j = 1 #O(1)
    while j < n: #O(Log N)
      j *= 2 # Exponential increase
      sum += 1 #O(1)
```

The runtime complexity of this algorithm is O(N Log N). This is because there are two loops, one nested inside of the other, that have dependence on N. However, the inner loop, which depends on approaching N, increases exponentially, so the time to reach N is halved. Thus, instead of O(N^2), the time complexity os O(N Log N)


c)

```python
def bunnyEars(bunnies):
  if bunnies == 0: #O(1)
    return 0

  return 2 + bunnyEars(bunnies-1) #O(N)
```

The runtime complexity of this algorithm is O(N). This is due to the bunnyEars function having a single recursive callstack, and resolving once bunnies reaches 0. The single dependency and isolated callstack means that this function resolves once one condition is met, hence the O(N) complexity.

## Exercise II

N-story building
~
~
~
~
~
~ Mid --> begin search here
~
~
~
~
~

Egg breaks once being thrown off of floor F or higher. How to **minimize** number of dropped and broken eggs?

My first instinct is to start at floor 0, and progress linearly up the floors until we reach the first instance of an egg breaking. This will minimize broken eggs. However, the question asks us to balance the number of broken eggs **and** dropped eggs. So while we might be minimizing broken eggs with this approach, we are not minimizing the number of dropped eggs.

Therefore, since the floors of a building **have** to be sorted, I recommend implementing a binary search algorithm to determine the floor of F at which an egg breaks. Slice the # of floors(f) in half, and drop an egg at that middle floor. If broken at mid, eliminate upper half of floors and work down until the egg does not break. If not broken, eliminate bottom half and work up until egg breaks.

This provides a balance of eggs dropped and eggs broken. It also affords us a very efficient runtime complexity of O(Log N), which is much faster at scale than O(N).



