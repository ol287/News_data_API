import requests
import pandas as pd

# Define the API endpoint and parameters
api_url = "https://newsapi.org/v2/everything"
params = {
    "q": "political",
    "apiKey": "3fc6bfd0e2134566ae743a5eee447ebd"
}

try:
    # Make the API request
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an error for bad status codes

    # Parse the JSON response
    data = response.json()

    # Extract relevant data into a DataFrame
    if "articles" in data:
        df = pd.DataFrame(data["articles"])
        print("Data successfully retrieved and stored in a DataFrame.")
    else:
        print("No articles found in the API response.")
        df = pd.DataFrame()

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    df = pd.DataFrame()

# Display the DataFrame
print(df.head())

print(df.shape)

print(df.columns)