def round_robin_load_balancing(servers, requests):
    n = len(servers)

    print("Round Robin Load Balancing\n")

    for i, req in enumerate(requests):
        server = servers[i % n]

        print(f"Request {i+1}: '{req}' -> {server}")
        print(f"{server} processed: '{req}'\n")


# servers list
servers = ["Server1", "Server2", "Server3", "Server4"]

# incoming requests
requests = [
    "Hello",
    "Hi Arsalan",
    "Login Request",
    "Fetch Data",
    "Update Profile",
    "Logout",
    "Upload File",
    "Download File",
    "Search Query",
    "Payment Request"
]


round_robin_load_balancing(servers, requests)