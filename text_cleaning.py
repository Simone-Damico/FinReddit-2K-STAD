import re
import string

def preprocess_reddit_post(text: str) -> str:
    """
    Clean a raw text string by removing unwanted characters and formatting
    specific to social media posts (e.g., Reddit).
    
    This function applies the following cleaning steps:
    - Removes placeholder '[deleted]' tokens
    - Removes HTML tags
    - Removes URLs
    - Removes Reddit-specific prefixes (/r/, u/)
    - Removes tabulations, newlines, and other whitespace characters
    - Removes punctuation
    - Removes digits

    Parameters:
        text (str): The input text string to be cleaned.

    Returns:
        str: The cleaned text.
    """

    # Regex patterns for various unwanted elements
    regex_html = r'<.*?>'  # HTML tags
    regex_url = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    regex_whitespace = r'[\t\n\r\f\v]'  # Whitespace characters (tabs, newlines, etc.)
    regex_reddit_sub = r'/r/'  # Reddit subreddit notation
    regex_reddit_user = r'u/'  # Reddit user notation

    # Replace deleted marker
    text = text.replace('[deleted]', '')

    # Remove HTML, URLs, Reddit notations, and excess whitespace
    text = re.sub(regex_html, '', text)
    text = re.sub(regex_url, '', text)
    text = re.sub(regex_reddit_sub, '', text)
    text = re.sub(regex_reddit_user, '', text)
    text = re.sub(regex_whitespace, '', text)

    # Remove punctuation and digits
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)

    return text
