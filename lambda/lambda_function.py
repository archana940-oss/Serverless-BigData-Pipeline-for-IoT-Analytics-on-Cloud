

import json
from datetime import datetime


def lambda_handler(event, context):
    """
    Sample Lambda function to simulate IoT data processing.
    """

    response = {
        "status": "Success",
        "message": "IoT data processed successfully.",
        "project": "Serverless Big Data Pipeline for IoT Analytics on Cloud",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response, indent=4)
    }
