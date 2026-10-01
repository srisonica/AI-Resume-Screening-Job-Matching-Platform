from information_extractor import extract_skills
from job_analyzer import extract_job_skills


def calculate_match(resume_skills, job_skills):
    """
    Compare resume skills with job-required skills.
    """

    # Convert both lists to lowercase
    resume_skills_lower = {skill.lower() for skill in resume_skills}
    job_skills_lower = {skill.lower() for skill in job_skills}

    # Find matching skills
    matched_skills = resume_skills_lower.intersection(job_skills_lower)

    # Find missing skills
    missing_skills = job_skills_lower - resume_skills_lower

    # Calculate match percentage
    if len(job_skills_lower) == 0:
        match_percentage = 0
    else:
        match_percentage = (
            len(matched_skills) / len(job_skills_lower)
        ) * 100

    return matched_skills, missing_skills, match_percentage