#from bokeh.io import show, output_notebook
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral9, Spectral11, Category20b
from bokeh.embed import components

from graficacion.models import *
from django.db.models import Count


def distribucion_habilidades():
    # Supongamos que 'data_skills' es el resultado de la consulta
    #SQL en forma de un DataFrame

    # data_skills = pd.DataFrame({'skill_name': ['Skill1','Skill2', 'Skill3'], 'num_applicants': [100, 150, 80]})
    #output_notebook()

    # Datos de ejemplo
    #data_skills = {'skill_name': ['Skill1', 'Skill2', 'Skill3'], 'num_applicants': [100, 150, 80]}
    skills = Skill.objects.annotate(num_applicants=Count('applicantskill'))

    # Crea los datos para la gráfica
    data_skills = {
        'skill_name': [skill.skill_name for skill in skills],
        'num_applicants': [skill.num_applicants for skill in skills]
    }


    source = ColumnDataSource(data=data_skills)

    p = figure(x_range=data_skills['skill_name'], 
               height=450,
               title="Distribución de Habilidades entre los Aplicantes",
               toolbar_location=None, 
               tools="",
               sizing_mode="stretch_width")

    p.vbar(x='skill_name', 
           top='num_applicants', 
           width=0.9, 
           source=source, 
           #legend_field="skill_name", 
           line_color='white', 
           fill_color=factor_cmap('skill_name',
                                  palette=Spectral9, 
                                  factors=data_skills['skill_name']
                                  ))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Habilidades"
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    
    #show(p)
    #return p
    dh_script, dh_div = components(p)
    return dh_script, dh_div


from django.db.models import Avg

def experiencia_promedio_por_campo():
    # Supongamos que 'data_experience' es el resultado de la consulta SQL en forma de un DataFrame
    # data_experience = pd.DataFrame({'field_name': ['Field1', 'Field2', 'Field3'], 'avg_experience': [5.5, 3.2, 6.1]})

    # Datos de ejemplo
    #data_experience = {'field_name': ['Field1', 'Field2', 'Field3'], 'avg_experience': [5.5, 3.2, 6.1]}
    experiences = ApplicantExperience.objects.values('experience_field__field_name').annotate(avg_experience=Avg('years_of_experience'))

    # Crea los datos para la gráfica
    data_experience = {
        'field_name': [experience['experience_field__field_name'] for experience in experiences],
        'avg_experience': [experience['avg_experience'] for experience in experiences]
    }

    source = ColumnDataSource(data=data_experience)

    p = figure(x_range=data_experience['field_name'], 
               height=450, 
               title="Experiencia Promedio por Campo",
               toolbar_location=None, 
               tools="",
               sizing_mode="stretch_width")

    p.vbar(x='field_name', top='avg_experience', width=0.9, source=source, 
           #legend_field="field_name",
           line_color='white', fill_color=factor_cmap('field_name',
                                                      palette=Spectral9, factors=data_experience['field_name']))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Años Promedio de Experiencia"
    p.xaxis.axis_label = "Campos de Experiencia"
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    #show(p)
    ep_script, ep_div = components(p)
    return ep_script, ep_div

def cantidad_aplicantes_por_empresa():
    # Supongamos que 'data_companies' es el resultado de la consulta SQL en forma de un DataFrame
    # data_companies = pd.DataFrame({'company_name': ['Company1', 'Company2', 'Company3'], 'num_applicants': [200, 150, 180]})
    # Datos de ejemplo
    #data_companies = {'company_name': ['Company1', 'Company2', 'Company3'], 'num_applicants': [200, 150, 180]}
    companies = ApplicantExperience.objects.values('company__company_name').annotate(num_applicants=Count('applicant'))

    # Crea los datos para la gráfica
    data_companies = {
        'company_name': [company['company__company_name'] for company in companies],
        'num_applicants': [company['num_applicants'] for company in companies]
    }

    source = ColumnDataSource(data=data_companies)

    p = figure(x_range=data_companies['company_name'], 
               height=450, 
               title="Cantidad de Aplicantes por Empresa",
               toolbar_location=None, 
               tools="",
               sizing_mode="stretch_width")

    p.vbar(x='company_name', top='num_applicants', width=0.9, source=source,
           line_color='white', fill_color=factor_cmap('company_name',
                                                      palette=Spectral9, factors=data_companies['company_name']))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Empresas"
    #p.xaxis.major_label_orientation = "vertical" 

    #show(p)
    script, div = components(p)
    return script, div


def distribucion_aplicantes_por_cargo():
    positions = ApplicantExperience.objects.values('position__position_name').annotate(num_applicants=Count('applicant'))

    # Crea los datos para la gráfica
    data_positions = {
        'position_name': [position['position__position_name'] for position in positions],
        'num_applicants': [position['num_applicants'] for position in positions]
    }

    source = ColumnDataSource(data=data_positions)

    p = figure(x_range=data_positions['position_name'], 
               height=450, 
               title="Distribución de Aplicantes por Cargo",
               toolbar_location=None, 
               tools="",
               sizing_mode="stretch_width")

    p.vbar(x='position_name', top='num_applicants', width=0.9, source=source,
           line_color='white', fill_color=factor_cmap('position_name', palette=Spectral9, factors=data_positions['position_name']))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Cargos"
    #p.xaxis.major_label_orientation = "vertical"  # Hace que los nombres de los cargos se muestren en vertical

    #show(p)
    script, div = components(p)
    return script, div

