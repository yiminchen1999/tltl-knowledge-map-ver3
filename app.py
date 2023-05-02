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
import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import os
import smtplib

#import plotly.express as px
import plotly.tools as tls
# Define your email and password
EMAIL = 'yc4195@cumc.columbia.edu'
PASSWORD = 'SZcym@991019'
df = pd.read_csv('assets/week_keyword_table_s01_2021.csv',index_col=0)
animated_title_style = {
    "font-size": "2rem",
    "font-weight": "bold",
    "color": "#fff",
    "text-shadow": "1px 1px 3px #333",
    "margin-left": "2rem",  # Add margin to move the title to the right
}
# Load the data
data = pd.read_excel("assets/2022_student1_10projects_combined.xlsx",
     engine='openpyxl')

# Define a dictionary mapping labels to colors
label_colors = {'positive': 'green', 'negative': 'red', 'neutral': 'grey'}

# Create a new column in the DataFrame containing the color for each label
data['color'] = data['label'].map(label_colors)
# Set the plot style
sns.set_style("ticks")
sns.set_context("talk")

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data as a scatter plot using the colors from the 'color' column
sns.scatterplot(data=data, x='Name', y='score', hue='label', palette=label_colors)

# Set the axis labels and title
plt.xlabel('Project Name')
plt.ylabel('Score')
plt.title('Sentiment Analysis Results')

# Set the x-axis tick labels
tick_labels = ['dream1', 'dream2', 'dream3', 'frank', 'lofi', 'omni', 'remix', 'rube', 'testing', 'tool']
plt.xticks(range(10), tick_labels, rotation=45)

# Set the legend outside the plot and adjust spacing
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.subplots_adjust(right=0.8)



# Load the data
data1 = pd.read_excel("assets/frank_2022_SA_01_combined.xlsx",
     engine='openpyxl')
# frank project for 12 students
# Define a dictionary mapping labels to colors
label_colors = {'positive': 'green', 'negative': 'red', 'neutral': 'grey'}

# Create a new column in the DataFrame containing the color for each label
data1['color'] = data1['label'].map(label_colors)

# Set the plot style
sns.set_style("ticks")
sns.set_context("talk")

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the data as a scatter plot using the colors from the 'color' column
sns.scatterplot(data=data1, x='file_number', y='score', hue='label', palette=label_colors)

# Set the axis labels and title
# Set the x-axis ticks
plt.xticks(range(1, 13), range(1, 13))

plt.xlabel('File Number')
plt.ylabel('Score')
plt.title('Sentiment Analysis Results')


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
                dbc.NavItem(dbc.NavLink("Knowledge Maps/Mainpage", href="/page-1")),
                dbc.NavItem(dbc.NavLink("Feedback/Message board ", href="/page-3")),
                dbc.NavItem(dbc.NavLink("Sentiment Analysis", href="/page-2")),

                dbc.NavItem(dbc.NavLink("TLTL Lab Link💡", href="https://tltlab.org/")),

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
# Individual Aggregate Graph
div4 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s1_aggregate_1.html"), id="graph1")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div5 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s1_aggregate_1.html"), id="graph2")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div6 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_s1_aggregate_1.html"), id="graph3")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
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

# Class Collective Graph
div7 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_class_1.html"), id="graph1")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div8 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_class_1.html"), id="graph2")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
div9 = html.Div([html.Iframe(src=app.get_asset_url("assets/2021_class_1.html"), id="graph3")] ) #width='90%', height='600', , style={"background":"transparent", "height":"700px"})
#content = html.Div(id="page-content")
# Define the initial HTML content to display in the Iframe component
initial_html_class = open('assets/2021_class_1.html', 'r').read()

with open('assets/2022_class_1.html', 'r') as f:
    second_html_class = f.read()

