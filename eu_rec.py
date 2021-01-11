#Imports
import streamlit as st
import pandas as pd
import pickle

#Loading Data 
euc_df = pickle.load(open( "pickle_jar/euclidean_dist_df.p", "rb"))
idr_df = pd.read_csv('in_depth_reviews.csv')

st.title('Instachart')


filter_bourbon = st.selectbox('Bourbon Similarity', sorted(idr_df['Name'].values))
top_three_choices = st.selectbox('Choose between the top three most similar bourbons', [1,2,3])

bourbon_recommender = euc_df.loc[filter_bourbon]

bourbon_recommender.sort_values(ascending=True, inplace=True)

# st.write(bourbon_recommender[1:4])
chosen_bourbon = bourbon_recommender.index[top_three_choices]

series_bourbon = idr_df.loc[idr_df['Name']==chosen_bourbon]

# st.text('Recommended Bourbon')
# st.write(series_bourbon.loc[series_bourbon.index[0]].at['Name'])

name = series_bourbon.loc[series_bourbon.index[0]].at['Name']

url = series_bourbon.loc[series_bourbon.index[0]].at['Link']

link = f'Name of the Recommended Bourbon: [{name}]({url})'


st.markdown(link, unsafe_allow_html=True)

st.markdown(series_bourbon.loc[series_bourbon.index[0]].at['Distillery'])

st.markdown(series_bourbon.loc[series_bourbon.index[0]].at['Proof'])

st.markdown(series_bourbon.loc[series_bourbon.index[0]].at['Mashbill'])