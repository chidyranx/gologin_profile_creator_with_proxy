# GoLogin Proxy Profile Generator

This script fetches proxy profiles from Webshare.io API and creates corresponding profiles in GoLogin for automation purposes.

## Disclaimer

This script is provided for educational and informational purposes only. Usage of this script may violate the terms of service of Webshare.io and GoLogin. The developers of this script are not responsible for any misuse or damage caused by the usage of this script. Use it at your own risk.

## Requirements

- Python 3.x
- `gologin` library (`pip install gologin`)
- `requests` library (`pip install requests`)

## How it Works

1. **Fetching Proxy Profiles**: The script sends a request to the Webshare.io API to retrieve a list of proxy profiles.
2. **Creating GoLogin Profiles**: For each proxy profile obtained, the script creates a corresponding profile in GoLogin, setting up necessary parameters such as operating system, browser configuration, and proxy settings.
3. **Storing Profiles**: The generated GoLogin profiles are stored as text files on the local system for further usage.

## Usage

1. Obtain an API token from Webshare.io and replace the `token` variable in the script with your token.
2. Ensure you have installed the required libraries (`gologin` and `requests`) using `pip`.
3. Run the script using Python.

## Script Explanation

- The script starts by fetching proxy profiles from the Webshare.io API using an authentication token.
- It then iterates through the retrieved profiles, extracting details such as username, password, proxy address, and port.
- For each profile, it creates a corresponding GoLogin profile, specifying the necessary parameters like operating system, browser configuration, and proxy settings.
- Finally, it stores the generated GoLogin profiles as text files in a specified directory for later use.

## Usage Example

```bash
python gologin_proxy_profile_generator.py
