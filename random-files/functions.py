"""En todos los gráficos se les debe cambiar los datos dentro del diccionario con los resultados de las queries ordenados de la misma forma que se muestra en los ejemplos.

Todas las funciones retornan un componente para manipulación del DOM en HTML, el cual se puede insertar en un archivo HTML.

Versiones de las librerias usadas:
Bokeh: 3.4.1
Pandas: 2.2.2
Numpy: 1.26.4
"""

from bokeh.io import show, output_notebook
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.embed import components


def habilidadesAplicantes(query):
    # data_skills es un diccionario que contiene la información de la query a la BD, se tiene que cambiar
    data_skills = {
        "skills_name": ["Python", "R", "SQL", "Java", "C++", "Scala"],
        "num_applicants": [120, 100, 90, 80, 70, 60],
    }

    source = ColumnDataSource(data=data_skills)

    p = figure(
        x_range=data_skills["skill_name"],
        plot_height=350,
        title="Distribución de Habilidades entre los Aplicantes",
        toolbar_location=None,
        tools="",
    )

    p.vbar(
        x="skill_name",
        top="num_applicants",
        width=0.9,
        source=source,
        legend_field="skill_name",
        line_color="white",
        fill_color=factor_cmap(
            "skill_name", palette=Spectral6, factors=data_skills["skill_name"]
        ),
    )

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Habilidades"
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    p_div = components(p)
    return p_div


def experienciaPromedio(query):
    # data_experience es un diccionario que contiene la información de la query a la BD, se tiene que cambiar
    data_experience = {
        "field_name": ["Field1", "Field2", "Field3"],
        "avg_experience": [5.5, 3.2, 6.1],
    }
    source = ColumnDataSource(data=data_experience)

    p = figure(
        x_range=data_experience["field_name"],
        plot_height=350,
        title="Experiencia Promedio por Campo",
        toolbar_location=None,
        tools="",
    )

    p.vbar(
        x="field_name",
        top="avg_experience",
        width=0.9,
        source=source,
        legend_field="field_name",
        line_color="white",
        fill_color=factor_cmap(
            "field_name", palette=Spectral6, factors=data_experience["field_name"]
        ),
    )

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Años Promedio de Experiencia"
    p.xaxis.axis_label = "Campos de Experiencia"
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    p_div = components(p)
    return p_div


def aplicantesCargo(query):
    # data_positions es un diccionario que contiene la información de la query a la BD, se tiene que cambiar
    data_positions = {
        "position_name": ["Position1", "Position2", "Position3"],
        "num_applicants": [120, 160, 140],
    }

    source = ColumnDataSource(data=data_positions)

    p = figure(
        x_range=data_positions["position_name"],
        plot_height=350,
        title="Distribución de Aplicantes por Cargo",
        toolbar_location=None,
        tools="",
    )

    p.vbar(
        x="position_name",
        top="num_applicants",
        width=0.9,
        source=source,
        legend_field="position_name",
        line_color="white",
        fill_color=factor_cmap(
            "position_name", palette=Spectral6, factors=data_positions["position_name"]
        ),
    )

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Cargos"
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    p_div = components(p)
    return p_div


def habilidadesCampoExperiencia(query):
    # data_field_skills es un diccionario que contiene la información de la query a la BD, se tiene que cambiar
    data_field_skills = {
        "field_name": ["Field1", "Field1", "Field2"],
        "skill_name": ["Skill1", "Skill2", "Skill1"],
        "num_applicants": [50, 30, 80],
    }

    source = ColumnDataSource(data=data_field_skills)

    p = figure(
        x_range=data_field_skills["field_name"],
        plot_height=350,
        title="Habilidades Más Demandadas por Campo de Experiencia",
        toolbar_location=None,
        tools="",
    )

    p.vbar(
        x="field_name",
        top="num_applicants",
        width=0.9,
        source=source,
        legend_field="skill_name",
        line_color="white",
        fill_color=factor_cmap(
            "skill_name", palette=Spectral6, factors=data_field_skills["skill_name"]
        ),
    )

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Campos de Experiencia"
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    p_div = components(p)
    return p_div


def aplicantesExperiencia(query):
    # data_experience_years es un diccionario que contiene la información de la query a la BD, se tiene que cambiar
    data_experience_years = {
        "years_of_experience": [1, 2, 3, 4, 5],
        "num_applicants": [20, 40, 60, 80, 100],
    }

    source = ColumnDataSource(data=data_experience_years)

    p = figure(
        plot_height=350,
        title="Tendencias de Aplicantes por Año de Experiencia",
        toolbar_location=None,
        tools="",
    )

    p.vbar(
        x="years_of_experience",
        top="num_applicants",
        width=0.9,
        source=source,
        line_color="white",
        fill_color=Spectral6,
    )

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Número de Aplicantes"
    p.xaxis.axis_label = "Años de Experiencia"

    p_div = components(p)
    return p_div
