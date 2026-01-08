import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# Page Configuration
st.set_page_config(
    layout="wide",
    page_title="The Wealth Blueprint",
    page_icon="📊",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Dark Theme Professional Dashboard
st.markdown("""
    <style>
    /* Import Professional Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Styling */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background-color: #000000;
    }
    
    /* Main Container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* Header */
    .app-header {
        background: linear-gradient(135deg, #000000 0%, #7f1d1d 100%);
        border: 1px solid #dc2626;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);
    }
    
    .app-title {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .app-subtitle {
        color: #e0e7ff;
        font-size: 1.6rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    /* Section Cards (Black with Red Border) */
    .section-card {
        background-color: #0f0f0f; /* Very dark grey, almost black */
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid #7f1d1d; /* Dark Red border */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }
    
    .section-title {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        padding-bottom: 0.8rem;
        border-bottom: 2px solid #333333;
        border-left: 5px solid #dc2626; /* The Vertical Red Line */
        padding-left: 1.5rem; /* Added Space between line and text */
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid #3b82f6; /* <--- The Red Border */
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: #7f1d1d; /* <--- Brighter Red on Hover */
        box-shadow: 0 4px 16px rgba(220, 38, 38, 0.2); /* Red Glow */
        transform: translateY(-2px);
    }
    
    .metric-label {
        color: #ffffff;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.8rem;
    }
    
    .metric-value {
        color: #ffffff;
        text-shadow: 0 0 10px rgba (220, 38, 38, 0.6);
        font-size: 2rem;
        font-weight: 700;
        margin: 0.3rem 0;
    }
    
    .metric-subtitle {
        color: #64748b;
        font-size: 0.75rem;
        margin-top: 0.5rem;
    }
    
    /* Input Labels */
    .input-label {
        color: #ffffff;
        font-size: 0.9rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .input-value {
        color: #3b82f6;
        font-size: 1.1rem;
        font-weight: 700;
        margin-top: 0.3rem;
    }
    
    /* Risk Profile Buttons */
    .risk-button {
        background-color: #1e293b;
        border: 2px solid #475569;
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 0.5rem;
    }
    
    .risk-button:hover {
        border-color: #3b82f6;
        background-color: #334155;
    }
    
    .risk-button.active {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        border-color: #ef4444;
    }
    
    .risk-button-label {
        color: #ffffff;
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    /* Slider Customization */
    .stSlider > div > div > div {
        background-color: #1e293b;
    }
    
    .stSlider > div > div > div > div {
        background-color: #3b82f6;
    }
    
    /* Number Input */
    .stNumberInput > div > div > input {
        background-color: #1e293b;
        color: #ffffff;
        border: 1px solid #475569;
        border-radius: 6px;
    }
    
    /* Toggle Switch */
    .stCheckbox > label {
        color: #e2e8f0;
        font-weight: 600;
    }
    
    /* Summary Box */
    .summary-box {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 2rem 0;
        border-left: 4px solid #dc2626;
    }
    
    .summary-text {
        color: #e0e7ff;
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 0;
    }
    
   /* Tab Styling - Updated for Bigger & Bold Text */
    /* FORCE Tab Styling - Bigger & Bold */
    button[data-baseweb="tab"] {
        padding: 1rem 2rem !important;
    }
    
    button[data-baseweb="tab"] div p {
        font-size: 1.3rem !important; /* Much Bigger */
        font-weight: 700 !important;  /* Extra Bold */
        color: #e2e8f0 !important;    /* Light Grey Text */
    }
    
    /* Active Tab Text Color (White) */
    button[aria-selected="true"] div p {
        color: #ffffff !important;
    }
    
    /* DataFrame Styling */
    .dataframe {
        background-color: #1e293b !important;
        color: #e2e8f0 !important;
    }
    
    /* Download Button */
    .stDownloadButton > button {
        background-color: #000000;
        color: #ffffff;
        border: 1px solid #dc2626;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        width: 100%;
    }
    
    .stDownloadButton > button:hover {
        background-color: #2563eb;
    }

    /* Increase Size of Slider Value (The floating number on the handle) */
    div[data-testid="stThumbValue"] {
        font-size: 1.8rem !important; 
        font-weight: 800 !important;
        padding-bottom: 5px !important; 
    }
    </style>
""", unsafe_allow_html=True)

# Financial Constants
# Updated Strategic Asset Allocation Framework 
RISK_PROFILES = {
    "Conservative": {
        "allocations": {
            "Debt MF": 60, "Gold ETF": 10,          # Defensive
            "Large Cap": 20,                        # Core Equity
            "Mid Cap": 10, "Small Cap": 0           # Alpha Generators
        },
        "returns": {
            "Debt MF": 0.07, "Gold ETF": 0.11,
            "Large Cap": 0.13,
            "Mid Cap": 0.15, "Small Cap": 0.18
        }
    },
    "Balanced": {
        "allocations": {
            "Debt MF": 30, "Gold ETF": 10,
            "Large Cap": 30,
            "Mid Cap": 20, "Small Cap": 10
        },
        "returns": {
            "Debt MF": 0.075, "Gold ETF": 0.11,
            "Large Cap": 0.135,
            "Mid Cap": 0.16, "Small Cap": 0.19
        }
    },
    "Aggressive": {
        "allocations": {
            "Debt MF": 10, "Gold ETF": 5,
            "Large Cap": 25,
            "Mid Cap": 30, "Small Cap": 30
        },
        "returns": {
            "Debt MF": 0.08, "Gold ETF": 0.11,
            "Large Cap": 0.14,
            "Mid Cap": 0.18, "Small Cap": 0.22
        }
    }
}
LTCG_TAX_RATE = 0.125
LTCG_EXEMPTION = 125000

# Helper Functions
def calculate_stepup_sip(initial_sip, tenure_years, stepup_rate, monthly_rate):
    """Calculate Step-up SIP with monthly compounding"""
    months = tenure_years * 12
    stepup_monthly_rate = stepup_rate / 100
    
    data = []
    total_invested = 0
    current_wealth = 0
    current_sip = initial_sip
    
    for month in range(1, months + 1):
        # Annual step-up
        if month > 1 and (month - 1) % 12 == 0:
            current_sip = current_sip * (1 + stepup_monthly_rate)
        
        total_invested += current_sip
        current_wealth = (current_wealth + current_sip) * (1 + monthly_rate)
        
        data.append({
            'Month': month,
            'Year': month / 12,
            'SIP_Amount': current_sip,
            'Total_Invested': total_invested,
            'Current_Wealth': current_wealth,
            'Returns': current_wealth - total_invested
        })
    
    return pd.DataFrame(data)

def calculate_inflation_adjusted(future_value, inflation_rate, years):
    """Calculate real purchasing power"""
    return future_value / ((1 + inflation_rate/100) ** years)

def calculate_ltcg_tax(gains):
    """Calculate LTCG tax"""
    if gains <= LTCG_EXEMPTION:
        return 0
    return (gains - LTCG_EXEMPTION) * LTCG_TAX_RATE

def years_to_reach_goal(target, current_sip, stepup_rate, monthly_return):
    """Calculate years needed to reach financial goal"""
    current_wealth = 0
    months = 0
    sip = current_sip
    max_months = 50 * 12
    
    while current_wealth < target and months < max_months:
        months += 1
        if months > 1 and (months - 1) % 12 == 0:
            sip = sip * (1 + stepup_rate/100)
        current_wealth = (current_wealth + sip) * (1 + monthly_return)
    
    return months / 12 if current_wealth >= target else None

# Initialize session state for risk profile
if 'selected_risk' not in st.session_state:
    st.session_state.selected_risk = 'Balanced'

# App Header
st.markdown("""
    <div class="app-header">
        <h1 class="app-title">📊 The Wealth Blueprint</h1>
        <p class="app-subtitle">Strategic Asset Planner - Advanced Analytics for Long-term Wealth Creation</p>
    </div>
""", unsafe_allow_html=True)

# Section 1: Investment Parameters
st.markdown("""
    <div class="section-card">
        <h2 class="section-title">&nbsp;&nbsp; Investment Parameters</h2>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<p class="input-label">Monthly SIP Amount (₹)</p>', unsafe_allow_html=True)
    sip_amount = st.number_input(
        "sip_amount_label",
        min_value=500,
        max_value=500000,
        value=20000,
        step=1000,
        label_visibility="collapsed"
    )
    st.markdown(f'<p class="input-value">₹{sip_amount:,}</p>', unsafe_allow_html=True)

with col2:
    st.markdown('<p class="input-label">Tenure (Years)</p>', unsafe_allow_html=True)
    tenure_years = st.number_input(
        "tenure_label",
        min_value=5,
        max_value=40,
        value=15,
        step=1,
        label_visibility="collapsed"
    )
    st.markdown(f'<p class="input-value">{tenure_years} Years</p>', unsafe_allow_html=True)

with col3:
    st.markdown('<p class="input-label">Annual Step-up (%)</p>', unsafe_allow_html=True)
    stepup_percent = st.number_input(
        "stepup_label",
        min_value=0,
        max_value=30,
        value=10,
        step=1,
        label_visibility="collapsed"
    )
    st.markdown(f'<p class="input-value">{stepup_percent}%</p>', unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

# Section 2: Strategy & Risk Profile
st.markdown("""
    <div class="section-card">
        <h2 class="section-title"> &nbsp;&nbsp; Select Risk Profile</h2>
    </div>
""", unsafe_allow_html=True)

# Risk Profile Selection with Tabs
tab1, tab2 = st.tabs(["Strategy & Allocation", "Projection Analysis"])
with tab1:
    # --- 0. Asset Class Definitions (Tooltips) ---
    tooltips = {
        "Debt": "Low-risk funds that lend money to the government/companies. Acts as a safety net.",
        "Gold": "Invests in physical gold prices. Protects value during inflation or market panic.",
        "Large": "Top 100 established companies. Stable growth with moderate risk.",
        "Mid": "Medium-sized growing companies. Higher growth potential than large caps but riskier.",
        "Small": "Small, emerging companies. Highest growth potential but very volatile (risky)."
    }

    # --- 1. Risk Profile Buttons ---
    col_r1, col_r2, col_r3 = st.columns(3)
    
    with col_r1:
        if st.button("🛡️ Conservative", use_container_width=True, key="btn_con", 
                     type="primary" if st.session_state.selected_risk == "Conservative" else "secondary"):
            st.session_state.selected_risk = "Conservative"
            st.rerun()
            
    with col_r2:
        if st.button("⚖️ Balanced", use_container_width=True, key="btn_bal", 
                     type="primary" if st.session_state.selected_risk == "Balanced" else "secondary"):
            st.session_state.selected_risk = "Balanced"
            st.rerun()

    with col_r3:
        if st.button("🚀 Aggressive", use_container_width=True, key="btn_agg", 
                     type="primary" if st.session_state.selected_risk == "Aggressive" else "secondary"):
            st.session_state.selected_risk = "Aggressive"
            st.rerun()

    # Get Data
    profile_data = RISK_PROFILES[st.session_state.selected_risk]
    allocs = profile_data["allocations"]
    rets = profile_data["returns"]
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- CLASS I: DEFENSIVE ASSETS (Green Header) ---
    st.markdown(f"""
        <div style='background-color: #064e3b; padding: 12px 15px; border-radius: 8px; border-left: 5px solid #34d399; margin-bottom: 15px;'>
            <h4 style='color: white; margin:0;'>🛡️ I. Defensive Assets (Safety & Cushioning)</h4>
        </div>
    """, unsafe_allow_html=True)
    
    col_def1, col_def2 = st.columns(2)
    with col_def1:
        st.markdown('<p class="input-label">Debt Mutual Funds</p>', unsafe_allow_html=True)
        debt_pct = st.slider("", 0, 100, allocs["Debt MF"], key="s_debt", help=tooltips["Debt"], label_visibility="collapsed")
        # Text Size Increased to 1.3rem
        st.markdown(f'<p style="margin-top:-5px;"><span style="font-size:0.9rem; color:#9ca3af; font-weight:400;">(Suggested: <b style="color:#3b82f6">{allocs["Debt MF"]}%</b> | Expected Return: <b style="color:#3b82f6">{rets["Debt MF"]*100:.1f}%</b>)</span></p>', unsafe_allow_html=True)
        
    with col_def2:
        st.markdown('<p class="input-label">Gold ETFs</p>', unsafe_allow_html=True)
        gold_pct = st.slider("", 0, 100, allocs["Gold ETF"], key="s_gold", help=tooltips["Gold"], label_visibility="collapsed")
        st.markdown(f'<p style="margin-top:-5px;"><span style="font-size:0.9rem; color:#9ca3af; font-weight:400;">(Suggested: <b style="color:#3b82f6">{allocs["Gold ETF"]}%</b> | Expected Return: <b style="color:#3b82f6">{rets["Gold ETF"]*100:.1f}%</b>)</span></p>', unsafe_allow_html=True)
        
    # --- CLASS II: CORE EQUITY (Blue Header) ---
    st.markdown(f"""
        <div style='background-color: #172554; padding: 12px 15px; border-radius: 8px; border-left: 5px solid #60a5fa; margin-top: 25px; margin-bottom: 15px;'>
            <h4 style='color: white; margin:0;'>⚓ II. Core Equity (Stability)</h4>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="input-label">Large Cap </p>', unsafe_allow_html=True)
    large_pct = st.slider("", 0, 100, allocs["Large Cap"], key="s_large", help=tooltips["Large"], label_visibility="collapsed")
    st.markdown(f'<p style="margin-top:-5px;"><span style="font-size:0.9rem; color:#9ca3af; font-weight:400;">(Suggested: <b style="color:#3b82f6">{allocs["Large Cap"]}%</b> | Expected Return: <b style="color:#3b82f6">{rets["Large Cap"]*100:.1f}%</b>)</span></p>', unsafe_allow_html=True)
    
    # --- CLASS III: ALPHA GENERATORS (Mustard Yellow Header) ---
    st.markdown(f"""
        <div style='background-color: #713f12; padding: 12px 15px; border-radius: 8px; border-left: 5px solid #facc15; margin-top: 25px; margin-bottom: 15px;'>
            <h4 style='color: white; margin:0;'>🚀 III. Alpha Generators (High Growth)</h4>
        </div>
    """, unsafe_allow_html=True)

    col_alp1, col_alp2 = st.columns(2)
    with col_alp1:
        st.markdown('<p class="input-label">Mid Cap Funds</p>', unsafe_allow_html=True)
        mid_pct = st.slider("", 0, 100, allocs["Mid Cap"], key="s_mid", help=tooltips["Mid"], label_visibility="collapsed")
        st.markdown(f'<p style="margin-top:-5px;"><span style="font-size:0.9rem; color:#9ca3af; font-weight:400;">(Suggested: <b style="color:#3b82f6">{allocs["Mid Cap"]}%</b> | Expected Return: <b style="color:#3b82f6">{rets["Mid Cap"]*100:.1f}%</b>)</span></p>', unsafe_allow_html=True)
        
    with col_alp2:
        st.markdown('<p class="input-label">Small Cap Funds</p>', unsafe_allow_html=True)
        small_pct = st.slider("", 0, 100, allocs["Small Cap"], key="s_small", help=tooltips["Small"], label_visibility="collapsed")
        st.markdown(f'<p style="margin-top:-5px;"><span style="font-size:0.9rem; color:#9ca3af; font-weight:400;">(Suggested: <b style="color:#3b82f6">{allocs["Small Cap"]}%</b> | Expected Return: <b style="color:#3b82f6">{rets["Small Cap"]*100:.1f}%</b>)</span></p>', unsafe_allow_html=True)
        
    # Check Total
    total_alloc = debt_pct + gold_pct + large_pct + mid_pct + small_pct
    if total_alloc != 100:
        st.warning(f"⚠️ Total Allocation is {total_alloc}%. Please adjust to 100%.")

   
    # --- Strategy Decoder (Risk Profile Perspective) ---
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("💡 Strategy Logic: Understanding Your Profile"):
        st.markdown("""
<div style='color: #e0e7ff; font-size: 0.95rem; line-height: 1.6;'>
<p>This planner creates a custom <b>Strategic Asset Allocation</b> for you. Instead of a one-size-fits-all approach, we tailor the asset mix to match your financial personality. Here is the logic behind each profile:</p>

<div style='margin-bottom: 15px; border-left: 3px solid #3b82f6; padding-left: 10px;'>
<h5 style='color: #3b82f6; margin: 0;'>🛡️ The Conservative Strategy (Safety First)</h5>
<p style='margin: 5px 0 0 0;'>
<b>The Philosophy:</b> The primary goal here is <b>Capital Preservation</b>. We prioritize protecting your principal amount over chasing high returns. This is ideal for investors with a lower risk appetite or shorter time horizons.<br>
<b>Suggested Allocation:</b>
<br>• <b>70% Defensive Assets:</b> (60% Debt + 10% Gold). Acts as a strong "anchor," ensuring stability even if markets fall.
<br>• <b>30% Equity Exposure:</b> (20% Large Cap + 10% Mid Cap). A small portion to help your money grow slightly faster than inflation.
<br><b>Expected Return:</b> <span style='color: #3b82f6'><b>~9.0% - 10.5%</b></span> (Focus on Stability)
</p>
</div>

<div style='margin-bottom: 15px; border-left: 3px solid #f59e0b; padding-left: 10px;'>
<h5 style='color: #f59e0b; margin: 0;'>⚖️ The Balanced Strategy (Growth + Stability)</h5>
<p style='margin: 5px 0 0 0;'>
<b>The Philosophy:</b> This approach seeks the <b>"Golden Mean."</b> It aims to generate significant wealth while maintaining a safety cushion. It is designed for investors who want growth but cannot stomach sharp drops in portfolio value.<br>
<b>Suggested Allocation:</b>
<br>• <b>40% Defensive Assets:</b> (30% Debt + 10% Gold). Enough to absorb market shocks and reduce anxiety during downturns.
<br>• <b>60% Equity Exposure:</b> (30% Large Cap + 30% Alpha Generators). A majority allocation to stocks drives wealth creation, split evenly to optimize the risk-reward ratio.
<br><b>Expected Return:</b> <span style='color: #f59e0b'><b>~12.0% - 13.5%</b></span> (Moderate Growth)
</p>
</div>

<div style='margin-bottom: 0px; border-left: 3px solid #dc2626; padding-left: 10px;'>
<h5 style='color: #dc2626; margin: 0;'>🚀 The Aggressive Strategy (Max Compounding)</h5>
<p style='margin: 5px 0 0 0;'>
<b>The Philosophy:</b> The focus here is purely <b>Wealth Maximization</b>. This strategy accepts high short-term volatility in exchange for potentially superior long-term returns. It is best suited for long tenures (10+ years) where time can smooth out market bumps.<br>
<b>Suggested Allocation:</b>
<br>• <b>15% Defensive Assets:</b> (10% Debt + 5% Gold). A minimal safety net, kept only for liquidity.
<br>• <b>85% Equity Exposure:</b> (25% Large Cap + 60% Alpha Generators). The portfolio is heavily skewed towards high-growth assets. We aggressively target wealth multiplication, understanding that the ride may be volatile.
<br><b>Expected Return:</b> <span style='color: #dc2626'><b>~15.0% - 17.0%</b></span> (High Growth Potential)
</p>
</div>
</div>
""", unsafe_allow_html=True)

with tab2:
    # --- NEW: Metric Explainer (Question Mark Toggle) ---
    with st.expander("❓ Guide: How to Read This Report"):
        st.markdown("""
            <div style='color: #e0e7ff; font-size: 0.9rem; line-height: 1.5;'>
                <p style='margin-bottom: 10px;'><b>Understanding Your Projections:</b></p>
                <ul style='padding-left: 20px;'>
                    <li>💰 <b>Maturity Value:</b> The estimated total value of your portfolio at the end of the tenure (Pre-tax).</li>
                    <li>📉 <b>Wealth Gain:</b> Pure profit. It is calculated as <i>Maturity Value - Total Invested</i>.</li>
                    <li>🚀 <b>Growth Multiplier:</b> Shows how many times your money has multiplied (e.g., 2.3x means your money more than doubled).</li>
                    <li>💼 <b>Tax Impact (LTCG):</b> Estimated Long Term Capital Gains tax (12.5%) on profits above ₹1.25 Lakh.</li>
                    <li>🛒 <b>Real Purchasing Power:</b> The "Actual" value of your money in the future, adjusted for inflation. (e.g., ₹1 Crore in 20 years might only buy what ₹30 Lakhs buys today).</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # ... (Rest of your Tab 2 calculation code starts here: weighted_return = ...)    
    # Calculate weighted return based on user sliders
    weighted_return = (
        (debt_pct * rets["Debt MF"]) + 
        (gold_pct * rets["Gold ETF"]) + 
        (large_pct * rets["Large Cap"]) + 
        (mid_pct * rets["Mid Cap"]) + 
        (small_pct * rets["Small Cap"])
    ) / 100
    
    monthly_return = weighted_return / 12
    
    # Calculate SIP
    df_sip = calculate_stepup_sip(sip_amount, tenure_years, stepup_percent, monthly_return)
    
    final_invested = df_sip['Total_Invested'].iloc[-1]
    final_wealth = df_sip['Current_Wealth'].iloc[-1]
    final_returns = df_sip['Returns'].iloc[-1]
    
    # Inflation adjustment
    st.markdown('<p class="input-label">Expected Inflation Rate (%)</p>', unsafe_allow_html=True)
    inflation_rate = st.slider("inflation_slider", 0.0, 15.0, 6.0, 0.5, label_visibility="collapsed")
    st.markdown(f'<p style="font-size: 1.5rem; font-weight: 700; color: #3b82f6; margin-top: 5px;">{inflation_rate}% Annual Inflation</p>', unsafe_allow_html=True)
    
    real_value = calculate_inflation_adjusted(final_wealth, inflation_rate, tenure_years)
    
    # Tax calculation
    ltcg_tax = calculate_ltcg_tax(final_returns)
    post_tax_wealth = final_wealth - ltcg_tax
    
    # Top Metrics
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Maturity Value 
                    <span title="The final accumulated value of your investment at the end of the tenure, before any tax deductions." style="cursor: help; color: #60a5fa; font-size: 0.8rem;">(?)</span>
                </div>
                <div class="metric-value">₹{final_wealth:,.0f}</div>
                <div class="metric-subtitle">Pre-Tax Corpus</div>
            </div>
        """, unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Total Invested
                    <span title="The actual principal amount you have paid from your pocket over the entire tenure." style="cursor: help; color: #60a5fa; font-size: 0.8rem;">(?)</span>
                </div>
                <div class="metric-value">₹{final_invested:,.0f}</div>
                <div class="metric-subtitle">Principal Amount</div>
            </div>
        """, unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Wealth Gain
                    <span title="The pure profit generated by your investment (Maturity Value minus Total Invested)." style="cursor: help; color: #60a5fa; font-size: 0.8rem;">(?)</span>
                </div>
                <div class="metric-value">₹{final_returns:,.0f}</div>
                <div class="metric-subtitle">Total Returns</div>
            </div>
        """, unsafe_allow_html=True)
    
    with metric_col4:
        multiplier = final_wealth / final_invested
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">
                    Growth Multiplier
                    <span title="A ratio showing how many times your money has grown. (e.g., 3.0x means your money has tripled)." style="cursor: help; color: #60a5fa; font-size: 0.8rem;">(?)</span>
                </div>
                <div class="metric-value">{multiplier:.2f}x</div>
                <div class="metric-subtitle">Investment Growth</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Visualizations
    viz_col1, viz_col2 = st.columns([1, 1])
    
    with viz_col1:
        st.markdown('<h3 style="color: #ffffff; margin-bottom: 1rem;">Portfolio Mix</h3>', unsafe_allow_html=True)
        
        # Donut Chart - Colors matched to Tab 1 Headers
        # Defensive = Greens | Core = Blue | Alpha = Mustard/Yellows
        fig_donut = go.Figure(data=[go.Pie(
            labels=['Debt (Defensive)', 'Gold (Defensive)', 'Large Cap (Core)', 'Mid Cap (Alpha)', 'Small Cap (Alpha)'],
            values=[debt_pct, gold_pct, large_pct, mid_pct, small_pct],
            hole=0.6,
            marker=dict(colors=[
                '#059669', '#10b981',  # Greens for Defensive (Matches Header)
                '#3b82f6',             # Blue for Core (Matches Header)
                '#b45309', '#d97706'   # Mustard/Dark Yellows for Alpha (Matches Header, Darker for white text visibility)
            ]),
            textinfo='percent',
            textfont=dict(size=14, color='#ffffff', family="Inter, sans-serif", weight="bold"),
            hovertemplate='<b>%{label}</b><br>%{value:.0f}%<br>₹%{value:,.0f}<extra></extra>'
        )])
        
        fig_donut.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)', # Transparent to blend with card
            plot_bgcolor='rgba(0,0,0,0)',
            height=400,
            showlegend=True,
            legend=dict(
                orientation="v",
                yanchor="middle", y=0.5,
                xanchor="left", x=1.0,
                font=dict(color='#e2e8f0', size=12)
            ),
            annotations=[dict(
                text=f'<b>Portfolio<br>Mix</b>',
                x=0.5, y=0.5,
                font_size=16,
                font_color='#10b981', # Emerald Text
                showarrow=False
            )],
            margin=dict(l=20, r=100, t=20, b=20)
        )
        
        st.plotly_chart(fig_donut, use_container_width=True)
    
    with viz_col2:
        st.markdown('<h3 style="color: #ffffff; margin-bottom: 1rem;">Growth Projection</h3>', unsafe_allow_html=True)
        
        # Area Chart - Emerald & Grey
        fig_growth = go.Figure()
        
        # Trace 1: Principal (Light Grey)
        fig_growth.add_trace(go.Scatter(
            x=df_sip['Year'],
            y=df_sip['Total_Invested'],
            name='Principal',
            fill='tozeroy',
            mode='lines',
            line=dict(color='#9ca3af', width=1), # Light Grey Line
            fillcolor='rgba(156, 163, 175, 0.2)', # Transparent Grey Fill
            hovertemplate='<b>Year %{x:.1f}</b><br>Principal: ₹%{y:,.0f}<extra></extra>'
        ))
        
        # Trace 2: Wealth (Emerald Green)
        fig_growth.add_trace(go.Scatter(
            x=df_sip['Year'],
            y=df_sip['Current_Wealth'],
            name='Total Wealth',
            fill='tonexty',
            mode='lines',
            line=dict(color='#10b981', width=3), # Emerald Green Line
            fillcolor='rgba(16, 185, 129, 0.2)', # Transparent Emerald Fill
            hovertemplate='<b>Year %{x:.1f}</b><br>Wealth: ₹%{y:,.0f}<br>Returns: ₹%{customdata:,.0f}<extra></extra>',
            customdata=df_sip['Returns']
        ))
        
        fig_growth.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400,
            xaxis_title="Years",
            yaxis_title="Amount (₹)",
            font=dict(color='#e2e8f0', size=12),
            hovermode='x unified',
            legend=dict(
                orientation="h",
                yanchor="bottom", y=1.02,
                xanchor="center", x=0.5
            ),
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig_growth, use_container_width=True)
    
    # Goal Analysis
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<p class="input-label">Financial Goal Target (₹)</p>', unsafe_allow_html=True)
    goal_amount = st.number_input(
        "goal_label",
        min_value=100000,
        max_value=100000000,
        value=10000000,
        step=100000,
        label_visibility="collapsed"
    )
    
    years_needed = years_to_reach_goal(goal_amount, sip_amount, stepup_percent, monthly_return)
    
    if years_needed and years_needed <= 50:
        if years_needed <= tenure_years:
            summary_text = f"✅ <b>Goal Achievable!</b> You will reach your goal of <b>₹{goal_amount/10000000:.2f} Cr</b> in approximately <b>{years_needed:.1f} years</b>. That's <b>{tenure_years - years_needed:.1f} years</b> ahead of your planned tenure!"
        else:
            extra_years = years_needed - tenure_years
            summary_text = f"⚠️ To reach your goal of <b>₹{goal_amount/10000000:.2f} Cr</b>, you need to stay invested for <b>{extra_years:.1f} more years</b> beyond your current tenure of {tenure_years} years."
    else:
        required_sip = (goal_amount / final_wealth) * sip_amount if final_wealth > 0 else 0
        summary_text = f"❌ Your goal of <b>₹{goal_amount/10000000:.2f} Cr</b> is ambitious. Consider increasing your monthly SIP to approximately <b>₹{required_sip:,.0f}</b> or extending your investment tenure significantly."
    
    st.markdown(f"""
        <div class="summary-box">
            <p class="summary-text">{summary_text}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Tax & Real Value Summary
    col_sum1, col_sum2 = st.columns(2)
    
    with col_sum1:
        st.markdown(f"""
            <div class="section-card">
                <h3 style="color: #ffffff; margin-bottom: 1rem;">💼 Tax Impact (LTCG)</h3>
                <p style="color: #e2e8f0; margin: 0.5rem 0;">
                    <b>Gross Wealth:</b> ₹{final_wealth:,.0f}<br>
                    <b>LTCG Tax (12.5%):</b> <span style="color: #ef4444;">-₹{ltcg_tax:,.0f}</span><br>
                    <b style="color: #10b981; font-size: 1.2rem;">Net Post-Tax Wealth:</b> ₹{post_tax_wealth:,.0f}
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col_sum2:
        st.markdown(f"""
            <div class="section-card">
                <h3 style="color: #ffffff; margin-bottom: 1rem;">🔄 Real Purchasing Power</h3>
                <p style="color: #e2e8f0; margin: 0.5rem 0;">
                    <b>Future Value:</b> ₹{final_wealth:,.0f}<br>
                    <b>Inflation Adjusted ({inflation_rate}%):</b><br>
                    <b style="color: #10b981; font-size: 1.2rem;">Today's Value:</b> ₹{real_value:,.0f}
                </p>
            </div>
        """, unsafe_allow_html=True)

# Year-wise Breakdown Table
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div class="section-card">
        <h2 class="section-title">📅 Detailed Year-wise Projections</h2>
    </div>
""", unsafe_allow_html=True)

# --- NEW: Explanation Toggle for Table ---
with st.expander("ℹ️ How to Read This Table? (Calculation Logic)"):
    st.markdown("""
        <div style='color: #e0e7ff; font-size: 0.95rem; line-height: 1.6;'>
            <p>This table provides a transparent, year-by-year breakdown of your wealth accumulation journey. Here is how each column is calculated:</p>
            
            <ul style='margin-bottom: 10px;'>
                <li><b>Monthly SIP:</b> This shows your contribution amount for that year. <br>
                <i>Note: If you selected a "Step-up," you will see this amount increase every year (e.g., Year 2 is 10% higher than Year 1).</i></li>
                
                <li><b>Total Invested:</b> The cumulative sum of all SIP installments paid up to that year. This is your "Skin in the game."</li>
                
                <li><b>Total Wealth:</b> The market value of your portfolio at the end of that year. <br>
                <i>Logic: It accounts for the compounding interest earned on both your principal and previous years' interest.</i></li>
                
                <li><b>Wealth Gain:</b> The difference between your <i>Total Wealth</i> and <i>Total Invested</i>. This represents the power of compounding working in your favor.</li>
            </ul>
            <p style='color: #9ca3af; font-size: 0.9rem;'>
                <i>*Pro Tip: Notice how "Wealth Gain" starts small in the early years but grows exponentially in the later years. This is the "Hockey Stick" effect of long-term compounding.</i>
            </p>
        </div>
    """, unsafe_allow_html=True)

# ... (Previous code remains the same until 'Year-wise Breakdown Table' section)

# 1. PREPARE DATA
yearly_data = df_sip[df_sip['Month'] % 12 == 0].copy()
yearly_data['Year'] = (yearly_data['Month'] // 12).astype(int)

# [Step 1] Select using ORIGINAL column names first (Prevents KeyError)
yearly_data = yearly_data[['Year', 'SIP_Amount', 'Total_Invested', 'Current_Wealth', 'Returns']]

# [Step 2] Rename to Display Names
yearly_data.columns = ['Year', 'Monthly SIP', 'Total Invested', 'Total Wealth', 'Wealth Gain']

# [Step 3] Reset index to keep the CSV export clean
yearly_data.reset_index(drop=True, inplace=True)

# 2. PREPARE DISPLAY TABLE
display_data = yearly_data.copy()

# [CRITICAL FIX] Set 'Year' as the Index. 
# This completely removes the unwanted "0, 1, 2..." column.
display_data.set_index('Year', inplace=True)

# Format numbers with ₹ and commas
for col in ['Monthly SIP', 'Total Invested', 'Total Wealth', 'Wealth Gain']:
    display_data[col] = display_data[col].apply(lambda x: f"₹{x:,.0f}")

# 3. DEFINE STYLING
def highlight_rows(row):
    # Standard Dark Grey for data rows
    return ['background-color: #1e293b; color: white; font-size: 1.2rem; font-family: Inter; border-bottom: 1px solid #334155'] * len(row)

# 4. APPLY STYLES & RENDER
# Note: The 'Year' column is now an index, so it automatically gets the Blue Header style ('th').
styled_df = display_data.style\
    .apply(highlight_rows, axis=1)\
    .set_table_styles([
        # Style Headers (including the 'Year' column now)
        {'selector': 'th', 'props': [
            ('background-color', '#041759'), 
            ('color', 'white'), 
            ('font-size', '1.3rem'), 
            ('font-weight', 'bold'),
            ('padding', '12px'),
            ('border-bottom', '2px solid #3b82f6')
        ]},
        # Style Data Cells
        {'selector': 'td', 'props': [('padding', '12px')]}
    ])

st.table(styled_df)

# Export functionality
st.markdown("<br>", unsafe_allow_html=True)
csv = yearly_data.to_csv(index=False)
st.download_button(
    label="📥 Download Projections as CSV",
    data=csv,
    file_name=f"wealth_blueprint_{datetime.now().strftime('%Y%m%d')}.csv",
    mime="text/csv"
)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; padding: 2rem; border-top: 1px solid #334155;'>
        <p style='color: #64748b; margin: 0.3rem 0;'>
            💎 <b>The Wealth Blueprint</b> - Professional Financial Planning Tool
        </p>
        <p style='color: #475569; font-size: 0.9rem; margin: 0.3rem 0;'>
            Designed & Developed by <b style='color: #3b82f6;'>Neshitha Korrapati</b> | 
            www.linkedin.com/in/neshitha-korrapati | neshitha.kc@gmail.com }
        </p>
        <p style='color: #475569; font-size: 0.85rem; margin: 1rem 0 0 0;'>
            ⚠️ <i>Disclaimer: Projections based on assumed returns. Actual results may vary. 
            Consult a certified financial advisor before making investment decisions.</i>
        </p>
    </div>
""", unsafe_allow_html=True)
