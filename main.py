from fastapi import FastAPI
from typing import List
from models import Experience, Education, Skill
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import requests
import time


app = FastAPI(
    title="Get to know Ashwin",
    description="An API to showcase my profile, experience, projects, and skills for the API Management Consultant role at JYSK",
    version="1.0.0",
    contact={
        "name": "Ashwin Kirtane",
        "url": "https://www.linkedin.com/in/ashwinkirtane/",
        "email": "ashwin.kirtane@gmail.com",
        "phone": "+45 52820655"
    }
)

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != "9aj8cpp8iLCKRAf0Zrb9ViWw8QVryMbJirUYXJDZUlmuBdxqVozvv8s28IZKwXep":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )

@app.get("/about", dependencies=[Depends(verify_token)], tags=["Profile"])
def get_about():
    print('In the about API function')
    return {
        "name": "Ashwin Kirtane",
        "location": "Copenhagen, Denmark",
        "current_company": "Danske Bank",
        "summary": "Technologist with expertise in API Design and Architecture, and designing scalable enterprise "
                   "solutions at a financial firm. Led optimization initiatives through tech-stack modernization and "
                   "cloud migration. I also led Agile transformation initiatives collaborating with cross-functional "
                   "stakeholders across APAC and EMEA to deliver regulatory-compliant, high-performance solutions. "
                   "Extensive experience working with Open Banking APIs."
    }

@app.get("/experience", response_model=List[Experience], dependencies=[Depends(verify_token)], tags=["Experience"])
def get_experience():
    return [
        Experience(
            company="Danske Bank",
            position="MBA Strategy Intern",
            years="April 2025 – August 2025",
            description="Aligned sprint goals with Forward '28 strategy in the Digital Core Tribe."
        ),
        Experience(
            company="HSBC",
            position="Technology Consultant",
            years="Sept 2021 - Sept 2024",
            description="Led API design and implementation (15+ documented APIs), automated ITSM workflows, and built "
                        "dashboards for strategic insights and was a workstream lead, managing delivery cycles, "
                        "refining backlogs, and integrating reporting systems for cross-team visibility."
        ),
        Experience(
            company="HSBC",
            position="Fullstack Engineer",
            years="July 2017 - Sept 2021",
            description="Migrated legacy core banking systems to GCP using domain-driven design, and built "
                        "microservices that cut onboarding time from 40 days to 8 minutes. Designed CDC-Kafka data "
                        "pipelines and a secure service mesh for REST APIs to enable real-time, scalable, and "
                        "compliant cloud integrations."
        )
    ]

@app.get("/education", response_model=List[Education], dependencies=[Depends(verify_token)], tags=["Education"])
def get_education():
    return [
        Education(
            institution="Copenhagen Business School",
            location="Copenhagen, Denmark",
            degree="Masters of Business Administration (MBA) with a concentration in Digitalisation and AI",
            years="Sept 2024 – Sept 2025"
        ),
        Education(
            institution="Dhirubhai Ambani University",
            location="Gandhinagar, India",
            degree="Bachelors of Technology in Computer Science",
            years="2013 – 2017"
        )
    ]


@app.get("/skills", response_model=List[Skill], dependencies=[Depends(verify_token)], tags=["Skills"])
def get_skills():
    return [
        Skill(category="API Development", items=["REST APIs", "API Gateway", "GraphQL"]),
        Skill(category="Technology", items=["Python", "Java", "SQL", "NoSQL"]),
        Skill(category="Agile and Tooling", items=["Jira", "Azure DevOps", "Git", "Postman", "DevOps", "DevSecOps"]),
        Skill(category="Cloud", items=["GCP", "AWS"]),
        Skill(category="Soft Skills", items=["Agile Project Management", "Stakeholder Communication", "OKRs and Strategy Execution"])
    ]

def trigger_about_api():
    url = "https://jysk-resume.onrender.com/about"
    headers = {
        'Authorization': 'Bearer 9aj8cpp8iLCKRAf0Zrb9ViWw8QVryMbJirUYXJDZUlmuBdxqVozvv8s28IZKwXep'
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        print('Success')
    else:
        print(response.status_code)


if __name__ == "__main__":
    program_starts = time.time()
    while True:
        now = time.time()
        seconds = now - program_starts
        if seconds > 300:
            print(f'Triggering about API')
            trigger_about_api()
            program_starts = time.time()
