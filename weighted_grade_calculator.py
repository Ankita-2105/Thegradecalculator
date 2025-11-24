def weighted_grade(scores, weights):
    """
    scores: list of scores (e.g., [85, 90, 80])
    weights: list of weights as decimals (e.g., [0.2, 0.3, 0.5])
    Returns: weighted grade
    """
    return sum(score * weight for score, weight in zip(scores, weights))

# Example usage:
scores = [85, 90, 80]
weights = [0.2, 0.3, 0.5]
final_grade = weighted_grade(scores, weights)
print("Weighted Grade:", final_grade)