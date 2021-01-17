import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import datetime
import os

st.title("Test Project")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['second column'])

'You selected:', option

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date < end_date:
    st.success(f'Start date: {start_date} \n\nEnd date: {end_date}')
else:
    st.error('Error: End date must fall after start date.')

# TODO: include the .json and .csv of YouTube statistics for the US (DONE)
for dirname, _, filenames in os.walk('C:/Users/ongad/OneDrive/Desktop/CruzHacks Data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
nRowsRead = None  # specify 'None' if want to read whole file
# CAvideos.csv has 40881 rows in reality, but we are only loading/previewing the first 1000 rows
df1 = pd.read_csv('C:/Users/ongad/OneDrive/Desktop/CruzHacks Data/USvideos.csv', delimiter=',', nrows=nRowsRead)
df1.dataframeName = 'USvideos.csv'
nRow, nCol = df1.shape

# define variables for video link, title, views, likes, dislikes, comments, date columns
link = df1.video_id
title = df1.title
views = df1.views
likes = df1.likes
dislikes = df1.dislikes
comments = df1.comment_count
dates = df1.trending_date
print(f'There are {nRow} rows and {nCol} columns')
df1.head(5)
# TODO: Once the table is set up properly, with the results filtered by start and end date, we can include a SelectBox
#  to display certain metrics like the ones we defined above sorted in descending order.

DATA_URL = ('USvideos.csv')
st.dataframe({"Link": link, "Trending Date": dates, "Title": title, "Views": views, "Likes": likes, "Dislikes": dislikes, "Comment count": comments})
