import requests
import validators

def validate_url(url):
    """Check if a URL is valid and safe."""
    # Validate the URL format
    if not validators.url(url):
        print("Invalid URL format. Please try again.")
        return

    try:
        # Perform a GET request to check the URL's status
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"URL is accessible: {url}")
            print("The link appears safe, but always verify manually.")
        else:
            print(f"URL responded with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error while connecting to the URL: {e}")
        print("This link could be unsafe or inactive.")

if __name__ == "__main__":
    print("Welcome to the Phishing Link Validator!")
    user_url = input("Enter a URL to validate: ").strip()
    validate_url(user_url)

