def evaluate_answer(answer: str):

    length = len(answer.split())

    if length < 5:
        return 3, "Too short answer. Try explaining more."

    elif length < 15:
        return 6, "Good but can be more detailed."

    else:
        return 9, "Excellent detailed answer."