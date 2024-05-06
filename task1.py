def keyword_highlighter(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    highlighted_reviews = []

    for review in reviews:
        for keyword in keywords:
            if keyword in review.lower():
                review = review.replace(keyword, keyword.upper())
        highlighted_reviews.append(review)
    
    return highlighted_reviews


reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
print("\n".join(keyword_highlighter(reviews)))

def sentiment_tally(reviews, positive_words, negative_words):
    tally_results = []

    for review in reviews:
        pos_count = sum(review.lower().count(word) for word in positive_words)
        neg_count = sum(review.lower().count(word) for word in negative_words)
        tally_results.append((pos_count, neg_count))

    return tally_results


positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

sentiment_counts = sentiment_tally(reviews, positive_words, negative_words)
for count in sentiment_counts:
    print(f"Positive words: {count[0]}, Negative words: {count[1]}")




def review_summary(reviews):
    summaries = []

    for review in reviews:
        if len(review) > 30:
            summary = review[:30].rstrip()
            if review[30] != ' ':
                summary = summary[:summary.rfind(' ')]
            summaries.append(summary + "...")
        else:
            summaries.append(review)
    
    return summaries


for summary in review_summary(reviews):
    print(summary)


