from django.contrib import admin

# Register your models here.
from .models_default import Applicant, Skill, ExperienceField, Company, Position, ApplicantSkill, ApplicantExperience

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name',)
    search_fields = ('skill_name',)

@admin.register(ExperienceField)
class ExperienceFieldAdmin(admin.ModelAdmin):
    list_display = ('field_name',)
    search_fields = ('field_name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    search_fields = ('company_name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_name',)
    search_fields = ('position_name',)

@admin.register(ApplicantSkill)
class ApplicantSkillAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'skill')
    search_fields = ('applicant__first_name', 'applicant__last_name', 'skill__skill_name')

@admin.register(ApplicantExperience)
class ApplicantExperienceAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'experience_field', 'years_of_experience', 'company', 'position')
    search_fields = ('applicant__first_name', 'applicant__last_name', 'experience_field__field_name', 'company__company_name', 'position__position_name')
    list_filter = ('experience_field', 'company', 'position')
