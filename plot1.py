import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_excel('data6.xlsx', sheet_name='Data')

df_selected = df.loc[df['Год'].isin([2005, 2012, 2019, 2021])]

colors = px.colors.qualitative.Set2  # выбираем цветовую палитру

fig = go.Figure()
fig.add_trace(go.Bar(x=df_selected['Год'], y=df_selected['Республика'], name='республика', marker_color=colors[0], width=0.5))
fig.add_trace(go.Bar(x=df_selected['Год'], y=df_selected['Города и поселки городского типа'], name='города и поселки городского типа', marker_color=colors[1], width=0.5))
fig.add_trace(go.Bar(x=df_selected['Год'], y=df_selected['Сельские населенные пункты'], name='сельские населенные пункты', marker_color=colors[2], width=0.5))
fig.update_layout(title='Доля населения, пользующегося услугами водоснабжения', xaxis_title='Год', yaxis_title='Доля населения, %')
fig.update_xaxes(tickmode='array', tickvals=[2005, 2012, 2019, 2021])
fig.show()