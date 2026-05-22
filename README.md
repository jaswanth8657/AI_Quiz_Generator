\# AI Quiz Generator



\## Project Overview



AI Quiz Generator is a Python-based interactive quiz application that works in the terminal/command prompt. The application asks multiple-choice quiz questions, accepts user answers, validates responses, calculates scores, and displays the final result automatically.



This project was developed as part of an internship mini project to understand real-world application development, user interaction, and Python programming concepts. The project also demonstrates features commonly used in online quiz systems such as difficulty levels, timers, random question generation, and colored terminal output.



\---



\# Features



✅ Welcome Message  

✅ Multiple Choice Questions (MCQ)  

✅ Difficulty Levels (Easy, Medium, Hard)  

✅ Random Question Selection  

✅ Timer for Each Question  

✅ Answer Validation  

✅ Score Calculation  

✅ Colored Terminal Output  

✅ Save Scores in Text File  



\---



\# Technologies Used



\- Python

\- Colorama Library



\---



\# Project Structure



```text

AI\_Quiz\_Generator/

│

├── quiz.py

├── questions.txt

├── scores.txt

└── README.md

```



\---



\# Installation



\## Step 1: Download or Clone the Project



Download the project folder and open it in VS Code or any Python IDE.



\---



\## Step 2: Install Required Library



Run the following command in terminal:



```bash

pip install colorama

```



\---



\# How to Run the Project



Open terminal inside the project folder and run:



```bash

python quiz.py

```



\---



\# Question File Format



Questions are stored in `questions.txt` using the following format:



```text

difficulty|question|option1|option2|option3|option4|correct\_option

```



Example:



```text

easy|What is Python?|A scripting language|A programming language|A database|An operating system|2

```



\---



\# Difficulty Levels



The application supports three difficulty levels:



\- Easy

\- Medium

\- Hard



Users can select a difficulty level before starting the quiz. Questions are filtered based on the selected level.



\---



\# Random Question Feature



The quiz application randomly shuffles questions every time the program runs. This ensures that users get different question orders during each attempt.



\---



\# Timer Feature



Each question includes a timer limit of 10 seconds. If the user exceeds the time limit, the question is automatically skipped.



\---



\# Colored Terminal Output



The application uses the Colorama library to provide colored text output in the terminal for better user experience.



Examples:

\- Green → Correct Answers

\- Red → Wrong Answers

\- Yellow → Questions

\- Cyan → Final Results



\---



\# Score Saving System



At the end of the quiz, the final score is automatically stored in `scores.txt`.



Example:



```text

easy Score: 4/5

medium Score: 3/5

```



\---



\# Sample Output



```text

===== Welcome to AI Quiz Generator =====



Choose Difficulty Level:

1\. Easy

2\. Medium

3\. Hard



Enter choice: 2



Question 1:

What is AI?



1\. Artificial Intelligence

2\. Automated Internet

3\. Advanced Interface

4\. Artificial Integration



Enter option number: 1



Correct Answer!



Question 2:

Which language is commonly used for Machine Learning?



1\. HTML

2\. CSS

3\. Python

4\. XML



Enter option number: 3



Correct Answer!



===== Quiz Finished =====



Final Score: 2/2



Score saved successfully!

```



\---



\# Python Concepts Used



This project helped in understanding:



\- Variables

\- Loops

\- Conditional Statements

\- File Handling

\- User Input

\- String Manipulation

\- Random Module

\- Time Module

\- Terminal Styling

\- Data Validation



\---



\# Learning Outcomes



Through this project, practical knowledge was gained about:



\- Building interactive terminal applications

\- Structuring Python projects

\- Handling user input and validation

\- Implementing real-time features like timers

\- Working with files for data storage

\- Improving user experience using colored outputs



This project also helped in understanding how real-world applications manage user interaction, process data, and maintain program flow.



\---



\# Future Improvements



The project can be further enhanced by adding:



\- Graphical User Interface (GUI)

\- Web Version using Flask or Django

\- AI-generated Questions

\- Database Integration

\- User Login System

\- Leaderboard Feature

\- API Integration

\- Machine Learning-based Adaptive Quiz System



\---



\# Conclusion



AI Quiz Generator is a beginner-friendly Python project that demonstrates core programming concepts along with interactive application development. The project provides hands-on experience in creating quiz systems and serves as a foundation for building more advanced AI and web-based applications in the future.



\---



\# Author



Developed by Jaswanth Maddi



Internship Mini Project – AI Quiz Generator

