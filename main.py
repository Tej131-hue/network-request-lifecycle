import time

def simulate_request_flow(url):
    print(f"\nUser enters URL: {url}")
    time.sleep(1)

    print("→ Performing DNS Lookup...")
    time.sleep(1)

    print("→ IP Address Resolved: 93.184.216.34")
    time.sleep(1)

    print("→ Sending HTTP Request to Server...")
    time.sleep(1)

    print("→ Server is processing the request...")
    time.sleep(1)

    print("→ Response received: 200 OK")
    print("→ Webpage successfully loaded!\n")


if __name__ == "__main__":
    website = input("Enter a website URL: ")
    simulate_request_flow(website)