def dot_product(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of the same length")
    return sum(a * b for a, b in zip(vector_a, vector_b))

# Example usage
vec_a = [1, 2, 3]
vec_b = [4, 5, 6]
result = dot_product(vec_a, vec_b)
print("Dot product:", result)