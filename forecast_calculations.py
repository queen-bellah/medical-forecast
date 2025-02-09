import logging

# Setting up logging to keep track of what the code does
logging.basicConfig(
    filename='forecast_log.txt',   # Save logs in this file
    level=logging.INFO,            # Log important information
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format for log messages
)

def detect_anomalies(usage_list):
    """
    Find unusually high values in the usage data.
    """
    if not usage_list:
        logging.error("The usage list is empty.")
        raise ValueError("The usage list is empty. Please provide valid data.")

    mean_usage = sum(usage_list) / len(usage_list)
    threshold = 1.5 * mean_usage  # Anything 1.5 times above the average is flagged

    anomalies = [value for value in usage_list if value > threshold]
    if anomalies:
        logging.warning(f"Anomalies detected with values: {anomalies}")
    else:
        logging.info("No anomalies detected in the data.")

    return anomalies


def analyze_trends(usage_list):
    """
    Check if usage is generally going up, down, or staying the same.
    """
    if not usage_list:
        logging.error("The usage list is empty.")
        raise ValueError("The usage list is empty. Please provide valid data.")

    if usage_list[-1] > usage_list[0]:
        trend = "increasing"
    elif usage_list[-1] < usage_list[0]:
        trend = " decreasing "
    else:
        trend = "stable"

    logging.info(f"Trend analysis result: {trend}")
    return trend


def forecast_usage_sma(usage_list):
    """
    Predict the next day's usage using a simple average.
    """
    if not usage_list:
        logging.error("The usage list is empty.")
        raise ValueError("The usage list is empty. Please provide valid data.")

    anomalies = detect_anomalies(usage_list)
    clean_usage_list = [usage for usage in usage_list if usage not in anomalies]  # Remove anomalies

    sma_forecast = sum(clean_usage_list) / len(clean_usage_list)
    logging.info(f"SMA calculated: {sma_forecast} based on cleaned input: {clean_usage_list}")

    return round(sma_forecast, 2)


def forecast_usage_wma(usage_list):
    """
    Predict the next day's usage giving more weight to recent days.
    """
    if not usage_list:
        logging.error("The usage list is empty.")
        raise ValueError("The usage list is empty. Please provide valid data.")

    anomalies = detect_anomalies(usage_list)
    clean_usage_list = [usage for usage in usage_list if usage not in anomalies]  # Remove anomalies

    weights = list(range(1, len(clean_usage_list) + 1))  # More recent days get higher weights
    weighted_sum = sum(usage * weight for usage, weight in zip(clean_usage_list, weights))
    wma_forecast = weighted_sum / sum(weights)

    logging.info(f"WMA calculated: {wma_forecast} based on cleaned input: {clean_usage_list} with weights: {weights}")

    return round(wma_forecast, 2)


# Sample data: the number 300 is unusually high and will be flagged as an anomaly
# daily_usage = [100, 120, 110, 300, 125, 115]  
daily_usage = [100, 120, 110, 130, 125, 115, 140]

# Find and display anomalies
anomalies = detect_anomalies(daily_usage)
print("Anomalies detected with values:", anomalies)

# Forecast using Simple Moving Average
sma_forecast = forecast_usage_sma(daily_usage)
print("Simple Moving Average Forecast:", sma_forecast)

# Forecast using Weighted Moving Average
wma_forecast = forecast_usage_wma(daily_usage)
print("Weighted Moving Average Forecast:", wma_forecast)

# Analyze the trend in the data
trend = analyze_trends(daily_usage)
print("Trend Analysis:", trend)
