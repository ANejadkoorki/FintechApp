import pandas as pd
import plotly.graph_objects as go
from pprint import pprint


def financial_data_display(input_file):
    df = pd.read_csv(input_file)
    list_of_averages = get_average_of_columns(df)
    # convert int type to str type
    df["<DTYYYYMMDD>"] = df["<DTYYYYMMDD>"].astype('str')
    # convert to datetime object
    df["<DTYYYYMMDD>"] = pd.to_datetime(df["<DTYYYYMMDD>"], format="%Y-%m-%d")
    df["<DTYYYYMMDD>"] = df["<DTYYYYMMDD>"].astype('str')
    total_rows = []
    for index, row in df.iterrows():
        total_rows.append([item_of_row for item_of_row in row])
    return total_rows, list_of_averages


def get_average_of_columns(df):
    list_of_averages = list()
    for column, items in df.iteritems():
        if column in ["<TICKER>", "<DTYYYYMMDD>", "<PER>"]:
            continue
        else:
            average = round(sum(items) / len(items), 2)
            list_of_averages.append((column, average))
    list_of_averages.insert(0, df["<TICKER>"][0])
    return list_of_averages


def financial_data_plot(input_file):
    df = pd.read_csv(input_file)
    # convert int type to str type
    df["<DTYYYYMMDD>"] = df["<DTYYYYMMDD>"].astype('str')
    # convert to datetime object
    df["<DTYYYYMMDD>"] = pd.to_datetime(df["<DTYYYYMMDD>"], format="%Y-%m-%d")
    fig = go.Figure(data=[go.Candlestick(x=df["<DTYYYYMMDD>"],
                                         open=df['<OPEN>'],
                                         high=df['<HIGH>'],
                                         low=df['<LOW>'],
                                         close=df['<CLOSE>'])
                          ])
    fig.update_layout(xaxis_rangeslider_visible=False)
    return fig.show()
