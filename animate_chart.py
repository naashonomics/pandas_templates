import pandas as pd 
import streamlit as st 
import plotly.express as px 

# load built-in gapminder dataset from plotly
df= px.data.gapminder()
st.header("GDP Per Cap Data")
st.write(df)


#fetch all years in data set which are unique 
year_options=df['year'].unique().tolist()


year=st.selectbox('which year would you like to see data for ?',year_options,0)

#filter data set user wants base on the selected year 

df1=df[df['year']==year] 
#plot without animation 
fig = px.scatter(df1, x='gdpPercap', y='lifeExp',size='pop', color='continent',hover_name='continent',log_x=True,size_max=55,range_x=[100,100000],range_y=[25,90])
fig.update_layout(width=1000)
#plot with animation 
fig1 = px.scatter(df, x='gdpPercap', y='lifeExp',size='pop', color='continent',hover_name='continent',log_x=True,size_max=55,range_x=[100,100000],range_y=[25,90],animation_frame="year",animation_group="country")
fig1.update_layout(width=1000)

st.header("Customized Plot for " + str(year) )
st.write(fig)


st.header("animated Plot")
st.write(fig1)
