# DJF Walking throught the problem

## Statement

"Given an image represented by an NxN matrix, where each pixel in
the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you
do this in place?"

## Ontology??
- image:
    - photograph?
    - jpg or other image file?
- matrix: rectangular grid of numbers
- pixel: atomic components of an image = a "cell" with independent light / color values from sensors
- bytes: number of bits in a computer representation of a "character"
- rotate: Imagine the image is printed on a piece of paper, which is spun counter-clockwise

## Interpretation

- The problem reduces to writing code to "spin" a rectangular grid of numbers so that:
    - the top row becomes the left-most column
    - the left-most column becomes the bottom row
    - the bottom row becomes the right-most column
    - the right-most column becomes the top row
    

## First analysis

- Take the hint to rotate the outer layer, then the next layer inward, and so on.

- 4x4, outer layer:

```
    top row to left col
        [0, c] -> [n-1-c, 0]; c in 0 ... n-1

    right col to top row
        [r, n-1] -> [0, r];  r in 0 ... n-1 

    bottom row to right col
        [n-1, c] -> [n-1-c, n-1];  c in 0 ... n-1

    left col to bottom row
        [r, 0] -> [n-1, r];  r in 0 ... n-1
```

- 4x4 outer layer rewrite:

```
    r == 0 :  [r, c] -> [n-1 - c, r]
    c == n-1: [r, c] -> [n-1 - c, r]
    r == n-1: [r, c] -> [n-1 - c, r]
    c == 0 :  [r, c] -> [n-1 - c, r]
```

- 4x4 outer layer general rule:

```
    [r, c] -> [n-1 -c, r]
```

- Claim: the rule fits the general case
    - The rule works for the next layer inward (3x3) because we never specified n.  

    - Therefore:  general rule:  

```
    [r, c] -> [n-1 -c, r]
```

## Can we decompose this rule into transformations we already know?
- top-bottom flip

```
    [x, y] -> [n-1 - x, y]
```

- spin on rising axis:

```
    0,   0   ->  n-1, n-1
    0,   n-1 ->  0,   n-1
    n-1, 0   ->  n-1, 0
    n-1, n-1 ->  0,   0
    1, 3     ->  n-1 -3, n-1 -1

    [r, s] -> [n-1 - s, n-1 - r]
```

- spin on flip about falling axis:
    - This is matrix transposition

```
    [r, s] -> [s, r]
```

- Composition of rising axis spin and top-bottom flip

```
    [x, y] : flip top-bottom : spin on rising axis

    [x, y] -> [n-1 - x, y] -> [n-1 - (y), n-1 - (n-1 - x)]
    [x, y] -> [n-1 - y, x]
    or
    [r, c] -> [n-1-c, r]
```

    - This is the same as our general rule, above.

