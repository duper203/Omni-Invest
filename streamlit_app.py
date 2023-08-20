import streamlit as st



st.title("Invest!!!")

# select box - 투자사 스타트업
option = st.selectbox(
    'How would you like to be contacted?',
    ('Investor', 'Startup'))



# text button
input_user_name = st.text_input(label="Name", value="")


# 검색 버튼

if st.button("Confirm"):
    con = st.container()
    con.caption("Your search would be about:")
    con.write(f"{str(option)} -> {str(input_user_name)}")


########## 밑에 칼럼 ############

num_columns = 5  # Change this to the desired number of columns

columns = st.columns(num_columns)

for col in columns:
    st.header("Content for column")
    with st.expander("See explanation"):
        st.write(" The chart above shows some numbers I picked for you.I rolled actual dice for these, so they're *guaranteed* tobe random.")