def habilidades_mas_demandadas_por_campo():
    # data_field_skills es un diccionario que contiene la información de la query a la BD, se tiene que cambiar
    '''
    data_field_skills = {
        "field_name": ["Field1", "Field2", "Field3"],
        "skill_name": ["Skill1", "Skill2", "Skill1"],
        "num_applicants": [50, 30, 80],
    }

    source = ColumnDataSource(data=data_field_skills)
    '''
    field_skills = ApplicantExperience.objects.values('experience_field__field_name', 'applicant__applicantskill__skill__skill_name').annotate(num_applicants=Count('applicant')).order_by('-num_applicants')

    # Crea los datos para la gráfica
    data_field_skills = {
        'field_name': [fs['experience_field__field_name'] for fs in field_skills],
        'skill_name': [fs['applicant__applicantskill__skill__skill_name'] for fs in field_skills],
        'num_applicants': [fs['num_applicants'] for fs in field_skills]
    }

    # Elimina los duplicados y maneja los valores None
    unique_fields = list(set(data_field_skills['field_name']))
    unique_skills = list(set(skill for skill in data_field_skills['skill_name'] if skill is not None))

    source = ColumnDataSource(data=data_field_skills)

    p = figure(x_range=unique_fields,
               height=450,
               title="Habilidades Más Demandadas por Campo de Experiencia",
               toolbar_location=None,
               tools="",
               sizing_mode="stretch_width")

    p.vbar(
        x="field_name",
        top="num_applicants",
        width=0.9,
        source=source,
        legend_field="skill_name",
        line_color="white",
        fill_color=factor_cmap(
            "skill_name", palette=Spectral11, factors=unique_skills
        ),
    )

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Campos de Experiencia"
    #from math import pi
    #p.xaxis.major_label_orientation = pi/4

    p.legend.orientation = "vertical"
    p.legend.location = "top_right"
    p.legend.label_text_font_size = "8pt"
    p.add_layout(p.legend[0], 'right')

    script, div = components(p)
    return script, div



def tendencias_aplicantes_por_ano_experiencia():
    # Obtener los datos de la base de datos
    experience_years = ApplicantExperience.objects.values('years_of_experience').annotate(num_applicants=Count('applicant')).order_by('years_of_experience')

    # Preparar los datos para la gráfica
    data_experience_years = {
        'years_of_experience': [str(ey['years_of_experience']) for ey in experience_years],  # Convertir a cadena
        'num_applicants': [ey['num_applicants'] for ey in experience_years]
    }

    source = ColumnDataSource(data=data_experience_years)

    p = figure(x_range=data_experience_years['years_of_experience'], 
               height=450, 
               title="Tendencias de Aplicantes por Año de Experiencia",
               toolbar_location=None, 
               tools="", 
               sizing_mode="stretch_width")

    p.vbar(x='years_of_experience', top='num_applicants', width=0.9, source=source,
           line_color='white', fill_color=factor_cmap('years_of_experience', palette=Category20b[20], factors=data_experience_years['years_of_experience']))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Años de Experiencia"

    script, div = components(p)
    return script, div





'''
def habilidades_mas_demandadas_por_campo2():
    # Unir las tablas ApplicantExperience y ApplicantSkill a través de la tabla Applicant
    field_skills = ApplicantExperience.objects.values('experience_field__field_name', 'applicant__applicantskill__skill__skill_name').annotate(num_applicants=Count('applicant')).order_by('-num_applicants')

    # Crea los datos para la gráfica
    data_field_skills = {
        'field_name': [fs['experience_field__field_name'] for fs in field_skills],
        'skill_name': [fs['applicant__applicantskill__skill__skill_name'] for fs in field_skills],
        'num_applicants': [fs['num_applicants'] for fs in field_skills]
    }

    # Elimina los duplicados y maneja los valores None
    unique_fields = list(set(data_field_skills['field_name']))
    unique_skills = list(set(skill for skill in data_field_skills['skill_name'] if skill is not None))

    source = ColumnDataSource(data=data_field_skills)

    p = figure(x_range=unique_fields, height=450, title="Habilidades Más Demandadas por Campo de Experiencia",
               toolbar_location=None, tools="")

    p.vbar(x='field_name', top='num_applicants', width=0.9, source=source,
           line_color='white', fill_color=factor_cmap('skill_name', palette=Spectral11, factors=unique_skills))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Campos de Experiencia"
    #p.xaxis.major_label_orientation = "vertical"  # Hace que los nombres de los campos se muestren en vertical

    #show(p)
    script, div = components(p)
    return script, div

'''