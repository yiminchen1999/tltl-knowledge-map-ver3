import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import pandas as pd
#import numpy as np
import base64
#import plotly.express as px
from dash.dependencies import Input, Output, State
from dash import html
import dash
import requests
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import os
import smtplib
from email.message import EmailMessage

#import plotly.express as px
import plotly.tools as tls
animated_title_style = {
    "font-size": "2rem",
    "font-weight": "bold",
    "color": "#fff",
    "text-shadow": "1px 1px 3px #333",
    "margin-left": "2rem",  # Add margin to move the title to the right
}
# Load the data
#data = pd.read_excel("assets/Year2023text/combined/2023_student1_8projects_combined.xlsx",engine='openpyxl')




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

server = app.server

navbar_style = {
    "box-shadow": "0 0 10px rgba(0, 0, 0, 0.3)",
}

navbar = dbc.Navbar(
    [
        html.A(
            "Knowledge Maps for Making",
            className="navbar-brand text-black",
            style={
                "font-size": "2.5rem",
                "font-weight": "bold",
                "color": "#fff",
                "margin-left": "2rem"
            }
        ),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("KNOWLEDGE MAPPING", href="/page-1")),
                dbc.NavItem(dbc.NavLink("GPT ASSISTANT", href="/page-3")),
                dbc.NavItem(dbc.NavLink("SENTIMENT MAPPING", href="/page-2")),

                dbc.NavItem(dbc.NavLink("ABOUT OUR LAB", href="https://tltlab.org/")),

            ],
            className="ml-auto",
            navbar=True,
        ),
    ],
    color="light",
    dark=False,
    sticky="top",
    style=navbar_style,
    className="navbar-custom"
)







content = html.Div(id="page-content")
initial_html = open("assets/2021_s1_weekly_1.html", 'r').read()
with open('assets/2021_s2_weekly_1.html', 'r') as f:
    second_html = f.read()

with open('assets/2021_s2_weekly_1.html', 'r') as f:
    third_html = f.read()
content = html.Div(id="page-content")
# Define the initial HTML content to display in the Iframe component
initial_html_aggregate = open('assets/2021_s1_aggregate_1.html', 'r').read()
initial_html_aggregate1 = open('assets/2021_s1_aggregate_1.html', 'r').read()
initial_html_posi= open('assets/class_positive_map_2021_1.html', 'r').read()
initial_html_nega= open('assets/class_negative_map_2021_1.html', 'r').read()

with open('assets/2021_s2_aggregate_1.html', 'r') as f:
    second_html_aggregate = f.read()

with open('assets/2021_s3_aggregate_1.html', 'r') as f:
    third_html_aggregate = f.read()


# Define the initial HTML content to display in the Iframe component
initial_html_class = open('assets/2021_class_1.html', 'r').read()

category_colors = {
    "Digital Fabrication": '#e3342f',
    "Electronics": '#f6993f',
    "Math/ Physics": '#ffed4a',
    "Programming": '#38c172',
    "Design/ Think": '#4dc0b5',
    "Materials": '#9561e2',
    "Hand Tools": '#f66d9b',
}


button_style = {
    'width': '60px',
    'height': '60px',
    'border-radius': '0',
    'border-top': '30px solid transparent',
    'border-bottom': '30px solid transparent',
    'border-right': '50px solid #343a40',
    'box-shadow': '0px 2px 10px rgba(0, 0, 0, 0.25)',
    'background-color': '#343a40',
    'color': 'white',
    'font-size': '1.2rem',
    'display': 'flex',
    'justify-content': 'center',
    'align-items': 'center',
    'cursor': 'pointer'
}

play_icon = html.I(className="bi bi-play-fill")

# Define the Sidebar
sidebar = html.Div(
    [
        dbc.Row(
            [html.H5('Individual knowledge map',
                        style={'margin-top': '12px', 'margin-left': '14px'})],
            style={"height": "5vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [html.Div([html.Hr(),html.P('Select a year first',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='text-black'),
                          dcc.Dropdown(id='yeardropdown', options=[{'label': '2021', 'value': '2021'},
                                                                    {'label': '2022', 'value': '2022'},
                                                                    {'label': '2023', 'value': '2023'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),

                          html.P('Select a student name',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='text-black'),
                          dcc.Dropdown(id='mydropdown',
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),
html.Hr(),

dbc.Card([
    dbc.CardHeader("Knowledge Categories", className="bg-primary text-white text-center"),
    dbc.Row([
        dbc.Col([
            dbc.ListGroup([
                html.Li(category.capitalize(),
                        className="list-group-item",
                        style={"list-style-type": "none", "background-color": category_colors[category], "font-size": "14px"})
                for category in list(category_colors)[:4]
            ], flush=True, className="border-0 shadow-sm list-group-flush")
        ], md=6.5),
        dbc.Col([
            dbc.ListGroup([
                html.Li(category.capitalize(),
                        className="list-group-item",
                        style={"list-style-type": "none", "background-color": category_colors[category], "font-size": "14px"})
                for category in list(category_colors)[4:]
            ], flush=True, className="border-0 shadow-sm list-group-flush")
        ], md=6.5),
    ],justify="around")
], className="border-0 shadow-sm mb-4", style={"background-color": "#F0F0F0"}),


                        html.Hr() ],
                      className='p-4')],
            # Add padding to the div
            style={'height': '73vh', 'margin': '10px', 'display': 'flex'},
            className='bg-white rounded shadow-sm mb-3' # Add a white background, rounded corners, and shadow
        ),



        html.Hr(style={ 'margin': '30px 0'}),
        dbc.Row(
            [html.H5('Collective knowledge map',style={'margin-top': '12px', 'margin-left': '14px'})],
            style={"height": "5vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [html.Div([html.Hr(),html.P('Select a year',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='text-black'),
                          dcc.Dropdown(id='yeardropdown1', options=[{'label': '2021', 'value': '2021'},
                                                                    {'label': '2022', 'value': '2022'},
                                                                    {'label': '2023', 'value': '2023'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}),
html.Hr()
                       ],
                          className='p-4') # Add padding to the div
            ],
            style={'height': '110vh', 'margin': '10px', 'display': 'flex'},
            className='bg-white rounded shadow-sm' #  white background, rounded corners, and shadow
        ),
        html.Hr(style={ 'margin': '20px 0'}),
    ],
    style={'padding-top': '20px', 'padding-bottom': '20px', 'background-color': '#f8f9fa'} # adding and background color to the sidebar
)



