
def reply(msg):

    msg=msg.lower()

    if "hello" in msg:
        return "Hello! I am your AI Career Assistant."
    if "skill" in msg:
        return "Key skills: Python, Machine Learning, NLP, Deep Learning."
    if "job" in msg:
        return "Upload your resume to get top job matches."
    if "career" in msg:
        return "Top careers include AI Engineer, Data Scientist, ML Engineer."

    return "Ask about careers, skills, or job opportunities."
