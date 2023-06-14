import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

#аналогично как plot4
df = pd.read_excel('data6_3.xlsx', sheet_name='Data')

cat_order = pd.Categorical(df.columns[1:], categories=['Республика', 'г.Минск', 'Минская область', 'Брестская область', 'Витебская область', 'Гомельская область', 'Гродненская область', 'Могилевская область'], ordered=True)

bars = []
colors = px.colors.sequential.Viridis_r[1:]
for year in df['Год']:
    bars.append(go.Bar(x=df.columns[1:], y=df[df['Год'] == year].iloc[:, 1:].values[0], name=str(year), marker_color=colors[len(bars)]))

fig = go.Figure(bars)
fig.update_layout(title='Доля населения, пользующегося услугами водоснабжения', xaxis_title='Область', yaxis_title='Доля населения, %', barmode='group')
fig.update_xaxes(categoryorder='array', categoryarray=cat_order)
fig.show()