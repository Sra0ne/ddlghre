from flask import Flask, redirect, request
import requests
import json

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_to_latest_release(path):
    # Parse the GitHub repository URL from the request path
    parts = path.split('/')
    owner = parts[0]
    repo = parts[1]

    # Query the GitHub API to get the latest release information
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url)
    data = json.loads(response.text)

    # Extract the download URL of the latest release asset
    url = None
    for asset in data['assets']:
        if asset['name'].endswith('.zip'):
            url = asset['browser_download_url']
            break

    # Redirect to the latest release download URL
    if url is not None:
        return redirect(url, code=302)
    else:
        return f"Error: no ZIP assets found for {owner}/{repo}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

