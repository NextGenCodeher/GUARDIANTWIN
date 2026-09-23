import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time
from streamlit_autorefresh import st_autorefresh
# -------------------------------------------------

# PAGE CONFIG

# -------------------------------------------------

st.set_page_config(page_title="GuardianTwin", page_icon="🏥", layout="wide")

# -------------------------------------------------

# CUSTOM CSS

# -------------------------------------------------

st.markdown(
    """

<style>

.stApp,
body,
.css-18e3th9,
.reportview-container,
.main,
.block-container,
.css-1xonnm4,
.css-18e3th9 {
    background-color: #081526 !important;
    color: #f8fbff !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #082a44 !important;
    border-right: 1px solid rgba(255,255,255,0.22) !important;
    color: #f8fbff !important;
}

section[data-testid="stSidebar"] * {
    color: #f8fbff !important;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 22px !important;
    padding: 18px !important;
    border: 1px solid rgba(255,255,255,0.20) !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35) !important;
    color: #f8fbff !important;
}

/* Card content text */
[data-testid="metric-container"] span,
[data-testid="metric-container"] div,
[data-testid="metric-container"] p,
[data-testid="metric-container"] h2,
[data-testid="metric-container"] h3 {
    color: #ffffff !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 18px !important;
    font-weight: 600 !important;
    color: #e2f1ff !important;
    background: rgba(255, 255, 255, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.10) !important;
    border-radius: 14px !important;
    margin-right: 6px !important;
}

.stTabs [data-baseweb="tab"] button,
.stTabs [data-baseweb="tab"] span {
    color: #e2f1ff !important;
}

.stTabs [data-baseweb="tab"].baseweb-tabs-tab--active,
.stTabs [data-baseweb="tab"].baseweb-tabs-tab--active button,
.stTabs [data-baseweb="tab"].baseweb-tabs-tab--active span {
    background: #1472b8 !important;
    color: #ffffff !important;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.18) !important;
}

.stTabs [data-baseweb="tab"] button:hover,
.stTabs [data-baseweb="tab"] button:focus {
    color: #ffffff !important;
}

/* Headers */
h1, h2, h3, h4, h5, h6,
strong,
label,
button,
p,
span,
a,
li,
div,
summary {
    color: #f8fbff !important;
}

/* Markdown text */
.css-1n0xqz4,
.css-1v0mbdj,
.css-ffhzg2,
.css-1d391kg,
.css-1lcbmhc,
.css-12oz5g7,
.css-1n0xqz4 {
    color: #f8fbff !important;
}

/* Tables and dataframes */
.stDataFrame,
.css-1b3p1ko,
.css-1kyxreq,
.css-1v0mbdj,
.react-grid-item {
    color: #f8fbff !important;
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
}

/* Button and select text */
button,
select,
input,
textarea,
.streamlit-expanderHeader,
.css-1h9z7r5,
.css-18ni7ap {
    color: #f8fbff !important;
}

button,
.css-1x8cf1d,
.css-1kyxreq button {
    background-color: rgba(20, 114, 184, 0.95) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.16) !important;
}

/* Input boxes and selectors */
.stTextInput>div>div>input,
.stSelectbox,
.stSelectbox *,
.stSelectbox>div>div>div>div>div,
.stSelectbox>div>div>div>div>div>div,
.stSelectbox input,
.stSelectbox select,
input,
select,
textarea,
option {
    background: #000000 !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
}

section[data-testid="stSidebar"] select,
section[data-testid="stSidebar"] option,
section[data-testid="stSidebar"] div[data-testid="stSelectbox"] select,
section[data-testid="stSidebar"] div[data-testid="stSelectbox"] option,
section[data-testid="stSidebar"] div[role="combobox"],
section[data-testid="stSidebar"] div[role="combobox"] div,
section[data-testid="stSidebar"] div[role="combobox"] span,
section[data-testid="stSidebar"] div[role="combobox"] input,
section[data-testid="stSidebar"] div[role="listbox"],
section[data-testid="stSidebar"] div[role="listbox"] > div,
section[data-testid="stSidebar"] div[role="option"],
section[data-testid="stSidebar"] div[role="option"] span,
section[data-testid="stSidebar"] div[role="option"] div {
    background: #000000 !important;
    color: #ffffff !important;
}

section[data-testid="stSidebar"] button,
section[data-testid="stSidebar"] button span,
section[data-testid="stSidebar"] div[data-testid="stSelectbox"] button,
section[data-testid="stSidebar"] div[data-testid="stSelectbox"] div[role="combobox"],
section[data-testid="stSidebar"] div[role="listbox"],
section[data-testid="stSidebar"] div[role="listbox"] > div,
section[data-testid="stSidebar"] div[role="option"],
section[data-testid="stSidebar"] div[role="option"] span,
section[data-testid="stSidebar"] div[role="option"] div,
section[data-testid="stSidebar"] div[role="option"] input,
section[data-testid="stSidebar"] div[role="option"] label,
section[data-testid="stSidebar"] div[role="option"] p {
    background: #000000 !important;
    color: #ffffff !important;
}

section[data-testid="stSidebar"] .css-1u8p0vw,
section[data-testid="stSidebar"] .css-1d391kg,
section[data-testid="stSidebar"] .css-1d391kg span,
section[data-testid="stSidebar"] .css-1d391kg div,
section[data-testid="stSidebar"] div[role="listbox"] *,
section[data-testid="stSidebar"] div[role="option"] * {
    color: #ffffff !important;
    background: #000000 !important;
}

select::placeholder,
input::placeholder,
textarea::placeholder {
    color: #f8fbff !important;
    opacity: 1 !important;
}

div[role="listbox"],
div[role="listbox"] *,
div[role="option"],
div[role="option"] *,
div[role="presentation"],
div[role="presentation"] *,
div[role="menu"],
div[role="menu"] *,
div[role="menuitem"],
div[role="menuitem"] *,
ul[role="listbox"],
ul[role="listbox"] *,
li[role="option"],
li[role="option"] *,
div[class*="Select"],
div[class*="Select"] *,
div[class*="option"],
div[class*="option"] * {
    background: #000000 !important;
    color: #ffffff !important;
    border-color: rgba(255,255,255,0.18) !important;
}

/* Container panels */
.css-1kiw93k,
.css-1q8dd3e,
.css-15tx938,
.css-1mifyqa,
.css-13hzrol {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
}

.hero-panel {
    background: linear-gradient(160deg, rgba(59, 130, 246, 0.94), rgba(14, 165, 233, 0.90) 44%, rgba(15, 23, 42, 0.92));
    border-radius: 32px;
    border: 1px solid rgba(255, 255, 255, 0.18);
    padding: 30px;
    box-shadow: 0 35px 70px rgba(0, 0, 0, 0.28);
    color: #eef4ff;
}

.hero-panel h1 {
    margin: 0;
    font-size: 2.6rem;
    line-height: 1.05;
}

.hero-panel p {
    margin: 0.7rem 0 0;
    color: rgba(255, 255, 255, 0.88);
    font-size: 1rem;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.16);
    background: rgba(255, 255, 255, 0.09);
    padding: 0.7rem 1rem;
    font-weight: 700;
    color: #f8fbff;
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.05);
}

.glass-card {
    background: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    border-radius: 24px !important;
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.32) !important;
    backdrop-filter: blur(18px);
    color: #f8fbff !important;
}

.timeline-entry {
    background: rgba(255, 255, 255, 0.06) !important;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.13) !important;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 18px 36px rgba(0, 0, 0, 0.20) !important;
}

.timeline-entry h3 {
    margin-bottom: 0.55rem;
    color: #ffffff !important;
    font-size: 1.4rem;
    font-weight: 700;
}

.status-chip {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 999px;
    padding: 8px 14px;
    font-size: 0.95rem;
    font-weight: 700;
    border: 1px solid rgba(255,255,255,0.16);
    color: white !important;
    background: #22c55e;
}

.timeline-band {
    background: rgba(255,255,255,0.08);
    border-radius: 999px;
    height: 12px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.14);
}

.timeline-progress {
    background: linear-gradient(90deg, #38bdf8, #8b5cf6);
    height: 100%;
    transition: width 0.35s ease;
}

.timeline-caption {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    align-items: center;
    color: rgba(248, 251, 255, 0.78);
    font-size: 0.95rem;
}

.timeline-entry p {
    margin: 0.35rem 0;
    color: #e2f1ff !important;
    font-size: 1rem;
    line-height: 1.6;
}

.section-title {
    margin-top: 1.25rem;
    margin-bottom: 1rem;
    padding: 1rem 1.1rem;
    border-radius: 18px;
    background: rgba(11, 35, 58, 0.82);
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.03);
    font-size: 1.05rem;
    font-weight: 700;
}

.stTabs [data-baseweb="tab"] {
    font-size: 1rem !important;
    font-weight: 700 !important;
    color: #e2f1ff !important;
    background: rgba(255, 255, 255, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 16px !important;
    margin-right: 6px !important;
}

.stTabs [data-baseweb="tab"].baseweb-tabs-tab--active {
    background: linear-gradient(135deg, rgba(56, 189, 248, 0.95), rgba(59, 130, 246, 0.90)) !important;
    color: #ffffff !important;
    box-shadow: 0 14px 30px rgba(14, 165, 233, 0.18) !important;
}

.stTabs [data-baseweb="tab"] button:hover,
.stTabs [data-baseweb="tab"] button:focus {
    color: #ffffff !important;
}

button,
.css-1x8cf1d,
.css-1kyxreq button,
.st-buttongroup button {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.96), rgba(14, 165, 233, 0.95)) !important;
    color: #ffffff !important;
    border: none !important;
    box-shadow: 0 12px 26px rgba(14, 165, 233, 0.18) !important;
}

button:hover,
.css-1kyxreq button:hover,
.st-buttongroup button:hover {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.92), rgba(59, 130, 246, 0.92)) !important;
}

.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #38bdf8, #8b5cf6) !important;
}

</style>

""",
    unsafe_allow_html=True,
)

