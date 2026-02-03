import streamlit as st
from src.models.prediction_model import PredictionModel
from src.models.auth_model import AuthModel
from src.views.ui import MainView

class MainController:
    def __init__(self):
        self.model = PredictionModel()
        self.auth_model = AuthModel()
        self.view = MainView()

    def run(self):
        self.view.setup_page()
        page = self.view.render_sidebar()

        # Auth Flow
        if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
            if page == "Login":
                username, password = self.view.render_login()
                if username and password:
                    user = self.auth_model.login(username, password)
                    if user:
                        st.session_state["logged_in"] = True
                        st.session_state["user"] = user
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error("Invalid username or password")
            elif page == "Register":
                username, email, password = self.view.render_register()
                if username and email and password:
                    success = self.auth_model.register(username, email, password)
                    if success:
                        st.success("Registration successful! Please log in.")
            return

        # Main App Flow
        if page == "🏠 Dashboard":
            self.view.render_home_page()
        elif page == "⚡ Predictor":
            inputs = self.view.render_prediction_page()
            
            if inputs:
                with st.spinner("Analyzing data and generating prediction..."):
                    score = self.model.predict(inputs)
                    recommendations = self.model.get_recommendations(inputs)
                
                self.view.render_result_card(score, recommendations)

if __name__ == "__main__":
    controller = MainController()
    controller.run()
