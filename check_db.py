from backend.db.database import SessionLocal
from backend.db.models import RegulatoryRule

db = SessionLocal()
try:
    rules = db.query(RegulatoryRule).all()
    print(f"📊 Total Countries Scraped: {len(rules)}")
    for rule in rules:
        print(f"📍 {rule.country}: {len(rule.visa_policy)} characters of text found.")
finally:
    db.close()