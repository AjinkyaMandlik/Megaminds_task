def lambda_handler(event, context):
    print("Data received and processing started")

    # Simple report
    report = {
        "message": "Daily data processed successfully"
    }

    print("Report generated:", report)

    return {
        "statusCode": 200,
        "body": report
    }
