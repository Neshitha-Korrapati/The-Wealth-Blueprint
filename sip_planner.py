import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import io

# Page Configuration
st.set_page_config(
    page_title="The Wealth Blueprint",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Light Theme CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    .main {
        background-color: #FFFFFF;
    }
    
    .stApp {
        background-color: #F8F9FA;
    }
    
    /* Header Styling */
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
        background: linear-gradient(135deg, #0056B3 0%, #003D82 100%);
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0, 86, 179, 0.15);
    }
    
    .main-title {
        color: #FFFFFF;
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .main-subtitle {
        color: #E8F4FF;
        font-size: 1.1rem;
        font-weight: 400;
        margin-top: 0.5rem;
    }
    
    /* Premium Metric Cards */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 12px;
        padding: 1.8rem 1.5rem;
        box-shadow: 0 2px 8px rgba(31, 41, 55, 0.08);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .metric-card:hover {
        box-shadow: 0 8px 24px rgba(0, 86, 179, 0.15);
        transform: translateY(-4px);
        border-color: #0056B3;
    }
    
    .metric-label {
        color: #6B7280;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.8rem;
    }
    
    .metric-value {
        color: #0056B3;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
        line-height: 1;
    }
    
    .metric-subtitle {
        color: #9CA3AF;
        font-size: 0.8rem;
        margin-top: 0.5rem;
        font-weight: 400;
    }
    
    /* Section Headers */
    .section-header {
        background: linear-gradient(90deg, #0056B3 0%, transparent 100%);
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        margin: 2.5rem 0 1.5rem 0;
    }
    
    .section-header h3 {
        color: #FFFFFF;
        margin: 0;
        font-size: 1.4rem;
        font-weight: 700;
    }
    
    /* Info Cards */
    .info-card {
        background: #F9FAFB;
        border: 1px solid #E5E7EB;
        border-left: 4px solid #0056B3;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .info-card h3 {
        color: #1F2937;
        font-size: 1.1rem;
        margin-bottom: 0.8rem;
        font-weight: 600;
    }
    
    .info-card p {
        color: #4B5563;
        font-size: 0.95rem;
        margin: 0.5rem 0;
        line-height: 1.6;
    }
    
    /* Warning Box */
    .warning-box {
        background: #FEF2F2;
        border: 1px solid #FCA5A5;
        border-left: 4px solid #DC2626;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .warning-box h4 {
        color: #DC2626;
        margin: 0 0 0.5rem 0;
        font-weight: 600;
    }
    
    .warning-box p {
        color: #7F1D1D;
        margin: 0;
    }
    
    /* Success Box */
    .success-box {
        background: #F0FDF4;
        border: 1px solid #86EFAC;
        border-left: 4px solid #10B981;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Reality Check Box */
    .reality-check {
        background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
        border: 2px solid #3B82F6;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
    }
    
    .reality-check h4 {
        color: #1E40AF;
        margin: 0 0 0.8rem 0;
        font-weight: 700;
    }
    
    .reality-check p {
        color: #1E3A8A;
        margin: 0.5rem 0;
        font-size: 1rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2.5rem 1rem;
        margin-top: 3rem;
        border-top: 2px solid #E5E7EB;
        background: #F9FAFB;
        border-radius: 8px;
    }
    
    .footer h3 {
        color: #0056B3;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .footer p {
        color: #6B7280;
        margin: 0.3rem 0;
    }
    
    .footer a {
        color: #0056B3;
        text-decoration: none;
        font-weight: 600;
    }
    
    .footer a:hover {
        text-decoration: underline;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F9FAFB 0%, #F3F4F6 100%);
    }
    
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #1F2937;
        font-weight: 700;
    }
    
    /* Button Styling */
    .stDownloadButton > button {
        background-color: #0056B3;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        background-color: #003D82;
        box-shadow: 0 4px 12px rgba(0, 86, 179, 0.3);
    }
    
    /* Table Styling */
    .dataframe {
        border: 1px solid #E5E7EB !important;
        border-radius: 8px !important;
    }
    
    /* Tooltip Icon */
    .tooltip-icon {
        color: #0056B3;
        cursor: help;
        font-weight: bold;
        margin-left: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Constants
RISK_PROFILES = {
    "Conservative": {
        "debt_allocation": 0.70,
        "equity_allocation": 0.30,
        "debt_return": 0.07,
        "equity_return": 0.12,
        "description": "Low risk with capital preservation focus"
    },
    "Balanced": {
        "debt_allocation": 0.50,
        "equity_allocation": 0.50,
        "debt_return": 0.08,
        "equity_return": 0.135,
        "description": "Moderate risk with balanced growth"
    },
    "Aggressive": {
        "debt_allocation": 0.20,
        "equity_allocation": 0.80,
        "debt_return": 0.08,
        "equity_return": 0.16,
        "description": "High risk with maximum growth potential"
    }
}

LTCG_TAX_RATE = 0.125
LTCG_EXEMPTION_LIMIT = 125000

# Helper Functions
def calculate_stepup_sip(initial_sip, tenure_years, stepup_rate, monthly_rate, inflation_rate):
    """Calculate wealth with step-up SIP"""
    months = tenure_years * 12
    stepup_monthly_rate = stepup_rate / 100
    monthly_inflation = (1 + inflation_rate/100) ** (1/12) - 1
    
    wealth_data = []
    total_invested = 0
    current_wealth = 0
    current_sip = initial_sip
    
    for month in range(1, months + 1):
        if month > 1 and (month - 1) % 12 == 0:
            current_sip = current_sip * (1 + stepup_monthly_rate)
        
        total_invested += current_sip
        current_wealth = (current_wealth + current_sip) * (1 + monthly_rate)
        
        inflation_adjusted_wealth = current_wealth / ((1 + monthly_inflation) ** month)
        
        wealth_data.append({
            'Month': month,
            'Year': month / 12,
            'SIP_Amount': current_sip,
            'Total_Invested': total_invested,
            'Current_Wealth': current_wealth,
            'Returns': current_wealth - total_invested,
            'Inflation_Adjusted_Wealth': inflation_adjusted_wealth
        })
    
    return pd.DataFrame(wealth_data)

def calculate_flat_sip(sip_amount, tenure_years, monthly_rate):
    """Calculate standard flat SIP"""
    months = tenure_years * 12
    wealth_data = []
    total_invested = 0
    current_wealth = 0
    
    for month in range(1, months + 1):
        total_invested += sip_amount
        current_wealth = (current_wealth + sip_amount) * (1 + monthly_rate)
        
        wealth_data.append({
            'Month': month,
            'Year': month / 12,
            'Flat_Invested': total_invested,
            'Flat_Wealth': current_wealth
        })
    
    return pd.DataFrame(wealth_data)

def calculate_ltcg_tax(gains):
    """Calculate LTCG tax"""
    if gains <= LTCG_EXEMPTION_LIMIT:
        return 0
    return (gains - LTCG_EXEMPTION_LIMIT) * LTCG_TAX_RATE

def calculate_delay_impact(initial_sip, base_tenure, stepup_rate, monthly_rate, delay_years):
    """Calculate cost of delay"""
    df_base = calculate_stepup_sip(initial_sip, base_tenure, stepup_rate, monthly_rate, 0)
    
    if base_tenure > delay_years:
        df_delayed = calculate_stepup_sip(initial_sip, base_tenure - delay_years, stepup_rate, monthly_rate, 0)
        delayed_wealth = df_delayed['Current_Wealth'].iloc[-1]
    else:
        delayed_wealth = 0
    
    base_wealth = df_base['Current_Wealth'].iloc[-1]
    wealth_lost = base_wealth - delayed_wealth
    
    return {
        'delay_years': delay_years,
        'base_wealth': base_wealth,
        'delayed_wealth': delayed_wealth,
        'wealth_lost': wealth_lost,
        'loss_percentage': (wealth_lost / base_wealth * 100) if base_wealth > 0 else 0
    }

def calculate_goal_check(target_amount, monthly_sip, stepup_rate, monthly_return):
    """Calculate years needed to reach a financial goal"""
    current_wealth = 0
    total_months = 0
    current_sip = monthly_sip
    max_months = 50 * 12  # 50 years max
    
    while current_wealth < target_amount and total_months < max_months:
        total_months += 1
        if total_months > 1 and (total_months - 1) % 12 == 0:
            current_sip = current_sip * (1 + stepup_rate/100)
        current_wealth = (current_wealth + current_sip) * (1 + monthly_return)
    
    return total_months / 12 if current_wealth >= target_amount else None

# App Header
st.markdown("""
    <div class="main-header">
        <h1 class="main-title">💎 The Wealth Blueprint</h1>
        <p class="main-subtitle">An Advanced Analytics Tool for Long-term Wealth Creation</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar - User Inputs
with st.sidebar:
    st.markdown("### ⚙️ Investment Parameters")
    st.markdown("---")
    
    sip_amount = st.number_input(
        "💰 Monthly SIP Amount (₹)",
        min_value=500,
        max_value=500000,
        value=10000,
        step=500,
        help="Your initial monthly investment"
    )
    
    stepup_percent = st.slider(
        "📈 Annual Step-up %",
        min_value=0,
        max_value=30,
        value=10,
        step=1,
        help="Yearly increase in SIP amount"
    )
    
    tenure_years = st.slider(
        "⏰ Investment Tenure (Years)",
        min_value=5,
        max_value=40,
        value=20,
        step=1,
        help="Total investment period"
    )
    
    st.markdown("---")
    st.markdown("### 🎯 Risk Profile")
    
    risk_profile = st.selectbox(
        "Select Your Risk Appetite",
        options=list(RISK_PROFILES.keys()),
        index=1
    )
    
    st.info(f"**{risk_profile}**: {RISK_PROFILES[risk_profile]['description']}")
    
    st.markdown("---")
    st.markdown("### 💹 Economic Assumptions")
    
    inflation_rate = st.slider(
        "Expected Annual Inflation (%)",
        min_value=0.0,
        max_value=15.0,
        value=6.0,
        step=0.5,
        help="Expected average inflation rate"
    )
    
    st.markdown("---")
    st.markdown("### 🎯 Goal Planning")
    
    target_goal = st.number_input(
        "Financial Goal (₹)",
        min_value=100000,
        max_value=100000000,
        value=10000000,
        step=100000,
        help="Target corpus you want to achieve"
    )

# Calculate
profile = RISK_PROFILES[risk_profile]
debt_alloc = profile["debt_allocation"]
equity_alloc = profile["equity_allocation"]
debt_return = profile["debt_return"]
equity_return = profile["equity_return"]

weighted_return = (debt_alloc * debt_return) + (equity_alloc * equity_return)
monthly_return = weighted_return / 12

# Calculate dataframes
df_stepup = calculate_stepup_sip(sip_amount, tenure_years, stepup_percent, monthly_return, inflation_rate)
df_flat = calculate_flat_sip(sip_amount, tenure_years, monthly_return)

# Extract values
final_invested = df_stepup['Total_Invested'].iloc[-1]
final_wealth = df_stepup['Current_Wealth'].iloc[-1]
final_returns = df_stepup['Returns'].iloc[-1]
inflation_adjusted_wealth = df_stepup['Inflation_Adjusted_Wealth'].iloc[-1]

ltcg_tax = calculate_ltcg_tax(final_returns)
post_tax_wealth = final_wealth - ltcg_tax

debt_amount = final_wealth * debt_alloc
equity_amount = final_wealth * equity_alloc

# Top Metric Cards
st.markdown("### 📊 Investment Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">💎 Total Corpus</div>
            <div class="metric-value">₹{final_wealth:,.0f}</div>
            <div class="metric-subtitle">Future Value</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">💰 Total Investment</div>
            <div class="metric-value">₹{final_invested:,.0f}</div>
            <div class="metric-subtitle">Principal Amount</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">📈 Wealth Gained</div>
            <div class="metric-value">₹{final_returns:,.0f}</div>
            <div class="metric-subtitle">Total Returns</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">🔄 Real Value</div>
            <div class="metric-value">₹{inflation_adjusted_wealth:,.0f}</div>
            <div class="metric-subtitle">Today's Purchasing Power</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Secondary Metrics
col5, col6, col7, col8 = st.columns(4)

with col5:
    roi_percent = (final_returns / final_invested) * 100
    st.metric("ROI", f"{roi_percent:.1f}%", help="Return on Investment")

with col6:
    wealth_multiplier = final_wealth / final_invested
    st.metric("Wealth Multiplier", f"{wealth_multiplier:.2f}x")

with col7:
    st.metric("Nominal CAGR", f"{weighted_return*100:.2f}%", help="Compound Annual Growth Rate")

with col8:
    real_return = weighted_return - (inflation_rate/100)
    st.metric("Real CAGR", f"{real_return*100:.2f}%", help="Inflation-adjusted return")

# Goal Reality Check
st.markdown("---")
years_to_goal = calculate_goal_check(target_goal, sip_amount, stepup_percent, monthly_return)

if years_to_goal and years_to_goal <= 50:
    goal_status = "achievable"
    goal_message = f"✅ You can reach your goal of **₹{target_goal:,.0f}** in approximately **{years_to_goal:.1f} years** with your current investment plan!"
    if years_to_goal < tenure_years:
        goal_message += f" You'll reach it **{tenure_years - years_to_goal:.1f} years** before your planned tenure."
    elif years_to_goal > tenure_years:
        extra_years = years_to_goal - tenure_years
        goal_message += f" However, you need to extend your investment by **{extra_years:.1f} years** to reach this goal."
else:
    goal_status = "challenging"
    required_sip = (target_goal / final_wealth) * sip_amount if final_wealth > 0 else 0
    goal_message = f"⚠️ Your goal of **₹{target_goal:,.0f}** may be challenging with current parameters. Consider increasing your monthly SIP to approximately **₹{required_sip:,.0f}** or extending your tenure."

st.markdown(f"""
    <div class="reality-check">
        <h4>🎯 Goal Reality Check</h4>
        <p><strong>Your Target:</strong> ₹{target_goal:,.0f}</p>
        <p><strong>Projected Corpus:</strong> ₹{final_wealth:,.0f}</p>
        <p>{goal_message}</p>
    </div>
""", unsafe_allow_html=True)

# Tax Impact Section
st.markdown("<div class='section-header'><h3>💼 Tax Impact Analysis (India LTCG 2024-25)</h3></div>", unsafe_allow_html=True)

col_tax1, col_tax2 = st.columns(2)

with col_tax1:
    st.markdown(f"""
        <div class="info-card">
            <h3>📋 Tax Calculation Breakdown</h3>
            <p><b>Total Capital Gains:</b> ₹{final_returns:,.0f}</p>
            <p><b>LTCG Exemption:</b> ₹{LTCG_EXEMPTION_LIMIT:,.0f}</p>
            <p><b>Taxable Gains:</b> ₹{max(0, final_returns - LTCG_EXEMPTION_LIMIT):,.0f}</p>
            <p><b>Tax Rate:</b> {LTCG_TAX_RATE*100}%</p>
            <p style='color: #DC2626; font-size: 1.2rem; margin-top: 1rem;'><b>Tax Payable:</b> ₹{ltcg_tax:,.0f}</p>
        </div>
    """, unsafe_allow_html=True)

with col_tax2:
    st.markdown(f"""
        <div class="info-card">
            <h3>💵 Post-Tax Net Wealth</h3>
            <p><b>Gross Corpus:</b> ₹{final_wealth:,.0f}</p>
            <p><b>Less: LTCG Tax:</b> ₹{ltcg_tax:,.0f}</p>
            <p style='color: #0056B3; font-size: 1.3rem; margin-top: 1rem;'><b>Net Wealth:</b> ₹{post_tax_wealth:,.0f}</p>
            <p style='color: #0056B3;'><b>Net Returns:</b> ₹{final_returns - ltcg_tax:,.0f}</p>
        </div>
    """, unsafe_allow_html=True)

# Visualizations
st.markdown("<div class='section-header'><h3>📈 Advanced Analytics & Visualizations</h3></div>", unsafe_allow_html=True)

# 1. Growth Area Chart
st.markdown("#### 💹 Wealth Accumulation Breakdown")

fig_growth = go.Figure()

fig_growth.add_trace(go.Scatter(
    x=df_stepup['Year'],
    y=df_stepup['Total_Invested'],
    name='Principal Invested',
    fill='tozeroy',
    mode='lines',
    line=dict(color='#9CA3AF', width=2),
    fillcolor='rgba(156, 163, 175, 0.3)',
    hovertemplate='Year %{x:.1f}<br>Principal: ₹%{y:,.0f}<extra></extra>'
))

fig_growth.add_trace(go.Scatter(
    x=df_stepup['Year'],
    y=df_stepup['Returns'],
    name='Wealth Gained',
    fill='tonexty',
    mode='lines',
    line=dict(color='#0056B3', width=2),
    fillcolor='rgba(0, 86, 179, 0.3)',
    hovertemplate='Year %{x:.1f}<br>Gains: ₹%{y:,.0f}<extra></extra>'
))

fig_growth.update_layout(
    template='plotly_white',
    xaxis_title="Investment Years",
    yaxis_title="Amount (₹)",
    font=dict(color='#1F2937', size=12, family='Inter'),
    hovermode='x unified',
    height=450,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)

st.plotly_chart(fig_growth, use_container_width=True)

# 2. Step-up Delta Chart
st.markdown("---")
st.markdown("#### ⚡ The Step-up Advantage: Flat vs. Step-up SIP")

df_comparison = df_stepup.merge(df_flat, on=['Month', 'Year'])

fig_delta = go.Figure()

fig_delta.add_trace(go.Scatter(
    x=df_comparison['Year'],
    y=df_comparison['Flat_Wealth'],
    name=f'Flat SIP (₹{sip_amount:,}/month)',
    mode='lines',
    line=dict(color='#9CA3AF', width=3, dash='dash'),
    hovertemplate='Year %{x:.1f}<br>Flat SIP: ₹%{y:,.0f}<extra></extra>'
))

fig_delta.add_trace(go.Scatter(
    x=df_comparison['Year'],
    y=df_comparison['Current_Wealth'],
    name=f'Step-up SIP ({stepup_percent}% annual)',
    mode='lines',
    line=dict(color='#0056B3', width=4),
    fill='tonexty',
    fillcolor='rgba(0, 86, 179, 0.1)',
    hovertemplate='Year %{x:.1f}<br>Step-up: ₹%{y:,.0f}<extra></extra>'
))

fig_delta.update_layout(
    template='plotly_white',
    xaxis_title="Investment Years",
    yaxis_title="Total Wealth (₹)",
    font=dict(color='#1F2937', size=12, family='Inter'),
    hovermode='x unified',
    height=450,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
)

st.plotly_chart(fig_delta, use_container_width=True)

flat_final = df_flat['Flat_Wealth'].iloc[-1]
delta_wealth = final_wealth - flat_final
delta_percentage = (delta_wealth / flat_final) * 100

st.markdown(f"""
    <div class="success-box">
        <p style='color: #065F46; font-size: 1.1rem; margin: 0;'>
        <b>🎯 Step-up Advantage:</b> By increasing your SIP by {stepup_percent}% annually, you gain an additional 
        <b>₹{delta_wealth:,.0f}</b> ({delta_percentage:.1f}% more) compared to a flat SIP!
        </p>
    </div>
""", unsafe_allow_html=True)

# 3. Asset Allocation Donut
st.markdown("---")
col_donut1, col_donut2 = st.columns([1, 1])

with col_donut1:
    st.markdown("#### 🥧 Portfolio Asset Allocation")
    
    fig_donut = go.Figure(data=[go.Pie(
        labels=['Equity', 'Debt'],
        values=[equity_amount, debt_amount],
        hole=0.65,
        marker=dict(colors=['#0056B3', '#60A5FA']),
        textinfo='label+percent',
        textfont=dict(size=16, color='#1F2937', family='Inter'),
        hovertemplate='<b>%{label}</b><br>₹%{value:,.0f}<br>%{percent}<extra></extra>'
    )])
    
    fig_donut.update_layout(
        template='plotly_white',
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        height=400,
        annotations=[dict(
            text=f'<b>{risk_profile}</b>',
            x=0.5, y=0.5,
            font_size=20,
            font_color='#0056B3',
            showarrow=False
        )]
    )
    
    st.plotly_chart(fig_donut, use_container_width=True)

with col_donut2:
    st.markdown("#### 📊 Allocation Details")
    st.markdown(f"""
        <div class="info-card">
            <div style='margin-bottom: 1.5rem;'>
                <p style='color: #0056B3; font-size: 1.1rem; margin: 0.5rem 0;'>
                    <b>🔵 Equity ({equity_alloc*100:.0f}%)</b>
                </p>
                <p style='margin: 0.3rem 0;'>
                    <b>Amount:</b> ₹{equity_amount:,.0f}<br>
                    <b>Return:</b> {equity_return*100:.1f}% p.a.<br>
                    <b>Risk:</b> {'High' if equity_alloc >= 0.7 else 'Moderate' if equity_alloc >= 0.4 else 'Low'}
                </p>
            </div>
            <div>
                <p style='color: #60A5FA; font-size: 1.1rem; margin: 0.5rem 0;'>
                    <b>🔵 Debt ({debt_alloc*100:.0f}%)</b>
                </p>
                <p