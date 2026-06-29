def generate_feedback(prediction,studytime,failures,absences,goout,health,internet,famsup,schoolsup):

    suggestions = []

    # Performance Level
    if prediction >= 16:
        level = "🟢 Excellent"

    elif prediction >= 13:
        level = "🔵 Very Good"

    elif prediction >= 10:
        level = "🟡 Good"

    elif prediction >= 8:
        level = "🟠 Average"

    else:
        level = "🔴 Needs Improvement"

    # Suggestions

    if studytime <= 1:
        suggestions.append("Increase your weekly study time.")

    if failures > 0:
        suggestions.append("Revise previous subjects carefully.")

    if absences > 10:
        suggestions.append("Reduce absences to improve consistency.")

    if goout >= 4:
        suggestions.append("Reduce time spent going out before exams.")

    if health <= 2:
        suggestions.append("Maintain a healthy daily routine.")

    if internet == 0:
        suggestions.append("Use online learning resources whenever possible.")

    if famsup == 0:
        suggestions.append("Seek support from family or teachers.")

    if schoolsup == 1:
        suggestions.append("Make full use of your school's academic support.")

    if len(suggestions) == 0:
        suggestions.append("Keep up the excellent work!")

    return level, suggestions