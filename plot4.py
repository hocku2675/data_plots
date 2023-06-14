import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('data6_4.xlsx', sheet_name='Data')

cat_order = pd.Categorical(df.columns[1:], categories=['Республика', 'бассейн реки Неман', 'бассейн реки Западная Двина', 'бассейн реки Западный Буг', 'бассейн реки Днепр', 'бассейн реки Припять'], ordered=True)

# создаем список объектов bar для каждого года
bars = []
colors = px.colors.sequential.Viridis_r
for year in df['Год']:
    bars.append(go.Bar(x=df.columns[1:], y=df[df['Год'] == year].iloc[:, 1:].values[0], name=str(year), marker_color=colors[min(len(bars), len(colors)-1)]))

# создаем график с помощью списка объектов bar
fig = go.Figure(bars)
fig.update_layout(title='Интенсивность использования запасов пресной воды (водный стресс) ', xaxis_title='Область', yaxis_title='Интенсивность, %', barmode='group')
fig.update_xaxes(categoryorder='array', categoryarray=cat_order)
fig.show()