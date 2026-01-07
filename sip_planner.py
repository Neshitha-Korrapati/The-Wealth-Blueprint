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
        font-size: 1.1rem;
        font-weight: 400;
        margin-top: 0.5rem;
    }
    
    /* Section Cards */
    .section-card {
        background-color: #262730;
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid #7f1d1d;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    }
    
    .section-title {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        padding-bottom: 0.8rem;
        border-bottom: 2px solid #3b82f6;
        border-left: 5px solid #dc2626;
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid #334155;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        border-color: #3b82f6;
        box-shadow: 0 4px 16px rgba(59, 130, 246, 0.2);
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
        font-size: 1.1rem;
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
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #1e293b;
        border-radius: 8px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: #94a3b8;
        border-radius: 6px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6;
        color: #ffffff;
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
    </style>
""", unsafe_allow_html=True)

# Financial Constants
RISK_PROFILES = {
    "Conservative": {
        "debt_alloc": 0.70,
        "equity_alloc": 0.30,
        "debt_return": 0.07,
        "equity_return": 0.12
    },
    "Balanced": {
        "debt_alloc": 0.50,
        "equity_alloc": 0.50,
        "debt_return": 0.08,
        "equity_return": 0.135
    },
    "Aggressive": {
        "debt_alloc": 0.20,
        "equity_alloc": 0.80,
        "debt_return": 0.08,
        "equity_return": 0.16
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
        <h2 class="section-title">1. Investment Parameters</h2>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

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

with col4:
    st.markdown('<p class="input-label">Live Data</p>', unsafe_allow_html=True)
    live_data = st.checkbox("Enable Real-time Sync", value=False)
    st.markdown(f'<p class="input-value">{"Sync: 05:29" if live_data else "Static Mode"}</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Section 2: Strategy & Risk Profile
st.markdown("""
    <div class="section-card">
        <h2 class="section-title">2. Select Risk Profile</h2>
    </div>
""", unsafe_allow_html=True)

# Risk Profile Selection with Tabs
tab1, tab2 = st.tabs(["Strategy & Allocation", "Projection Analysis"])
with tab1:
    # Risk Profile Buttons
    col_r1, col_r2, col_r3 = st.columns(3)
    
    with col_r1:
        if st.button("Conservative", use_container_width=True, key="btn_conservative"):
            st.session_state.selected_risk = "Conservative"
    
    with col_r2:
        if st.button("Balanced", use_container_width=True, key="btn_balanced", type="primary"):
            st.session_state.selected_risk = "Balanced"
    
    with col_r3:
        if st.button("Aggressive", use_container_width=True, key="btn_aggressive"):
            st.session_state.selected_risk = "Aggressive"
    
    st.markdown(f"""
        <div style='text-align: center; margin: 1rem 0;'>
            <p style='color: #3b82f6; font-size: 1.2rem; font-weight: 600;'>
                Selected: {st.session_state.selected_risk}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Get selected profile
    profile = RISK_PROFILES[st.session_state.selected_risk]
    debt_alloc = profile["debt_alloc"]
    equity_alloc = profile["equity_alloc"]
    debt_return = profile["debt_return"]
    equity_return = profile["equity_return"]
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Asset Allocation Sliders
    col_a1, col_a2 = st.columns(2)
    
    with col_a1:
        st.markdown('<p class="input-label">Debt MF (%)</p>', unsafe_allow_html=True)
        debt_percent = st.slider(
            "debt_slider",
            0, 100,
            int(debt_alloc * 100),
            label_visibility="collapsed"
        )
        st.markdown(f'<p class="input-value">{debt_percent}% (Adaptive Return: {debt_return*100:.1f}%)</p>', unsafe_allow_html=True)
    
    with col_a2:
        st.markdown('<p class="input-label">Flexi Cap (%)</p>', unsafe_allow_html=True)
        equity_percent = 100 - debt_percent
        st.markdown(f'<p class="input-value">{equity_percent}% (Adaptive Return: {equity_return*100:.2f}%)</p>', unsafe_allow_html=True)
    
    # Additional asset classes
    col_a3, col_a4 = st.columns(2)
    
    with col_a3:
        st.markdown('<p class="input-label">Gold ETF (%)</p>', unsafe_allow_html=True)
        gold_percent = st.slider("gold_slider", 0, 50, 10, label_visibility="collapsed")
        st.markdown(f'<p class="input-value">{gold_percent}% (Adaptive Return: 15.51%)</p>', unsafe_allow_html=True)
    
    with col_a4:
        st.markdown('<p class="input-label">Mid Cap (%)</p>', unsafe_allow_html=True)
        midcap_percent = st.slider("midcap_slider", 0, 50, 5, label_visibility="collapsed")
        st.markdown(f'<p class="input-value">{midcap_percent}% (Adaptive Return: 27.66%)</p>', unsafe_allow_html=True)
    
    col_a5, col_a6 = st.columns(2)
    
    with col_a5:
        st.markdown('<p class="input-label">Nifty 50 (%)</p>', unsafe_allow_html=True)
        nifty_percent = st.slider("nifty_slider", 0, 50, 30, label_visibility="collapsed")
        st.markdown(f'<p class="input-value">{nifty_percent}% (Adaptive Return: 15.87%)</p>', unsafe_allow_html=True)
    
    with col_a6:
        st.markdown('<p class="input-label">Small Cap (%)</p>', unsafe_allow_html=True)
        smallcap_percent = st.slider("smallcap_slider", 0, 50, 5, label_visibility="collapsed")
        st.markdown(f'<p class="input-value">{smallcap_percent}% (Adaptive Return: 20.23%)</p>', unsafe_allow_html=True)

with tab2:
    # Calculate weighted return
    weighted_return = (debt_alloc * debt_return) + (equity_alloc * equity_return)
    monthly_return = weighted_return / 12
    
    # Calculate SIP
    df_sip = calculate_stepup_sip(sip_amount, tenure_years, stepup_percent, monthly_return)
    
    final_invested = df_sip['Total_Invested'].iloc[-1]
    final_wealth = df_sip['Current_Wealth'].iloc[-1]
    final_returns = df_sip['Returns'].iloc[-1]
    
    # Inflation adjustment
    st.markdown('<p class="input-label">Expected Inflation Rate (%)</p>', unsafe_allow_html=True)
    inflation_rate = st.slider("inflation_slider", 0.0, 15.0, 6.0, 0.5, label_visibility="collapsed")
    st.markdown(f'<p class="input-value">{inflation_rate}% Annual Inflation</p>', unsafe_allow_html=True)
    
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
                <div class="metric-label">Maturity Value</div>
                <div class="metric-value">₹{final_wealth:,.0f}</div>
                <div class="metric-subtitle">Pre-Tax Corpus</div>
            </div>
        """, unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Total Invested</div>
                <div class="metric-value">₹{final_invested:,.0f}</div>
                <div class="metric-subtitle">Principal Amount</div>
            </div>
        """, unsafe_allow_html=True)
    
    with metric_col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Wealth Gain</div>
                <div class="metric-value">₹{final_returns:,.0f}</div>
                <div class="metric-subtitle">Total Returns</div>
            </div>
        """, unsafe_allow_html=True)
    
    with metric_col4:
        multiplier = final_wealth / final_invested
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Growth Multiplier</div>
                <div class="metric-value">{multiplier:.2f}x</div>
                <div class="metric-subtitle">Investment Growth</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Visualizations
    viz_col1, viz_col2 = st.columns([1, 1])
    
    with viz_col1:
        st.markdown('<h3 style="color: #ffffff; margin-bottom: 1rem;">Portfolio Mix</h3>', unsafe_allow_html=True)
        
        # Donut Chart - Emerald Green & Grey Theme
        fig_donut = go.Figure(data=[go.Pie(
            labels=['Debt MF', 'Flexi Cap', 'Mid Cap', 'Small Cap'],
            values=[debt_alloc*100, equity_alloc*50, 20, 10],
            hole=0.6,
            # COLORS: Grey for Debt, Shades of Emerald for Equity
            marker=dict(colors=['#d1d5db', '#10b981', '#34d399', '#6ee7b7']),
            textinfo='label+percent',
            textfont=dict(size=14, color='#ffffff'),
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

yearly_data = df_sip[df_sip['Month'] % 12 == 0].copy()
yearly_data['Year'] = yearly_data['Month'] // 12
yearly_data = yearly_data[['Year', 'SIP_Amount', 'Total_Invested', 'Current_Wealth', 'Returns']]
yearly_data.columns = ['Year', 'Monthly SIP', 'Total Invested', 'Total Wealth', 'Wealth Gain']

# Format display
display_data = yearly_data.copy()
for col in ['Monthly SIP', 'Total Invested', 'Total Wealth', 'Wealth Gain']:
    display_data[col] = display_data[col].apply(lambda x: f"₹{x:,.0f}")

st.dataframe(display_data, use_container_width=True, hide_index=True, height=400)

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
            Designed & Developed by <b style='color: #3b82f6;'>[Your Name]</b> | 
            PGDM Finance & Analytics | {datetime.now().strftime('%B %Y')}
        </p>
        <p style='color: #475569; font-size: 0.85rem; margin: 1rem 0 0 0;'>
            ⚠️ <i>Disclaimer: Projections based on assumed returns. Actual results may vary. 
            Consult a certified financial advisor before making investment decisions.</i>
        </p>
    </div>
""", unsafe_allow_html=True)
