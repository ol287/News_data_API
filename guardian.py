import requests
import pandas as pd

# Define the API endpoint and parameters
api_url = "https://content.guardianapis.com/search"
params = {
    "q": "political",
    "api-key": "68c37710-31f8-4617-a1ee-2e6a94250c8a"
}

try:
    # Make the API request
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an error for bad status codes

    # Parse the JSON response
    data = response.json()

    # Extract relevant data into a DataFrame
    if "response" in data and "results" in data["response"]:
        df = pd.DataFrame(data["response"]["results"])
        print("Data successfully retrieved and stored in a DataFrame.")
    else:
        print("No results found in the API response.")
        df = pd.DataFrame()

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    df = pd.DataFrame()

# Display the DataFrame
print(df.head())
