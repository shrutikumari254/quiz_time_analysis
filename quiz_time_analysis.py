import time

questions = [
    ("What is 5 + 3?", "8"),
    ("Capital of India?", "Delhi"),
    ("What is 10 - 4?", "6")
]

time_taken = []
score = 0

print("----- QUIZ STARTED -----\n")

for question, answer in questions:
    start_time = time.time()
    user_answer = input(question + " ")
    end_time = time.time()

    time_taken.append(end_time - start_time)

    if user_answer.lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

print("----- QUIZ FINISHED -----\n") 

total_time = sum(time_taken)
average_time = total_time / len(time_taken)

print("Score:", score, "/", len(questions))
print("Total Time Taken:", round(total_time, 2), "seconds")
print("Average Time per Question:", round(average_time, 2), "seconds")
print("Fastest Answer Time:", round(min(time_taken), 2), "seconds")
print("Slowest Answer Time:", round(max(time_taken), 2), "seconds")


import matplotlib.pyplot as plt

plt.plot(time_taken, marker='o')
plt.xlabel("Question Number")
plt.ylabel("Time (seconds)")
plt.title("Quiz Time Analysis")
plt.show()


