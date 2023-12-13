import streamlit as st
def find_largest(n1,n2,n3):
  return max(n1,n2,n3)

st.title('Find largest number')
n1=st.number_input('Enter first number', value =0.0)
n2=st.number_input('Enter second number', value =0.0)
n3=st.number_input('Enter third number', value =0.0)

if st.button('Find Larget'):
  largest = find_largest(n1,n2,n3)
  st.success(f'The largest number is: {largest}')