html_graphs = html.Div(
    [
        dbc.Container(
            [dbc.Row(
                [
                    dbc.Col(
                        [
html.Div(
    [
        html.P(
            'Weekly Knowledge Map',
            className='fs-5 text-center font-weight-bold',
            style={"font-size": "2.5rem", "font-weight": "bold", "margin-right": "-10px", "flex": "1"}
        ),
        html.Button(
            'i',
            id='info-button',
            className='badge rounded-pill bg-primary',
            style={ 'font-size': '0.95rem',"margin-left": "10px"}
        ),
    ],
    className='d-flex align-items-center',
    style={'display': 'flex'}
),
dbc.Modal(
    [
        dbc.ModalHeader("Weekly Knowledge Map"),
        dbc.ModalBody(
            [
                html.Ul(
                    [
                        html.Li("Knowledge keywords mentioned in reflection for a particular week.", style={'color': 'darkgrey'}),
                        html.Li("Each node represents a knowledge keyword with name underneath", style={'color': 'darkgrey'}),
                        html.Li("Color corresponds to the specific knowledge category", style={'color': 'darkgrey'}),
                    ]
                ),
                #html.Br(),
                html.P("  What can you do with the weekly knowledge map?"),
                html.P("    1.  Identify the specific concepts that you have applied during the week.",style={'color': 'darkgrey'}),
                html.P("    2.  By reviewing the nodes and categories on the map, you can reflect on the knowledge areas that you have engaged with and assess your level of understanding and application.", style={'color': 'darkgrey'})
            ]
        ),
        dbc.ModalFooter(html.Button('Close', id='close-button', className='btn btn-secondary'))
    ],
    id="info-modal",
    centered=True
),
                            #html.Button('i', id='info-button', className='badge rounded-pill bg-primary', style={'vertical-align': 'top'}),
                            html.P('Key concepts mentioned in a specific week',
                             className='fs-6 text-center',
                        style={"font-size": "1.0rem"}),
                            html.Iframe(id='html-iframe', srcDoc=initial_html, width='100%', height='600',
                                        style={'height': '60vh'}),

                            dbc.Row([dbc.Col([html.Div([
                                # html.Label('Select a week:', style={'fontSize': '20px'}),
                                dcc.Slider(
                                    id='myslider',
                                    min=1,
                                    max=10,
                                    value=1,
                                    step=1,
                                    updatemode='drag',
                                    marks={1: {'label': '1'}, 2: {'label': '2'}, 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                                           8: '8', 9: '9', 10: '10'},
                                    tooltip={"placement": "bottom", "always_visible": True}, included=False
                                ),
                                #dbc.Button("Click me!", id="button-1", color="primary", className="ml-2"),
                                dbc.Label("Week", className="text-center w-100 mb-0", width='10%'),
                            ], style={'width': '95%', 'margin': '20px', 'margin-top': '20px',
                                      'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 5}),

                    dbc.Col(
                        [


#, style={'width': '95%', 'margin': '30px', 'margin-top': '20px','color': '#000000','fontSize': '15px','padding': '5px'}
html.Div(
    [
        html.P(
            'Aggregate Knowledge Map',
            className='fs-5 text-center font-weight-bold',
            style={"font-size": "2.5rem", "font-weight": "bold", "margin-right": "-90px", "flex": "1"}
        ),
        html.Button(
            'i',
            id='info-button2',
            className='badge rounded-pill bg-primary',
            style={ 'font-size': '0.95rem',"margin-left": "10px"}
        ),
   html.Button(
                "play",
                id="button-1",
    className="btn-outline-secondary",
    style={"border-radius": "60px","margin-left": "10px"}
)
    ],
    className='d-flex align-items-center',
    style={'display': 'flex'}
),



dbc.Modal(
    [
        dbc.ModalHeader("Aggregate Knowledge Map"),
        dbc.ModalBody(
            [
                html.Ul(
                    [
                        html.Li("Knowledge keywords mentioned in reflections up to a certain week", style={'color': 'darkgrey'}),
                        html.Li("The color of the node corresponds to a specific knowledge category", style={'color': 'darkgrey'}),
                        html.Li("Within the same category, darker shades indicate their earlier occurrence", style={'color': 'darkgrey'}),
                        html.Li("Clicking on a node reveals the week in which the keyword was first mentioned", style={'color': 'darkgrey'}),
                        html.Li("Size of the node reflects the frequency of its occurrence", style={'color': 'darkgrey'}),
                    ]
                ),
                #html.Br(),3. You can click on the play button to see animated images showcasing the development of knowledge over time.
                html.P("  What can you do with the aggregate knowledge map?"),
                html.P("    1.  You can visualize your personal learning journey by identifying which concepts you have applied and how frequently you have engaged with them over time.",style={'color': 'darkgrey'}),
                html.P("    2.  It can help you identify patterns in your learning and identify topics that you may want to explore further.", style={'color': 'darkgrey'}),
                html.P("    3. You can click on the play button to see animated images showcasing the development of knowledge over time in 2023.",
                    style={'color': 'darkgrey'}),
            ]
        ),
        dbc.ModalFooter(html.Button('Close', id='close-button2', className='btn btn-secondary'))
    ],
    id="info-modal2",
    centered=True
),
                            html.P('Development of key concepts over time',
                                   className='fs-6 text-center',
                                   style={"font-size": "1.0rem"}),
                            html.Iframe(id='html-iframe-2', srcDoc=initial_html_aggregate, width='100%', height='600',
                                        style={'height': '60vh'}),

                            dbc.Row([dbc.Col([html.Div([
                                # html.Label('Select a week:', style={'fontSize': '20px'}),
                                dcc.Slider(
                                    id='myslider2',
                                    min=1,
                                    max=10,
                                    value=1,
                                    step=1,
                                    updatemode='drag',
                                    marks={1: {'label': '1'}, 2: {'label': '2'}, 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                                           8: '8', 9: '9', 10: '10'},
                                    tooltip={"placement": "bottom", "always_visible": True}, included=False
                                ),
                                dbc.Label("Week", className="text-center w-100 mb-0", width='10%'),

dbc.Container(


dbc.Modal(
    [
        dbc.ModalHeader("",id="final-window"),
        dbc.ModalBody(html.Img(id="gif-player",style={'width': '100%', 'height': '100%'})),
        dbc.ModalFooter(
            dbc.Button("Close", id="close-button3", className="ml-auto")
        )
    ],
    id="gif-modal",
    #centered=True,
    size="lg",
    style={'width': '100%',  'height': '1000px',  'overflow': 'hidden'}
)

)


                            ], style={'width': '95%', 'margin': '20px', 'margin-top': '20px',
                                      'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 5}),
                    #dbc.Col(
                        #[
                           # html.Div(
                                #html.P('Collective Knowledge in the Class (weekly)',
                                       #className='text-nowrap bd-highlight',
                                       #style={'fontWeight': 'bold'}),

                               # className='d-flex justify-content-end',
                               # style={'text-align': 'right', 'margin-right': '-70px'}
                            #),




dbc.Col(
                        [  html.Div([html.Div('Collective Knowledge Map', id='title',
                                                   className='fs-4 font-weight-bold title-text',
                                                   style={'fontWeight': 'bold', 'cursor': 'pointer'}),
                                          html.Button('i', id='info-button4', className='badge rounded-pill bg-primary',
                                                      style={ 'font-size': '0.8rem',
                                                             'display': 'inline-block', 'margin': '10px'})],
                                         className='d-flex justify-content-end align-items-center',
         style={'margin-right': '-85px'}
         ),




dbc.Modal(
    [
        dbc.ModalHeader("Collective Knowledge Map"),
        dbc.ModalBody(
            [
                html.Ul(
                    [
                        html.Li("All knowledge keywords mentioned by all students in a class in their reflections for a particular week", style={'color': 'darkgrey'}),
                        html.Li("The color of the node corresponds to a specific knowledge category ", style={'color': 'darkgrey'}),
                        html.Li("Clicking on a node reveals the names of the students who mentioned the keyword", style={'color': 'darkgrey'}),
                        html.Li("Size of the node reflects the number of students who mentioned it", style={'color': 'darkgrey'}),

                    ]
                ),
                #html.Br(),
                html.P(" What can you do with the collective knowledge map?"),
                html.P("    1.  You can see what concepts your classmates have applied.",style={'color': 'darkgrey'}),
                html.P("    2.  It can serve as a resource for collaboration, discussion, and peer learning.", style={'color': 'darkgrey'})
            ]
        ),
        dbc.ModalFooter(html.Button('Close', id='close-button4', className='btn btn-secondary'))
    ],
    id="info-modal4",
    centered=True
),

html.Div(
                                html.P('All key concepts mentioned in the class',
                                       className='text-nowrap bd-highlight',
                                       style={'fontWeight': 'bold'}),

                                className='fs-6 d-flex justify-content-end',
                                style={'text-align': 'right', 'margin-right': '-50px'}
                            ),
                            html.Iframe(id='html-iframe-4', srcDoc=initial_html_aggregate, width='170%', height='800',
                                        style={'height': '75vh'}),

                            dbc.Row([dbc.Col([html.Div([
                                # html.Label('Select a week:', style={'fontSize': '20px'}),
                                dcc.Slider(
                                    id='myslider3',
                                    min=1,
                                    max=10,
                                    value=1,
                                    step=1,
                                    updatemode='drag',
                                    marks={1: {'label': '1'}, 2: {'label': '2'}, 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                                           8: '8', 9: '9', 10: '10'},
                                    tooltip={"placement": "bottom", "always_visible": True}, included=False
                                ),
                                dbc.Label("Week", className="text-center w-100 mb-0", width='10%'),
                            ], style={'width': '160%', 'margin': '20px', 'margin-top': '20px',
                                      # 'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 6}),

                ], style={"height": "100vh"}
            )

            ],
            fluid=True
        )
    ])

@app.callback(
    Output("info-modal", "is_open"),
    [Input("info-button", "n_clicks"), Input("close-button", "n_clicks")],
    [State("info-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("info-modal2", "is_open"),
    [Input("info-button2", "n_clicks"), Input("close-button2", "n_clicks")],
    [State("info-modal2", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("info-modal4", "is_open"),
    [Input("info-button4", "n_clicks"), Input("close-button4", "n_clicks")],
    [State("info-modal4", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# Get the absolute path of the current working directory
#base_dir = os.path.abspath(os.getcwd())

# Set the path to the GIF file relative to the base directory
#gif_path = os.path.join(base_dir, "assets/animation_1.gif")

@app.callback(
    Output("gif-modal", "is_open"),
    [Input("button-1", "n_clicks"), Input("close-button3", "n_clicks")],
    [State("gif-modal", "is_open")]
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    [Output("gif-player", "src"), Output("final-window", "children")],
    [Input("button-1", "n_clicks"), Input('yeardropdown', 'value'), Input('mydropdown', 'value')]
)
def play_gif(n_clicks, yeardropdown, mydropdown):
    if n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Eury':
        with open("assets/2023_s1_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
               html.P(mydropdown+"’s development of knowledge over time") )

    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Sadia':
        with open("assets/2023_s2_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Helen':
        with open("assets/2023_s3_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Xichen':
        with open("assets/2023_s4_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Zhanlan':
        with open("assets/2023_s5_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Katie':
        with open("assets/2023_s6_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Andrea':
        with open("assets/2023_s7_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Ana Maria':
        with open("assets/2023_s8_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Heidi':
        with open("assets/2023_s9_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Mariana':
        with open("assets/2023_s10_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Inara':
        with open("assets/2023_s11_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))
    elif n_clicks is not None and yeardropdown == '2023' and mydropdown == 'Kiki':
        with open("assets/2023_s12_animation_2.0.gif", "rb") as f:
            gif_data = f.read()
        return ("data:image/gif;base64," + base64.b64encode(gif_data).decode(),
                html.P(mydropdown + "’s development of knowledge over time"))

    else:
        return (
            None,
            html.P("Sorry it only shows animation for year 2023!" )
        )





# Define the App Layout
page_1_layout = html.Div(
    [
        dbc.Container(
            [
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col(
                            sidebar,
                            width=3,
                            className='bg-dark p-4',
                            style={'border-radius': '20px', 'box-shadow': '4px 4px 8px 0 rgba(0,0,0,0.2)'}
                        ),
dbc.Col(
    html_graphs,
    className='p-4',
    style={'border-radius': '30px', 'box-shadow': '4px 4px 8px 0 rgba(0,0,0,0.2)', 'margin-right': '-130px'}
),
                    ],
                    className='mt-4'
                )
            ],
            fluid=True,
            className='p-4'
        )
    ],
    style={'background': '#f8f9fa'}
)

# define the layout for the second page


sidebarpage2 = html.Div(
    [
        dbc.Row(
            [html.H5('COLLECTIVE SENTIMENT MAP ',
                        style={'margin-top': '12px', 'margin-left': '14px'})],
            style={"height": "5vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [html.Div([html.Hr(),html.P('Select a year',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='text-black'),
                          dcc.Dropdown(id='yeardropdown2', options=[{'label': '2021', 'value': '2021'},
                                                                    {'label': '2022', 'value': '2022'},
                                                                    {'label': '2023', 'value': '2023'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),
html.Hr(),

dbc.Card([
    dbc.CardHeader("Knowledge Categories", className="bg-primary text-white text-center"),
    dbc.Row([
        dbc.Col([
            dbc.ListGroup([
                html.Li(category.capitalize(),
                        className="list-group-item",
                        style={"list-style-type": "none", "background-color": category_colors[category], "font-size": "14px"})
                for category in list(category_colors)[:4]
            ], flush=True, className="border-0 shadow-sm list-group-flush")
        ], md=6.5),
        dbc.Col([
            dbc.ListGroup([
                html.Li(category.capitalize(),
                        className="list-group-item",
                        style={"list-style-type": "none", "background-color": category_colors[category], "font-size": "14px"})
                for category in list(category_colors)[4:]
            ], flush=True, className="border-0 shadow-sm list-group-flush")
        ], md=6.5),
    ],justify="around")
], className="border-0 shadow-sm mb-4", style={"background-color": "#F0F0F0"}),
                       ],
                          className='p-4')], # Add padding to the div
            style={'height': '63vh', 'margin': '10px', 'display': 'flex'},
            className='bg-white rounded shadow-sm' # Add a white background, rounded corners, and shadow
        ),
        html.Hr(style={ 'margin': '30px 0'}),
        dbc.Row(
            [html.H5('SENTIMENT SIGNALS  ACROSS STUDENTS',style={'margin-top': '12px', 'margin-left': '14px'})],
            style={"height": "8vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [html.Div([html.Hr(),html.P('Only available for 2023 students',
                                 style={'font-size': '0.92rem'},
                                 className='text-black'),
                        ],
                          className='p-4') # Add padding to the div
            ],
            style={'height': '60vh', 'margin': '10px', 'display': 'flex'},
            className='bg-white rounded shadow-sm' #  white background, rounded corners, and shadow
        ),
html.Hr(style={ 'margin': '40px 0'}),
dbc.Row(
            [html.H5('SENTIMENT SIGNALS ACROSS PROJECTS',style={'margin-top': '12px', 'margin-left': '14px'})],
            style={"height": "8vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [html.Div([html.Hr(),html.P('Only available for 2023 students',
                                 style={'font-size': '0.92rem'},
                                 className='text-black'),
                        ],
                          className='p-4')
            ],
            style={'height': '70vh', 'margin': '10px', 'display': 'flex'},
            className='bg-white rounded shadow-sm' #  white background, rounded corners, and shadow
        ),
        html.Hr(style={ 'margin': '20px 0'}),
    ],
    style={'padding-top': '20px', 'padding-bottom': '20px', 'background-color': '#f8f9fa'} # adding and background color to the sidebar
)



data = pd.read_excel("assets/Year2023text/combined/2023_student1_8projects_combined.xlsx",
     engine='openpyxl')


html_graphs2 = html.Div(
    [
        dbc.Container(
            [dbc.Row(
                [
                    dbc.Col(
                        [

                            html.Div(
                                [
                                    html.P(
                                        'Positive Sentiment in Each Week',
                                        className='fs-5 text-center font-weight-bold',
                                        style={"font-size": "2.5rem", "font-weight": "bold", "margin-right": "-40px",
                                               "flex": "1"}
                                    ),
                                    html.Button(
                                        'i',
                                        id='info-button6',
                                        className='badge rounded-pill bg-primary',
                                        style={'font-size': '0.95rem', "margin-left": "10px"}
                                    ),
                                ],
                                className='d-flex align-items-center',
                                style={'display': 'flex'}
                            ),
                            dbc.Modal(
                                [
                                    dbc.ModalHeader("Positive Sentiment in Each Week"),
dbc.ModalBody(
            [
                html.Ul(
                    [
                        html.Li("All knowledge keywords mentioned by all students in a class in their reflections with a positive sentiment for a particular week", style={'color': 'darkgrey'}),
                        html.Li("The color of the node corresponds to a specific knowledge category", style={'color': 'darkgrey'}),
                        html.Li("Clicking on a node reveals the names of the students who mentioned the keyword ", style={'color': 'darkgrey'}),
                        html.Li("Size of the node reflects the number of students who mentioned it", style={'color': 'darkgrey'}),
                    ]
                ),
                #html.Br(),
                html.P("  What can you do with this Map?"),
                html.P("    1.  Identify the knowledge categories and specific knowledge keywords that have elicited positive sentiment from the students in the class.",style={'color': 'darkgrey'}),
                html.P("    2.  Gain insights into what concepts are resonating with the students in the class and incorporate them into future lesson plans or discussions.", style={'color': 'darkgrey'})
            ]
        ),
                                    dbc.ModalFooter(
                                        html.Button('Close', id='close-button6', className='btn btn-secondary'))
                                ],
                                id="info-modal6",
                                centered=True
                            ),
                            # html.Button('i', id='info-button', className='badge rounded-pill bg-primary', style={'vertical-align': 'top'}),
                            html.P(
                                'Identify the knowledge categories and specific keywords that have elicited positive sentiment from students',
                                className='fs-6 text-center',
                                style={"font-size": "1.0rem"}),
                            html.Iframe(id='html-iframe-5', srcDoc="", width='100%', height='600',
                                        style={'height': '50vh'}),

                            dbc.Row([dbc.Col([html.Div([
                                # html.Label('Select a week:', style={'fontSize': '20px'}),
                                dcc.Slider(
                                    id='myslider4',
                                    min=1,
                                    max=10,
                                    value=1,
                                    step=1,
                                    updatemode='drag',
                                    marks={1: {'label': '1'}, 2: {'label': '2'}, 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                                           8: '8', 9: '9', 10: '10'},
                                    tooltip={"placement": "bottom", "always_visible": True}, included=False
                                ),
                                dbc.Label("Week", className="text-center w-100 mb-0", width='10%'),
                            ], style={'width': '95%', 'margin': '20px', 'margin-top': '20px',
                                      # 'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 5}),

                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.P(
                                        'Negative Sentiment in Each Week ',
                                        className='fs-5 text-center font-weight-bold',
                                        style={"font-size": "2.5rem", "font-weight": "bold", "margin-right": "-40px",
                                               "flex": "1"}
                                    ),
                                    html.Button(
                                        'i',
                                        id='info-button7',
                                        className='badge rounded-pill bg-primary',
                                        style={'display': 'inline-block','font-size': '0.95rem', "margin-left": "10px"}
                                    ),
                                ],
                                className='d-flex align-items-center',
                                style={'display': 'flex'}
                            ),
                            dbc.Modal(
                                [
                                    dbc.ModalHeader("Negative Sentiment in Each Week"),
                                    dbc.ModalBody(
                                    [
                                    html.Ul(
                                     [
                        html.Li("All knowledge keywords mentioned by all students in a class in their reflections with a negative sentiment for a particular week", style={'color': 'darkgrey'}),
                        html.Li("The color of the node corresponds to a specific knowledge category", style={'color': 'darkgrey'}),
                        html.Li("Clicking on a node reveals the names of the students who mentioned the keyword ", style={'color': 'darkgrey'}),
                        html.Li("Size of the node reflects the number of students who mentioned it", style={'color': 'darkgrey'}),
                                     ]
                                             ),
                #html.Br(),
                html.P("  What can you do with this map?"),
                html.P("    1.  Identify which knowledge students may be struggling with or finding challenging.",style={'color': 'darkgrey'}),
                html.P("    2.  Adjust teaching methods accordingly or provide additional support to help students overcome difficulties.", style={'color': 'darkgrey'})
            ]
        ),

                                    dbc.ModalFooter(
                                        html.Button('Close', id='close-button7', className='btn btn-secondary'))
                                ],
                                id="info-modal7",
                                centered=True
                            ),
                            # html.Button('i', id='info-button', className='badge rounded-pill bg-primary', style={'vertical-align': 'top'}),
                            html.P(
                                'Identify the knowledge categories and specific keywords that have elicited negative sentiment from students',
                                className='fs-6 text-center',
                                style={"font-size": "1.0rem"}),
                            html.Iframe(id='html-iframe-6', src="", width='100%', height='600',
                                        style={'height': '50vh'}),

                            dbc.Row([dbc.Col([html.Div([
                                dcc.Slider(
                                    id='myslider5',
                                    min=1,
                                    max=10,
                                    value=1,
                                    step=1,
                                    updatemode='drag',
                                    marks={1: {'label': '1'}, 2: {'label': '2'}, 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                                           8: '8', 9: '9', 10: '10'},
                                    tooltip={"placement": "bottom", "always_visible": True}, included=False
                                ),
                                dbc.Label("Week", className="text-center w-100 mb-0", width='10%'),
                            ], style={'width': '95%', 'margin': '20px', 'margin-top': '20px',
                                      # 'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 5}),
#p-2 align-items-stretch text-end fs-6 font-weight-bold
                    dbc.Col(
                        [
                            #html.Div([
                                #html.Div('Sentiment Analysis of one student on all projects',
                                         #id='title',
                                         #className='fs-5 text-center font-weight-bold',
                                         #style={'fontWeight': 'bold', 'cursor': 'pointer'}),
                               # html.Div(id='text-box-container')
                            #]),

 html.Div([
                                html.Div([html.Div('Sentiment Signals Organized by Students', id='title',
                                                   className='fs-4 text-center font-weight-bold title-text',
                                                   style={'fontWeight': 'bold', 'cursor': 'pointer'}),
                                          html.Button('i', id='info-button9', className='badge rounded-pill bg-primary',
                                                      style={ 'font-size': '0.8rem',
                                                             'display': 'inline-block', 'margin': '10px'})],
                                         className='d-flex text-center justify-content-center align-items-center'),
 dbc.Modal(
                                [
                                    dbc.ModalHeader("Sentiment Signals Organized by Students"),
dbc.ModalBody(
            [
                html.Ul(
                    [
                        html.Li("Display sentiment analysis of one student’s projects over the semester", style={'color': 'darkgrey'}),
                        html.Li("Each dot on the map represents a sentence that contains knowledge keyword(s)", style={'color': 'darkgrey'}),
                        html.Li("Red indicates negative sentiment", style={'color': 'darkgrey'}),
                        html.Li("Green indicates positive sentiment", style={'color': 'darkgrey'}),
                        html.Li("Grey indicates neutral sentiment", style={'color': 'darkgrey'}),
                    ]
                ),
                #html.Br(),
                html.P("  What can you do with this graph?"),
                html.P("    1.  Gain insight into the a student’s overall attitudes towards different projects throughout the semester.",style={'color': 'darkgrey'}),
                html.P("    2.  Identify projects where the student may be struggling or excelling and where further feedback or guidance is needed.", style={'color': 'darkgrey'})
            ]
        ),
                                    dbc.ModalFooter(
                                        html.Button('Close', id='close-button9', className='btn btn-secondary'))
                                ],
                                id="info-modal9",
                                centered=True
                            ),

html.Div(
                                html.P('Sentiment signals of one student’s projects over the semester',
                                       className='text-nowrap bd-highlight',
                                       style={'fontWeight': 'bold'}),

                                className='fs-6 d-flex justify-content-center',
                                style={'text-align': 'center', 'margin-right': '-50px'}
                            ),
                                html.Div(id='text-box-container',
                                         style={'display': 'flex', 'justify-content': 'space-between'})
                            ]),
                            html.Div([
                                dcc.Graph(id='my-graph')
                            ]),

                            dbc.Row([dbc.Col([html.Div([
                                # html.Label('Select a week:', style={'fontSize': '20px'}),
                                dcc.Slider(
                                    id='myslider6',
                                    min=1,
                                    max=12,
                                    value=1,
                                    step=1,
                                    updatemode='drag',
                                    marks={1: {'label': 'Eury'}, 2: {'label': 'Sadia'}, 3: {'label': 'Helen'}, 4: {'label': 'Xichen'}, 5: {'label': 'Zhanlan'}, 6: {'label': 'Katie'}, 7: {'label': 'Andrea'},
                                           8: {'label': 'Ana Maria'}, 9: {'label': 'Heidi'}, 10: {'label': 'Mariana'},11: {'label': 'Inara'},12: {'label': 'Kiki'}},
                                    included=False
                                ),
                                #dbc.Label("Student Name", className="text-center w-100 mb-0", width='10%'),
                            ], style={'width': '90%', 'margin': '20px', 'margin-top': '20px',
                                      # 'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 10}),#

                    dbc.Col(
                        [
                            html.Div([
                                html.Div([html.Div('Sentiment Signals Organized by Projects', id='title',
                                                   className='fs-4 text-center font-weight-bold title-text',
                                                   style={'fontWeight': 'bold', 'cursor': 'pointer'}),
                                          html.Button('i', id='info-button8', className='badge rounded-pill bg-primary',
                                                      style={ 'font-size': '0.8rem',
                                                             'display': 'inline-block', 'margin': '10px'})],
                                         className='d-flex text-center justify-content-center align-items-center'),
 dbc.Modal(
                                [
                                    dbc.ModalHeader("Sentiment Signals Organized by Projects"),
                                    dbc.ModalBody(
                                        [
                                            html.Ul(
                                                [
                                                    html.Li(
                                                        "Display sentiment analysis of a project for all students in a class",
                                                        style={'color': 'darkgrey'}),
                                                    html.Li(
                                                        "Each dot on the map represents a sentence that contains knowledge keyword(s)",
                                                        style={'color': 'darkgrey'}),
                                                    html.Li(
                                                        "Red indicates negative sentiment",
                                                        style={'color': 'darkgrey'}),
                                                    html.Li(
                                                        "Green indicates positive sentiment",
                                                        style={'color': 'darkgrey'}),
                                                    html.Li("Grey indicates neutral sentiment",
                                                            style={'color': 'darkgrey'}),
                                                ]
                                            ),
                                            # html.Br(),
                                            html.P("  What can you do with this graph?"),
                                            html.P(
                                                "    1.  Identify common positive and negative sentiment trends in a project across all students.",
                                                style={'color': 'darkgrey'}),
                                            html.P(
                                                "    2.  Communicate with students who exhibit a relatively higher amount of negative sentiment to offer them assistance.",
                                                style={'color': 'darkgrey'})
                                        ]
                                    ),
                                    dbc.ModalFooter(
                                        html.Button('Close', id='close-button8', className='btn btn-secondary'))
                                ],
                                id="info-modal8",
                                centered=True
                            ),

html.Div(
                                html.P('Sentiment signals of a project for all students in the class',
                                       className='text-nowrap bd-highlight',
                                       style={'fontWeight': 'bold'}),

                                className='fs-6 d-flex justify-content-center',
                                style={'text-align': 'center', 'margin-right': '-50px'}
                            ),
                                html.Div(id='text-box-container',
                                         style={'display': 'flex', 'justify-content': 'space-between'})
                            ]),
                            html.Div([
                                dcc.Graph(id='my-graph2')
                            ]),
                            dbc.Row([dbc.Col([html.Div([
                                # html.Label('Select a week:', style={'fontSize': '20px'}),
                                dcc.Slider(
                                    id='myslider7',
                                    min=1,
                                    max=9,
                                    value=1,
                                    step=1,
                                    updatemode='drag',
                                    marks={1: {'label': 'frank'}, 2: {'label': 'omni'},
                                           3: {'label': 'remix'}, 4: {'label': 'rube'}, 5: {'label': 'dream1'},
                                           6: {'label': 'dream2'},
                                           7: {'label': 'dream3'}, 8: {'label': 'lofi'},9: {'label': 'tool'}},
                                     included=False
                                ),
                                #dbc.Label("Project Name", className="text-center w-100 mb-0", width='10%'),
                            ], style={'width': '90%', 'margin': '20px', 'margin-top': '20px',
                                      # 'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 10})

                ], style={"height": "220vh"}
            )

            ],
            fluid=True
        )
    ])

@app.callback(
    Output("info-modal6", "is_open"),
    [Input("info-button6", "n_clicks"), Input("close-button6", "n_clicks")],
    [State("info-modal6", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("info-modal7", "is_open"),
    [Input("info-button7", "n_clicks"), Input("close-button7", "n_clicks")],
    [State("info-modal7", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("info-modal8", "is_open"),
    [Input("info-button8", "n_clicks"), Input("close-button8", "n_clicks")],
    [State("info-modal8", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("info-modal9", "is_open"),
    [Input("info-button9", "n_clicks"), Input("close-button9", "n_clicks")],
    [State("info-modal9", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# Define the App Layout

page_2_layout = html.Div(
    [
        dbc.Container(
            [
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col(
                            sidebarpage2,
                            width=3,
                            className='bg-dark p-4',
                            style={'border-radius': '20px', 'box-shadow': '4px 4px 8px 0 rgba(0,0,0,0.2)'}
                        ),
                        dbc.Col(
                            html_graphs2,
                            className='p-4',
                            style={'border-radius': '20px', 'box-shadow': '4px 4px 8px 0 rgba(0,0,0,0.2)','margin-right': '-130px'}
                        ),
                    ],
                    className='mt-4'
                )
            ],
            fluid=True,
            className='p-4'
        )
    ],
    style={'background': '#f8f9fa'}
)


from email.message import EmailMessage

page_3_layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('GPT ASSISTANT'), className="mt-3 mb-5")
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label("Select a student name"),
            dcc.Dropdown(
                id='student-dropdown',
                options=[
                    {'label': 'Eury', 'value': 'Eury'},
                    {'label': 'Sadia', 'value': 'Sadia'},
                    {'label': 'Helen', 'value': 'Helen'},
                    {'label': 'Xichen', 'value': 'Xichen'},
                    {'label': 'Zhanlan', 'value': 'Zhanlan'},
                    {'label': 'Katie', 'value': 'Katie'},
                    {'label': 'Andrea', 'value': 'Andrea'},
                    {'label': 'Ana Maria', 'value': 'Ana Maria'},
                    {'label': 'Heidi', 'value': 'Heidi'},
                    {'label': 'Mariana', 'value': 'Mariana'},
                    {'label': 'Inara', 'value': 'Inara'},
                    {'label': 'Kiki', 'value': 'Kiki'}
                ],
                style={'width': '100%'}
            ),
            html.Br(),
            html.Div(id='teacher-letter-text', className="mt-3")
        ], width=6, className="mx-auto"),
        dbc.Col([
            html.P('If you have any feedback for the GPT Assistant, please type it below:', className="mb-2"),
            dcc.Textarea(id='feedback-input', value='', placeholder='Type your feedback here...',
                         style={'width': '100%', 'height': 200, 'resize': 'vertical'}, className="mb-3"),
            dbc.Button('Submit', id='submit-button', color='primary', className="mb-3")
        ], width=6, className="mx-auto")
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='output-container', children=''), className="text-center")
    ])
], className="my-5")


import os
import smtplib
from email.message import EmailMessage

@app.callback(
    Output('teacher-letter-text', 'children'),
    Input('student-dropdown', 'value'))
def display_student_feedback(name):
    if name:
        file_path = f"{name}.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                feedback = f.read().splitlines()
        else:
            feedback = [f"No feedback found for {name}."]
    else:
        feedback = ["Select a student to view their feedback."]
    return [html.P(paragraph) for paragraph in feedback]

@app.callback(
    Output('output-container', 'children'),
    Input('submit-button', 'n_clicks'),
    State('student-dropdown', 'value'),
    State('feedback-input', 'value'))
def save_feedback(n_clicks, student_name, feedback_text):
    if n_clicks:
        if not student_name:
            return html.Div('Please select a student name.', style={'color': 'red'})
        if not feedback_text:
            return html.Div('Feedback cannot be empty.', style={'color': 'red'})

        return html.Div('Feedback submitted successfully!', style={'color': 'green'})



    # create the callback for rendering the different pages
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/page-1":
        return html.Div(page_1_layout)
    elif pathname == "/page-2":
        return html.Div(page_2_layout)
    elif pathname == "/page-3":
        return html.Div(page_3_layout)
    else:
        return html.Div(page_1_layout)




@app.callback(
    dash.dependencies.Output('popup', 'displayed'),
    [dash.dependencies.Input('popup', 'submit_n_clicks')]
)
def display_popup(n):
    if n is None:
        return True
    else:
        return False


# define the app layout
app.layout = html.Div(
    [
        dcc.ConfirmDialog(
            id='popup',
            message='Thank you for visiting my website, and if you want to view details of each map, just click the information box at the right side!',
            displayed=False,

        ),

    html.Div(
        #html.H1('Welcome to my website!', style={'text-align': 'center'}),
        style={
            'width': '100%',
            'height': '6vh',
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'background': 'linear-gradient(to right, #000000, #fff)'
        }
    ),
        dcc.Location(id="url"),
        navbar,
        html.Div(id="page-content"),
html.Div(
        #html.H1('Welcome to my website!', style={'text-align': 'center'}),
        style={
            'width': '100%',
            'height': '6vh',
            'display': 'flex',
            'justify-content': 'button',
            'align-items': 'center',
            'background': 'linear-gradient(to right, #000000, #fff)'
        }
    ),
    ]
)



import pandas as pd


import pandas as pd
import plotly.graph_objs as go

@app.callback(
    Output('my-graph', 'figure'),
    [Input('myslider6', 'value')]
)
def update_graph(selected_week):
    # Get the corresponding file based on the selected week
    file_name = f'assets/Year2023text/combined/2023_student{selected_week}_8projects_combined.xlsx'
    # Load the data from the file
    data = pd.read_excel(file_name,engine='openpyxl')
    # Define a dictionary mapping labels to colors
    label_colors = {'positive': 'green', 'negative': 'red', 'neutral': 'rgb(211, 211, 211)'}
    # Create a new column in the DataFrame containing the color for each label
    data['color'] = data['label'].map(label_colors)
    # Create the tick labels for the x-axis
    tick_labels = ['Project 1', 'Project 2', 'Project 3', 'Project 4', 'Project 5', 'Project 6', 'Project 7',
                   'Project 8']

    # Create the graph figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Name'], y=data['score'], mode='markers', marker=dict(color=data['color'], size=15, line=dict(width=1, color='black')),
                             text=data['label'], hovertemplate="<b>%{text}</b><br><br>Name: %{x}<br>Score: %{y:.2f}<extra></extra>"))
    fig.update_layout(
        xaxis=dict(showgrid=False, tickangle=45, tickfont=dict(size=14),
                   ticktext=tick_labels),
        yaxis=dict(title='<b>Score</b>', showgrid=True, gridcolor='rgb(238,238,238)', tickfont=dict(size=14),
                   zeroline=True, zerolinecolor='rgb(128,128,128)'),
        legend=dict(title='<b>Sentiment</b>', orientation='h', yanchor='top', xanchor='left', y=1.1, x=0),
                      #margin=dict(l=50, r=50, t=100, b=50),
                      plot_bgcolor='rgb(255, 255, 255)',
                      paper_bgcolor='rgb(255, 255, 255)',
                      font=dict(size=13, color='grey'))
    return fig


@app.callback(
    Output('my-graph2', 'figure'),
    [Input('myslider7', 'value')]
)

def update_graph(project):
    # Get the corresponding file based on the selected week
    file_name = f'assets/Year2023text/combined/2023_student_{project}.xlsx'
    # Load the data from the file
    data = pd.read_excel(file_name,engine='openpyxl')
    # Define a dictionary mapping labels to colors
    label_colors = {'positive': 'green', 'negative': 'red', 'neutral': 'rgb(211, 211, 211)'}
    # Create a new column in the DataFrame containing the color for each label
    data['color'] = data['label'].map(label_colors)
    # Create the tick labels and tick values for the x-axis
    marks = {1: {'label': 'Eury'}, 2: {'label': 'Sadia'}, 3: {'label': 'Helen'}, 4: {'label': 'Xichen'},
             5: {'label': 'Zhanlan'}, 6: {'label': 'Katie'}, 7: {'label': 'Andrea'},
             8: {'label': 'Ana Maria'}, 9: {'label': 'Heidi'}, 10: {'label': 'Mariana'}, 11: {'label': 'Inara'},
             12: {'label': 'Kiki'}}
    tick_labels = [marks[i]['label'] for i in range(1, len(marks) + 1)]
    tick_vals = list(range(1, len(marks) + 1))
    # Create the graph figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['student number'], y=data['score'], mode='markers', marker=dict(color=data['color'], size=15, line=dict(width=1, color='black')),
                             text=data['label'], hovertemplate="<b>%{text}</b><br><br>Name: %{x}<br>Score: %{y:.2f}<extra></extra>"))
    fig.update_layout(
        xaxis=dict(showgrid=False, tickangle=45, tickfont=dict(size=14), ticktext=tick_labels, tickvals=tick_vals),
        yaxis=dict(title='<b>Score</b>', showgrid=True, gridcolor='rgb(238,238,238)', tickfont=dict(size=14),
                   zeroline=True, zerolinecolor='rgb(128,128,128)'),
        legend=dict(title='<b>Sentiment</b>', orientation='h', yanchor='top', xanchor='left', y=1.1, x=0),
        plot_bgcolor='rgb(255, 255, 255)',
        paper_bgcolor='rgb(255, 255, 255)',
        font=dict(size=13, color='grey'))
    return fig



# Define the callbacks of year dropdown and weekly dropdown
@app.callback(
    Output('mydropdown', 'options'),
    Input('yeardropdown', 'value'))
def update_students(year):
    if year == '2021':
        options = [
            {'label': 'Student 1', 'value': 'student 1'},
            {'label': 'Student 2', 'value': 'student 2'},
            {'label': 'Student 3', 'value': 'student 3'},
            {'label': 'Student 4', 'value': 'student 4'},
            {'label': 'Student 5', 'value': 'student 5'},
            {'label': 'Student 6', 'value': 'student 6'},
            {'label': 'Student 7', 'value': 'student 7'}
        ]
    elif year == '2022':
        options = [
            {'label': 'Student 1', 'value': 'Student 1'},
            {'label': 'Student 2', 'value': 'Student 2'},
            {'label': 'Student 3', 'value': 'Student 3'},
            {'label': 'Student 4', 'value': 'Student 4'},
            {'label': 'Student 5', 'value': 'Student 5'},
            {'label': 'Student 6', 'value': 'Student 6'},
            {'label': 'Student 7', 'value': 'Student 7'},
            {'label': 'Student 8', 'value': 'Student 8'},
            {'label': 'Student 9', 'value': 'Student 9'},
            {'label': 'Student 10', 'value': 'Student 10'},
            {'label': 'Student 11', 'value': 'Student 11'},
            {'label': 'Student 12', 'value': 'Student 12'}
        ]
    elif year == '2023':
        options = [
            {'label': 'Eury', 'value': 'Eury'},
            {'label': 'Sadia', 'value': 'Sadia'},
            {'label': 'Helen', 'value': 'Helen'},
            {'label': 'Xichen', 'value': 'Xichen'},
            {'label': 'Zhanlan', 'value': 'Zhanlan'},
            {'label': 'Katie', 'value': 'Katie'},
            {'label': 'Andrea', 'value': 'Andrea'},
            {'label': 'Ana Maria', 'value': 'Ana Maria'},
            {'label': 'Heidi', 'value': 'Heidi'},
            {'label': 'Mariana', 'value': 'Mariana'},
            {'label': 'Inara', 'value': 'Inara'},
            {'label': 'Kiki', 'value': 'Kiki'}
        ]
    else:
        options = []
    return options



# Define the callback function for Individual Weekly Graph
@app.callback(
    Output('html-iframe', 'srcDoc'),
   #[Input('mydropdown', 'value')]
    [Input('yeardropdown', 'value'),Input('mydropdown', 'value'),Input('myslider', 'value')]
)

def update_output(yeardropdown,mydropdown,myslider):
    # Define the HTML content to display based on the dropdown menu
    if yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 1:
        return open('assets/2021_s1_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 1:
        return open('assets/2021_s2_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 1:
        return open('assets/2021_s3_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 1:
        return open('assets/2021_s4_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 1:
        return open('assets/2021_s5_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 1:
        return open('assets/2021_s6_weekly_1.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 1:
        return open('assets/2021_s7_weekly_1.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 2:
        return open('assets/2021_s1_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 2:
        return open('assets/2021_s2_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 2:
        return open('assets/2021_s3_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 2:
        return open('assets/2021_s4_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 2:
        return open('assets/2021_s5_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 2:
        return open('assets/2021_s6_weekly_2.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 2:
        return open('assets/2021_s7_weekly_2.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 3:
        return open('assets/2021_s1_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 3:
        return open('assets/2021_s2_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 3:
        return open('assets/2021_s3_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 3:
        return open('assets/2021_s4_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 3:
        return open('assets/2021_s5_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 3:
        return open('assets/2021_s6_weekly_3.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 3:
        return open('assets/2021_s7_weekly_3.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 4:
        return open('assets/2021_s1_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 4:
        return open('assets/2021_s2_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 4:
        return open('assets/2021_s3_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 4:
        return open('assets/2021_s4_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 4:
        return open('assets/2021_s5_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 4:
        return open('assets/2021_s6_weekly_4.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 4:
        return open('assets/2021_s7_weekly_4.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 5:
        return open('assets/2021_s1_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 5:
        return open('assets/2021_s2_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 5:
        return open('assets/2021_s3_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 5:
        return open('assets/2021_s4_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 5:
        return open('assets/2021_s5_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 5:
        return open('assets/2021_s6_weekly_5.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 5:
        return open('assets/2021_s7_weekly_5.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 6:
        return open('assets/2021_s1_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider ==6:
        return open('assets/2021_s2_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 6:
        return open('assets/2021_s3_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 6:
        return open('assets/2021_s4_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 6:
        return open('assets/2021_s5_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 6:
        return open('assets/2021_s6_weekly_6.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 6:
        return open('assets/2021_s7_weekly_6.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 7:
        return open('assets/2021_s1_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider == 7:
        return open('assets/2021_s2_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 7:
        return open('assets/2021_s3_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 7:
        return open('assets/2021_s4_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 7:
        return open('assets/2021_s5_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 7:
        return open('assets/2021_s6_weekly_7.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 7:
        return open('assets/2021_s7_weekly_7.html', 'r').read()

    elif yeardropdown=='2021' and mydropdown== 'student 1'and myslider == 8:
        return open('assets/2021_s1_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 2'and myslider ==8:
        return open('assets/2021_s2_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 3'and myslider == 8:
        return open('assets/2021_s3_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 4'and myslider == 8:
        return open('assets/2021_s4_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 5'and myslider == 8:
        return open('assets/2021_s5_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 6'and myslider == 8:
        return open('assets/2021_s6_weekly_8.html', 'r').read()
    elif yeardropdown=='2021' and mydropdown== 'student 7'and myslider == 8:
        return open('assets/2021_s7_weekly_8.html', 'r').read()

    if yeardropdown=='2022' and mydropdown== 'Student 1'and myslider == 1:
        return open('assets/2022_s1_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 2'and myslider == 1:
        return open('assets/2022_s2_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 3'and myslider == 1:
        return open('assets/2022_s3_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 4'and myslider == 1:
        return open('assets/2022_s4_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 5'and myslider == 1:
        return open('assets/2022_s5_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 6'and myslider == 1:
        return open('assets/2022_s6_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 7'and myslider == 1:
        return open('assets/2022_s7_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 8'and myslider == 1:
        return open('assets/2022_s8_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 9'and myslider == 1:
        return open('assets/2022_s9_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 10'and myslider == 1:
        return open('assets/2022_s10_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 11'and myslider == 1:
        return open('assets/2022_s11_weekly_1.html', 'r').read()
    elif yeardropdown=='2022' and mydropdown== 'Student 12'and myslider == 1:
        return open('assets/2022_s12_weekly_1.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 2:
        return open('assets/2022_s1_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 2:
        return open('assets/2022_s2_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 2:
        return open('assets/2022_s3_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 2:
        return open('assets/2022_s4_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 2:
        return open('assets/2022_s5_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 2:
        return open('assets/2022_s6_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 2:
        return open('assets/2022_s7_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 2:
        return open('assets/2022_s8_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 2:
        return open('assets/2022_s9_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 2:
        return open('assets/2022_s10_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 2:
        return open('assets/2022_s11_weekly_2.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 2:
        return open('assets/2022_s12_weekly_2.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 3:
        return open('assets/2022_s1_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 3:
        return open('assets/2022_s2_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 3:
        return open('assets/2022_s3_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 3:
        return open('assets/2022_s4_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 3:
        return open('assets/2022_s5_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 3:
        return open('assets/2022_s6_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 3:
        return open('assets/2022_s7_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 3:
        return open('assets/2022_s8_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 3:
        return open('assets/2022_s9_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 3:
        return open('assets/2022_s10_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 3:
        return open('assets/2022_s11_weekly_3.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 3:
        return open('assets/2022_s12_weekly_3.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 4:
        return open('assets/2022_s1_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 4:
        return open('assets/2022_s2_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 4:
        return open('assets/2022_s3_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 4:
        return open('assets/2022_s4_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 4:
        return open('assets/2022_s5_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 4:
        return open('assets/2022_s6_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 4:
        return open('assets/2022_s7_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 4:
        return open('assets/2022_s8_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 4:
        return open('assets/2022_s9_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 4:
        return open('assets/2022_s10_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 4:
        return open('assets/2022_s11_weekly_4.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 4:
        return open('assets/2022_s12_weekly_4.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 5:
        return open('assets/2022_s1_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 5:
        return open('assets/2022_s2_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 5:
        return open('assets/2022_s3_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 5:
        return open('assets/2022_s4_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 5:
        return open('assets/2022_s5_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 5:
        return open('assets/2022_s6_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 5:
        return open('assets/2022_s7_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 5:
        return open('assets/2022_s8_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 5:
        return open('assets/2022_s9_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 5:
        return open('assets/2022_s10_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 5:
        return open('assets/2022_s11_weekly_5.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 5:
        return open('assets/2022_s12_weekly_5.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 6:
        return open('assets/2022_s1_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 6:
        return open('assets/2022_s2_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 6:
        return open('assets/2022_s3_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 6:
        return open('assets/2022_s4_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 6:
        return open('assets/2022_s5_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 6:
        return open('assets/2022_s6_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 6:
        return open('assets/2022_s7_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 6:
        return open('assets/2022_s8_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 6:
        return open('assets/2022_s9_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 6:
        return open('assets/2022_s10_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 6:
        return open('assets/2022_s11_weekly_6.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 6:
        return open('assets/2022_s12_weekly_6.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 7:
        return open('assets/2022_s1_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 7:
        return open('assets/2022_s2_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 7:
        return open('assets/2022_s3_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 7:
        return open('assets/2022_s4_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 7:
        return open('assets/2022_s5_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 7:
        return open('assets/2022_s6_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 7:
        return open('assets/2022_s7_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 7:
        return open('assets/2022_s8_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 7:
        return open('assets/2022_s9_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 7:
        return open('assets/2022_s10_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 7:
        return open('assets/2022_s11_weekly_7.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 7:
        return open('assets/2022_s12_weekly_7.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 8:
        return open('assets/2022_s1_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 8:
        return open('assets/2022_s2_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 8:
        return open('assets/2022_s3_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 8:
        return open('assets/2022_s4_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 8:
        return open('assets/2022_s5_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 8:
        return open('assets/2022_s6_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 8:
        return open('assets/2022_s7_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 8:
        return open('assets/2022_s8_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 8:
        return open('assets/2022_s9_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 8:
        return open('assets/2022_s10_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 8:
        return open('assets/2022_s11_weekly_8.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 8:
        return open('assets/2022_s12_weekly_8.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 9:
        return open('assets/2022_s1_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 9:
        return open('assets/2022_s2_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 9:
        return open('assets/2022_s3_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 9:
        return open('assets/2022_s4_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 9:
        return open('assets/2022_s5_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 9:
        return open('assets/2022_s6_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 9:
        return open('assets/2022_s7_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 9:
        return open('assets/2022_s8_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 9:
        return open('assets/2022_s9_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 9:
        return open('assets/2022_s10_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 9:
        return open('assets/2022_s11_weekly_9.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 9:
        return open('assets/2022_s12_weekly_9.html', 'r').read()

    elif yeardropdown == '2022' and mydropdown == 'Student 1' and myslider == 10:
        return open('assets/2022_s1_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 2' and myslider == 10:
        return open('assets/2022_s2_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 3' and myslider == 10:
        return open('assets/2022_s3_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 4' and myslider == 10:
        return open('assets/2022_s4_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 5' and myslider == 10:
        return open('assets/2022_s5_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 6' and myslider == 10:
        return open('assets/2022_s6_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 7' and myslider == 10:
        return open('assets/2022_s7_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 8' and myslider == 10:
        return open('assets/2022_s8_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 9' and myslider == 10:
        return open('assets/2022_s9_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 10' and myslider == 10:
        return open('assets/2022_s10_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 11' and myslider == 10:
        return open('assets/2022_s11_weekly_10.html', 'r').read()
    elif yeardropdown == '2022' and mydropdown == 'Student 12' and myslider == 10:
        return open('assets/2022_s12_weekly_10.html', 'r').read()


    if yeardropdown=='2023' and mydropdown== 'Eury'and myslider == 1:
        return open('assets/2023_s1_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Sadia'and myslider == 1:
        return open('assets/2023_s2_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Helen'and myslider == 1:
        return open('assets/2023_s3_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Xichen'and myslider == 1:
        return open('assets/2023_s4_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Zhanlan'and myslider == 1:
        return open('assets/2023_s5_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Katie'and myslider == 1:
        return open('assets/2023_s6_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Andrea'and myslider == 1:
        return open('assets/2023_s7_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Ana Maria'and myslider == 1:
        return open('assets/2023_s8_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Heidi'and myslider == 1:
        return open('assets/2023_s9_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Mariana'and myslider == 1:
        return open('assets/2023_s10_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Inara'and myslider == 1:
        return open('assets/2023_s11_weekly_1.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Kiki'and myslider == 1:
        return open('assets/2023_s12_weekly_1.html', 'r').read()

    elif yeardropdown=='2023' and mydropdown== 'Eury'and myslider == 2:
        return open('assets/2023_s1_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Sadia'and myslider == 2:
        return open('assets/2023_s2_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Helen'and myslider == 2:
        return open('assets/2023_s3_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Xichen'and myslider == 2:
        return open('assets/2023_s4_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Zhanlan'and myslider == 2:
        return open('assets/2023_s5_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Katie'and myslider == 2:
        return open('assets/2023_s6_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Andrea'and myslider == 2:
        return open('assets/2023_s7_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Ana Maria'and myslider == 2:
        return open('assets/2023_s8_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Heidi'and myslider == 2:
        return open('assets/2023_s9_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Mariana'and myslider == 2:
        return open('assets/2023_s10_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Inara'and myslider == 2:
        return open('assets/2023_s11_weekly_2.html', 'r').read()
    elif yeardropdown=='2023' and mydropdown== 'Kiki'and myslider == 2:
        return open('assets/2023_s12_weekly_2.html', 'r').read()


    elif yeardropdown == '2023' and mydropdown == 'Eury' and myslider == 3:
        return open('assets/2023_s1_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Sadia' and myslider == 3:
        return open('assets/2023_s2_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Helen' and myslider == 3:
        return open('assets/2023_s3_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Xichen' and myslider == 3:
        return open('assets/2023_s4_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Zhanlan' and myslider == 3:
        return open('assets/2023_s5_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Katie' and myslider == 3:
        return open('assets/2023_s6_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Andrea' and myslider == 3:
        return open('assets/2023_s7_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Ana Maria' and myslider == 3:
        return open('assets/2023_s8_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Heidi' and myslider == 3:
        return open('assets/2023_s9_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Mariana' and myslider == 3:
        return open('assets/2023_s10_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Inara' and myslider == 3:
        return open('assets/2023_s11_weekly_3.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Kiki' and myslider == 3:
        return open('assets/2023_s12_weekly_3.html', 'r').read()


    elif yeardropdown == '2023' and mydropdown == 'Eury' and myslider == 4:

        return open('assets/2023_s1_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Sadia' and myslider == 4:

        return open('assets/2023_s2_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Helen' and myslider == 4:

        return open('assets/2023_s3_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Xichen' and myslider == 4:

        return open('assets/2023_s4_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Zhanlan' and myslider == 4:

        return open('assets/2023_s5_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Katie' and myslider == 4:

        return open('assets/2023_s6_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Andrea' and myslider == 4:

        return open('assets/2023_s7_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Ana Maria' and myslider == 4:

        return open('assets/2023_s8_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Heidi' and myslider == 4:

        return open('assets/2023_s9_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Mariana' and myslider == 4:

        return open('assets/2023_s10_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Inara' and myslider == 4:

        return open('assets/2023_s11_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Kiki' and myslider == 4:

        return open('assets/2023_s12_weekly_4.html', 'r').read()

    elif yeardropdown == '2023' and mydropdown == 'Eury' and myslider == 5:
        return open('assets/2023_s1_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Sadia' and myslider == 5:
        return open('assets/2023_s2_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Helen' and myslider == 5:
        return open('assets/2023_s3_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Xichen' and myslider == 5:
        return open('assets/2023_s4_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Zhanlan' and myslider == 5:
        return open('assets/2023_s5_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Katie' and myslider == 5:
        return open('assets/2023_s6_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Andrea' and myslider == 5:
        return open('assets/2023_s7_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Ana Maria' and myslider == 5:
        return open('assets/2023_s8_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Heidi' and myslider == 5:
        return open('assets/2023_s9_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Mariana' and myslider == 5:
        return open('assets/2023_s10_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Inara' and myslider == 5:
        return open('assets/2023_s11_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and mydropdown == 'Kiki' and myslider == 5:
        return open('assets/2023_s12_weekly_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider in [6, 7, 8, 9]:
        # Create a dictionary mapping slider values to file names
        file_dict = {6: 'weekly_6.html', 7: 'weekly_7.html', 8: 'weekly_8.html', 9: 'weekly_9.html'}

        # Create a dictionary mapping dropdown options to folder names
        folder_dict = {'Eury': 's1', 'Sadia': 's2', 'Helen': 's3', 'Xichen': 's4', 'Zhanlan': 's5',
                       'Katie': 's6', 'Andrea': 's7', 'Ana Maria': 's8', 'Heidi': 's9', 'Mariana': 's10',
                       'Inara': 's11', 'Kiki': 's12'}

        # Get the file name based on the slider value
        file_name = file_dict[myslider]

        # Get the folder name based on the dropdown option
        folder_name = folder_dict[mydropdown]

        # Construct the full file path
        file_path = f'assets/2023_{folder_name}_{file_name}'

        # Return the file contents
        return open(file_path, 'r').read()



# Define the callback function for Individual Aggregate Graph
@app.callback(
    Output('html-iframe-2', 'srcDoc'),
[Input('yeardropdown', 'value'), Input('mydropdown', 'value'), Input('myslider2', 'value')]
    #[Input('mydropdown2', 'value')]
)
def update_output(yeardropdown,mydropdown,myslider2):
    # Define the HTML content to display based on the dropdown menu
    if yeardropdown=='2021' and myslider2==1 and mydropdown == 'student 1':
        return open('assets/2021_s1_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown == 'student 2':
        return open('assets/2021_s2_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown == 'student 3':
        return open('assets/2021_s3_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown == 'student 4':
        return open('assets/2021_s4_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown == 'student 5':
        return open('assets/2021_s5_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown == 'student 6':
        return open('assets/2021_s6_aggregate_1.html', 'r').read()
    elif yeardropdown=='2021' and myslider2==1 and mydropdown == 'student 7':
        return open('assets/2021_s7_aggregate_1.html', 'r').read()

    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 1':
        return open('assets/2022_s1_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_1.html', 'r').read()
    elif yeardropdown=='2022' and myslider2==1 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_1.html', 'r').read()

    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Eury':
        return open('assets/2023_s1_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Sadia':
        return open('assets/2023_s2_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Helen':
        return open('assets/2023_s3_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Xichen':
        return open('assets/2023_s4_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Zhanlan':
        return open('assets/2023_s5_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Katie':
        return open('assets/2023_s6_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Andrea':
        return open('assets/2023_s7_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Ana Maria':
        return open('assets/2023_s8_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Heidi':
        return open('assets/2023_s9_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Mariana':
        return open('assets/2023_s10_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Inara':
        return open('assets/2023_s11_aggregate_1.html', 'r').read()
    elif yeardropdown=='2023' and myslider2==1 and mydropdown == 'Kiki':
        return open('assets/2023_s12_aggregate_1.html', 'r').read()

    if yeardropdown == '2021' and myslider2 == 2 and mydropdown == 'student 1':
        return open('assets/2021_s1_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown == 'student 2':
        return open('assets/2021_s2_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown == 'student 3':
        return open('assets/2021_s3_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown == 'student 4':
        return open('assets/2021_s4_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown == 'student 5':
        return open('assets/2021_s5_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown == 'student 6':
        return open('assets/2021_s6_aggregate_2.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 2 and mydropdown == 'student 7':
        return open('assets/2021_s7_aggregate_2.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 1 ':
        return open('assets/2022_s1_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_2.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 2 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_2.html', 'r').read()

    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Eury':
        return open('assets/2023_s1_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Sadia':
        return open('assets/2023_s2_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Helen':
        return open('assets/2023_s3_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Xichen':
        return open('assets/2023_s4_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Zhanlan':
        return open('assets/2023_s5_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Katie':
        return open('assets/2023_s6_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Andrea':
        return open('assets/2023_s7_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Ana Maria':
        return open('assets/2023_s8_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Heidi':
        return open('assets/2023_s9_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Mariana':
        return open('assets/2023_s10_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Inara':
        return open('assets/2023_s11_aggregate_2.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 2 and mydropdown == 'Kiki':
        return open('assets/2023_s12_aggregate_2.html', 'r').read()
    #start here 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
    #week 3
    if yeardropdown == '2021' and myslider2 == 3 and mydropdown == 'student 1':
        return open('assets/2021_s1_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown == 'student 2':
        return open('assets/2021_s2_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown == 'student 3':
        return open('assets/2021_s3_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown == 'student 4':
        return open('assets/2021_s4_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown == 'student 5':
        return open('assets/2021_s5_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown == 'student 6':
        return open('assets/2021_s6_aggregate_3.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 3 and mydropdown == 'student 7':
        return open('assets/2021_s7_aggregate_3.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 1':
        return open('assets/2022_s1_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_3.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 3 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_3.html', 'r').read()

    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Eury':
        return open('assets/2023_s1_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Sadia':
        return open('assets/2023_s2_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Helen':
        return open('assets/2023_s3_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Xichen':
        return open('assets/2023_s4_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Zhanlan':
        return open('assets/2023_s5_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Katie':
        return open('assets/2023_s6_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Andrea':
        return open('assets/2023_s7_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Ana Maria':
        return open('assets/2023_s8_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Heidi':
        return open('assets/2023_s9_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Mariana':
        return open('assets/2023_s10_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Inara':
        return open('assets/2023_s11_aggregate_3.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 3 and mydropdown == 'Kiki':
        return open('assets/2023_s12_aggregate_3.html', 'r').read()
# Week 4

    if yeardropdown == '2021' and myslider2 == 4 and mydropdown == 'student 1':
        return open('assets/2021_s1_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown == 'student 2':
        return open('assets/2021_s2_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown == 'student 3':
        return open('assets/2021_s3_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown == 'student 4':
        return open('assets/2021_s4_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown == 'student 5':
        return open('assets/2021_s5_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown == 'student 6':
        return open('assets/2021_s6_aggregate_4.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 4 and mydropdown == 'student 7':
        return open('assets/2021_s7_aggregate_4.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 1':
        return open('assets/2022_s1_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_4.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 4 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_4.html', 'r').read()

    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Eury':
        return open('assets/2023_s1_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Sadia':
        return open('assets/2023_s2_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Helen':
        return open('assets/2023_s3_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Xichen':
        return open('assets/2023_s4_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Zhanlan':
        return open('assets/2023_s5_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Katie':
        return open('assets/2023_s6_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Andrea':
        return open('assets/2023_s7_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Ana Maria':
        return open('assets/2023_s8_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Heidi':
        return open('assets/2023_s9_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Mariana':
        return open('assets/2023_s10_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Inara':
        return open('assets/2023_s11_aggregate_4.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 4 and mydropdown == 'Kiki':
        return open('assets/2023_s12_aggregate_4.html', 'r').read()
# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 5
    if yeardropdown == '2021' and myslider2 == 5 and mydropdown == 'student 1':
        return open('assets/2021_s1_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown == 'student 2':
        return open('assets/2021_s2_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown == 'student 3':
        return open('assets/2021_s3_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown == 'student 4':
        return open('assets/2021_s4_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown == 'student 5':
        return open('assets/2021_s5_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown == 'student 6':
        return open('assets/2021_s6_aggregate_5.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 5 and mydropdown == 'student 7':
        return open('assets/2021_s7_aggregate_5.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 1':
        return open('assets/2022_s1_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_5.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 5 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_5.html', 'r').read()

    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Eury':
        return open('assets/2023_s1_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Sadia':
        return open('assets/2023_s2_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Helen':
        return open('assets/2023_s3_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Xichen':
        return open('assets/2023_s4_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Zhanlan':
        return open('assets/2023_s5_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Katie':
        return open('assets/2023_s6_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Andrea':
        return open('assets/2023_s7_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Ana Maria':
        return open('assets/2023_s8_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Heidi':
        return open('assets/2023_s9_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Mariana':
        return open('assets/2023_s10_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Inara':
        return open('assets/2023_s11_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 == 5 and mydropdown == 'Kiki':
        return open('assets/2023_s12_aggregate_5.html', 'r').read()
    elif yeardropdown == '2023' and myslider2 in [6, 7, 8, 9]:
        # Create a dictionary mapping slider values to file names
        file_dict = {6: 'aggregate_6.html', 7: 'aggregate_7.html', 8: 'aggregate_8.html', 9: 'aggregate_9.html'}

        # Create a dictionary mapping dropdown options to folder names
        folder_dict = {'Eury': 's1', 'Sadia': 's2', 'Helen': 's3', 'Xichen': 's4', 'Zhanlan': 's5',
                       'Katie': 's6', 'Andrea': 's7', 'Ana Maria': 's8', 'Heidi': 's9', 'Mariana': 's10',
                       'Inara': 's11', 'Kiki': 's12'}

        # Get the file name based on the slider value
        file_name = file_dict[myslider2]

        # Get the folder name based on the dropdown option
        folder_name = folder_dict[mydropdown]

        # Construct the full file path
        file_path = f'assets/2023_{folder_name}_{file_name}'

        # Return the file contents
        return open(file_path, 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 6
    if yeardropdown == '2021' and myslider2 == 6 and mydropdown == 'student 1':
        return open('assets/2021_s1_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown == 'student 2':
        return open('assets/2021_s2_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown == 'student 3':
        return open('assets/2021_s3_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown == 'student 4':
        return open('assets/2021_s4_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown == 'student 5':
        return open('assets/2021_s5_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown == 'student 6':
        return open('assets/2021_s6_aggregate_6.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 6 and mydropdown == 'student 7':
        return open('assets/2021_s7_aggregate_6.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 1':
        return open('assets/2022_s1_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_6.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 6 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_6.html', 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 7
    if yeardropdown == '2021' and myslider2 == 7 and mydropdown == 'student 1':
        return open('assets/2021_s1_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown == 'student 2':
        return open('assets/2021_s2_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown == 'student 3':
        return open('assets/2021_s3_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown == 'student 4':
        return open('assets/2021_s4_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown == 'student 5':
        return open('assets/2021_s5_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown == 'student 6':
        return open('assets/2021_s6_aggregate_7.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 7 and mydropdown == 'student 7':
        return open('assets/2021_s7_aggregate_7.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 1':
        return open('assets/2022_s1_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_7.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 7 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_7.html', 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 8
    if yeardropdown == '2021' and myslider2 == 8 and mydropdown == 'student 1':
        return open('assets/2021_s1_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown == 'student 2':
        return open('assets/2021_s2_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown == 'student 3':
        return open('assets/2021_s3_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown == 'student 4':
        return open('assets/2021_s4_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown == 'student 5':
        return open('assets/2021_s5_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown == 'student 6':
        return open('assets/2021_s6_aggregate_8.html', 'r').read()
    elif yeardropdown == '2021' and myslider2 == 8 and mydropdown == 'student 7':
        return open('assets/2021_s7_aggregate_8.html', 'r').read()

    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 1':
        return open('assets/2022_s1_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_8.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 8 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_8.html', 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 9
    if yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 1':
        return open('assets/2022_s1_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_9.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 9 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_9.html', 'r').read()

# 2021:8 weeks ; 2022:10 weeks ; 2023: 5 weeks
# week 10
    if yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 1':
        return open('assets/2022_s1_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 2':
        return open('assets/2022_s2_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 3':
        return open('assets/2022_s3_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 4':
        return open('assets/2022_s4_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 5':
        return open('assets/2022_s5_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 6':
        return open('assets/2022_s6_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 7':
        return open('assets/2022_s7_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 8':
        return open('assets/2022_s8_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 9':
        return open('assets/2022_s9_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 10':
        return open('assets/2022_s10_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 11':
        return open('assets/2022_s11_aggregate_10.html', 'r').read()
    elif yeardropdown == '2022' and myslider2 == 10 and mydropdown == 'Student 12':
        return open('assets/2022_s12_aggregate_10.html', 'r').read()





# Define the callback function for Individual Weekly Graph
@app.callback(
    Output('html-iframe-4', 'srcDoc'),
    [Input('yeardropdown1', 'value'),Input('myslider3', 'value')]
    #[Input('yeardropdown', 'value'), Input('mydropdown', 'value'), Input('myslider2', 'value')]
)

def update_output(yeardropdown1,myslider3):
    # Define the HTML content to display based on the dropdown menu
    #2021
    if yeardropdown1 == '2021' and myslider3 ==1:
        return open('assets/2021_class_1.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 ==2:
        return open('assets/2021_class_2.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 3:
        return open('assets/2021_class_3.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 4:
        return open('assets/2021_class_4.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 5:
        return open('assets/2021_class_5.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 6:
        return open('assets/2021_class_6.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 7:
        return open('assets/2021_class_7.html', 'r').read()
    elif yeardropdown1 == '2021' and myslider3 == 8:
        return open('assets/2021_class_8.html', 'r').read()
    #2022
    if yeardropdown1 == '2022'and myslider3 ==1:
        return open('assets/2022_class_1.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 ==2:
        return open('assets/2022_class_2.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 3:
        return open('assets/2022_class_3.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 4:
        return open('assets/2022_class_4.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 5:
        return open('assets/2022_class_5.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 6:
        return open('assets/2022_class_6.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 7:
        return open('assets/2022_class_7.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 8:
        return open('assets/2022_class_8.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 9:
        return open('assets/2022_class_9.html', 'r').read()
    elif yeardropdown1 == '2022' and myslider3 == 10:
        return open('assets/2022_class_10.html', 'r').read()

        # 2023
    if yeardropdown1 == '2023'and myslider3 ==1:
        return open('assets/2023_class_1.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 ==2:
        return open('assets/2023_class_2.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 == 3:
        return open('assets/2023_class_3.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 == 4:
        return open('assets/2023_class_4.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 == 5:
        return open('assets/2023_class_5.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 ==6:
        return open('assets/2023_class_6.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 == 7:
        return open('assets/2023_class_7.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 == 8:
        return open('assets/2023_class_8.html', 'r').read()
    elif yeardropdown1 == '2023' and myslider3 == 9:
        return open('assets/2023_class_9.html', 'r').read()


# Define the callback function for positive
@app.callback(
    Output('html-iframe-5', 'srcDoc'),
    [Input('yeardropdown2', 'value'),Input('myslider4', 'value')]
    #[Input('yeardropdown', 'value'), Input('mydropdown', 'value'), Input('myslider2', 'value')]
)

def update_output(yeardropdown2,myslider4):
    # Define the HTML content to display based on the dropdown menu
    #2021
    if yeardropdown2 == '2021' and myslider4 ==1:
        return open('assets/class_positive_map_2021_1.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider4 ==2:
        return open('assets/class_positive_map_2021_2.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider4 == 3:
        return open('assets/class_positive_map_2021_3.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider4 == 4:
        return open('assets/class_positive_map_2021_4.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider4 == 5:
        return open('assets/class_positive_map_2021_5.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider4 == 6:
        return open('assets/class_positive_map_2021_6.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider4 == 7:
        return open('assets/class_positive_map_2021_7.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider4 == 8:
        return open('assets/class_positive_map_2021_8.html', 'r').read()
    #2022
    if yeardropdown2 == '2022'and myslider4 ==1:
        return open('assets/class_positive_map_2022_1.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider4 ==2:
        return open('assets/class_positive_map_2022_2.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider4 == 3:
        return open('assets/class_positive_map_2022_3.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider4 == 4:
        return open('assets/class_positive_map_2022_4.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider4 == 5:
        return open('assets/class_positive_map_2022_5.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider4 == 6:
        return open('assets/class_positive_map_2022_6.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider4 == 7:
        return open('assets/class_positive_map_2022_7.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider4 == 8:
        return open('assets/class_positive_map_2022_8.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider4 == 9:
        return open('assets/class_positive_map_2022_9.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider4 == 10:
        return open('assets/class_positive_map_2022_10.html', 'r').read()
        # 2023
    for i in range(1, 10):
        if yeardropdown2 == '2023' and myslider4 == i:
            return open('assets/class_positive_map_2023_' + str(i) + '.html', 'r').read()

def send_email(feedback_text):
    sender_email = 'tltlknowledgemap123@gmail.com'
    sender_password = 'knowledgemap123'
    receiver_email = 'tltlknowledgemap123@gmail.com'
    subject = 'New Feedback Received'
    message = f'The following feedback was received:\n\n{feedback_text}'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, f'Subject: {subject}\n\n{message}')
    server.quit()

# Define the callback function for negative
@app.callback(
    Output('html-iframe-6', 'srcDoc'),
    [Input('yeardropdown2', 'value'),Input('myslider5', 'value')]
    #[Input('yeardropdown', 'value'), Input('mydropdown', 'value'), Input('myslider2', 'value')]
)

def update_output(yeardropdown2,myslider5):
    # Define the HTML content to display based on the dropdown menu
    #2021
    for i in range(1, 8):
        if yeardropdown2 == '2021' and myslider5 == i:
            return open('assets/class_negative_map_2023_' + str(i) + '.html', 'r').read()
    #2022
    for i in range(1, 10):
        if yeardropdown2 == '2022' and myslider5 == i:
            return open('assets/class_negative_map_2022_' + str(i) + '.html', 'r').read()

        # 2023
    for i in range(1, 10):
        if yeardropdown2 == '2023' and myslider5 == i:
            return open('assets/class_negative_map_2023_' + str(i) + '.html', 'r').read()


if __name__ == "__main__":
    app.run_server(port=8073)