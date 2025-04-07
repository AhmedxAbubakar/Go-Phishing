import re

def is_suspicious_email(email_body):
    patterns = [r"http[s]?://[^\s]+", r"urgent", r"click here", r"verify account"]
    for pattern in patterns:
        if re.search(pattern, email_body, re.IGNORECASE):
            return True
    return False

email = input("Paste the email body: ")
if is_suspicious_email(email):
    print("⚠️ Suspicious content detected.")
else:
    print("✅ Email looks clean.")
