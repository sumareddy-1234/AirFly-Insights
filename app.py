import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AirFly Insights", layout="wide")

st.title("✈️ AirFly Insights – Airline Operations Dashboard")

df = pd.read_csv("cleaned_flights.csv")

# -----------------------------
# Sidebar Navigation
# -----------------------------

st.sidebar.title("Dashboard Navigation")

section = st.sidebar.radio(
    "Select Section",
    [
        "Data Overview",
        "Traffic & Airport Activity",
        "Route Analysis",
        "Airport Performance",
        "Delay Analysis",
        "Delay Causes",
        "Seasonal Insights",
        "Airline Performance",
        "Operational Results"
    ]
)

# -----------------------------
# Filters
# -----------------------------

st.sidebar.header("Filters")

airline = st.sidebar.selectbox(
    "Airline",
    ["All"] + sorted(df["AIRLINE"].unique())
)

if airline != "All":
    df = df[df["AIRLINE"] == airline]

# -----------------------------
# KPI Metrics
# -----------------------------

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Flights", len(df))
col2.metric("Average Arrival Delay", round(df["ARR_DELAY"].mean(),2))
col3.metric("Airports", df["ORIGIN"].nunique())
col4.metric("Cancelled Flights", int(df["CANCELLED"].sum()))

# -----------------------------
# DATA OVERVIEW
# -----------------------------

if section == "Data Overview":

    st.subheader("Dataset Sample")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Summary Statistics")
    st.write(df.describe())

# -----------------------------
# TRAFFIC ACTIVITY
# -----------------------------

elif section == "Traffic & Airport Activity":

    st.subheader("Top Busiest Origin Airports")

    top_airports = df["ORIGIN"].value_counts().head(10).reset_index()
    top_airports.columns = ["ORIGIN", "Count"]

    fig = px.bar(top_airports, x="Count", y="ORIGIN", orientation='h',
                 title="Top 10 Busiest Origin Airports",
                 labels={"Count": "Number of Flights", "ORIGIN": "Origin Airport"},
                 color_discrete_sequence=['#1f77b4'])
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Hourly Flight Traffic")

    hourly = df["HOUR"].value_counts().sort_index().reset_index()
    hourly.columns = ["HOUR", "Count"]

    fig = px.bar(hourly, x="HOUR", y="Count",
                 title="Hourly Flight Traffic",
                 labels={"HOUR": "Hour of the Day", "Count": "Number of Flights"},
                 color_discrete_sequence=['#ff7f0e'])
    
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# ROUTE ANALYSIS
# -----------------------------

elif section == "Route Analysis":

    st.subheader("Top Routes by Average Delay")

    route_delay = df.groupby("ROUTE")["ARR_DELAY"].mean().sort_values(ascending=False).head(10).reset_index()

    fig = px.bar(route_delay, x="ARR_DELAY", y="ROUTE", orientation='h',
                 title="Top 10 Routes by Average Arrival Delay",
                 labels={"ARR_DELAY": "Average Delay (Minutes)", "ROUTE": "Route"},
                 color_discrete_sequence=['#d62728'])
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Route Congestion Bubble Analysis")

    route_stats = (
        df.groupby("ROUTE")
        .agg(
            FLIGHT_COUNT=("ROUTE","count"),
            AVG_ARR_DELAY=("ARR_DELAY","mean"),
            TOTAL_DELAY=("ARR_DELAY","sum")
        )
        .reset_index()
    )

    fig = px.scatter(route_stats, x="FLIGHT_COUNT", y="AVG_ARR_DELAY", size="TOTAL_DELAY", hover_name="ROUTE",
                     title="Route Congestion & Delay Intensity Analysis",
                     labels={"FLIGHT_COUNT": "Flight Volume (Number of Flights)",
                             "AVG_ARR_DELAY": "Average Arrival Delay (Minutes)",
                             "TOTAL_DELAY": "Total Delay"},
                     color="AVG_ARR_DELAY",
                     color_continuous_scale="Viridis",
                     opacity=0.7,
                     size_max=40)
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# AIRPORT PERFORMANCE
# -----------------------------

