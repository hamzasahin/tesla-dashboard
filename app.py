# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load your CSV data
data_path = 'data/7SAYGDEE1PF623846-drives.csv'  # Update this path to your actual CSV file location
data = pd.read_csv(data_path)

# Convert 'Started At (PST)' to datetime and create a 'Time of Day' category
data['Started At (PST)'] = pd.to_datetime(data['Started At (PST)'])
data['Time of Day'] = pd.cut(data['Started At (PST)'].dt.hour,
                             bins=[0, 6, 12, 18, 24],
                             labels=['Night', 'Morning', 'Afternoon', 'Evening'],
                             right=False)

# Visualization 1: Line Chart for Driving Duration Over Time
fig_line = px.line(data, x='Started At (PST)', y='Duration (Minutes)', title='Driving Duration Over Time')
fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
fig_line.update_xaxes(title_text='Date')
fig_line.update_yaxes(title_text='Duration (Minutes)')

# Visualization 2: Pie Chart for Distribution of Driving Times of Day
fig_pie = px.pie(data, names='Time of Day', title='Distribution of Driving Times of Day')
fig_pie.update_traces(textinfo='percent+label')
fig_pie.update_layout(showlegend=True)

# Initialize your Dash app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Tesla Driving Dashboard', style={'textAlign': 'center', 'marginTop': '20px', 'marginBottom': '20px'}),

    html.Div([
        dcc.Dropdown(
            id='data-type-dropdown',
            options=[
                {'label': 'Driving Duration Over Time', 'value': 'DURATION'},
                {'label': 'Distribution of Driving Times of Day', 'value': 'TIME_OF_DAY'},
            ],
            value='DURATION',
            style={'width': '48%', 'margin': '0 auto'}
        )
    ], style={'marginBottom': '20px'}),

    html.Div(id='graph-container', style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'})
])

@app.callback(
    Output('graph-container', 'children'),
    [Input('data-type-dropdown', 'value')]
)
def update_graph(selected_value):
    if selected_value == 'DURATION':
        return dcc.Graph(id='line-chart-driving-duration', figure=fig_line)
    elif selected_value == 'TIME_OF_DAY':
        return dcc.Graph(id='pie-chart-time-of-day', figure=fig_pie)

server = app.server
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)