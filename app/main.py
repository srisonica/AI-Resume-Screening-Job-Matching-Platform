import fitz

from information_extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills
)

from job_analyzer import extract_job_skills
from matcher import calculate_match


# ==========================================
# FILE PATHS
# ==========================================

resume_path = "data/resumes/Sonica Balakrishnan Resume 1.pdf"
job_path = "data/jobs/data_engineer_job.txt"


# ==========================================
# EXTRACT TEXT FROM RESUME
# ==========================================

document = fitz.open(resume_path)

resume_text = ""

for page in document:
    resume_text += page.get_text()

document.close()


# ==========================================
# EXTRACT RESUME INFORMATION
# ==========================================

candidate_name = extract_name(resume_text)
candidate_email = extract_email(resume_text)
candidate_phone = extract_phone(resume_text)
resume_skills = extract_skills(resume_text)


# ==========================================
# EXTRACT JOB SKILLS
# ==========================================

job_skills = extract_job_skills(job_path)


# ==========================================
# CALCULATE MATCH
# ==========================================

matched_skills, missing_skills, match_percentage = calculate_match(
    resume_skills,
    job_skills
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n")
print("=" * 50)
print("        AI RESUME SCREENING RESULT")
print("=" * 50)

print("\nCandidate Information")
print("-" * 50)

print(f"Name  : {candidate_name}")
print(f"Email : {candidate_email}")
print(f"Phone : {candidate_phone}")


print("\nResume Skills")
print("-" * 50)

for skill in sorted(resume_skills):
    print(f"• {skill}")


print("\nRequired Job Skills")
print("-" * 50)

for skill in sorted(job_skills):
    print(f"• {skill}")


print("\nMatched Skills")
print("-" * 50)

for skill in sorted(matched_skills):
    print(f"✓ {skill}")


print("\nMissing Skills")
print("-" * 50)

for skill in sorted(missing_skills):
    print(f"✗ {skill}")


print("\nMatch Score")
print("-" * 50)

print(f"{match_percentage:.2f}%")

print("\n" + "=" * 50)