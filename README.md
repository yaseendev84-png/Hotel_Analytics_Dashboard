# 🏨 365 Hotels & Resorts Performance & Revenue Analytics Dashboard

An interactive Streamlit application designed for hotel revenue managers and decision-makers to track operational performance, model booking scenarios, and reduce channel leakage from Online Travel Agencies (OTAs)[span_0](start_span)[span_0](end_span).

---

## 📌 Project Overview

This analytics dashboard provides executive-level monitoring for hospitality operations, enabling teams to:
* **Simulate Booking Scenarios:** Interactively estimate successful bookings, gross revenue, and net income based on capacity, daily rates, and channel mix[span_1](start_span)[span_1](end_span).
* **Identify Commission Leakage:** Highlight excess dependency on third-party OTAs and calculate direct-booking recovery opportunities[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).
* **Track Key Hospitality KPIs:** Monitor Occupancy Rates, Average Daily Rates (ADR), Revenue per Available Room (RevPAR), and Cancellation Rates[span_4](start_span)[span_4](end_span).

---

## ⚙️ Business Rules & Strategic Thresholds

* **OTA Commission Rate:** Applied at an estimated **15.0%** across third-party booking channels[span_5](start_span)[span_5](end_span).
* **OTA Share Alert:** Triggers an automated strategy warning when OTA booking share exceeds **50.0%**[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).
* **Cancellation Target:** Designed to track and maintain booking cancellation leakage below **20.0%**[span_8](start_span)[span_8](end_span).
* **Direct Booking Recovery:** Target converting 10% of OTA bookings to direct channels to recover lost commission margins[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span).

---

## 📁 Repository Structure

```text
├── 365 hotels and resorts/
│   └── 365 Hotels & Resort (Students)/
│       ├── hotel_analytics.py              # Main Streamlit dashboard script
│       ├── fact_bookings.csv                # Historical booking transaction data
│       ├── fact_aggregated_bookings.csv     # Daily aggregated booking summary
│       ├── dim_hotels.csv                   # Property dimension dataset
│       ├── dim_rooms.csv                    # Room categories dataset
│       └── dim_date.csv                     # Date dimension table
├── requirements.txt                         # Python dependencies
└── README.md                                # Project documentation