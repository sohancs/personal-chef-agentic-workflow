**Steps to Run the App**

1. **Start the MCP Server**

   ```bash
   cd mcp-server
   uvicorn groceries_server:app --reload --host 0.0.0.0 --port 8085
   ```

   * Keep this terminal running while the app is in use.

2. **Start the ADK Web UI**

   * Open a new terminal and run:

     ```bash
     adk web
     ```
   * The app will be accessible at:

     ```
     http://127.0.0.1:8000/dev-ui/
     ```

3. **Select the Workflow**

   * In the ADK Web UI, choose **`agentic_workflow`** from the dropdown menu in the top-left corner.

> **Note:** ADK looks for `agent.py` inside the `agentic_workflow` folder, where the `SequentialAgent` is defined, to start the workflow.
