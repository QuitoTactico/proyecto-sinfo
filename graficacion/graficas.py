from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral11, Category20b
from bokeh.embed import components
from bokeh.transform import dodge

from graficacion.models import *
from django.db.models import Count, Avg

def distribucion_habilidades():
    skills = Skill.objects.annotate(num_applicants=Count('applicantskill'))

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
           line_color='white', 
           fill_color=factor_cmap('skill_name',
                                  palette=Spectral11, 
                                  factors=data_skills['skill_name']
                                  ))

    hover = HoverTool()
    hover.tooltips = [("Habilidad", "@skill_name"), ("Número de Aplicantes", "@num_applicants")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Habilidades"
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    
    dh_script, dh_div = components(p)
    return dh_script, dh_div

def experiencia_promedio_por_campo():
    experiences = ApplicantExperience.objects.values('experience_field__field_name').annotate(avg_experience=Avg('years_of_experience'))

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
           line_color='white', fill_color=factor_cmap('field_name',
                                                      palette=Spectral11, factors=data_experience['field_name']))

    hover = HoverTool()
    hover.tooltips = [("Campo", "@field_name"), ("Años Promedio de Experiencia", "@avg_experience")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Años Promedio de Experiencia"
    p.xaxis.axis_label = "Campos de Experiencia"
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    ep_script, ep_div = components(p)
    return ep_script, ep_div

def cantidad_aplicantes_por_empresa():
    companies = ApplicantExperience.objects.values('company__company_name').annotate(num_applicants=Count('applicant'))

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
                                                      palette=Spectral11, factors=data_companies['company_name']))

    hover = HoverTool()
    hover.tooltips = [("Empresa", "@company_name"), ("Número de Aplicantes", "@num_applicants")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Empresas"

    script, div = components(p)
    return script, div

def distribucion_aplicantes_por_cargo():
    positions = ApplicantExperience.objects.values('position__position_name').annotate(num_applicants=Count('applicant'))

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
           line_color='white', fill_color=factor_cmap('position_name', palette=Spectral11, factors=data_positions['position_name']))

    hover = HoverTool()
    hover.tooltips = [("Cargo", "@position_name"), ("Número de Aplicantes", "@num_applicants")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Cargos"

    script, div = components(p)
    return script, div

''' # APILADAS NO SE VE MUY BIEN
def habilidades_mas_demandadas_por_campo():
    field_skills = ApplicantExperience.objects.values('experience_field__field_name', 'applicant__applicantskill__skill__skill_name').annotate(num_applicants=Count('applicant')).order_by('-num_applicants')

    # Filtrar los valores nulos
    filtered_field_skills = [fs for fs in field_skills if fs['experience_field__field_name'] is not None and fs['applicant__applicantskill__skill__skill_name'] is not None]

    # Crear listas separadas para cada campo
    field_names = [fs['experience_field__field_name'] for fs in filtered_field_skills]
    skill_names = [fs['applicant__applicantskill__skill__skill_name'] for fs in filtered_field_skills]
    num_applicants = [fs['num_applicants'] for fs in filtered_field_skills]

    unique_fields = list(set(field_names))
    unique_skills = list(set(skill_names))

    # Crear un nuevo diccionario para el ColumnDataSource con columnas separadas para cada habilidad
    data = {'field_name': unique_fields}
    for skill in unique_skills:
        data[skill] = [0] * len(unique_fields)
    
    for i, field in enumerate(field_names):
        skill = skill_names[i]
        if skill in data:
            field_index = unique_fields.index(field)
            data[skill][field_index] += num_applicants[i]

    source = ColumnDataSource(data=data)

    p = figure(x_range=unique_fields,
               height=450,
               title="Habilidades Más Demandadas por Campo de Experiencia",
               toolbar_location=None,
               tools="",
               sizing_mode="stretch_width")

    # Apilar las barras usando vbar_stack
    p.vbar_stack(unique_skills, x='field_name', width=0.9, color=Spectral11[:len(unique_skills)],
                 source=source, legend_label=unique_skills)

    hover = HoverTool()
    hover.tooltips = [("Campo de Experiencia", "@field_name"), ("Habilidad y # de aplicantes", "@$name @field_name")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Campos de Experiencia"

    p.legend.orientation = "vertical"
    p.legend.location = "top_right"
    p.legend.label_text_font_size = "8pt"
    p.add_layout(p.legend[0], 'right')

    script, div = components(p)
    return script, div
'''

def habilidades_mas_demandadas_por_campo():
    field_skills = ApplicantExperience.objects.values('experience_field__field_name', 'applicant__applicantskill__skill__skill_name').annotate(num_applicants=Count('applicant')).order_by('-num_applicants')

    # Filtrar los valores nulos
    filtered_field_skills = [fs for fs in field_skills if fs['experience_field__field_name'] is not None and fs['applicant__applicantskill__skill__skill_name'] is not None]

    # Crear listas separadas para cada campo
    field_names = [fs['experience_field__field_name'] for fs in filtered_field_skills]
    skill_names = [fs['applicant__applicantskill__skill__skill_name'] for fs in filtered_field_skills]
    num_applicants = [fs['num_applicants'] for fs in filtered_field_skills]

    unique_fields = list(set(field_names))
    unique_skills = list(set(skill_names))

    # Crear un nuevo diccionario para el ColumnDataSource con columnas separadas para cada habilidad
    data = {'field_name': unique_fields}
    for skill in unique_skills:
        data[skill] = [0] * len(unique_fields)
    
    for i, field in enumerate(field_names):
        skill = skill_names[i]
        if skill in data:
            field_index = unique_fields.index(field)
            data[skill][field_index] += num_applicants[i]

    source = ColumnDataSource(data=data)

    p = figure(x_range=unique_fields,
               height=450,
               title="Habilidades Más Demandadas por Campo de Experiencia",
               toolbar_location=None,
               tools="",
               sizing_mode="stretch_width")

    # Configuración para barras agrupadas
    colors = Spectral11[:len(unique_skills)]
    bar_width = 0.08  # Ancho de las barras más angosto
    offsets = [-0.3 + i * bar_width for i in range(len(unique_skills))]

    for i, (skill, offset) in enumerate(zip(unique_skills, offsets)):
        p.vbar(x=dodge('field_name', offset, range=p.x_range), 
               top=skill, width=bar_width, source=source,
               color=colors[i], legend_label=skill, name=skill)

    hover = HoverTool()
    hover.tooltips = [("Campo de Experiencia", "@field_name"), ("# de Aplicantes", "@$name")]
    p.add_tools(hover)

    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Campos de Experiencia"

    p.legend.orientation = "vertical"
    p.legend.location = "top_right"
    p.legend.label_text_font_size = "8pt"
    p.add_layout(p.legend[0], 'right')

    script, div = components(p)
    return script, div
    
def tendencias_aplicantes_por_ano_experiencia():
    experience_years = ApplicantExperience.objects.values('years_of_experience').annotate(num_applicants=Count('applicant')).order_by('years_of_experience')

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

    hover = HoverTool()
    hover.tooltips = [("Años de Experiencia", "@years_of_experience"), ("Número de Aplicantes", "@num_applicants")]
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Años de Experiencia"

    script, div = components(p)
    return script, div
