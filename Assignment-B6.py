def evaluate_performance(punctuality, quality, teamwork, initiative, communication):
    score = 0
    feedback = []

    # Scoring rules
    if punctuality >= 4:
        score += 2
        feedback.append("Excellent punctuality.")
    elif punctuality >= 2:
        score += 1
        feedback.append("Moderate punctuality, try to improve.")
    else:
        feedback.append("Poor punctuality. Needs improvement.")

    if quality >= 4:
        score += 2
        feedback.append("Delivers high-quality work.")
    elif quality >= 2:
        score += 1
        feedback.append("Work quality is acceptable.")
    else:
        feedback.append("Work quality is poor.")

    if teamwork >= 4:
        score += 2
        feedback.append("Strong team player.")
    elif teamwork >= 2:
        score += 1
        feedback.append("Cooperates fairly well with the team.")
    else:
        feedback.append("Needs to improve collaboration.")

    if initiative >= 4:
        score += 2
        feedback.append("Shows great initiative.")
    elif initiative >= 2:
        score += 1
        feedback.append("Occasionally takes initiative.")
    else:
        feedback.append("Rarely shows initiative.")

    if communication >= 4:
        score += 2
        feedback.append("Excellent communicator.")
    elif communication >= 2:
        score += 1
        feedback.append("Communicates effectively most of the time.")
    else:
        feedback.append("Communication skills need work.")

    # Decision Rules
    if score >= 9:
        performance = "Outstanding"
    elif score >= 6:
        performance = "Good"
    elif score >= 4:
        performance = "Satisfactory"
    else:
        performance = "Needs Improvement"

    return performance, feedback


if __name__ == "__main__":
    print("Rate the employee on a scale of 0-5")

    punctuality = int(input("Punctuality: "))
    quality = int(input("Quality of Work: "))
    teamwork = int(input("Teamwork: "))
    initiative = int(input("Initiative: "))
    communication = int(input("Communication Skills: "))

    result, remarks = evaluate_performance(punctuality, quality, teamwork, initiative, communication)

    print("\nEmployee Performance Evaluation:")
    print("Performance Level:", result)
    print("Remarks:")
    for r in remarks:
        print("-", r)

