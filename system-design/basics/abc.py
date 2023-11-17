files = [
    "00-computer-architecture.mp4",
    "01-application-architecture.mp4",
    "02-design-requirements.mp4",
    "03-networking-basics.mp4",
    "04-tcp-and-udp.mp4",
    "05-dns.mp4",
    "06-http.mp4",
    "07-websockets.mp4",
    "08-api-paradigms.mp4",
    "09-api-design.mp4",
    "10-caching.mp4",
    "11-cdns.mp4",
    "12-proxies-and-load-balancing.mp4",
    "13-consistent-hashing.mp4",
    "14-sql.mp4",
    "15-nosql.mp4",
    "16-replication-and-sharding.mp4",
    "17-cap-theorem.mp4",
    "18-object-storage.mp4",
    "19-message-queues.mp4"
]


for file in files:
    parts = file.split(".")
    filename = parts[0] + ".md"
    # subprocess.run(["touch", filename])
    parts = parts[0].split("-")
    parts = parts[1:]
    for i, part in enumerate(parts):
        parts[i] = part.capitalize()

    heading = " ".join(parts)

    s = f"""

## {heading} 

<video width="1000" height="240" controls>
  <source src="http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/system-design/basics/{file}" type="video/mp4">
</video>
"""
    f = open(filename, "a")
    f.write(s)
    f.close()