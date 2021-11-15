import pandas as pd
import plotly.graph_objects as go
from datetime import datetime


def financial_data_display(input_file):
    data = pd.read_csv(input_file)
    total_rows = []
    for index, row in data.iterrows():
        total_rows.append([item_of_row for item_of_row in row])
    return total_rows


def financial_data_plot(input_file):
    df = pd.read_csv(input_file)
    df["<DTYYYYMMDD>"] = df["<DTYYYYMMDD>"].astype('str')
    df["<DTYYYYMMDD>"] = pd.to_datetime(df["<DTYYYYMMDD>"], format="%Y-%m-%d")
    fig = go.Figure(data=[go.Candlestick(x=df["<DTYYYYMMDD>"],
                    open=df['<FIRST>'],
                    high=df['<HIGH>'],
                    low=df['<LOW>'],
                    close=df['<CLOSE>'])
                          ])
    fig.update_layout(xaxis_rangeslider_visible=False)
    return fig.show()


