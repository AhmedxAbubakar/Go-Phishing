import re

def phishing_score(email_body):
    score = 0
    indicators = {
        "URLs": r"http[s]?://[^\s]+",
        "Shortened URLs": r"https?://(bit\.ly|tinyurl\.com|goo\.gl|t\.co|ow\.ly|is\.gd)/\S+",
        "Urgency": r"\b(urgent|immediately|asap|act now|important)\b",
        "Action Triggers": r"\b(click here|verify account|login now|update info|reset password)\b",
        "Spoof Warning": r"\b(from.*@.*\.ru|from.*@.*\.cn|reply-to:.*)\b",
        "Attachments": r"\b(attachment|invoice|receipt|doc|pdf|download)\b"
    }

    for label, pattern in indicators.items():
        matches = re.findall(pattern, email_body, re.IGNORECASE)
        if matches:
            print(f"⚠️ {label} detected: {len(matches)} occurrence(s).")
            score += len(matches)

    return score

def analyze_email(email_body):
    score = phishing_score(email_body)

    print("\n--- Risk Assessment ---")
    if score >= 5:
        print("🔴 High risk: Strong signs of phishing.")
    elif score >= 3:
        print("🟠 Medium risk: Some suspicious indicators found.")
    elif score >= 1:
        print("🟡 Low risk: Minor signs present.")
    else:
        print("✅ Clean: No obvious phishing indicators detected.")

# Run
email = input("Paste the email body: ")
analyze_email(email)
import re

def phishing_score(email_body):
    score = 0
    indicators = {
        "URLs": r"http[s]?://[^\s]+",
        "Shortened URLs": r"https?://(bit\.ly|tinyurl\.com|goo\.gl|t\.co|ow\.ly|is\.gd)/\S+",
        "Urgency": r"\b(urgent|immediately|asap|act now|important)\b",
        "Action Triggers": r"\b(click here|verify account|login now|update info|reset password)\b",
        "Spoof Warning": r"\b(from.*@.*\.ru|from.*@.*\.cn|reply-to:.*)\b",
        "Attachments": r"\b(attachment|invoice|receipt|doc|pdf|download)\b"
    }

    for label, pattern in indicators.items():
        matches = re.findall(pattern, email_body, re.IGNORECASE)
        if matches:
            print(f"⚠️ {label} detected: {len(matches)} occurrence(s).")
            score += len(matches)

    return score

def analyze_email(email_body):
    score = phishing_score(email_body)

    print("\n--- Risk Assessment ---")
    if score >= 5:
        print("🔴 High risk: Strong signs of phishing.")
    elif score >= 3:
        print("🟠 Medium risk: Some suspicious indicators found.")
    elif score >= 1:
        print("🟡 Low risk: Minor signs present.")
    else:
        print("✅ Clean: No obvious phishing indicators detected.")

# Run
email = input("Paste the email body: ")
analyze_email(email)
