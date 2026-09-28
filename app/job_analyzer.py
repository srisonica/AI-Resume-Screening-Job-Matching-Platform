# Job Description Analyzer

job_path = "data/jobs/data_engineer_job.txt"

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

# Display the results
print("----- REQUIRED JOB SKILLS -----")

for skill in found_skills:
    print(skill)