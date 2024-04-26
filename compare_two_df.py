import streamlit as st
import pandas as pd

st.title("Streamlit App")

# Load DataFrames
df1 = pd.read_csv("employee.csv")
df2 = pd.read_csv("Student.csv")

# Display DataFrame 1
st.header("DataFrame 1")
st.write(df1.head())

# Display DataFrame 2
st.header("DataFrame 2")
st.write(df2.head())

# Select columns to compare from DataFrame 1
df1_col = st.selectbox("Select a column from DataFrame 1", df1.columns)

# Select columns to compare from DataFrame 2
df2_col = st.selectbox("Select a column from DataFrame 2", df2.columns)

# Global variables to store the results of "Perform Operations" function
perform_result = None

# Function to perform comparison
def perform_operations(df1, df2, df1_col, df2_col):
    global perform_result  # Declare global variable
    # Compare the specified columns of the two DataFrames and identify matching and unmatched rows
    df1_matching = df1[df1[df1_col].isin(df2[df2_col])]
    df1_unmatching = df1[~df1[df1_col].isin(df2[df2_col])]
    
    df2_matching = df2[df2[df2_col].isin(df1[df1_col])]
    df2_unmatching = df2[~df2[df2_col].isin(df1[df1_col])]

    # Store the results in global variable
    perform_result = (df1_matching, df2_matching, df1_unmatching, df2_unmatching)
    # st.write("Perform_result",perform_result)


    # Print the final DataFrames with matching and unmatched rows of both the DataFrames
    st.subheader("Matching rows in DataFrame 1:")
    st.write(df1_matching)
    st.subheader("Unmatching rows in DataFrame 1:")
    st.write(df1_unmatching)
    
    st.subheader("Matching rows in DataFrame 2:")
    st.write(df2_matching)
    st.subheader("Unmatching rows in DataFrame 2:")
    st.write(df2_unmatching)

    combined_df_matched = pd.concat([df1_matching, df2_matching])
    st.subheader('Combined matched Records')
    st.dataframe(combined_df_matched.style)

    # Display Unmatched records
    combined_df_unmatched = pd.concat([df1_unmatching, df2_unmatching])
    st.subheader('Combined Unmatched Records')
    st.dataframe(combined_df_unmatched.style)


# Function to finalize comparison
# def finalize_comparison(perform_result):
#     # Use global variable to access the results of "Perform Operations" function
   

#     st.write("Perform_result in finalize method",perform_result)
    
#     if perform_result is not None:
#         a, b, c, d = perform_result
#         # Combine all matched dataframes into one dataframe
#         combined_df_matched = pd.concat([a, b])
#         st.dataframe(combined_df_matched.style.set_properties(**{'width': '80%'}))

#         # Display Unmatched records
#         combined_df_unmatched = pd.concat([c, d])
#         st.subheader('Combined Unmatched Records')
#         st.dataframe(combined_df_unmatched.style.set_properties(**{'width':'65%'}))
#     else:
#         st.warning("Please perform operations first.")

# Button to trigger comparison
if st.button("Perform Operations"):
    perform_operations(df1, df2, df1_col, df2_col)


# Button to finalize comparison
# if st.button("Finalize Comparison"):
#     finalize_comparison(perform_result)

