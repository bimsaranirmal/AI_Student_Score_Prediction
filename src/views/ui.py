import streamlit as st
from .styles import get_css

class MainView:
    def setup_page(self):
        st.set_page_config(
            page_title="Student Analytics Platform",
            page_icon="⚡",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        st.markdown(get_css(), unsafe_allow_html=True)

    def render_login(self):
        st.markdown("<div style='text-align: center;'><h1>🔐 Login</h1></div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Log In", use_container_width=True)
                
                if submitted:
                    return username, password
        return None, None

    def render_register(self):
        st.markdown("<div style='text-align: center;'><h1>📝 Register</h1></div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.form("register_form"):
                username = st.text_input("Choose Username")
                email = st.text_input("Email Address")
                password = st.text_input("Create Password", type="password")
                submitted = st.form_submit_button("Sign Up", use_container_width=True)
                
                if submitted:
                    return username, email, password
        return None, None, None

    def render_sidebar(self):
        with st.sidebar:
            st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=60)
            
            if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
                st.markdown("## Welcome")
                page = st.radio(
                    "",
                    ["Login", "Register"],
                    label_visibility="collapsed"
                )
                return page
            
            st.markdown(f"## Hello, {st.session_state['user']['username']}!")
            page = st.radio(
                "Navigator",
                ["🏠 Dashboard", "⚡ Predictor"],
                label_visibility="collapsed"
            )
            
            st.markdown("---")
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state["logged_in"] = False
                st.session_state["user"] = None
                st.rerun()

            if page == "⚡ Predictor":
                self.render_user_manual()
                
            return page

    def render_user_manual(self):
        st.markdown("---")
        st.markdown("### 📘 Quick Guide")
        
        st.info("Input student details to generate AI-powered performance predictions.")

        st.markdown("""
        **How it works:**
        1. **Profile:** Set demographics & course.
        2. **Habits:** Input study & attendance data.
        3. **Lifestyle:** Sleep & environment stats.
        4. **Predict:** Get score & insights.
        """)

        st.caption("Powered by CatBoost AI")

    def render_home_page(self):
        st.markdown("""
        <div style='text-align:center; padding-bottom: 3rem;'>
            <h1 style='font-size: 3.5rem; margin-bottom: 0.5rem;'>Student Analytics AI</h1>
            <p style='font-size:1.2rem; color:#94a3b8; max-width: 600px; margin: 0 auto;'>
            Unlock academic potential with advanced machine learning predictions and personalized behavioral insights.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class='card'>
                <div style='font-size: 2rem;'>🎯</div>
                <h3>Precision AI</h3>
                <p style='color: #cbd5e1;'>
                Forecast exam scores with high accuracy using our state-of-the-art CatBoost regression model.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class='card'>
                <div style='font-size: 2rem;'>🧬</div>
                <h3>Deep Analysis</h3>
                <p style='color: #cbd5e1;'>
                Understand how sleep, attendance, and study methods impact academic performance.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class='card'>
                <div style='font-size: 2rem;'>💡</div>
                <h3>Smart Insights</h3>
                <p style='color: #cbd5e1;'>
                Receive tailored recommendations to optimize study habits and improve grades.
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div class='section-title'>🚀 Platform Capabilities</div>", unsafe_allow_html=True)
        
        c1, c2 = st.columns([2, 1])
        with c1:
             st.markdown("""
            <div class='card'>
                <ul style='font-size:1.1rem; color:#cbd5e1; list-style: none; padding-left: 0; line-height: 2;'>
                    <li>✨ <b>Predictive Scoring:</b> Anticipate results before the exam</li>
                    <li>✨ <b>Risk Assessment:</b> Identify at-risk students early</li>
                    <li>✨ <b>Holistic Tracking:</b> Monitor lifestyle vs. performance trends</li>
                    <li>✨ <b>Decision Support:</b> Data-backed academic planning</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class='card' style='text-align: center; background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 51, 234, 0.1)); border: 1px solid rgba(147, 51, 234, 0.2);'>
                <h3>Ready to Start?</h3>
                <p>Jump to the predictor tool now.</p>
            </div>
            """, unsafe_allow_html=True)

        self.render_footer()

    def render_prediction_page(self):
        st.markdown("<h1 style='text-align: center;'>⚡ Performance Predictor</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #94a3b8; margin-bottom: 2rem;'>Configure student parameters to generate a forecast.</p>", unsafe_allow_html=True)
        
        return self._render_input_form()

    def _render_input_form(self):
        with st.container():
            st.markdown("<div class='section-title'>👤 Profile Details</div>", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            with c1:
                age = st.number_input("Student Age", min_value=10, max_value=60, value=20)
                gender = st.selectbox("Gender Identity", options=["male", "female"], index=0)
            with c2:
                course = st.selectbox("Academic Stream", options=["Science", "Maths", "IT", "Engineering", "Business", "Arts"])
                exam_difficulty = st.selectbox("Exam Complexity", options=["easy", "medium", "hard"])
            with c3:
                class_attendance = st.slider("Attendance Rate (%)", 0, 100, 80)
                facility_rating = st.slider("Campus Facilities (1-5)", 1, 5, 3)

            st.markdown("<div class='section-title'>📚 Study Metrics</div>", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns(3)
            with c1:
                study_hours = st.slider("Daily Study (Hours)", 0.0, 15.0, 4.0, step=0.5)
            with c2:
                study_method = st.selectbox("Primary Strategy", options=["self-study", "group-study", "online", "tuition"])
            with c3:
                internet_access = st.selectbox("Internet Connectivity", options=["yes", "no"])

            st.markdown("<div class='section-title'>🌙 Lifestyle Factors</div>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                sleep_hours = st.slider("Daily Sleep (Hours)", 0.0, 12.0, 7.0, step=0.5)
            with c2:
                sleep_quality = st.selectbox("Sleep Consistency", options=["poor", "average", "good", "excellent"])

        st.markdown("<br>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            predict_btn = st.button("✨ Generate AI Prediction", use_container_width=True)

        if predict_btn:
             return {
                "age": age,
                "gender": gender,
                "course": course,
                "study_hours": study_hours,
                "class_attendance": class_attendance,
                "internet_access": internet_access,
                "sleep_hours": sleep_hours,
                "sleep_quality": sleep_quality,
                "study_method": study_method,
                "facility_rating": facility_rating,
                "exam_difficulty": exam_difficulty
            }
        return None

    def render_result_card(self, score, recommendations):
        # Determine Color and Label
        if score >= 85:
            label, color_code = "Outstanding", "#22c55e"
        elif score >= 70:
            label, color_code = "Strong", "#3b82f6"
        elif score >= 50:
            label, color_code = "Moderate", "#f59e0b"
        else:
            label, color_code = "At Risk", "#ef4444"

        st.markdown(f"""
        <div class='card' style='border: 1px solid {color_code}40;'>
            <h2 style='text-align: center; margin-bottom: 2rem;'>Prediction Results</h2>
            <div class='metric-container'>
                <div class='metric-label'>Estimated Score</div>
                <div class='metric-value'>{score}</div>
                <div style='color: {color_code}; font-weight: 600; font-size: 1.5rem; margin-top: 1rem;'>
                    {label} Performance
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(score / 100)

        # ------------------ RECOMMENDATIONS ------------------
        st.markdown("<div class='section-title'>💡 AI Recommendations</div>", unsafe_allow_html=True)
        
        for rec in recommendations:
            st.info(rec)

        self.render_footer()

    def render_footer(self):
        st.markdown("<div class='footer'>Student Analytics Platform 2.0 • 2026 Edition</div>", unsafe_allow_html=True)
        st.markdown("""
        <div style='text-align: center; opacity: 0.5; font-size: 0.8rem;'>
            Disclaimer: Predictions are based on statistical patterns and should be used as a guide only.
        </div>
        """, unsafe_allow_html=True)
