def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("What is your Name? \n")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = float(input("What is your Math Score? \n"))
    science_score = float(input("What is your Science Score? \n"))
    english_score = float(input("What is your English Score? \n"))

    # Calculate the average grade 
    average_grade = (math_score + english_score + science_score)/3

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f'{student_name}, Your average Grade is:{average_grade}')