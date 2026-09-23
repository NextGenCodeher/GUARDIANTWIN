# 🏥 GuardianTwin – AI-Powered Health Monitoring System

GuardianTwin is a cloud-connected wearable health monitoring system
that uses Digital Twin concepts, machine-learning-based health risk
analysis, anomaly detection, and interactive visualization for
continuous patient monitoring.

## 🎯 Project Objective

The objective of GuardianTwin is to create a digital representation
of a patient's health condition using physiological and activity data.

In a real-world implementation, the health data would be collected
continuously from wearable devices. Since a physical wearable device
was unavailable during development, public wearable-health datasets
were used to simulate the monitoring workflow.

## ✨ Features

- Patient Caregiver Dashboard
- Digital Twin health monitoring
- Patient-specific baseline comparison
- Health anomaly detection
- Risk probability estimation
- Health stability analysis
- Heart-rate monitoring
- HRV monitoring using RMSSD and SDNN
- Sleep monitoring
- Daily activity/steps monitoring
- Fall-risk indication
- ML-based health insights
- Patient health event timeline
- Interactive Plotly visualizations
- Cloud-connected data access

## ☁️ Cloud Integration

GuardianTwin accesses the project dataset from cloud storage rather
than relying only on a local CSV file.

This allows the dashboard to retrieve patient data from a remotely
accessible source and demonstrates a cloud-connected monitoring
architecture.

## ⌚ Real-Time Monitoring Simulation

The intended system architecture collects physiological information
from wearable devices.

For the prototype, public wearable-health data is used in place of
a physical smartwatch. Patient records can be processed sequentially
to simulate the flow of continuously arriving wearable data.

## 🧠 Digital Twin Concept

GuardianTwin maintains patient-specific baseline health information
and compares current observations against those baselines.

Changes in parameters such as heart rate, sleep, activity, RMSSD,
and SDNN can therefore be used to identify deviations from the
patient's expected physiological behaviour.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Machine Learning
- Digital Twin concepts
- Cloud-based data integration
- Git
- GitHub

## 📊 Dashboard Modules

### Patient Overview
Provides the caregiver with the patient's current health status,
health stability, anomalies, activity, stress indicators and fall risk.

### Digital Twin
Compares current patient measurements with personalized baseline
values and visualizes health trends.

### ML Insights
Displays health-risk information, anomaly statistics, severity
distribution and risk trends.

### Event Log
Provides a chronological view of patient health events, severity
levels and monitoring recommendations.

## 🚀 Future Scope

- Integration with real smartwatches and wearable sensors
- Live IoT data ingestion
- Real-time cloud streaming
- Mobile caregiver notifications
- Emergency alerts
- Integration with hospital monitoring systems
- Enhanced predictive health models

## 👥 Contributors

Developed as part of the GuardianTwin wearable-based digital twin
health monitoring project.
