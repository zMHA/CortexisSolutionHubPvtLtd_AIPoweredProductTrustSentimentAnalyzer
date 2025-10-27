import gradio as gr
from scraper import scrape_reviews
from sentiment import analyze_sentiment
from trust_score import calculate_trust_score

def analyze_product(url):
    reviews = scrape_reviews(url)
    if not reviews:
        return "❌ No reviews found or invalid URL.", None, None

    results = analyze_sentiment(reviews)
    trust = calculate_trust_score(results, url)

    summary = {
        "Positive": sum(1 for r in results if r["label"] == "POSITIVE"),
        "Neutral": sum(1 for r in results if r["label"] == "NEUTRAL"),
        "Negative": sum(1 for r in results if r["label"] == "NEGATIVE"),
    }

    recommendation = (
        "✅ Trusted Product" if trust >= 80 else
        "⚠️ Be Cautious" if trust >= 50 else
        "🚫 Likely Fraudulent"
    )

    result_text = (
        f"**Trust Score:** {trust}%\n\n"
        f"**Summary:** {summary}\n\n"
        f"**Recommendation:** {recommendation}"
    )
    return result_text, [r["text"] for r in results], recommendation

iface = gr.Interface(
    fn=analyze_product,
    inputs=gr.Textbox(label="Paste Product URL"),
    outputs=[
        gr.Markdown(label="Results Summary"),
        gr.JSON(label="Sample Reviews"),
        gr.Textbox(label="AI Recommendation"),
    ],
    title="🧠 AI-Powered Product Trust & Sentiment Analyzer",
    description="Paste any product or website URL to check its overall trustworthiness and sentiment.",
)

if __name__ == "__main__":
    iface.launch()
