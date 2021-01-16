import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import datetime

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

# TODO: include the youtube statistics in the US later
# TODO: filter out the results using start date and end date
# TODO: displays view count, likes, dislikes, video name, channel name, number of comments (if possible) and URL's to the videos if possible