# -------------------------------------------------

# PLOTLY THEME HELPERS

# -------------------------------------------------


def apply_plotly_theme(
    fig,
    title=None,
    xaxis_title=None,
    yaxis_title=None,
    height=None,
):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(4,18,45,0.92)",
        font=dict(color="#f8fbff", family="Inter, Arial, sans-serif"),
        title_font=dict(color="#f8fbff", size=20, family="Inter, Arial, sans-serif"),
        legend=dict(
            orientation="h",
            y=-0.18,
            x=0.5,
            xanchor="center",
            font=dict(color="#f8fbff"),
        ),
        margin=dict(l=20, r=20, t=48, b=20),
        hovermode="x unified",
        colorway=["#38bdf8", "#fb7185", "#34d399", "#fbbf24", "#a855f7"],
    )
    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.08)",
        zeroline=False,
        color="#f8fbff",
        linecolor="rgba(255,255,255,0.16)",
        tickfont=dict(color="#f8fbff"),
        title_font=dict(color="#f8fbff"),
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.08)",
        zeroline=False,
        color="#f8fbff",
        linecolor="rgba(255,255,255,0.16)",
        tickfont=dict(color="#f8fbff"),
        title_font=dict(color="#f8fbff"),
    )
    if title is not None:
        fig.update_layout(title=title)
    if xaxis_title is not None or yaxis_title is not None:
        fig.update_layout(xaxis_title=xaxis_title, yaxis_title=yaxis_title)
    if height is not None:
        fig.update_layout(height=height)
    return fig


