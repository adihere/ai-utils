# Multimodal LangChain-Based App for Jira Data Classification

This project is a multimodal application that uses Hugging Face and Gradio to classify Jira data extracted from CSV files. The classification is based on a configurable prompt in a `config.json` file and categorizes the data into the following categories: Run the Enterprise, Change the Enterprise, Life Cycle Management, Tech Debt, Urgent Work, and Unclassified.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Configuration](#configuration)
- [Example](#example)
- [License](#license)

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/multimodal-jira-classifier.git
cd multimodal-jira-classifier
pip install -r requirements.txt
