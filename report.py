def generate_report(file_name, hash_value, status):

    report = f"""
DIGITAL FORENSIC VALIDATION REPORT

Evidence File: {file_name}
SHA-256 Hash: {hash_value}

Status: {status}
"""

    with open("reports/forensic_report.txt", "w") as f:
        f.write(report)

    print("Report generated in reports/forensic_report.txt")