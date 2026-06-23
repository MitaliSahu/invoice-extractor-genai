# Automated Invoice Data Extractor

This project extracts structured invoice data from PDF files using **Python**, **pdfplumber**, and **Ollama (local LLM)**.

## Project Overview

The Automated Invoice Data Extractor is a Python-based pipeline that reads invoice PDF files, extracts the text, processes it, and converts it into structured JSON data automatically.

This project helps reduce manual invoice data entry and improves speed and accuracy.

## Features

* Reads invoice PDF files
* Extracts raw text using `pdfplumber`
* Cleans and preprocesses invoice text
* Uses **Ollama (local LLM)** for structured data extraction
* Converts extracted data into JSON format
* Saves outputs as `.json` files

## Technologies Used

* Python
* pdfplumber
* Ollama
* JSON

## Installation

Clone the repository:

```bash
git clone https://github.com/MitaliSahu/invoice-extractor-genai.git
cd invoice-extractor-genai
```

Create virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama (if not installed):

Visit: https://ollama.com

Pull the model:

```bash
ollama pull llama3.2
```

## Project Structure

invoice-extractor-genai/
├── invoice_extractor.py
├── README.md
├── requirements.txt
├── invoices/
│   ├── invoice_1.pdf
│   ├── invoice_2.pdf
│   └── invoice_3.pdf
└── outputs/
├── output_invoice_1.json
├── output_invoice_2.json
└── output_invoice_3.json

## How to Run

Run the script:

```bash
python invoice_extractor.py
```

The extracted JSON files will be saved in the `outputs/` folder.

## Tested Invoice Types

1. Utility Bill
2. Service Invoice
3. Purchase Invoice

## Sample Output

```json
{
  "invoice_number": "INV001",
  "invoice_date": "23-06-2026",
  "due_date": "30-06-2026",
  "billed_by": "Apple Solutions",
  "billed_to": "Rahul Sharma",
  "total_amount": 4950,
  "currency": "INR"
}
```

## Author

Mitali Sahu
