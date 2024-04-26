# import streamlit as st 
# import pandas as pd


# st.write("Hellostre")

# df = pd.DataFrame({"Avinash",27,"Bing"})
# df



# df1 = pd.DataFrame({'col1': [1,2,3]})
# df1


# df3 = pd.DataFrame(["Avinash",27,"Bing"])
# df3

import pandas as pd
import streamlit as st

# Enable user to upload two CSV files
file1 = st.file_uploader('Upload CSV file 1')
if  file1 is not None:
   data1 = pd.read_csv(file1)
   st.dataframe(data1)
file2 = st.file_uploader('Upload CSV file 2')
if  file2 is not None:
   data2 = pd.read_csv(file2)
   st.subheader("Data from second File")
   st.dataframe(data2)

if  file1 is not None and file2 is not None:
   # Create two dataframes from the uploaded CSV files
   df1 = pd.read_csv(file1)
   df2 = pd.read_csv(file2)

   # Enable user to enter column names they want to compare
   col1 = st.text_input('Enter column name 1')
   col2 = st.text_input('Enter column name 2')

   # Compare the specified columns of the two dataframes and identify the matching rows and unmatched rows
   if col1 and col2:
      df1_matching = df1[df1[col1] == df1[col2]]
      df1_unmatching = df1[df1[col1]!= df1[col2]]
      
      df2_matching = df2[df2[col1] == df2[col2]]
      df2_unmatching = df2[df2[col1]!= df2[col2]]

   # Print the final dataframes with matching and unmatched rows of both the dataframes
   if col1 and col2:
      st.write('Matching rows in df1:')
      st.write(df1_matching)
      st.write('Unmatching rows in df1:')
      st.write(df1_unmatching)
      st.write('Matching rows in df2:')
      st.write(df2_matching)
      st.write('Unmatching rows in df2:')
      st.write(df2_unmatching)