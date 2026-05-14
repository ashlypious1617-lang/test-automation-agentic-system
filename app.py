import streamlit as st
import json
from datetime import datetime

# Mock test data based on the test-automation-schema
MOCK_TEST_CASES = {
    "Login Test": {
        "description": "Verify user login functionality",
        "steps": [
            {"id": 1, "action": "Navigate to login page", "status": "passed"},
            {"id": 2, "action": "Enter username", "status": "passed"},
            {"id": 3, "action": "Enter password", "status": "passed"},
            {"id": 4, "action": "Click login button", "status": "passed"},
            {"id": 5, "action": "Verify dashboard loads", "status": "passed"}
        ],
        "result": {
            "status": "passed",
            "execution_time": "2.3s",
            "timestamp": "2026-05-14T08:15:00Z"
        }
    },
    "Checkout Process": {
        "description": "Test e-commerce checkout flow",
        "steps": [
            {"id": 1, "action": "Add item to cart", "status": "passed"},
            {"id": 2, "action": "Navigate to cart", "status": "passed"},
            {"id": 3, "action": "Click checkout", "status": "passed"},
            {"id": 4, "action": "Enter shipping details", "status": "failed"},
            {"id": 5, "action": "Complete payment", "status": "skipped"}
        ],
        "result": {
            "status": "failed",
            "execution_time": "5.1s",
            "timestamp": "2026-05-14T08:10:00Z",
            "error": "Timeout waiting for shipping form to load"
        }
    },
    "API Health Check": {
        "description": "Verify API endpoints are responsive",
        "steps": [
            {"id": 1, "action": "Send GET request to /health", "status": "passed"},
            {"id": 2, "action": "Verify 200 status code", "status": "passed"},
            {"id": 3, "action": "Check response time < 500ms", "status": "failed"},
            {"id": 4, "action": "Validate response schema", "status": "passed"}
        ],
        "result": {
            "status": "failed",
            "execution_time": "1.8s",
            "timestamp": "2026-05-14T08:05:00Z",
            "error": "Response time exceeded threshold: 750ms"
        }
    }
}

def get_failure_analysis(test_case_name, test_data):
    """Generate failure analysis based on test results"""
    result = test_data["result"]
    
    if result["status"] == "passed":
        return "✅ **All tests passed successfully!** No issues detected."
    
    failed_steps = [step for step in test_data["steps"] if step["status"] == "failed"]
    
    if not failed_steps:
        return "⚠️ **Test marked as failed but no specific step failure identified.**"
    
    analysis = f"❌ **Failure Analysis for '{test_case_name}'**\n\n"
    analysis += f"**Failed Step(s):** {len(failed_steps)}\n\n"
    
    for step in failed_steps:
        analysis += f"- **Step {step['id']}**: {step['action']}\n"
    
    if "error" in result:
        analysis += f"\n**Error Message:** {result['error']}\n\n"
    
    # Pattern-based recommendations
    if "timeout" in result.get("error", "").lower():
        analysis += "**Possible Cause:** Timeout/Performance Pattern\n"
        analysis += "**Recommendation:** Check network latency, optimize page load, or increase timeout threshold.\n"
    elif "form" in result.get("error", "").lower():
        analysis += "**Possible Cause:** UI Element Not Found\n"
        analysis += "**Recommendation:** Verify element selectors, check for dynamic content loading.\n"
    elif "response time" in result.get("error", "").lower():
        analysis += "**Possible Cause:** Performance Degradation\n"
        analysis += "**Recommendation:** Investigate backend performance, database queries, or resource utilization.\n"
    else:
        analysis += "**Recommendation:** Review test logs and environment configuration.\n"
    
    return analysis

def main():
    st.set_page_config(page_title="Test Automation Analysis", page_icon="🧪", layout="wide")
    
    st.title("🧪 Test Automation Analysis")
    st.markdown("*Based on Test Automation Schema*")
    
    # Sidebar for test case selection
    st.sidebar.header("Select Test Case")
    test_case_names = list(MOCK_TEST_CASES.keys())
    selected_test = st.sidebar.selectbox("Test Case Name:", test_case_names)
    
    # Display test case details
    if selected_test:
        test_data = MOCK_TEST_CASES[selected_test]
        
        # Test Case Header
        st.header(f"📋 {selected_test}")
        st.markdown(f"*{test_data['description']}*")
        
        # Result Summary
        result = test_data["result"]
        col1, col2, col3 = st.columns(3)
        
        with col1:
            status_color = "🟢" if result["status"] == "passed" else "🔴"
            st.metric("Status", f"{status_color} {result['status'].upper()}")
        
        with col2:
            st.metric("Execution Time", result["execution_time"])
        
        with col3:
            st.metric("Timestamp", result["timestamp"].split("T")[1].split("Z")[0])
        
        st.divider()
        
        # Test Steps
        st.subheader("📝 Test Steps")
        
        for step in test_data["steps"]:
            status_icon = {
                "passed": "✅",
                "failed": "❌",
                "skipped": "⏭️"
            }.get(step["status"], "❓")
            
            col1, col2 = st.columns([1, 10])
            with col1:
                st.markdown(f"**{step['id']}**")
            with col2:
                st.markdown(f"{status_icon} {step['action']} *({step['status']})*")
        
        st.divider()
        
        # Failure Analysis
        st.subheader("🔍 Analysis")
        analysis = get_failure_analysis(selected_test, test_data)
        st.markdown(analysis)
        
        # Additional Info
        with st.expander("📊 View Raw Data"):
            st.json(test_data)

if __name__ == "__main__":
    main()

# Made with Bob
