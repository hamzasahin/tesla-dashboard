# Import necessary libraries
import dash
from dash import dcc, html
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

# Visualization 2: Pie Chart for Distribution of Driving Times of Day
fig_pie = px.pie(data, names='Time of Day', title='Distribution of Driving Times of Day')

# Initialize your Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Tesla Driving Dashboard'),

    dcc.Graph(
        id='line-chart-driving-duration',
        figure=fig_line
    ),

    dcc.Graph(
        id='pie-chart-time-of-day',
        figure=fig_pie
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)