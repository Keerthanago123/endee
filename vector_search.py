
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(resume_text,jobs):

    corpus=[j["skills"] for j in jobs]+[resume_text]

    vectorizer=TfidfVectorizer()
    vectors=vectorizer.fit_transform(corpus)

    similarity=cosine_similarity(vectors[-1],vectors[:-1])
    scores=similarity[0]

    results=[]
    for i,score in enumerate(scores):
        job=jobs[i]

        match=max(80,round(score*100,2))

        results.append({
            "role":job["role"],
            "company":job["company"],
            "skills":job["skills"],
            "url":job["url"],
            "match":match
        })

    results=sorted(results,key=lambda x:x["match"],reverse=True)

    return results[:5]
