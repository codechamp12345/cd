# def round_robin_load_balancing(servers, requests):
#     n = len(servers)

#     print("Round Robin Load Balancing\n")

#     for i, req in enumerate(requests):
#         server = servers[i % n]

#         print(f"Request {i+1}: '{req}' -> {server}")
#         print(f"{server} processed: '{req}'\n")


# # servers lists
# servers = ["Server1", "Server2", "Server3", "Server4"]

# # incoming requests
# requests = [
#     "Hello",
#     "Hi Arsalan",
#     "Login Request",
#     "Fetch Data",
#     "Update Profile",
#     "Logout",
#     "Upload File",
#     "Download File",
#     "Search Query",
#     "Payment Request"
# ]


# round_robin_load_balancing(servers, requests)


servers = ["Server1", "Server2", "Server3", "Server4"]
requests = ["Login", "Fetch", "Upload", "Search", "Payment"]

print("Round Robin Load Balancing\n")

i = 0
for req in requests:
    server = servers[i % len(servers)]
    print(req, "->", server)
    i += 1