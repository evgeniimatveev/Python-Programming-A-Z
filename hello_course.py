"""
Quick overview script for the Python-Programming-A-Z repository.

It prints the main sections of the course and what you will learn in each.
"""

sections = [
    ("S1 - Python Basics", "Core fundamentals: variables, types, strings, lists, dicts"),
    ("S2 - Control Flow & Functions", "If/else, loops, list comprehensions, functions, files"),
    ("S3 - Data Science & Advanced Topics", "NumPy, Pandas, Matplotlib, Seaborn, real datasets"),
]


def print_course_overview():
    print("\n🐍 Python Programming A-Z – course overview\n")
    print(f"{'Section':<35} | Topics")
    print("-" * 80)
    for name, topics in sections:
        print(f"{name:<35} | {topics}")
    print("\nTip: open the corresponding Jupyter notebooks in each section and code along.\n")


if __name__ == "__main__":
    print_course_overview()
