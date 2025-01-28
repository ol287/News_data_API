import requests
import pandas as pd

# Define the API endpoint and parameters
api_url = "https://newsdata.io/api/1/news"
params = {
    "apikey": "pub_66912f12c56b8cad28d3ff6776c4e3a6c80e5",
    "q": "political"
}

try:
    # Make the API request
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an error for bad status codes

    # Parse the JSON response
    data = response.json()

    # Extract relevant data into a DataFrame
    if "results" in data:
        df = pd.DataFrame(data["results"])
        print("Data successfully retrieved and stored in a DataFrame.")
    else:
        print("No results found in the API response.")
        df = pd.DataFrame()

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    df = pd.DataFrame()

# Display the DataFrame
print(df.head())

