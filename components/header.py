from dash import html

def Header(title):
    return html.H1(title, style={'textAlign': 'center', 'marginTop': '20px', 'marginBottom': '20px'})