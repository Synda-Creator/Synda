import logging
import random
import json
import time
from logger import setup_logger

# Initialize the logger
logger = setup_logger("ai_thinker")


def think_about_data(data):
    """Simulate AgentAyla thinking by performing data analysis."""
    logger.info("AgentAyla is thinking...")

    # Simulate some processing time to think
    time.sleep(random.uniform(1, 3))

    # Perform basic data analysis
    analysis_result = {
        "mean": sum(data) / len(data),
        "median": sorted(data)[len(data) // 2],
        "max": max(data),
        "min": min(data),
        "std_dev": (sum((x - (sum(data) / len(data))) ** 2 for x in data) / len(data)) ** 0.5
    }

    logger.info("Analysis completed.")
    logger.info(f"Analysis Result: {analysis_result}")

    return analysis_result


if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = [random.randint(1, 100) for _ in range(20)]
    logger.info(f"Sample Data: {sample_data}")

    result = think_about_data(sample_data)
    print(json.dumps(result, indent=4))
