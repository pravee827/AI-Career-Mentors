def calculate_ats(skills):

    total_required = 10

    score = (len(skills) / total_required) * 100

    return min(score, 100)