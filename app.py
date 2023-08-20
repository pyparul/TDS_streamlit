import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")
    
    st.write("Enter three numbers below:")

    col1, col2, col3 = st.columns(3)

    with col1:
        number1 = st.number_input("Number 1", value=0)

    with col2:
        number2 = st.number_input("Number 2", value=0)

    with col3:
        number3 = st.number_input("Number 3", value=0)

    if st.button("Find Largest"):
        largest_number = find_largest_number(number1, number2, number3)
        st.success(f"The largest number is: {largest_number}")

    st.markdown(
        """
        <style>
        .stButton button {
            background-color: #F63366;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
