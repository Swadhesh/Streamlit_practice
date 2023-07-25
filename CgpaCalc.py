import streamlit as st

def calculate_gpa(cgpa, credits, curr_gpa, curr_credits):
    tot_credits = credits + curr_credits
    a = cgpa * credits
    b = curr_gpa * curr_credits
    ans = (a + b) / tot_credits
    return ans

def main():
    st.markdown('<h1 style="color:lightgreen; text-align:center;">Current CGPA calculator</h1>',unsafe_allow_html=True)
    st.markdown('<h3 style="color:darkgreen; text-align:center;">By Swadhesh 20IT108</h3>',unsafe_allow_html=True)
    cgpa = st.number_input('Enter CGPA till your previous semester:', min_value=0.1, step=0.1, value=0.1)
    credits = st.number_input('Enter the total credits earned till your previous semester:', min_value=1, step=1, value=1)
    curr_gpa = st.number_input('Enter GPA of your current semester:', min_value=0.1, step=0.1, value=0.1)
    curr_credits = st.number_input('Enter credits earned in the current semester:', min_value=1, step=1, value=1)

    if st.button('Calculate current CGPA'):
        gpa = calculate_gpa(cgpa, credits, curr_gpa, curr_credits)
        st.success(f'Your current CGPA is: {gpa:.2f}')

if __name__ == '__main__':
    main()
