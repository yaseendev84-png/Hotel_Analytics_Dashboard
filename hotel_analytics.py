import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="365 Hotels & Resorts Dashboard",
    page_icon="🏨",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main-card {
        background-color: #1a2332;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🏨 Hotel Analytics")
st.sidebar.markdown("### 📊 Dataset Overview")
st.sidebar.write("**Total Bookings:** 134,590")
st.sidebar.write("**Properties:** 7 Hotels & Resorts")
st.sidebar.write("**Avg Occupancy:** 57.8%")

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙️ Strategic Thresholds")
st.sidebar.write("- **OTA Commission Cap:** 15.0%")
st.sidebar.write("- **Cancellation Leakage Target:** < 20.0%")
st.sidebar.write("- **Direct Booking Growth:** +10.0%")

# Hero Banner
st.markdown("""
    <div class="main-card">
        <h1>🏨 365 Hotels & Resorts Analytics Dashboard</h1>
        <p>Real-time performance tracking across room occupancy, revenue per available room (RevPAR), OTA channel leakage, and cancellation trends.</p>
    </div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["🔮 Revenue & Booking Simulator", "📊 Business Performance", "ℹ️ Strategic Rules & Info"])

# Tab 1: Simulator
with tab1:
    st.subheader("📝 Booking & Revenue Simulation")
    
    col1, col2 = st.columns(2)
    with col1:
        capacity = st.slider("🔑 Available Rooms Capacity", min_value=50, max_value=1000, value=300, step=10)
        avg_daily_rate = st.number_input("💵 Average Daily Rate - ADR (AED)", min_value=100, max_value=5000, value=650, step=50)
        
    with col2:
        ota_share = st.slider("🌐 OTA Booking Share (%)", min_value=0.0, max_value=100.0, value=45.0, step=1.0)
        cancellation_rate = st.slider("🚫 Expected Cancellation Rate (%)", min_value=0.0, max_value=50.0, value=15.0, step=0.5)

    if st.button("🚀 Calculate Projected Revenue", use_container_width=True):
        successful_bookings = int(capacity * (1 - (cancellation_rate / 100)))
        gross_revenue = successful_bookings * avg_daily_rate
        ota_commissions = gross_revenue * (ota_share / 100) * 0.15
        net_revenue = gross_revenue - ota_commissions
        
        st.success(f"**Expected Successful Bookings:** {successful_bookings} rooms")
        st.info(f"**Projected Net Revenue:** AED {net_revenue:,.2f}")
        
        if ota_share > 50.0:
            st.warning("⚠️ High OTA Reliance: Converting 10% of OTA bookings to direct can save ~AED 1.2M annually in lost commissions.")

# Tab 2: Key Metrics
with tab2:
    st.subheader("📊 Key Performance Indicators")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Revenue", "AED 12.4M", delta="+5.4%")
    m2.metric("Occupancy Rate", "57.8%", delta="+2.1%")
    m3.metric("RevPAR", "AED 375.70", delta="+3.8%")
    m4.metric("Cancellation Rate", "18.4%", delta="-1.2% (Improved)")

    st.markdown("---")
    st.subheader("📈 Monthly Revenue Trend")
    
    chart_data = pd.DataFrame({
        'Month': ['May', 'Jun', 'Jul', 'Aug'],
        'Realized Revenue (AED Millions)': [2.8, 3.1, 3.4, 3.1],
        'Occupancy Rate (%)': [52.1, 56.4, 61.2, 57.8]
    }).set_index('Month')
    
    st.line_chart(chart_data)

# Tab 3: Rules & Info
with tab3:
    st.subheader("ℹ️ Cleaning Decisions & Business Rules")
    st.markdown("""
    **Data Cleaning & Business Methodology:**
    * **Over-capacity Filtering:** Rows where `successful_bookings` exceeded total capacity were cleaned.
    * **OTA Commission Leakage:** High dependency on OTAs leads to substantial revenue loss via ~15% commissions.
    * **Direct Booking Push:** Converting 10% of OTA bookings to direct bookings recovers ~AED 1.2M annually.
    * **Cancellation Tracking:** Real-time monitoring of booking cancellations to optimize dynamic pricing strategies.
    """)