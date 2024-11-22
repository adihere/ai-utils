import gradio as gr
import pandas as pd
import json

# Load configuration
config_path = "config/config.json"
with open(config_path) as config_file:
    config = json.load(config_file)

# Mock classifier for demonstration, as the actual Hugging Face model can't run in the browser
def mock_classifier(description):
    categories = config["categories"]
    return {
        "labels": categories,
        "scores": [0.1] * len(categories)
    }

def classify_jira_data(file):
    # Read CSV file
    df = pd.read_csv(file.name)

    # Ensure the CSV has a 'Description' column for classification
    if 'Description' not in df.columns:
        return "CSV file must contain a 'Description' column"

    categories = config["categories"]

    results = []
    for description in df["Description"]:
        prediction = mock_classifier(description)
        best_category = prediction["labels"][0]
        results.append({
            "Description": description,
            "Category": best_category,
            "Score": prediction["scores"][0]
        })

    result_df = pd.DataFrame(results)
    return result_df

def main():
    interface = gr.Interface(
        fn=classify_jira_data,
        inputs=gr.File(label="Upload CSV File"),
        outputs=gr.Dataframe(label="Classification Results"),
        title="Jira Data Classifier",
        description="Upload a CSV file with Jira data and classify descriptions into predefined categories.",
    )
    interface.launch()

if __name__ == "__main__":
    main()