**Medical Supply Forecast Visualization**

A Python-based tool for forecasting daily medical supply usage using Simple Moving Average (SMA) and Weighted Moving Average (WMA) techniques. It also detects anomalies in usage data and provides trend analysis to support better decision-making in medical supply management.

___

## **Table of Contents**

1. [Features](#features)
2. [Usage](#usage)
3. [Examples](#examples)
4. [Technologies Used](#technologies-used)

___

## **Features**
** Anomaly Detection**
Why I Included It:
The task emphasizes effective management of medical supplies and the importance of accurate forecasting to avoid shortages. However, even the best forecasting models can be compromised if there are anomalies (unexpected spikes or drops) in the data. These anomalies could stem from unusual hospital activities (e.g., a sudden increase in PPE usage due to an unexpected outbreak) or data entry errors.

Contextual Example:
Imagine the daily usage of Personal Protective Equipment (PPE) in a hospital during a pandemic. If the hospital suddenly sees a massive spike in PPE usage on one day (e.g., from an average of 120 units to 300 units), it might skew the forecast, leading to over-ordering and unnecessary costs. Conversely, if there's an unexplained drop (e.g., due to a data entry error showing only 20 units used), the forecast might predict insufficient stock, risking shortages in critical moments.

By adding anomaly detection, I can filter or flag such outliers, ensuring the forecasts are based on reliable data, which directly supports the task's goal of accurate supply forecasting.
___

- **Trend Analysis:**
Why I Included It:
While the task focuses on forecasting the next day's usage, understanding long-term trends helps in making strategic supply decisions. Identifying whether supply usage is consistently increasing or decreasing allows hospitals to plan more effectively—not just for the next day, but for the coming weeks or months.

Contextual Example:
Let’s say the usage of surgical gloves is steadily increasing over the past month, indicating rising patient numbers or an increase in surgical procedures. A simple moving average (SMA) would give a flat forecast based on recent averages, but it wouldn’t account for this upward trend. By incorporating trend analysis, I can adjust forecasts to better reflect real-world conditions, preventing potential supply shortages before they become critical.

___

- **Forecasting:** Predicts future supply needs using SMA and WMA methods.

- **Logging:** Automatically logs key activities and anomalies for tracking.

---


## **Usage**

1. **Run the script:**
   ```bash
   python forecast.py
   ```


3. **Check Logs:**  
   Logs are saved in `forecast_log.txt` to help track anomalies and forecasting results.

---

## **Examples**

### **Sample Data:**
```python
daily_usage = [100, 120, 110, 130, 125, 115, 140]  # there is no anomaly
```

### **Sample Output:**
```yaml
Anomalies detected with values: []
Simple Moving Average Forecast: 120.0
Weighted Moving Average Forecast: 124.46
Trend Analysis: increasing
```

---

## **Technologies Used**

- **Python**
- **Logging Module** for tracking data processing
- **Basic Statistics** for trend and anomaly detection 
-**ChatGPT** for debugging 
-**Google** for research on the task especially the meaning of SMA and WMA their use and differences

---