# **Vector Dot Product Implementation**

## **Introduction**  
> The _dot product_ is a fundamental operation in linear algebra that takes two vectors and returns a scalar value. This operation is widely used in fields such as:
- Physics
- Machine Learning
- Computer graphics

---

## **Mathematical Expression**  
The dot product of two vectors _A_  and _B_, each of size $\ n \$, is calculated as:

$$\[
\mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} A_i B_i = A_1 B_1 + A_2 B_2 + \cdots + A_n B_n
\]$$

---

## **Code Example**  

Below is a snippet of the implementation in Python:  

```python
def dot_product(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of the same length")
    return sum(a * b for a, b in zip(vector_a, vector_b))

# Example usage
vec_a = [1, 2, 3]
vec_b = [4, 5, 6]
result = dot_product(vec_a, vec_b)
print("Dot product:", result)
```
---
## Here is a diagram elaborating the mathematical equation graphically.[^1]

![vector dot product](dot_product.png)

[^1]: This image has been taken from `https://byjus.com/maths/dot-product-of-two-vectors/`.

> [!WARNING]
> Information should be handled safely.


| version of algorithm       | time complexity          | space complexity  |
| ------------- |:-------------:| -----:|
| version 1      | O($n^2$) | O($n^2$) |
| version 2     | O($n^2$)     |  O(nlogn) |
| version 3 | O(nlogn)      |    O($n^2$) |

For more help you can visit [Byju's website](https://byjus.com/)

Here is a list of all what has been included in this readme file:
- [x] Headings
- [x] styling
- [x] text quoting
- [x] lists
- [x] checklists
- [x] links
- [x] images
- [x] tables
- [x] footnotes
- [x] mathematical equations
- [x] code
- [x] alerts
- [x] emojis

For our hardwork here's a little celebration :tada: :tada:      
