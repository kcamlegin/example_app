# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 21:41:40 2023

@author: Nigel Mack
"""


import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd
import dash_bootstrap_components as dbc

data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "price": [154.99, 268.65, 100.47, 96.75],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
        'headerTooltip': "This is stock ticket"

    },
    {
        "headerName": "Company",
        "field": "company",
        'headerTooltip': "This is Company name"
    },
    {
        "headerName": "Last Close Price",
        "field": "price",
        'headerTooltip': "This is last close price",
        "valueFormatter": {"function": """d3.format("($,.2f")(params.value)"""},
        "editable": True,
    },
]


grid = dag.AgGrid(
    id="tooltip-simple-example",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
    dashGridOptions = {'pagination':True,"tooltipShowDelay": 0},
    defaultColDef={"editable": False,"tooltipComponent": "CustomTooltip"},
)


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [dcc.Markdown("Example of custom tooltip"), grid],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run(debug=True)