def build_tier_color(value, positive=True):
    if positive:
        if value >= 80:
            return "#22c55e"
        if value >= 50:
            return "#f59e0b"
        return "#f87171"
    else:
        if value < 35:
            return "#22c55e"
        if value < 70:
            return "#f59e0b"
        return "#ef4444"


def build_tier_label(value, positive=True):
    if positive:
        if value >= 80:
            return "Excellent"
        if value >= 50:
            return "Good"
        return "Improving"
    else:
        if value < 35:
            return "Normal"
        if value < 70:
            return "Elevated"
        return "High"


def build_gauge_figure(value, title, min_value=0, max_value=100, unit="%", bar_color="#38bdf8"):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            number={"suffix": unit, "font": {"size": 24, "color": "#f8fbff"}},
            title={"text": title, "font": {"size": 18, "color": "#f8fbff"}},
            gauge={
                "axis": {"range": [min_value, max_value], "tickcolor": "#dbeafe"},
                "bar": {"color": bar_color, "thickness": 0.28},
                "steps": [
                    {"range": [min_value, max_value * 0.6], "color": "rgba(34,197,94,0.22)"},
                    {"range": [max_value * 0.6, max_value * 0.85], "color": "rgba(251,146,60,0.22)"},
                    {"range": [max_value * 0.85, max_value], "color": "rgba(239,68,68,0.22)"},
                ],
                "threshold": {
                    "line": {"color": "#f8fbff", "width": 4},
                    "thickness": 0.75,
                    "value": value,
                },
                "bordercolor": "rgba(255,255,255,0.12)",
                "borderwidth": 1,
            },
            domain={"x": [0, 1], "y": [0, 1]},
        )
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=40, b=10),
        font=dict(color="#f8fbff", family="Inter, Arial, sans-serif"),
        height=330,
    )
    return fig


# -------------------------------------------------

# LOAD DATA

# -------------------------------------------------

file_id = "1KGxmg3v9gKpenoav7ItSGjHdQQ0H5Nne"

url = f"https://drive.google.com/uc?id={file_id}"
@st.cache_data
def load_data():
    return pd.read_csv(url)

df = load_data()


st.sidebar.success("☁️ Cloud Connected")
# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("🧬 GuardianTwin")
st.sidebar.markdown("**Patient Monitoring Dashboard**")

patients = sorted(df["deviceId"].unique())
selected_patient = st.sidebar.selectbox("Select Patient", patients)

patient_data = df[df["deviceId"] == selected_patient]
patient_data = patient_data.sort_values("date")

# Automatic replay always ON

refresh_counter = st_autorefresh(
    interval=1000,
    limit=None,
    key="guardian_refresh"
)




if "last_patient" not in st.session_state or st.session_state.last_patient != selected_patient:
    st.session_state.last_patient = selected_patient
    st.session_state.replay_index = 1

if "replay_index" not in st.session_state:
    st.session_state.replay_index = 1



st.sidebar.markdown("---")
st.sidebar.subheader("Active Monitoring Models")
st.sidebar.success("✓ Sleep Predictor")
st.sidebar.success("✓ Anomaly Detector")
st.sidebar.success("✓ Health Risk")
st.sidebar.markdown("---")
st.sidebar.caption("GuardianTwin replays the patient timeline automatically in live mode.")

# -------------------------------------------------

# PATIENT DATA

# -------------------------------------------------

if st.session_state.replay_index < len(patient_data):
    st.session_state.replay_index += 1
else:
    st.session_state.replay_index = 1

display_data = patient_data.head(
    st.session_state.replay_index
)

latest = display_data.iloc[-1]
st.session_state.latest_data = latest

# ----------------------------------
# CLEAN SEVERITY LABELS
# ----------------------------------

display_data["severity_label"] = (
    display_data["severity_label"]
    .fillna("Normal")
    .replace("undefined", "Normal")
)
# ----------------------------------
# PATIENT STATUS CONFIG
# ----------------------------------

severity_config = {
    "Emergency": {"status": "🚨 CRITICAL", "color": "#ffffff", "bg": "#b91c1c"},
    "Urgent": {"status": "🔴 HIGH RISK", "color": "#ffffff", "bg": "#ef4444"},
    "Caution": {"status": "🟠 CAUTION", "color": "#ffffff", "bg": "#f59e0b"},
    "Watch": {"status": "🟡 WATCH", "color": "#111827", "bg": "#facc15"},
    "Normal": {"status": "🟢 STABLE", "color": "#ffffff", "bg": "#22c55e"},
}

patient_theme = severity_config.get(latest["severity_label"], severity_config["Normal"])
# -------------------------------------------------

# MAIN HEADER

# -------------------------------------------------

st.title("🏥 GuardianTwin | GPREC")
st.caption("Wearable-Based Digital Twin for Patient Monitoring")

# -------------------------------------------------

# TABS

# -------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "🏥 Patient Overview",
        "Digital Twin",
        "ML Insights",
        "Event Log",
    ]
)


# =================================================

# CAREGIVER VIEW

# =================================================

# =================================================
# CAREGIVER VIEW
# =================================================

