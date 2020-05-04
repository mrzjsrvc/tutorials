import pandas as pd
import plotly.express as px
import plotly

df = pd.read_csv("df.csv")                              # Read in data from CSV-file
print(df)

fig = px.line(df, x="Date", y="Measurement", color="Attribute", title="Weather in Karlskrona")
fig.write_html('first_figure.html')#, auto_open=True)   # "auto_open=True" opens the file automatically right after it's made
# fig.show()                                            # Show the figure locally in a python window
