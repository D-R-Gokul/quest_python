#program to grade students with average score
average_score = int(input("Enter your average score to print the result:  "))
if(0<= average_score and average_score < 50):
    print("Result is Fail")
elif(average_score < 75):
    print("Result is Second class")
elif(average_score <= 90):
    print("Result is First Class")
elif(average_score <= 100):
    print("Result is Distinction")
else:
    print("Invalid input entered")
    