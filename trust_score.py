def calculate_trust_score(results, url):
    pos = sum(1 for r in results if r["label"] == "POSITIVE")
    neg = sum(1 for r in results if r["label"] == "NEGATIVE")
    total = len(results) if results else 1

    sentiment_score = ((pos - neg) / total + 1) * 50  # 0–100

    diversity_score = min(100, total * 5)
    domain_score = 70 if any(x in url for x in ["amazon", "daraz", "ebay"]) else 40

    trust = (0.5 * sentiment_score) + (0.3 * diversity_score) + (0.2 * domain_score)
    return round(trust, 2)
