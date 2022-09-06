import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title('Cricket Score Predictor')

col1 ,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox ('Select Batting team',sorted(teams))
with col1:
    bowling_team = st.selectbox ('Select Bowling team',sorted(teams))

col3,col4,col5 = st.columns(3)

with col3:
    current_score =st.number_input('Current Score')
with col4:
    over_done = st.number_input('overs done (works for >5 over)')
with col5:
    wickets = st.number_input('Wickets Out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button ('predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr = current_score/ overs

    input_df =v
