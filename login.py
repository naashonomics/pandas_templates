import streamlit as st
import streamlit_authenticator as stauth

def login():
    names = ['Join Prime','Join Walmart plus']
    usernames = ['amazon','walmart']
    passwords = ['amazonpay','phonepe']
    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=30)
    name, authentication_status, username = authenticator.login('Login', 'main')
        
    if st.session_state["authentication_status"]:
        test=authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')
        
def main():
    login()

if __name__ == "__main__":
    main()
