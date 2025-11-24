# Project Statement: The Grade Calculator

#Problem statement:

Students and educators often face difficulties in quickly and accurately calculating final course grades under complex weighted scoring schemes. The manual calculation process is time-consuming and prone to human error, leading to uncertainty in academic standing. The project addresses this by providing a reliable, instantaneous computational tool.

# Scope of the project:

The project is strictly limited to a single-file, command-line Python utility. The scope focuses on demonstrating core programming concepts without incorporating advanced features like graphical user interfaces or database integration.

# In-Scope Boundaries (What the project does):

Collection of scores and weights for three fixed categories: Homework, Midterm, and Final Exam.

Implementation of robust input validation (numeric and range checking, $0\%-100\%$).

Accurate calculation of the weighted average.

Output of the final percentage and corresponding letter grade.

# Out-of-Scope Boundaries (What the project does NOT do):

Graphical User Interface (GUI) development.

Data persistence (saving results or grades to a file).

Dynamic adjustment of the number of grading categories.

# Target users:

Students: Seeking a simple, error-free tool to monitor their progress and simulate final grade outcomes based on anticipated scores.

Educators/Teaching Assistants: Requiring a portable script to quickly verify grade calculations or test various grading policies.

# High-level features:

Controlled Input: Utilizes modular functions to actively enforce numeric input and range limits, ensuring data integrity.

Weighted Summation: Contains the core arithmetic logic to correctly perform the weighted average formula.

Error Resilience: Implements the try-except structure to handle invalid user inputs gracefully (e.g., typing text instead of a number).

Conditional Output: Applies if-elif-else logic to automatically translate the calculated percentage into a discrete letter grade.
