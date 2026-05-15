# Test Automation Analysis App

A simple Streamlit application for analyzing test automation results based on the test-automation-schema.

## Features

- 📋 View test case details and descriptions
- 📝 Display test steps with pass/fail status
- 🔍 Automatic failure analysis with recommendations
- 📊 Mock data demonstrating different test scenarios

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

Start the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Usage

1. Select a test case from the sidebar dropdown
2. View test steps and their execution status
3. Review the failure analysis and recommendations
4. Expand "View Raw Data" to see the complete test data structure

## Mock Test Cases

The app includes three sample test cases:
- **Login Test** - Successful login flow (all steps passed)
- **Checkout Process** - Failed checkout with timeout issue
- **API Health Check** - Performance test with response time failure

## Schema Alignment

This app follows the test-automation-schema.jsonld structure:
- **TestCase**: Container for test scenarios
- **TestStep**: Individual actions within a test
- **TestResult**: Execution outcomes and analysis

## Project Screenshots

### Knowledge Graph
![Knowledge Graph](screenshots/knowledge-graph.png)

### CSV Data Ingestion
![CSV Upload](screenshots/csv-upload.png)

### MCP Configuration
![MCP Settings](screenshots/bob-mcp-settings.png)

### Streamlit UI
![Streamlit UI](screenshots/streamlit-ui.png)


## External Data Integration

A CSV data source was uploaded into IBM ICA Context Studio to simulate external test execution ingestion.

The ingested data includes:
- Test cases
- Test steps
- Execution results
- Failure scenarios