elif section == "Airport Performance":

    st.subheader("1. Airport vs Month Delay Heatmap")

    top_airports = df.groupby("ORIGIN")["ARR_DELAY"].mean().sort_values(ascending=False).head(10).index
    df_top = df[df["ORIGIN"].isin(top_airports)]

    airport_delay = df_top.groupby(["ORIGIN","MONTH"])["ARR_DELAY"].mean().reset_index()
    airport_delay_pivot = airport_delay.pivot(index="ORIGIN", columns="MONTH", values="ARR_DELAY")

    fig = px.imshow(airport_delay_pivot, text_auto=".1f", aspect="auto",
                    color_continuous_scale="Reds",
                    title="Top 10 Airports vs Month Average Delay",
                    labels=dict(x="Month", y="Airport", color="Avg Delay"))
                    
    fig.update_xaxes(type='category')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("2. Airport Delay Heatmap (Origin vs Destination)")
    top_dest = df['DEST'].value_counts().head(10).index
    df_filtered = df[df['ORIGIN'].isin(top_airports) & df['DEST'].isin(top_dest)]
    delay_matrix = df_filtered.pivot_table(values='ARR_DELAY', index='ORIGIN', columns='DEST', aggfunc='mean')
    
    fig_matrix = px.imshow(delay_matrix, text_auto=".1f", aspect="auto",
                           color_continuous_scale="rdbu_r",
                           title="Airport Delay Heatmap (Top 10 Origins vs Top 10 Destinations)",
                           labels=dict(x="Destination Airport", y="Origin Airport", color="Avg Delay"))
    st.plotly_chart(fig_matrix, use_container_width=True)
    
    st.subheader("3. Operationally Stressed Airports")
    airport_stats = df.groupby('ORIGIN').agg({'ARR_DELAY':'mean', 'ORIGIN':'count'}).rename(columns={'ORIGIN':'FLIGHT_COUNT'})
    airport_stats['STRESS_INDEX'] = airport_stats['ARR_DELAY'] * airport_stats['FLIGHT_COUNT']
    top_stress = airport_stats.sort_values('STRESS_INDEX', ascending=False).head(10).reset_index()

    fig_stress = px.bar(top_stress, x='STRESS_INDEX', y='ORIGIN', orientation='h',
                        title="Top 10 Operationally Stressed Airports",
                        labels={'STRESS_INDEX': 'Stress Index (Delay * Flights)', 'ORIGIN': 'Origin Airport'},
                        color='STRESS_INDEX', color_continuous_scale="Reds")
    fig_stress.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_stress, use_container_width=True)

# -----------------------------
# DELAY ANALYSIS
# -----------------------------

elif section == "Delay Analysis":

    st.subheader("1. Departure vs Arrival Delay Relationship")
    fig_scatter = px.scatter(df, x="DEP_DELAY", y="ARR_DELAY",
                             title="Departure vs Arrival Delay Relationship",
                             labels={"DEP_DELAY": "Departure Delay (Minutes)", "ARR_DELAY": "Arrival Delay (Minutes)"},
                             opacity=0.3,
                             color_discrete_sequence=['#8c564b'])
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("2. Average Arrival Delay by Day of Week")
    if "DAY_OF_WEEK" in df.columns:
        day_mapping = {
            0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 
            4: "Friday", 5: "Saturday", 6: "Sunday"
        }
        day_delay = df.groupby("DAY_OF_WEEK")["ARR_DELAY"].mean().reset_index()
        day_delay["Day_Name"] = day_delay["DAY_OF_WEEK"].map(day_mapping)
        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        fig = px.bar(day_delay, x="Day_Name", y="ARR_DELAY",
                     title="Average Arrival Delay by Day of Week",
                     labels={"ARR_DELAY": "Average Delay (Minutes)", "Day_Name": "Day of the Week"},
                     category_orders={"Day_Name": day_order},
                     color="ARR_DELAY", color_continuous_scale="Blues")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("3. Delay Pattern by Month and Hour")
    pivot = df.pivot_table(values='ARR_DELAY', index='MONTH', columns='HOUR', aggfunc='mean')
    fig = px.imshow(pivot, aspect="auto",
                    color_continuous_scale="YlOrRd",
                    title="Average Delay Heatmap: Month vs Hour of Day",
                    labels=dict(x="Hour of Day", y="Month", color="Avg Delay"))
    fig.update_yaxes(type='category')
    fig.update_xaxes(type='category')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("4. Average Delay by Distance (Binned)")
    bins = [0, 500, 1000, 1500, 2000, 2500, 3000, 10000]
    labels = ["<500", "500-1000", "1000-1500", "1500-2000", "2000-2500", "2500-3000", "3000+"]
    df["DISTANCE_BIN"] = pd.cut(df["DISTANCE"], bins=bins, labels=labels)
    dist_delay = df.groupby("DISTANCE_BIN", observed=True)["ARR_DELAY"].mean().reset_index()
    
    fig = px.bar(dist_delay, x="DISTANCE_BIN", y="ARR_DELAY",
                 title="Average Arrival Delay by Flight Distance Bins",
                 labels={"DISTANCE_BIN": "Distance (Miles)", "ARR_DELAY": "Average Delay (Minutes)"},
                 color="ARR_DELAY", color_continuous_scale="Purples")
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# DELAY CAUSES
# -----------------------------

elif section == "Delay Causes":

    st.subheader("Total Delay Minutes by Cause")

    delay_causes = df[
        [
            "DELAY_DUE_CARRIER",
            "DELAY_DUE_WEATHER",
            "DELAY_DUE_NAS",
            "DELAY_DUE_SECURITY",
            "DELAY_DUE_LATE_AIRCRAFT"
        ]
    ].sum().reset_index()
    delay_causes.columns = ["Cause", "Total Delay"]

    fig = px.bar(delay_causes, x="Total Delay", y="Cause", orientation='h',
                 title="Total Delay Minutes by Cause",
                 labels={"Total Delay": "Total Delay Minutes", "Cause": "Delay Cause"},
                 color="Cause",
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Percentage Contribution of Delay Causes")
    fig2 = px.pie(delay_causes, values="Total Delay", names="Cause",
                  title="Percentage Contribution of Delay Causes",
                  hole=0.3,
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# SEASONAL INSIGHTS
# -----------------------------

elif section == "Seasonal Insights":

    st.subheader("1. Seasonal Delay Comparison")

    df["SEASON"] = df["MONTH"].map({
        12:"Winter",1:"Winter",2:"Winter",
        3:"Spring",4:"Spring",5:"Spring",
        6:"Summer",7:"Summer",8:"Summer",
        9:"Autumn",10:"Autumn",11:"Autumn"
    })

    season_stats = df.groupby("SEASON")["ARR_DELAY"].mean().reset_index()

    fig = px.bar(season_stats, x="SEASON", y="ARR_DELAY",
                 title="Seasonal Average Delay Comparison",
                 labels={"SEASON": "Season", "ARR_DELAY": "Average Delay (Minutes)"},
                 color="SEASON",
                 color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("2. Monthly Delay Volatility (Operational Stability)")
    monthly_volatility = df.groupby('MONTH')["ARR_DELAY"].std().reset_index()
    
    fig_vol = px.line(monthly_volatility, x="MONTH", y="ARR_DELAY", markers=True,
                      title="Monthly Delay Volatility (Operational Stability)",
                      labels={"MONTH": "Month", "ARR_DELAY": "Delay Standard Deviation"})
    fig_vol.update_xaxes(type='category')
    st.plotly_chart(fig_vol, use_container_width=True)
    
    st.subheader("3. Weather vs Carrier Delay Trend")
    monthly_cause = df.groupby('MONTH')[['DELAY_DUE_WEATHER', 'DELAY_DUE_CARRIER']].mean().reset_index()
    
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(x=monthly_cause['MONTH'], y=monthly_cause['DELAY_DUE_WEATHER'],
                                   mode='lines+markers', name='Weather Delay'))
    fig_trend.add_trace(go.Scatter(x=monthly_cause['MONTH'], y=monthly_cause['DELAY_DUE_CARRIER'],
                                   mode='lines+markers', name='Carrier Delay'))
    fig_trend.update_layout(title="Weather vs Carrier Delay Trend",
                            xaxis_title="Month",
                            yaxis_title="Average Delay (Minutes)",
                            xaxis=dict(type='category'))
    st.plotly_chart(fig_trend, use_container_width=True)

# -----------------------------
# AIRLINE PERFORMANCE
# -----------------------------

elif section == "Airline Performance":

    st.subheader("1. Top 10 Airlines by Average Arrival Delay")

    airline_delay = df.groupby("AIRLINE")["ARR_DELAY"].mean().sort_values(ascending=False).head(10).reset_index()

    fig = px.bar(airline_delay, x="ARR_DELAY", y="AIRLINE", orientation='h',
                 title="Top 10 Airlines by Average Arrival Delay",
                 labels={"ARR_DELAY": "Average Arrival Delay (Minutes)", "AIRLINE": "Airline"},
                 color="ARR_DELAY",
                 color_continuous_scale="OrRd")
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("2. Top 10 Airlines by Delay Rate (>15 min)")
    df['IS_DELAYED'] = (df['ARR_DELAY'] > 15).astype(int)
    delay_rate = df.groupby('AIRLINE')['IS_DELAYED'].mean().sort_values(ascending=False).head(10).reset_index()
    
    fig_rate = px.bar(delay_rate, x='IS_DELAYED', y='AIRLINE', orientation='h',
                      title="Top 10 Airlines by Delay Rate (>15 min)",
                      labels={'IS_DELAYED': 'Delay Rate (Proportion of Flights Delayed)', 'AIRLINE': 'Airline'},
                      color='IS_DELAYED',
                      color_continuous_scale="Reds")
    fig_rate.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_rate, use_container_width=True)

# -----------------------------
# OPERATIONAL RESULTS
# -----------------------------

elif section == "Operational Results":

    st.subheader("Flight Status Distribution")

    df["FLIGHT_STATUS"] = "On Time"
    df.loc[df["ARR_DELAY"] > 15,"FLIGHT_STATUS"] = "Delayed"
    df.loc[df["CANCELLED"] == 1,"FLIGHT_STATUS"] = "Cancelled"

    status_percent = (df["FLIGHT_STATUS"].value_counts(normalize=True)*100).reset_index()
    status_percent.columns = ["Status", "Percentage"]

    fig = px.bar(status_percent, x="Status", y="Percentage",
                 title="Flight Status Distribution (%)",
                 labels={"Status": "Flight Status", "Percentage": "Percentage of Flights (%)"},
                 color="Status",
                 color_discrete_map={"On Time": "#2ca02c", "Delayed": "#ff7f0e", "Cancelled": "#d62728"})
    st.plotly_chart(fig, use_container_width=True)