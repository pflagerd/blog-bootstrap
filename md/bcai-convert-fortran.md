# BCAI's conversion of our Fortran 'nsqrt' code

## Experiment 1

### Prompt: "Please translate the following Fortran code into working Python."
    (Paste nsqrt.f)

### BCAI Notes:
    - Below is a direct translation of the Fortran program into working Python.
      The code reproduces the integer Newton iteration function nsqrt and the
      outer loops that exercise it. It keeps the same algorithmic behavior and
      integer divisions as the original Fortran.

    - This code mirrors the integer behavior of the Fortran program (uses integer
      division //).

    - It allocates values indexed from 1..MAXVAL (index 0 unused) to match the
      Fortran array indexing.

    - Running this will perform the same amount of work as the original Fortran
      program (it is intentionally heavy: 100 * 1,000,000 calls to nsqrt). If you
      want to test quickly, lower MAXVAL or SETS.

### BCAI's generated Python code: nsqrt.f to expt1.py

```python

# Test sqrt alg efficiency - Python translation of the Fortran example

MAXVAL = 1_000_000
SETS = 100

def nsqrt(s: int) -> int:
    """Integer square root using Newton's method, translated from the Fortran nsqrt.
       Returns the integer floor(sqrt(s)) using the same iteration and stopping criteria.
    """
    if s <= 0:
        return 0

    x0 = 1
    x1 = 1
    x2 = (1 + s) // 2

    # Iterate until x2 equals x1 or x0 (mirrors the Fortran GOTO loop)
    while True:
        if x2 == x1 or x2 == x0:
            break
        x0 = x1
        x1 = x2
        # integer division to mimic Fortran INTEGER behavior
        x2 = (x2 + s // x2) // 2

    # Final adjustment exactly as in the Fortran code
    if x2 * x2 > s:
        return x1
    else:
        return x2

def main():
    print("MAXVAL =", MAXVAL, ", SETS =", SETS)
    print("Start looping...")

    # create list with indices 0..MAXVAL; Fortran used 1..MAXVAL
    values = [0] * (MAXVAL + 1)

    for _set in range(SETS):
        for i in range(1, MAXVAL + 1):
            values[i] = nsqrt(i)

    print("Done looping.")

if __name__ == "__main__":
    main()

```

## Experiment 2: Try the previous experiment after removing hints of 'sqrt' in the code.

### Edit nsqrt.f to produce expt2.f
```
-> diff nsqrt.f expt2.f
1,5c1
< C Test sqrt alg efficiency
< C On laptop / cygwin, compile with 'gfortran tester.f' and
< C     run by './a.exe'
< C
<       PROGRAM Sqrts
---
>       PROGRAM Example
13c9
<       INTEGER nsqrt
---
>       INTEGER result
22,23c18,19
<               values(i) = nsqrt(i)
< C             PRINT *, "nsqrt(", i, ") is", values(i)
---
>               values(i) = result(i)
> C             PRINT *, "result(", i, ") is", values(i)
32c28
<       INTEGER FUNCTION nsqrt(s)
---
>       INTEGER FUNCTION result(s)
53c49
<           nsqrt = x1
---
>           result = x1
55c51
<           nsqrt = x2
---
>           result = x2

```

### BCAI's generated Python for expt2.f: expt2.py

```python

# Translated from the Fortran example to Python

MAXVAL = 1_000_000
SETS = 100

def result(s: int) -> int:
    """Integer square-root-like result function translated from Fortran.
    Performs integer arithmetic only, matching the original iteration.
    """
    if s <= 0:
        # Fortran code doesn't handle non-positive explicitly; return 0 for s<=0
        return 0

    x0 = 1
    x1 = 1
    x2 = (1 + s) // 2

    # Iterate until x2 equals previous value(s)
    while not (x2 == x1 or x2 == x0):
        x0 = x1
        x1 = x2
        x2 = (x2 + s // x2) // 2

    # Choose the integer that does not exceed the true sqrt
    if x2 * x2 > s:
        return x1
    else:
        return x2

def main():
    print(f"MAXVAL = {MAXVAL}, SETS = {SETS}")
    print("Start looping...")
    # Pre-allocate list (0-based in Python, use indices 0..MAXVAL-1 for values(1..MAXVAL))
    values = [0] * MAXVAL

    for _set in range(SETS):
        for i in range(1, MAXVAL + 1):
            # values(i) = result(i) in Fortran; map i->index i-1 in Python list
            values[i - 1] = result(i)

    print("Done looping.")

if __name__ == "__main__":
    main()

```

## Comparative results

- nsqrt.f / expt2.f (within 0.09 seconds real time): about 10 seconds
- expt1.py: 1m48.710s
- expt2.py: 1m50.953s

## Comparison of generated code (expt1.py vs expt2.py)
```python

-> diff -y --suppress-common-lines expt1.py expt2.py
# Test sqrt alg efficiency - Python translation of the Fortra |    # Translated from the Fortran example to Python
def nsqrt(s: int) -> int:                      |    def result(s: int) -> int:
    """Integer square root using Newton's method, translated  |        """Integer square-root-like result function translated fr
       Returns the integer floor(sqrt(s)) using the same iter |        Performs integer arithmetic only, matching the original i
                                  >            # Fortran code doesn't handle non-positive explicitly
    # Iterate until x2 equals x1 or x0 (mirrors the Fortran G |        # Iterate until x2 equals previous value(s)
    while True:                                               |        while not (x2 == x1 or x2 == x0):
        if x2 == x1 or x2 == x0:                              <
            break                                             <
        # integer division to mimic Fortran INTEGER behavior  <
    # Final adjustment exactly as in the Fortran code         |        # Choose the integer that does not exceed the true sqrt
    print("MAXVAL =", MAXVAL, ", SETS =", SETS)               |        print(f"MAXVAL = {MAXVAL}, SETS = {SETS}")
                                                              |        # Pre-allocate list (0-based in Python, use indices 0..MA
    # create list with indices 0..MAXVAL; Fortran used 1..MAX |        values = [0] * MAXVAL
    values = [0] * (MAXVAL + 1)                               <
            values[i] = nsqrt(i)                              |                # values(i) = result(i) in Fortran; map i->index
                                                              >                values[i - 1] = result(i)
```
