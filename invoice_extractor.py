import pdfplumber
import json
import ollama


def extract_invoice_data(pdf_path):
    # Step 1: Read PDF
    raw_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            raw_text += page.extract_text() + "\n"

    # Step 2: Clean text
    cleaned_text = "\n".join(
        [line.strip() for line in raw_text.split("\n") if line.strip()]
    )

    # Step 3: Prompt
    prompt = f"""
Extract the following fields from this invoice.
Return ONLY valid JSON.
If a field is missing, return null.

Fields:
invoice_number
invoice_date
due_date
billed_by
billed_to
line_items
subtotal
discount
tax_or_gst
total_amount
currency
payment_method
notes

Invoice text:
{cleaned_text}
"""

    # Step 4: Call Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "Extract invoice data and return only valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response["message"]["content"]

    # Step 5: Clean markdown and extra text
    if "```json" in result:
        result = result.split("```json")[1].split("```")[0].strip()
    elif "```" in result:
        result = result.split("```")[1].strip()

    # Step 6: Convert to JSON
    try:
        data = json.loads(result)
        return data
    except:
        print("JSON Error")
        print(result)
        return None


invoice_files = [
    "invoices/invoice_1.pdf",
    "invoices/invoice_2.pdf",
    "invoices/invoice_3.pdf"
]

for i, file in enumerate(invoice_files, start=1):
    output = extract_invoice_data(file)

    if output:
        print(f"\nInvoice {i} Output:")
        print(json.dumps(output, indent=4))

        with open(f"outputs/output_invoice_{i}.json", "w") as f:
            json.dump(output, f, indent=4)