with tab1:

    st.header("Patient Caregiver Dashboard")

    # ==================================
    # AI RISK EXPLANATION
    # ==================================

    deviations = {
        "Heart Rate": round(
            ((latest["HR"] - latest["HR_mean"]) / latest["HR_mean"]) * 100,
            1,
        ),
        "Sleep": round(
            ((latest["sleep_duration"] - latest["sleep_mean"]) / latest["sleep_mean"])
            * 100,
            1,
        ),
        "RMSSD": round(
            ((latest["rmssd"] - latest["rmssd_mean"]) / latest["rmssd_mean"]) * 100,
            1,
        ),
        "SDNN": round(
            ((latest["sdnn"] - latest["sdnn_mean"]) / latest["sdnn_mean"]) * 100,
            1,
        ),
    }

    affected_metrics = [
        (metric, value) for metric, value in deviations.items() if abs(value) >= 10
    ]

    affected_metrics = sorted(
        affected_metrics,
        key=lambda x: abs(x[1]),
        reverse=True,
    )

    # ==================================
    # PRIMARY RISK DRIVER
    # ==================================

    if affected_metrics:
        top_metric = affected_metrics[0][0]
        risk_driver_map = {
            "Heart Rate": "Elevated Cardiac Stress",
            "Sleep": "Sleep Deprivation",
            "RMSSD": "Autonomic Recovery Imbalance",
            "SDNN": "Reduced Heart Rate Variability",
        }
        primary_risk_driver = risk_driver_map.get(top_metric, "Physiological Deviation")
        explanation_lines = []
        for i, (metric, value) in enumerate(affected_metrics, start=1):
            direction = "above baseline" if value > 0 else "below baseline"
            explanation_lines.append(f"{i}. {metric}: {abs(value):.1f}% {direction}")
        explanation = "\n".join(explanation_lines)
    else:
        primary_risk_driver = "No Significant Risk Driver"
        explanation = "All monitored metrics are within expected baseline ranges."

    risk_probability = round(latest["risk_probability"], 1)
    risk_category = build_tier_label(risk_probability, positive=False)
    risk_color = build_tier_color(risk_probability, positive=False)

    st.markdown(
        f"""
        <div class="hero-panel">
            <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:1rem;">
                <div>
                    <div class="hero-badge">🛰️ GuardianTwin Active Monitoring</div>
                    <h1>Patient {selected_patient} Overview</h1>
                    <p>Immersive health insights, trend visualization, and care recommendations for the selected digital twin.</p>
                    <div style="display:inline-flex; align-items:center; gap:8px; margin-top:16px;">
                        <span style="display:inline-block; padding:8px 14px; border-radius:999px; border:1px solid {risk_color}; background:rgba(255,255,255,0.08); color:{risk_color}; font-weight:700;">{risk_category} Risk</span>
                        <span style="color:#e2e8f0;">{risk_probability}% probability</span>
                    </div>
                </div>
                <div style="display:grid; gap:14px; grid-template-columns: repeat(2, minmax(160px, 1fr)); width:min(520px,100%);">
                    <div style="background: {patient_theme['bg']}; border-radius: 18px; padding: 18px; border:1px solid {patient_theme['color']}; color: {patient_theme['color']}; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.08);">
                        <div style="opacity: 1; font-size: 0.92rem;">Current Severity</div>
                        <div style="font-size: 1.5rem; font-weight: 700; margin: 0.65rem 0; color: {patient_theme['color']}; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">{latest['severity_label']}</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.12); border-radius: 18px; padding: 18px; border:1px solid rgba(255,255,255,0.16);">
                        <div style="opacity: 0.8; font-size: 0.92rem;">Risk Probability</div>
                        <div style="font-size: 1.5rem; font-weight: 700; margin: 0.65rem 0;">{round(latest['risk_probability'],1)}%</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.12); border-radius: 18px; padding: 18px; border:1px solid rgba(255,255,255,0.16);">
                        <div style="opacity: 0.8; font-size: 0.92rem;">Active Models</div>
                        <div style="font-size: 1.5rem; font-weight: 700; margin: 0.65rem 0;">3 monitoring engines</div>
                    </div>
                    <div style="background: rgba(255,255,255,0.12); border-radius: 18px; padding: 18px; border:1px solid rgba(255,255,255,0.16);">
                        <div style="opacity: 0.8; font-size: 0.92rem;">Latest Record</div>
                        <div style="font-size: 1.5rem; font-weight: 700; margin: 0.65rem 0;">{latest['date']}</div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    

    st.markdown("---")

    health_score = round(100 - latest["risk_probability"], 1)
    activity_dev = round(
        (
            (latest["daily_steps"] - latest["steps_mean"]) / max(latest["steps_mean"], 1)
        )
        * 100,
        1,
    )

    fall_caption = "Movement stable"
    if latest["fall_risk"] == "High":
        fall_caption = "Immediate attention"
    elif latest["fall_risk"] == "Moderate":
        fall_caption = "Monitor mobility"

    stress_score = (
    abs(((latest["HR"] - latest["HR_mean"]) / latest["HR_mean"]) * 100)
    +
    abs(((latest["rmssd"] - latest["rmssd_mean"]) / latest["rmssd_mean"]) * 100)
    +
    abs(((latest["sdnn"] - latest["sdnn_mean"]) / latest["sdnn_mean"]) * 100)
) / 3

    if stress_score < 10:
        stress_level = "Low"
    elif stress_score < 25:
        stress_level = "Moderate"
    else:
        stress_level = "High"

    card_cols = st.columns(5)
    metrics = [
    ("⚠ Anomalies", int(latest["anomaly_count"]), "Detected by anomaly engine"),
    ("💚 Health Stability", f"{health_score}/100", "Digital Twin Health Index"),
    ("🚶 Daily Steps", int(latest["daily_steps"]), f"{int(latest['daily_steps']-latest['steps_mean']):+} steps"),
    ("😟 Stress", stress_level, "Stress monitoring"),
    ("🚨 Fall Risk", latest["fall_risk"], fall_caption),
]

    for column, (title, value, subtitle) in zip(card_cols, metrics):
        column.markdown(
            f"""
            <div class="glass-card" style="padding: 20px; min-height: 148px;">
                <div style="font-size:1rem; opacity:0.8;">{title}</div>
                <div style="font-size:2rem; font-weight:700; margin: 0.65rem 0;">{value}</div>
                <div style="opacity:0.78; line-height:1.6;">{subtitle}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    gauge_col1, gauge_col2 = st.columns(2)
    health_score = round(100 - latest['risk_probability'], 1)
    risk_gauge = build_gauge_figure(
        round(latest['risk_probability'], 1),
        'Risk Probability',
        bar_color=build_tier_color(round(latest['risk_probability'], 1), positive=False),
    )
    health_gauge = build_gauge_figure(
        health_score,
        'Health Stability',
        bar_color=build_tier_color(health_score, positive=True),
    )
    gauge_col1.plotly_chart(risk_gauge, width='stretch')
    gauge_col2.plotly_chart(health_gauge, width='stretch')

    st.markdown("---")

    # --------------------------------------
    # DIGITAL TWIN COMPARISON
    # --------------------------------------

    st.subheader("Digital Twin Comparison")
    
    st.subheader("🧠 Health Summary")

    anomaly_explanations = []

    # Heart Rate
    if latest["HR_anom"] == 1:

        hr_dev = round(
            ((latest["HR"] - latest["HR_mean"]) / latest["HR_mean"]) * 100,
            1
        )

        anomaly_explanations.append(
            f"❤️ Heart Rate is {abs(hr_dev)}% "
            f"{'above' if hr_dev > 0 else 'below'} baseline."
        )

    # Sleep
    if latest["sleep_anom"] == 1:

        sleep_dev = round(
            ((latest["sleep_duration"] - latest["sleep_mean"])
             / latest["sleep_mean"]) * 100,
            1
        )

        anomaly_explanations.append(
            f"😴 Sleep duration is {abs(sleep_dev)}% "
            f"{'above' if sleep_dev > 0 else 'below'} normal."
        )

    # RMSSD
    if latest["rmssd_anom"] == 1:

        rmssd_dev = round(
            ((latest["rmssd"] - latest["rmssd_mean"])
             / latest["rmssd_mean"]) * 100,
            1
        )

        anomaly_explanations.append(
            f"🫀 RMSSD deviated by {abs(rmssd_dev)}% from baseline."
        )

    # SDNN
    if latest["sdnn_anom"] == 1:

        sdnn_dev = round(
            ((latest["sdnn"] - latest["sdnn_mean"])
             / latest["sdnn_mean"]) * 100,
            1
        )

        anomaly_explanations.append(
            f"📈 SDNN deviated by {abs(sdnn_dev)}% from baseline."
        )

    # Activity
    if latest["steps_anom"] == 1:

        steps_dev = round(
            ((latest["daily_steps"] - latest["steps_mean"])
             / max(latest["steps_mean"], 1)) * 100,
            1
        )

        anomaly_explanations.append(
            f"🚶 Physical activity is {abs(steps_dev)}% "
            f"{'above' if steps_dev > 0 else 'below'} normal."
        )

    # Fall Risk
    if str(latest["fall_risk"]).lower() != "low":

        anomaly_explanations.append(
            f"⚠ {latest['fall_risk']} fall risk detected."
        )

    # ------------------------------------
    # FINAL AI SUMMARY
    # ------------------------------------

    if int(latest["anomaly_count"]) == 0:

        clinical_summary = """
✅ Patient is currently stable.

All monitored physiological indicators are within
expected baseline ranges.

No anomalies were detected by the monitoring system.
"""

        recommendation = """
Continue routine monitoring and maintain
current lifestyle patterns.
"""

    else:

        clinical_summary = "\n\n".join(anomaly_explanations)

        recommendation = latest["recommendation"]

    st.info(f"""
### Current Condition

{clinical_summary}

### Recommendation

{recommendation}
""")
    hr_dev = round(
    ((latest["HR"] - latest["HR_mean"])
     / latest["HR_mean"]) * 100,
    1
)

    sleep_dev = round(
    ((latest["sleep_duration"] - latest["sleep_mean"])
     / latest["sleep_mean"]) * 100,
    1
)

    activity_dev = round(
    ((latest["daily_steps"] - latest["steps_mean"])
     / max(latest["steps_mean"], 1)) * 100,
    1
)

    col1, col2 = st.columns(2)

    with col1:
        if abs(hr_dev) < 10:
            hr_status = "🟢 Normal"
        elif abs(hr_dev) < 20:
            hr_status = "🟡 Mild Change"
        else:
            hr_status = "🔴 Significant Change"

        st.markdown("### ❤️ Heart Activity")
        st.write(f"Current : {round(latest['HR'],1)} bpm")
        st.write(f"Baseline : {round(latest['HR_mean'],1)} bpm")
        st.write(f"Deviation : {hr_dev:+.1f}%")

        if abs(hr_dev) < 10:
            st.success("Heart activity remains within normal physiological limits.")
        elif hr_dev > 0:
            st.warning("Elevated heart activity compared to baseline.")
        else:
            st.warning("Reduced heart activity compared to baseline.")

        st.markdown("### 😴 Sleep")
        sleep_diff = round(
        latest["sleep_duration"] -
        latest["sleep_mean"],
        2
        )

        st.write(f"Current : {round(latest['sleep_duration'],2)} hrs")
        st.write(f"Baseline : {round(latest['sleep_mean'],2)} hrs")
        st.write(f"Difference : {sleep_diff:+.2f} hrs")

        if sleep_diff > 1:
            st.success("Sleep duration exceeded normal recovery requirements.")
        elif sleep_diff < -1:
            st.warning("Sleep duration is below expected recovery levels.")
        else:
            st.success("Sleep duration remains near baseline.")

        st.markdown("### 🚶 Activity")

        step_difference = int(
        latest["daily_steps"] -
        latest["steps_mean"]
    )

        st.write(
        f"Current : {int(latest['daily_steps'])} steps"
    )

        st.write(
        f"Baseline : {int(latest['steps_mean'])} steps"
    )

        st.write(
        f"Difference : {step_difference:+} steps"
    )

        if step_difference > 1000:

            st.success(
            "Activity level significantly exceeded baseline."
        )

        elif step_difference > 0:

            st.success(
            "Activity level slightly exceeded baseline."
        )

        elif step_difference > -1000:

            st.warning(
            "Activity level slightly below baseline."
        )

        else:

            st.warning(
            "Reduced mobility detected."
        )

    with col2:
        st.markdown("### 🫀 RMSSD")
        rmssd_diff = round(
        latest["rmssd"] -
        latest["rmssd_mean"],
        1
    )

        st.write(f"Current : {round(latest['rmssd'],1)}")
        st.write(f"Baseline : {round(latest['rmssd_mean'],1)}")
        st.write(f"Difference : {rmssd_diff:+.1f}")

        if rmssd_diff >= 0:
            st.success(
        "Recovery capacity remains healthy."
        )
        else:
            st.warning(
            "Recovery capacity below normal baseline."
        )
            
        st.markdown("### 📈 SDNN")
        sdnn_diff = round(
        latest["sdnn"] -
        latest["sdnn_mean"],
        1
    )

        st.write(f"Current : {round(latest['sdnn'],1)}")
        st.write(f"Baseline : {round(latest['sdnn_mean'],1)}")
        st.write(f"Difference : {sdnn_diff:+.1f}")

        if sdnn_diff >= 0:
            st.success(
            "Autonomic balance remains stable."
        )
        else:
            st.warning(
        "Reduced heart-rate variability detected."
        )

        st.markdown("### 🚨 Fall Risk")
        risk = str(latest["fall_risk"])

        st.write(
            f"Current Risk : {risk}"
        )

        if risk == "Low":

            st.success(
        "Stable mobility patterns detected."
    )

        elif risk == "Moderate":

            st.warning(
        "Moderate instability detected. Monitor movement carefully."
    )

        else:

            st.error(
        "High fall risk. Additional supervision recommended."
    )

    st.markdown("---")

    # --------------------------------------
    # GUIDANCE PANEL
    # --------------------------------------

    st.subheader("Caregiver Guidance")

    if primary_risk_driver == "Sleep Deprivation":
        guidance = """
😴 Sleep Recovery Focus

• Improve sleep consistency

• Monitor recovery patterns

• Reduce late-night stimulation

• Track sleep duration trends
"""
    elif primary_risk_driver == "Elevated Cardiac Stress":
        guidance = """
❤️ Cardiovascular Monitoring

• Monitor heart rate fluctuations

• Review physical activity levels

• Reduce excessive exertion

• Increase observation frequency
"""
    elif primary_risk_driver == "Autonomic Recovery Imbalance":
        guidance = """
🫀 Recovery Assessment

• Review HRV recovery patterns

• Encourage adequate recovery periods

• Monitor fatigue indicators

• Track RMSSD changes
"""
    elif primary_risk_driver == "Reduced Heart Rate Variability":
        guidance = """
📈 Variability Monitoring

• Observe stress levels

• Monitor SDNN trends

• Assess overall physiological stability

• Continue close monitoring
"""
    else:
        guidance = """
✅ Stable Condition

• Continue routine monitoring

• Maintain healthy lifestyle habits

• No immediate concerns detected
"""

    st.success(guidance)
    st.markdown("---")
    st.markdown("---")

with tab2:

    st.header("Digital Twin Explorer")

    hr_diff = round(latest["HR"] - latest["HR_mean"], 1)
    sleep_diff = round(latest["sleep_duration"] - latest["sleep_mean"], 2)
    steps_diff = int(latest["daily_steps"] - latest["steps_mean"])

    summary_cols = st.columns(3)
    summary_metrics = [
        ("❤️ Heart Rate", f"{round(latest['HR'],1)} bpm", f"{hr_diff:+.1f} vs baseline"),
        ("😴 Sleep", f"{round(latest['sleep_duration'],2)} hrs", f"{sleep_diff:+.2f} hrs"),
        ("🚶 Activity", f"{int(latest['daily_steps'])} steps", f"{steps_diff:+d} vs baseline"),
    ]

    for column, (label, value, delta) in zip(summary_cols, summary_metrics):
        column.markdown(
            f"""
            <div class="glass-card" style="padding: 22px; min-height: 135px;">
                <div style="opacity:0.78; font-size:0.95rem; margin-bottom:0.65rem;">{label}</div>
                <div style="font-size:1.7rem; font-weight:700; margin-bottom:0.5rem;">{value}</div>
                <div style="color: #dbeafe;">{delta}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    # HEART RATE

    with col1:

        fig_hr = go.Figure()

        fig_hr.add_trace(
            go.Scatter(
                x=display_data["date"],
                y=display_data["HR"],
                mode="lines+markers",
                name="Current HR",
            )
        )

        fig_hr.add_trace(
            go.Scatter(
                x=display_data["date"],
                y=display_data["HR_mean"],
                mode="lines+markers",
                name="Baseline HR",
            )
        )

        fig_hr.update_layout(title="Heart Rate vs Baseline")
        fig_hr.update_traces(
            selector=dict(name="Current HR"),
            line=dict(color="#fb7185", width=3),
            marker=dict(size=6),
        )
        fig_hr.update_traces(
            selector=dict(name="Baseline HR"),
            line=dict(color="#60a5fa", width=3, dash="dash"),
            marker=dict(size=6),
        )
        apply_plotly_theme(fig_hr)

        st.plotly_chart(fig_hr, width='stretch')

    # SLEEP

    with col2:

        fig_sleep = go.Figure()

        fig_sleep.add_trace(
            go.Scatter(
                x=display_data["date"],
                y=display_data["sleep_duration"],
                name="Current Sleep",
            )
        )

        fig_sleep.add_trace(
            go.Scatter(
                x=display_data["date"],
                y=display_data["sleep_mean"],
                name="Baseline Sleep",
            )
        )

        fig_sleep.update_layout(title="Sleep Duration vs Baseline")
        fig_sleep.update_traces(
            selector=dict(name="Current Sleep"),
            line=dict(color="#34d399", width=3),
            marker=dict(size=6),
        )
        fig_sleep.update_traces(
            selector=dict(name="Baseline Sleep"),
            line=dict(color="#818cf8", width=3, dash="dash"),
            marker=dict(size=6),
        )
        apply_plotly_theme(fig_sleep)

        st.plotly_chart(fig_sleep, width='stretch')

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:

        fig_rmssd = go.Figure()

        fig_rmssd.add_trace(
            go.Scatter(
                x=display_data["date"], y=display_data["rmssd"], name="Current RMSSD"
            )
        )

        fig_rmssd.add_trace(
            go.Scatter(
                x=display_data["date"],
                y=display_data["rmssd_mean"],
                name="Baseline RMSSD",
            )
        )

        fig_rmssd.update_layout(title="RMSSD Recovery Trend")
        fig_rmssd.update_traces(
            selector=dict(name="Current RMSSD"),
            line=dict(color="#f472b6", width=3),
            marker=dict(size=6),
        )
        fig_rmssd.update_traces(
            selector=dict(name="Baseline RMSSD"),
            line=dict(color="#38bdf8", width=3, dash="dash"),
            marker=dict(size=6),
        )
        apply_plotly_theme(fig_rmssd)

        st.plotly_chart(fig_rmssd, width='stretch')

    with col4:

        fig_sdnn = go.Figure()

        fig_sdnn.add_trace(
            go.Scatter(
                x=display_data["date"], y=display_data["sdnn"], name="Current SDNN"
            )
        )

        fig_sdnn.add_trace(
            go.Scatter(
                x=display_data["date"],
                y=display_data["sdnn_mean"],
                name="Baseline SDNN",
            )
        )

        fig_sdnn.update_layout(title="SDNN Trend")
        fig_sdnn.update_traces(
            selector=dict(name="Current SDNN"),
            line=dict(color="#38bdf8", width=3),
            marker=dict(size=6),
        )
        fig_sdnn.update_traces(
            selector=dict(name="Baseline SDNN"),
            line=dict(color="#fbbf24", width=3, dash="dash"),
            marker=dict(size=6),
        )
        apply_plotly_theme(fig_sdnn)

        st.plotly_chart(fig_sdnn, width='stretch')
    st.markdown("---")

    col5, col6 = st.columns(2)

    with col5:

        fig_steps = go.Figure()

        fig_steps.add_trace(
            go.Scatter(
                x=display_data["date"],
                y=display_data["daily_steps"],
                mode="lines+markers",
                name="Current Steps",
            )
        )

        fig_steps.add_trace(
            go.Scatter(
                x=display_data["date"],
                y=display_data["steps_mean"],
                mode="lines+markers",
                name="Baseline Steps",
            )
        )

        fig_steps.update_layout(title="Steps vs Baseline")

        fig_steps.update_traces(
            selector=dict(name="Current Steps"), line=dict(width=3), marker=dict(size=6)
        )

        fig_steps.update_traces(
            selector=dict(name="Baseline Steps"),
            line=dict(width=3, dash="dash"),
            marker=dict(size=6),
        )

        apply_plotly_theme(fig_steps)

        st.plotly_chart(fig_steps, width='stretch')

    with col6:

        stress_series = (
        abs(
            (display_data["HR"] - display_data["HR_mean"])
            / display_data["HR_mean"] * 100
        )
        +
        abs(
            (display_data["rmssd"] - display_data["rmssd_mean"])
            / display_data["rmssd_mean"] * 100
        )
        +
        abs(
            (display_data["sdnn"] - display_data["sdnn_mean"])
            / display_data["sdnn_mean"] * 100
        )
    ) / 3

        fig_stress = go.Figure()

        fig_stress.add_trace(
        go.Scatter(
            x=display_data["date"],
            y=stress_series,
            mode="lines+markers",
            name="Stress Index"
        )
    )

        fig_stress.update_layout(
        title="Stress Trend"
    )

        apply_plotly_theme(fig_stress)

        st.plotly_chart(
        fig_stress,
        width="stretch"
    )
# =================================================
# ML INSIGHTS
# =================================================

with tab3:

    st.header("Health Insights")

    # -------------------------
    # KPI CARDS
    # -------------------------

    risk_pct = int(min(latest["risk_probability"], 100))

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Risk Score", round(latest["risk_score"], 2))

    c2.metric("Risk Probability", f"{round(latest['risk_probability'],1)}%")

    c3.metric("Risk Level", latest["risk_level"])

    c4.metric("Anomaly Count", int(latest["anomaly_count"]))

    st.markdown("---")

    

    insight_g1, insight_g2 = st.columns(2)
    risk_pct = int(min(latest["risk_probability"], 100))
    anomaly_impact = min(int(latest["anomaly_count"] * 16), 100)
    insight_g1.plotly_chart(
        build_gauge_figure(
            risk_pct,
            "Risk Probability",
            bar_color=build_tier_color(risk_pct, positive=False),
        ),
        width='stretch',
    )
    insight_g2.plotly_chart(
        build_gauge_figure(
            anomaly_impact,
            "Anomaly Impact",
            bar_color=build_tier_color(anomaly_impact, positive=False),
        ),
        width='stretch',
    )

    st.markdown("---")
    
    st.info(f"""
### AI Model Summary

• Primary Risk Driver: {primary_risk_driver}

• Current Severity: {latest['severity_label']}

• Risk Probability: {round(latest['risk_probability'],1)}%

• Detected Anomalies: {int(latest['anomaly_count'])}

• Current Status: {build_tier_label(risk_pct, positive=False)}
""")

    # -------------------------
    # AI INTERPRETATION
    # -------------------------

    st.markdown("---")

    # -------------------------
    # RISK PROBABILITY BAR
    # -------------------------

    st.subheader("Risk Probability")

    risk_pct = int(min(latest["risk_probability"], 100))

    st.progress(risk_pct)

    st.write(f"Estimated Risk Probability: {risk_pct}%")

    st.markdown("---")

    # -------------------------
    # SEVERITY DISTRIBUTION
    # -------------------------

    st.subheader("Severity Distribution for Selected Patient")
    
    
    col_chart, col_info = st.columns([2, 1])
    
    with col_chart:
        severity_counts = (
        display_data.tail(50)["severity_label"]
    .value_counts()
    )
        
        fig_severity = go.Figure(
            data=[
                go.Pie(
                    labels=severity_counts.index,
                    values=severity_counts.values,
                    hole=0.5,
                    marker=dict(line=dict(color="#081526", width=2)),
                    textinfo="percent+label",
                    textfont=dict(color="#f8fbff"),
                )
            ]
        )

        fig_severity.update_layout(
        height=450,
        title_text=""
        )
        apply_plotly_theme(fig_severity)

        st.plotly_chart(fig_severity, width='stretch')
    
    with col_info:
        st.markdown("""
        ### 📊 What This Shows
        
        This chart displays the **timeline breakdown** of this patient's health status over the selected time period.
        
        Each slice represents how frequently the patient was in each severity level:
        
        🟢 **Normal** – Stable, healthy readings
        
        🟡 **Watch** – Minor deviations, routine monitoring
        
        🟠 **Caution** – Moderate concern, increased observation
        
        🔴 **Urgent** – High risk, immediate attention needed
        
        🚨 **Emergency** – Critical status, urgent intervention
        
        **Higher percentages** indicate the patient spent more time at that severity level.
        """)

    st.markdown("---")

    # -------------------------
    # RISK TREND
    # -------------------------

    st.subheader("Risk Trend")

    fig_risk = go.Figure()

    fig_risk.add_trace(
        go.Scatter(
            x=display_data["date"],
            y=display_data["risk_score"],
            mode="lines+markers",
            name="Risk Score",
            line=dict(color="#fb7185", width=3),
            marker=dict(size=6, color="#f8fbff", line=dict(color="#fb7185", width=1)),
        )
    )

    fig_risk.update_layout(
        title="Risk Score Across Time",
        xaxis_title="Date",
        yaxis_title="Risk Score",
    )
    apply_plotly_theme(fig_risk)

    st.plotly_chart(fig_risk, width='stretch')
    st.markdown("---")
    st.subheader("Severity Evolution")

    severity_map = {"Normal": 1, "Watch": 2, "Caution": 3, "Urgent": 4, "Emergency": 5}

    severity_reverse = {
        1: "Normal",
        2: "Watch",
        3: "Caution",
        4: "Urgent",
        5: "Emergency",
    }

    severity_data = display_data.copy()

    severity_data["severity_numeric"] = severity_data["severity_label"].map(
        severity_map
    )

    fig_severity_timeline = go.Figure()

    fig_severity_timeline.add_trace(
        go.Scatter(
            x=severity_data["date"],
            y=severity_data["severity_numeric"],
            mode="lines+markers",
            name="Severity",
        )
    )

    fig_severity_timeline.update_layout(
        title="Severity Progression",
        yaxis=dict(
            tickmode="array",
            tickvals=[1, 2, 3, 4, 5],
            ticktext=["Normal", "Watch", "Caution", "Urgent", "Emergency"],
        ),
    )

    apply_plotly_theme(fig_severity_timeline)

    st.plotly_chart(fig_severity_timeline, width='stretch')

# =================================================
# EVENT LOG
# =================================================

with tab4:

    st.header("Patient Event Timeline")

    color_map = {
        "Normal": "🟢",
        "Watch": "🟡",
        "Caution": "🟠",
        "Urgent": "🔴",
        "Emergency": "🚨",
    }

    timeline_data = display_data.tail(10)[
    ["date", "severity_label", "recommendation", "anomaly_count"]
    ].sort_values("date", ascending=False)

    for _, row in timeline_data.iterrows():
        icon = color_map.get(row["severity_label"], "⚪")
        st.markdown(
            f"""
            <div class="timeline-entry">
                <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.9rem;">
                    <span style="font-size:1.35rem;">{icon}</span>
                    <h3 style="margin:0;">{row['date']}</h3>
                </div>
                <p><strong>Severity:</strong> {row['severity_label']}</p>
                <p><strong>Anomaly Count:</strong> {row['anomaly_count']}</p>
                <p><strong>Recommendation:</strong> {row['recommendation']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
