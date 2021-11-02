import pandas as pd


def financial_data_display(input_file):
    data = pd.read_csv(input_file)
    total_rows = []
    for index, row in data.iterrows():
        total_rows.append([item_of_row for item_of_row in row])
    return total_rows


def financial_data_plot(input_file):
    data = pd.read_csv(input_file)
    return data.plot(kind='line', x='<VOL>', y='<CLOSE>')
