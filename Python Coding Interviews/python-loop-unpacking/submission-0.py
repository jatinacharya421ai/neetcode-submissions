from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_score, best_student_name = -1, ""
    for student, score in scores:
       if score > best_score:
         best_score, best_student_name = score, student
    return best_student_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))