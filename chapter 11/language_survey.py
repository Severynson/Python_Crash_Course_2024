from AnonymousSurvey import AnonymousSurvey

question = "Which language do you speak: "
quizz = AnonymousSurvey(question)

index = 1
while True:
    print(f"Participant #{index}:", end="")
    quizz.show_question()
    index += 1
    response = input("Your response: ")
    if response.upper() != "Q":
        quizz.store_response(response)
    else:
        print("Survey was completed successfuly by all participants.\n")
        break

quizz.show_results()
