[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?branch=development_integrationtests&project=usdot-its-jpo-data-portal_datahub-ingest&metric=alert_status)](https://sonarcloud.io/dashboard?id=usdot-its-jpo-data-portal_datahub-ingest&branch=master) ![Build Status](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiQTh6cGZjZ1duZGRBZnoxZldxQjAxem1oTklDT1ZMMTFNbytGYUpTTHZYdEFCbDdoRlpVUHV3OU1MbW1kV1lyTUVGTGFRTnpBWVJaS3RYYk9wRnk1TkUwPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik0ycWx1NWFZNDRKSzdOSzciLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

# datahub-ingest

Collects metadata from ITS DataHub datasets and stores it in ElasticSearch.

## Getting Started

Test locally using the `unittest.sh` script.

### Prerequisites

- Python 3.7+
- PIP
- Virtualenv (required for testing with the unittest.sh script)

### Configuration

Required environment variables:

`ENVIRONMENT_NAME` - The name of your currently deployed environment
`SLACK_WEBHOOK_URL` - The full URL of your Slack webhook to which notifications will be sent

### Installing

Run `pip install -r requirements.txt`

## Testing

Install virtualenv, Python 3, and then run `unittest.sh`.

### Code style tests

Run `pip install pylint` followed by `pylint .`.

## Deployment

See AWS Lambda for instructions on how to deploy a Lambda function.

## Builds

This project is built using AWS CodeBuild.

## Contributions

Contribute to this repository using the Issues and Pull Requests features of GitHub.

## Authors

The ITS DataHub team.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Code.gov Registration Info

Agency: DOT
Short Description: The ITS DataHub dataset ingest lambad function.
Status: Beta
Tags: transportation, connected vehicles, intelligent transportation systems, python, lambda
Labor Hours: 0
Contact Name: Brian Brotsos
Contact Phone:
