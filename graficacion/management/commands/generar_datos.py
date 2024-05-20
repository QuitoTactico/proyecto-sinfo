from faker import Faker
import random

from graficacion.models import *
from django.core.management.base import BaseCommand

fake = Faker()

#python manage.py generar_datos


def generate_applicants(num):
    applicants = []
    for _ in range(num):
        phone_number = fake.phone_number()
        phone_number = phone_number if len(phone_number) <= 20 else phone_number[:20]
        
        applicants.append({
            "applicant_id": _ + 1,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone_number": phone_number
        })
    return applicants

def generate_skills(skill_list):
    skills = []
    for i, skill in enumerate(skill_list):
        skills.append({
            "skill_id": i + 1,
            "skill_name": skill
        })
    return skills

def generate_experience_fields(field_list):
    experience_fields = []
    for i, field in enumerate(field_list):
        experience_fields.append({
            "field_id": i + 1,
            "field_name": field
        })
    return experience_fields

def generate_companies(company_list):
    companies = []
    for i, company in enumerate(company_list):
        companies.append({
            "company_id": i + 1,
            "company_name": company
        })
    return companies

def generate_positions(position_list):
    positions = []
    for i, position in enumerate(position_list):
        positions.append({
            "position_id": i + 1,
            "position_name": position
        })
    return positions

def generate_applicant_skills(applicants, skills, num):
    applicant_skills = []
    for _ in range(num):
        applicant_skills.append({
            "applicant_skill_id": _ + 1,
            "applicant_id": random.choice(applicants)["applicant_id"],
            "skill_id": random.choice(skills)["skill_id"]
        })
    return applicant_skills

def generate_applicant_experience(applicants, experience_fields, companies, positions, num):
    applicant_experience = []
    for _ in range(num):
        applicant_experience.append({
            "applicant_experience_id": _ + 1,
            "applicant_id": random.choice(applicants)["applicant_id"],
            "experience_field_id": random.choice(experience_fields)["field_id"],
            "years_of_experience": random.randint(1, 15),
            "company_id": random.choice(companies)["company_id"],
            "position_id": random.choice(positions)["position_id"]
        })
    return applicant_experience

# Definir listas de habilidades, campos de experiencia, empresas y cargos
skill_list = ["Python", "SQL", "Java", "C++", "JavaScript", "HTML", "CSS", "React", "Node.js", "Django"]
field_list = ["Software Development", "Data Science", "Web Development", "Database Administration", "Cybersecurity"]
company_list = ["Company A", "Company B", "Company C", "Company D", "Company E", "Company F", "Company G", "Company H", "Company I", "Company J"]
position_list = ["Software Engineer", "Data Analyst", "Web Developer", "Database Administrator", "Security Specialist"]



class Command(BaseCommand):
    help = 'Helps to generate data for the models'

    def handle(self, *args, **kwargs):
        try:
            applicants = generate_applicants(500)
            skills = generate_skills(skill_list)
            experience_fields = generate_experience_fields(field_list)
            companies = generate_companies(company_list)
            positions = generate_positions(position_list)
            applicant_skills = generate_applicant_skills(applicants, skills, 1000)
            applicant_experience = generate_applicant_experience(applicants, experience_fields, companies, positions, 1000)

            for applicant in applicants:
                Applicant.objects.create(
                    first_name=applicant["first_name"],
                    last_name=applicant["last_name"],
                    email=applicant["email"],
                    phone_number=applicant["phone_number"]
                )

            for skill in skills:
                Skill.objects.create(
                    skill_name=skill["skill_name"]
                )

            for field in experience_fields:
                ExperienceField.objects.create(
                    field_name=field["field_name"]
                )

            for company in companies:
                Company.objects.create(
                    company_name=company["company_name"]
                )

            for position in positions:
                Position.objects.create(
                    position_name=position["position_name"]
                )

            for applicant_skill in applicant_skills:
                ApplicantSkill.objects.create(
                    applicant_id=applicant_skill["applicant_id"],
                    skill_id=applicant_skill["skill_id"]
                )

            for applicant_exp in applicant_experience:
                ApplicantExperience.objects.create(
                    applicant_id=applicant_exp["applicant_id"],
                    experience_field_id=applicant_exp["experience_field_id"],
                    years_of_experience=applicant_exp["years_of_experience"],
                    company_id=applicant_exp["company_id"],
                    position_id=applicant_exp["position_id"]
                )

        
    
            self.stdout.write(self.style.SUCCESS(f'Modelo poblado correctamente'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Hubo un error mientras se generaban los datos:'))
            self.stdout.write(self.style.ERROR(f'{e}'))