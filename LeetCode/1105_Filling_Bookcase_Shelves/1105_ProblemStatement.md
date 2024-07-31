# 1105_Filling_Bookcase_Shelves

## Problem Statement

You are given an array `books` where `books[i] = [thickness_i, height_i]` indicates the thickness and height of the `i`-th book. You are also given an integer `shelfWidth`.

You need to place these books in order onto bookcase shelves that have a total width of `shelfWidth`. 

You can place books on a shelf such that the sum of their thicknesses is less than or equal to `shelfWidth`. After placing books on a shelf, the height of the bookcase increases by the maximum height of the books on that shelf. You need to repeat this process until all books are placed.

Note that the order of the books must be preserved as given.

### Example 1

**Input:**

```python
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
```

**Output:**

```
6
```

**Explanation:**

The sum of the heights of the 3 shelves is `1 + 3 + 2 = 6`. Note that book number 2 does not have to be on the first shelf.

### Example 2

**Input:**

```python
books = [[1,3],[2,4],[3,2]]
shelfWidth = 6
```

**Output:**

```
4
```

### Constraints

- `1 <= books.length <= 1000`
- `1 <= thickness_i <= shelfWidth <= 1000`
- `1 <= height_i <= 1000`

