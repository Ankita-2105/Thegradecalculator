# Thegradecalculator
# A robust Python command-line utility for calculating final course grades using weighted averages across three fixed categories. Features reliable input validation, error handling (`try-except`), and accurate letter grade assignment. Demonstrates core functions and control flow.

## Its primary function is to automate the calculation of a student's final course percentage and corresponding letter grade based on a weighted average of the core assessment categories (Homework, Midterm, and Final Exam). This project demonstrates the practical application of essential programming principles, particularly functional decomposition, robust error handling (using try-except blocks), and conditional logic (if-elif-else) to ensure an accurate and reliable result.

# This project runs on only python codes.
# This is a little command-line tool I built to make calculating grades fast and easy. Since it's built entirely in Python, you can run it anywhere and get an instant, accurate final score for any class.

## The python version used in this is python 3.13.

# Features:
## This grade calculator is designed to be simple, efficient, and easy to use directly from the terminal.
## Intuitive Command-Line Interface: Easy to input category names, scores, and weights without needing a graphical interface.

# How to Use It??
## Open your terminal or command prompt.
## Navigate to the folder where you saved the script.
## Clean Output: Gives you the final percentage, rounded off, along with the corresponding letter grade.

# The screenshots of the code used are given below:
<img width="975" height="993" alt="Screenshot (57)" src="https://github.com/user-attachments/assets/27013e95-2ebc-4a5a-9b00-a33438dfb5de" />
<img width="723" height="736" alt="Screenshot (58)" src="https://github.com/user-attachments/assets/9695dfe5-7d2a-4305-ae03-3d8ff9da3984" />
<img width="1668" height="322" alt="Screenshot (60)" src="https://github.com/user-attachments/assets/1fc2837f-aa2e-445c-9bc0-571464e2c127" />
<img width="754" height="227" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/cae1c777-ecd9-4b7f-9085-23eba0177021" />
<img width="828" height="490" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/4d002e54-3170-4bde-9bcf-116654df01d6" />
<img width="1588" height="186" alt="Screenshot (66)" src="https://github.com/user-attachments/assets/b061206f-efb2-4a74-bb88-9d801b793c87" />
<img width="626" height="335" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/f8a33126-78c2-4468-a229-1e47391710be" />

# The python codes used in this project are given below:
[grade_calculator.py](https://github.com/user-attachments/files/23701432/grade_calculator.py)

[weighted_grade_calculator.py](https://github.com/user-attachments/files/23701448/weighted_grade_calculator.py)

# Conclusion & Future Direction:
## The Grade Calculator successfully met all defined functional and non-functional requirements, serving as a reliable and practical tool for grade calculation while demonstrating mastery of Python fundamentals like modularity and exception handling. This foundational structure is highly extensible, with future enhancements planned to include support for dynamic, user-defined grading categories and data persistence to save grading schemes for later use.

# Future Amendments that i can do in this project:

# 1. Data Persistence and Storage:
## Right now, the calculator forgets the grades as soon as the session ends. Making it remember data is the most valuable next step.
## Benefit: Users can open the script and immediately resume calculating for a saved course.
# 2. User Experience (UX) Enhancements:
## Since it's a command-line tool, improving input validation and interface clarity is key.
## Robust Input Validation: Currently, if a user enters text when a number is expected (like for weights or scores), the program might crash.
## Action: Implement try...except blocks to handle ValueError and prompt the user again until valid numerical input is provided.
# 3. Error Handling and Documentation
## Handling Missing Categories: If the user hasn't completed a category (e.g., no exam score yet), ensure the script can calculate the current running grade out of the current total weight.
## Generate an Example Input File: As a feature, you could include a small example file (e.g., sample_course.json) that demonstrates the required data structure for saved courses, making it easier for users to manually create their own course files.

# I built this primarily for my own needs, but if you see a bug, have an idea for a neat feature (like saving grade data or a grade predictor), or just want to make the code cleaner, please jump in!
## Open an Issue to discuss a bug or new idea.
## Feel free to Fork the repo and submit a Pull Request with your changes!

# Thanks for checking out the project!!!