with open('assets/2023_class_1.html', 'r') as f:
    third_html_class = f.read()

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

                          html.P('Find your name to see your individual weekly keywords',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='text-black'),
                          dcc.Dropdown(id='mydropdown',
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),
                        html.Hr(),
                       dcc.Markdown('''
                           * Knowledge keywords mentioned in reflection for a particular week
                           * Each node represents a knowledge keyword with name underneath
                           * Color corresponds to the specific knowledge category 
                       ''', style={'margin-bottom': '2px', 'display': 'flex'}
                        ,
                                    className='fs-6 text-black'), ],
                      className='p-4')],
            # Add padding to the div
            style={'height': '73vh', 'margin': '10px', 'display': 'flex'},
            className='bg-white rounded shadow-sm' # Add a white background, rounded corners, and shadow
        ),


        html.Hr(style={ 'margin': '30px 0'}),
        dbc.Row(
            [html.H5('Collective knowledge map',style={'margin-top': '12px', 'margin-left': '14px'})],
            style={"height": "5vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [html.Div([html.Hr(),html.P('Select a year first',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='text-black'),
                          dcc.Dropdown(id='yeardropdown1', options=[{'label': '2021', 'value': '2021'},
                                                                    {'label': '2022', 'value': '2022'},
                                                                    {'label': '2023', 'value': '2023'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}),
html.Hr(),
                       dcc.Markdown('''
                           * All knowledge keywords all students mentioned in reflection for a particular week
                           * Color corresponds to the specific knowledge category 
                           * When clicking a node, text shows students who have mentioned this knowledge 
                           * Size of the node reflects the amount of students
                       ''', style={'margin-bottom': '2px', 'display': 'flex'}
                        ,
                                    className='fs-6 text-black'),
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

# Define the hidden div element for the popup window
popup_div = html.Div(id='popup-div', style={'display': 'none'})

# Define the callback function to update the state of the hidden div element
@app.callback(Output('popup-div', 'children'), [Input('info-button', 'n_clicks')])
def update_popup_div(n_clicks):
    if n_clicks:
        # Replace this with the information to be displayed in the popup window
        return html.P('This is some information that will be displayed in the popup window.')


html_graphs = html.Div(
    [
        dbc.Container(
            [dbc.Row(
                [
                    dbc.Col(
                        [
                            #html.P('Individual Key Concepts (weekly)', className='d-flex justify-content-between align-items-center',#className='fs-5 text-center font-weight-bold',
                                   #style={"font-size": "2.5rem","font-weight": "bold"}),

html.Div(
    [
        html.P(
            'Individual Key Concepts (weekly)',
            className='fs-5 text-center font-weight-bold',
            style={"font-size": "2.5rem", "font-weight": "bold", "margin-right": "-40px", "flex": "1"}
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
                                    dbc.ModalHeader("Information about Individual Key Concepts (weekly)"),
                                    dbc.ModalBody(
                                        " Knowledge keywords mentioned in reflection for a particular week, Each node represents a knowledge keyword with name underneath, Color corresponds to the specific knowledge category"),
                                    dbc.ModalFooter(
                                        html.Button('Close', id='close-button', className='btn btn-secondary'))
                                ],
                                id="info-modal",
                                centered=True
                            ),
                            #html.Button('i', id='info-button', className='badge rounded-pill bg-primary', style={'vertical-align': 'top'}),
                            html.P('Identify which concepts I’ve applied this week',
                             className='fs-6 text-center',
                        style={"font-size": "1.0rem"}),
                            html.Iframe(id='html-iframe', srcDoc=initial_html, width='100%', height='600',
                                        style={'height': '55vh'}),

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
                            ], style={'width': '85%', 'margin': '20px', 'margin-top': '20px',
                                      'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 5}),

                    dbc.Col(
                        [



html.Div(
    [
        html.P(
            'Individual Key Concepts (aggregated)',
            className='fs-5 text-center font-weight-bold',
            style={"font-size": "2.5rem", "font-weight": "bold", "margin-right": "-40px", "flex": "1"}
        ),
        html.Button(
            'i',
            id='info-button2',
            className='badge rounded-pill bg-primary',
            style={ 'font-size': '0.95rem',"margin-left": "10px"}
        ),
    ],
    className='d-flex align-items-center',
    style={'display': 'flex'}
),

                            dbc.Modal(
                                [
                                    dbc.ModalHeader("Information about Individual Key Concepts (aggregated)"),
                                    dbc.ModalBody(
                                        "Knowledge keywords mentioned in reflections up to a certain week;The color of the node corresponds to a specific knowledge category;Within the same category, darker shades indicate their earlier occurrence;Clicking on a node reveals the week in which the keyword was first mentioned;Size of the node reflects the frequency of its occurrence"),
                                    dbc.ModalFooter(
                                        html.Button('Close', id='close-button2', className='btn btn-secondary'))
                                ],
                                id="info-modal2",
                                centered=True
                            ),
                            html.P('Examine how my knowledge concepts evolve over time',
                                   className='fs-6 text-center',
                                   style={"font-size": "1.0rem"}),
                            html.Iframe(id='html-iframe-2', srcDoc=initial_html_aggregate, width='100%', height='600',
                                        style={'height': '55vh'}),

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
    [
        dbc.Row(
            [
                dbc.Col(),
                dbc.Col(
                    dbc.Button("Click me to see the animation!", id="button-1", color="light", className="ml-2"),
                    width="auto",
                    style={"display": "flex", "justify-content": "center"}
                ),
                dbc.Col()
            ]
        ),
dbc.Modal(
    [
        dbc.ModalHeader("Animated GIF"),
        dbc.ModalBody(
            html.Img(id="gif-player", src="")
        ),
        dbc.ModalFooter(
            dbc.Button("Close", id="close-button3", className="ml-auto")
        )
    ],
    id="gif-modal",
    centered=True,
    size="lg",
    style={"max-width": "100%", "max-height": "90vh"}
),
    ]
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
                        [  html.Div(
    [
        html.P(
            'Collective Knowledge in the Class (weekly)',
            className='text-nowrap bd-highlight',
            style={
                'fontWeight': 'bold',
                'padding-right': '10px',
                'padding-left': '10px',
                'display': 'inline-block',
                'margin': '0'
            }
        ),
        html.Button(
            'i',
            id='info-button4',
            className='badge rounded-pill bg-primary',
            style={
                'vertical-align': 'middle',
                'font-size': '0.95rem',
                'display': 'inline-block',
                'margin': '0'
            }
        ),
    ],
    className='d-flex justify-content-end align-items-center',
    style={'text-align': 'right', 'margin-right': '-90px'}
),


                            dbc.Modal(
                                [
                                    dbc.ModalHeader("Collective Knowledge in the Class (weekly)"),
                                    dbc.ModalBody(
                                        "All knowledge keywords mentioned by all students in a class in their reflections for a particular week;The color of the node corresponds to a specific knowledge category ;Clicking on a node reveals the names of the students who mentioned the keyword;Size of the node reflects the number of students who mentioned it"),
                                    dbc.ModalFooter(
                                        html.Button('Close', id='close-button4', className='btn btn-secondary'))
                                ],
                                id="info-modal4",
                                centered=True
                            ),

html.Div(
                                html.P('See what concepts other students have applied',
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
    Output("gif-player", "src"),
    [Input("button-1", "n_clicks")]
)
def play_gif(n_clicks):
    if n_clicks is not None:
        with open("assets/animation_1.gif", "rb") as f:
            gif_data = f.read()
        return "data:image/gif;base64," + base64.b64encode(gif_data).decode()
    else:
        return ""




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
                            style={'border-radius': '20px', 'box-shadow': '4px 4px 8px 0 rgba(0,0,0,0.2)'}
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
            [html.H5('Class collective sentiment analysis map',
                        style={'margin-top': '12px', 'margin-left': '14px'})],
            style={"height": "8vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [html.Div([html.Hr(),html.P('Select a year first',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='text-black'),
                          dcc.Dropdown(id='yeardropdown2', options=[{'label': '2021', 'value': '2021'},
                                                                    {'label': '2022', 'value': '2022'},
                                                                    {'label': '2023', 'value': '2023'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}
                                       ),
                       ],
                          className='p-4')], # Add padding to the div
            style={'height': '50vh', 'margin': '10px', 'display': 'flex'},
            className='bg-white rounded shadow-sm' # Add a white background, rounded corners, and shadow
        ),
        html.Hr(style={ 'margin': '60px 0'}),
        dbc.Row(
            [html.H5('Sentiment Analysis comparison between students on different projects',style={'margin-top': '12px', 'margin-left': '14px'})],
            style={"height": "15vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [html.Div([html.Hr(),html.P('Select a year first',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='text-black'),
                          dcc.Dropdown(id='yeardropdown4', options=[{'label': '2021', 'value': '2021'},
                                                                    {'label': '2022', 'value': '2022'},
                                                                    {'label': '2023', 'value': '2023'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}),],
                          className='p-4') # Add padding to the div
            ],
            style={'height': '60vh', 'margin': '10px', 'display': 'flex'},
            className='bg-white rounded shadow-sm' #  white background, rounded corners, and shadow
        ),
html.Hr(style={ 'margin': '40px 0'}),
dbc.Row(
            [html.H5('Sentiment Analysis comparison between projects on different students',style={'margin-top': '12px', 'margin-left': '14px'})],
            style={"height": "15vh"},
            className='bg-light text-white'
        ),
        dbc.Row(
            [html.Div([html.Hr(),html.P('Select a year first',
                                 style={'margin-top': '8px', 'margin-bottom': '4px'},
                                 className='text-black'),
                          dcc.Dropdown(id='yeardropdown5', options=[{'label': '2021', 'value': '2021'},
                                                                    {'label': '2022', 'value': '2022'},
                                                                    {'label': '2023', 'value': '2023'}],
                                       multi=False,
                                       style={'width': '220px', 'color': '#000000'}),],
                          className='p-4') # Add padding to the div
            ],
            style={'height': '70vh', 'margin': '10px', 'display': 'flex'},
            className='bg-white rounded shadow-sm' #  white background, rounded corners, and shadow
        ),
        html.Hr(style={ 'margin': '20px 0'}),
    ],
    style={'padding-top': '20px', 'padding-bottom': '20px', 'background-color': '#f8f9fa'} # adding and background color to the sidebar
)






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
                                        'Maps for positive sentiment analysis score',
                                        className='fs-5 text-center font-weight-bold',
                                        style={"font-size": "2.5rem", "font-weight": "bold", "margin-right": "-40px",
                                               "flex": "1"}
                                    ),
                                    html.Button(
                                        'i',
                                        id='info-button6',
                                        className='badge rounded-pill bg-primary',
                                        style={'display': 'inline-block','font-size': '0.95rem', "margin-left": "10px"}
                                    ),
                                ],
                                className='d-flex align-items-center',
                                style={'display': 'flex'}
                            ),
                            dbc.Modal(
                                [
                                    dbc.ModalHeader("Info about Class Positive Sentiment Collective Map"),
                                    dbc.ModalBody(
                                        " All knowledge keywords mentioned by all students in a class in their reflections with a positive sentiment for a particular week;The color of the node corresponds to a specific knowledge category ;Clicking on a node reveals the names of the students who mentioned the keyword ;Size of the node reflects the number of students who mentioned it"),
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
                            html.Iframe(id='html-iframe-5', srcDoc=initial_html_posi, width='100%', height='600',
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
                            ], style={'width': '85%', 'margin': '20px', 'margin-top': '20px',
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
                                        'Maps for negative sentiment analysis score',
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
                                    dbc.ModalHeader("Info about Class Negative Sentiment Collective Map"),
                                    dbc.ModalBody(
                                        " All knowledge keywords mentioned by all students in a class in their reflections with a negative sentiment for a particular week;The color of the node corresponds to a specific knowledge category ;Clicking on a node reveals the names of the students who mentioned the keyword ;Size of the node reflects the number of students who mentioned it"),
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
                            html.Iframe(id='html-iframe-6', src=initial_html_nega, width='100%', height='600',
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
                            ], style={'width': '85%', 'margin': '20px', 'margin-top': '20px',
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
                                html.Div([html.Div('Sentiment Analysis of one student on all projects', id='title',
                                                   className='fs-4 text-center font-weight-bold title-text',
                                                   style={'fontWeight': 'bold', 'cursor': 'pointer'}),
                                          html.Button('i', id='info-button9', className='badge rounded-pill bg-primary',
                                                      style={ 'font-size': '0.8rem',
                                                             'display': 'inline-block', 'margin': '10px'})],
                                         className='d-flex text-center justify-content-center align-items-center'),
 dbc.Modal(
                                [
                                    dbc.ModalHeader("Info about Sentiment Analysis of one student on all projects"),
                                    dbc.ModalBody(
                                        "Display sentiment analysis of one student on all projects in a class;Each dot on the map represents a sentence that contains knowledge keyword(s);Red indicates negative sentiment;Green indicates positive sentiment;Grey indicates neutral sentiment"),
                                    dbc.ModalFooter(
                                        html.Button('Close', id='close-button9', className='btn btn-secondary'))
                                ],
                                id="info-modal9",
                                centered=True
                            ),

html.Div(
                                html.P('Red indicates negative sentiment;Green indicates positive sentiment;Grey indicates neutral sentiment',
                                       className='text-nowrap bd-highlight',
                                       style={'fontWeight': 'bold'}),

                                className='fs-6 d-flex justify-content-center',
                                style={'text-align': 'center', 'margin-right': '-50px'}
                            ),
                                html.Div(id='text-box-container',
                                         style={'display': 'flex', 'justify-content': 'space-between'})
                            ]),
                            html.Div([
    dcc.Graph(
        figure={
            'data': [
                {'x': data['Name'], 'y': data['score'], 'type': 'scatter', 'mode': 'markers', 'marker': {'color': data['color']}}
            ],
            'layout': {
                'title': 'Sentiment Analysis Results',
                'xaxis': {'title': 'Project Name', 'tickvals': list(range(10)), 'ticktext': tick_labels, 'tickangle': 45},
                'yaxis': {'title': 'Score'},
                'legend': {'orientation': 'h', 'x': 0, 'y': 1.1},
                'margin': {'l': 50, 'b': 50, 't': 50, 'r': 50}
            }
        },
        id='my-graph'
    )
]),
                            #html.Iframe(id='html-iframe-7', src='assets/samplepic4.png', width='100%', height='600',style={'height': '65vh'}),
                            dbc.Row([dbc.Col([html.Div([
                                # html.Label('Select a week:', style={'fontSize': '20px'}),
                                dcc.Slider(
                                    id='myslider6',
                                    min=1,
                                    max=10,
                                    value=1,
                                    step=1,
                                    updatemode='drag',
                                    marks={1: {'label': '1'}, 2: {'label': '2'}, 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                                           8: '8', 9: '9', 10: '10'},
                                    tooltip={"placement": "bottom", "always_visible": True}, included=False
                                ),
                                dbc.Label("Student Name", className="text-center w-100 mb-0", width='10%'),
                            ], style={'width': '90%', 'margin': '20px', 'margin-top': '20px',
                                      # 'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 10}),#

                    dbc.Col(
                        [
                            html.Div([
                                html.Div([html.Div('Sentiment Analysis of all student on one projects', id='title',
                                                   className='fs-4 text-center font-weight-bold title-text',
                                                   style={'fontWeight': 'bold', 'cursor': 'pointer'}),
                                          html.Button('i', id='info-button8', className='badge rounded-pill bg-primary',
                                                      style={ 'font-size': '0.8rem',
                                                             'display': 'inline-block', 'margin': '10px'})],
                                         className='d-flex text-center justify-content-center align-items-center'),
 dbc.Modal(
                                [
                                    dbc.ModalHeader("Info about Sentiment Analysis of all student on one projects"),
                                    dbc.ModalBody(
                                        "Display sentiment analysis of a project for all students in a class;Each dot on the map represents a sentence that contains knowledge keyword(s);Red indicates negative sentiment;Green indicates positive sentiment;Grey indicates neutral sentiment"),
                                    dbc.ModalFooter(
                                        html.Button('Close', id='close-button8', className='btn btn-secondary'))
                                ],
                                id="info-modal8",
                                centered=True
                            ),

html.Div(
                                html.P('Red indicates negative sentiment;Green indicates positive sentiment;Grey indicates neutral sentiment',
                                       className='text-nowrap bd-highlight',
                                       style={'fontWeight': 'bold'}),

                                className='fs-6 d-flex justify-content-center',
                                style={'text-align': 'center', 'margin-right': '-50px'}
                            ),
                                html.Div(id='text-box-container',
                                         style={'display': 'flex', 'justify-content': 'space-between'})
                            ]),
                            html.Div([
                                dcc.Graph(
                                    id='sentiment-analysis-graph',
                                    figure={
                                        'data': [
                                            {
                                                'x': data1['file_number'],
                                                'y': data1['score'],
                                                'type': 'scatter',
                                                'mode': 'markers',
                                                'marker': {'color': data1['color']}
                                            }
                                        ],
                                        'layout': {
                                            #'title': 'Sentiment Analysis Results',
                                            'xaxis': {
                                                'title': 'File Number',
                                                'tickvals': list(range(1, 13)),
                                                'ticktext': list(range(1, 13))
                                            },
                                            'yaxis': {'title': 'Score'},
                                            'legend': {'orientation': 'h', 'x': 0, 'y': 1.1},
                                            'margin': {'l': 50, 'b': 50, 't': 50, 'r': 50}
                                        }
                                    }
                                )
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
                                    marks={1: {'label': 'dream1'}, 2: {'label': 'dream2'}, 3: {'label': 'dream3'},
                                           4: {'label': 'frank'}, 5: {'label': 'lofi'}, 6: {'label': 'omni'},
                                           7: {'label': 'remix'},
                                           8: {'label': 'rube'}, 9: {'label': 'testing'}},
                                     included=False
                                ),
                                dbc.Label("Project Name", className="text-center w-100 mb-0", width='10%'),
                            ], style={'width': '90%', 'margin': '20px', 'margin-top': '20px',
                                      # 'color': '#000000',
                                      'fontSize': '15px',
                                      'padding': '5px'})
                            ])]),

                        ], width={"size": 10})

                ], style={"height": "240vh"}
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
                            style={'border-radius': '20px', 'box-shadow': '4px 4px 8px 0 rgba(0,0,0,0.2)'}
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





page_3_layout  =  dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Feedback Page'), className="mt-3 mb-5")
    ]),
    dbc.Row([
        dbc.Col([
            html.P('Please provide your feedback below:', className="mb-2"),
            dcc.Textarea(id='feedback-input', value='', placeholder='Type your feedback here...',
                         style={'width': '100%', 'height': 200, 'resize': 'vertical'}, className="mb-3"),
            dbc.Button('Submit', id='submit-button', color='primary', className="mb-3")
        ], width=6, className="mx-auto")
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='output-container', children=''), className="text-center")
    ])
], className="my-5")




# Define the callback
# Define the callback
@app.callback(
    Output('output-container', 'children'),
    Input('submit-button', 'n_clicks'),
    Input('feedback-input', 'value')
)
def update_output(n_clicks, value):
    if n_clicks is None:
        return None
    elif n_clicks > 0:
        # Send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, f'Subject: New Feedback\n\n{value}')
            server.quit()
            return dbc.Alert(f'Thank you for your feedback! Your feedback has been sent to {EMAIL}', color='success')
        except:
            return dbc.Alert(f'There was an error sending your feedback. Please try again later.', color='danger')




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

# define the app layout
app.layout = html.Div(
    [
        dcc.Location(id="url"),
        navbar,
        html.Div(id="page-content"),
    ]
)

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

#def update_output(value):
    # Define the HTML content to display based on the dropdown menu
    #if value == 'option1':
        #return open('s1_aggregate_network1.html', 'r').read()
    #elif value == 'option2':
        #return open('s2_weekly_network1.html', 'r').read()
    #elif value == 'option3':
        #return open('s3_weekly_network1.html', 'r').read(

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



# Define the callback function for year Graph in total
#@app.callback(
    #Output('html-iframe-3', 'srcDoc'),
    #Input('mydropdown3', 'value')
    #Input('yeardropdown', 'value')
    #[Input('yeardropdown', 'value'), Input('mydropdown', 'value'), Input('myslider2', 'value')]
#)

#def update_output(value):
    # Define the HTML content to display based on the dropdown menu
    #if value == '2021':
        #return open('assets/2021_class_1.html', 'r').read()
    #elif value == '2022':
        #return open('assets/2022_class_1.html', 'r').read()
    #elif value == '2023':
        #return open('assets/2023_class_1.html', 'r').read()

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
    if yeardropdown2 == '2023'and myslider4 ==1:
        return open('assets/class_positive_map_2023_1.html', 'r').read()
    elif yeardropdown2 == '2023' and myslider4 ==2:
        return open('assets/class_positive_map_2023_2.html', 'r').read()
    elif yeardropdown2 == '2023' and myslider4 == 3:
        return open('assets/class_positive_map_2023_3.html', 'r').read()
    elif yeardropdown2 == '2023' and myslider4 == 4:
        return open('assets/class_positive_map_2023_4.html', 'r').read()
    elif yeardropdown2 == '2023' and myslider4 == 5:
        return open('assets/class_positive_map_2023_5.html', 'r').read()


# Define the callback function for negative
@app.callback(
    Output('html-iframe-6', 'srcDoc'),
    [Input('yeardropdown2', 'value'),Input('myslider5', 'value')]
    #[Input('yeardropdown', 'value'), Input('mydropdown', 'value'), Input('myslider2', 'value')]
)

def update_output(yeardropdown2,myslider5):
    # Define the HTML content to display based on the dropdown menu
    #2021
    if yeardropdown2 == '2021' and myslider5 ==1:
        return open('assets/class_negative_map_2021_1.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider5 ==2:
        return open('assets/class_negative_map_2021_2.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider5 == 3:
        return open('assets/class_negative_map_2021_3.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider5 == 4:
        return open('assets/class_negative_map_2021_4.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider5 == 5:
        return open('assets/class_negative_map_2021_5.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider5 == 6:
        return open('assets/class_negative_map_2021_6.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider5 == 7:
        return open('assets/class_negative_map_2021_7.html', 'r').read()
    elif yeardropdown2 == '2021' and myslider5 == 8:
        return open('assets/class_negative_map_2021_8.html', 'r').read()
    #2022
    if yeardropdown2 == '2022'and myslider5 ==1:
        return open('assets/class_negative_map_2022_1.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider5 ==2:
        return open('assets/class_negative_map_2022_2.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider5 == 3:
        return open('assets/class_negative_map_2022_3.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider5 == 4:
        return open('assets/class_negative_map_2022_4.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider5 == 5:
        return open('assets/class_negative_map_2022_5.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider5 == 6:
        return open('assets/class_negative_map_2022_6.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider5 == 7:
        return open('assets/class_negative_map_2022_7.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider5 == 8:
        return open('assets/class_negative_map_2022_8.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider5 == 9:
        return open('assets/class_negative_map_2022_9.html', 'r').read()
    elif yeardropdown2 == '2022' and myslider5 == 10:
        return open('assets/class_negative_map_2022_10.html', 'r').read()

        # 2023
    if yeardropdown2 == '2023'and myslider5 ==1:
        return open('assets/class_negative_map_2023_1.html', 'r').read()
    elif yeardropdown2 == '2023' and myslider5 ==2:
        return open('assets/class_negative_map_2023_2.html', 'r').read()
    elif yeardropdown2 == '2023' and myslider5 == 3:
        return open('assets/class_negative_map_2023_3.html', 'r').read()
    elif yeardropdown2 == '2023' and myslider5 == 4:
        return open('assets/class_negative_map_2023_4.html', 'r').read()
    elif yeardropdown2 == '2023' and myslider5 == 5:
        return open('assets/class_negative_map_2023_5.html', 'r').read()
if __name__ == "__main__":
    app.run_server(port=8073)