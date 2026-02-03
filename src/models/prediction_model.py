import pandas as pd
from catboost import CatBoostRegressor
import streamlit as st

class PredictionModel:
    def __init__(self, model_path="student_exam_model.cbm"):
        self.model_path = model_path
        self.model = self._load_model()

    @st.cache_resource
    def _load_model(_self):
        model = CatBoostRegressor()
        try:
            model.load_model("student_exam_model.cbm")
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None
        return model

    def predict(self, input_data: dict) -> float:
        """
        Predicts the exam score based on the input dictionary.
        Risk: Returns 0 if model is not loaded.
        """
        if self.model is None:
            return 0.0

        # Create DataFrame from input dict
        input_df = pd.DataFrame([input_data])
        
        # Predict
        try:
            prediction = self.model.predict(input_df)[0]
            # Clamp between 0 and 100
            return round(max(min(prediction, 100), 0), 1)
        except Exception as e:
            st.error(f"Prediction error: {e}")
            return 0.0

    def get_recommendations(self, inputs: dict) -> list:
        """
        Generates recommendations based on the input features.
        """
        recommendations = []
        
        study_hours = inputs.get("study_hours", 0)
        sleep_hours = inputs.get("sleep_hours", 0)
        class_attendance = inputs.get("class_attendance", 0)
        facility_rating = inputs.get("facility_rating", 0)
        internet_access = inputs.get("internet_access", "no")

        if study_hours < 4:
            recommendations.append("Consider increasing daily study time to at least 4–6 hours for better outcomes.")
        if sleep_hours < 7:
            recommendations.append("Aim for 7–9 hours of quality sleep nightly to improve focus and retention.")
        if class_attendance < 75:
            recommendations.append("Higher class attendance (≥80%) is strongly linked to improved performance.")
        if facility_rating < 3:
            recommendations.append("Facility quality impacts learning – explore alternative study environments if possible.")
        if internet_access == "no":
            recommendations.append("Reliable internet access can enhance learning through online resources.")

        if not recommendations:
            recommendations.append("You're on a great track! Continue maintaining your positive habits.")
            
        return recommendations
