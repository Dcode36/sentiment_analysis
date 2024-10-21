from textblob import TextBlob
import matplotlib.pyplot as plt

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    return polarity

def analyze_sentences(sentences):
    sentiment_results = {"Positive": 0, "Negative": 0, "Neutral": 0}
    polarity_scores = []

    for sentence in sentences:
        sentiment_score = get_sentiment(sentence)
        polarity_scores.append(sentiment_score)

        if sentiment_score > 0:
            sentiment_results["Positive"] += 1
        elif sentiment_score < 0:
            sentiment_results["Negative"] += 1
        else:
            sentiment_results["Neutral"] += 1

    return sentiment_results, polarity_scores

def calculate_percentage(sentiment_results, total):
    percentages = {key: (value / total) * 100 for key, value in sentiment_results.items()}
    return percentages

def plot_sentiment_chart(sentiment_results):
    labels = list(sentiment_results.keys())
    values = list(sentiment_results.values())

    plt.bar(labels, values, color=['green', 'red', 'blue'])
    plt.title('Sentiment Analysis Results')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Sentences')
    plt.show()

def plot_sentiment_pie_chart(sentiment_results):
    labels = list(sentiment_results.keys())
    values = list(sentiment_results.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['green', 'red', 'blue'])
    plt.title('Sentiment Distribution')
    plt.show()

# User input
user_input = input("Enter sentences separated by a semicolon (;): ").strip()
if not user_input:
    print("No input provided. Please enter sentences separated by a semicolon (;).")
else:
    sentences = user_input.split(';')

    # Analyze the sentences
    sentiment_results, polarity_scores = analyze_sentences(sentences)
    total_sentences = len(sentences)
    sentiment_percentages = calculate_percentage(sentiment_results, total_sentences)

    # Display the results
    print(f"Sentiment Analysis Results: {sentiment_results}")
    print(f"Polarity Scores of Sentences: {polarity_scores}")
    print(f"Sentiment Percentages: {sentiment_percentages}")

    # Plot the sentiment charts
    plot_sentiment_chart(sentiment_results)
    plot_sentiment_pie_chart(sentiment_results)
