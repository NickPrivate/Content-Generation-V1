import requests
import json
import time

def generate_script(prompt):
    api_url = "http://localhost:5000/api/generate"

    payload = {
        "prompt": prompt,
        "length": 150,
        "model": "llama3"
    }

    headers = {
        "Content-Type": "application/json"
    }

    print("Sending request to the server...")
    response = requests.post(api_url, headers=headers, data=json.dumps(payload), stream=True)

    print("Received response from the server")
    print("Response status code:", response.status_code)

    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                try:
                    json_line = json.loads(decoded_line)
                    yield json_line['response']
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                time.sleep(0.05)
    else:
        yield f"Failed to generate script: {response.status_code} - {response.text}"

if __name__ == "__main__":
    prompt = "Create a script about the top 5 parks in Los Angeles."
    script = generate_script(prompt)
    if script:
        print("Generated Script:")
        print(script)
    else:
        print("Script generation failed.")
