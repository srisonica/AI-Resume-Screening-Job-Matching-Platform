# Job Description Analyzer


def extract_job_skills(job_path):
    """
    Read a job description and extract required skills.
    """

    # Read the job description
    with open(job_path, "r", encoding="utf-8") as file:
        job_text = file.read()

    # Skills we want to look for
    skills = [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Apache Spark",
        "AWS",
        "Docker",
        "Git",
        "PostgreSQL",
        "Machine Learning",
        "Data Engineering"
    ]

    # Find skills mentioned in the job description
    found_skills = []

    for skill in skills:
        if skill.lower() in job_text.lower():
            found_skills.append(skill)

    return found_skills


# Test the function when this file is run directly
if __name__ == "__main__":

    job_path = "data/jobs/data_engineer_job.txt"

    job_skills = extract_job_skills(job_path)

    print("----- REQUIRED JOB SKILLS -----")

    for skill in job_skills:
        print(skill)