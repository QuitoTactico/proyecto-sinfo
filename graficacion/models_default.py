from django.db import models

class Applicant(models.Model):
    applicant_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill_name

class ExperienceField(models.Model):
    experience_field_id = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.field_name

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.company_name

class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.position_name

class ApplicantSkill(models.Model):
    applicant_skill_id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.applicant} - {self.skill}"

class ApplicantExperience(models.Model):
    applicant_experience_id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    experience_field = models.ForeignKey(ExperienceField, on_delete=models.CASCADE)
    years_of_experience = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.applicant} - {self.experience_field} ({self.years_of_experience} years)"


# esta vaina la creó por default, el comando que está en el .txt creará models.py automáticamente