#from bokeh.io import show, output_notebook
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral9
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

    p = figure(x_range=data_skills['skill_name'], height=350,
    title="Distribución de Habilidades entre los Aplicantes",
    toolbar_location=None, tools="")

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
