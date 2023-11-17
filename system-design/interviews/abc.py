files = [
"001-how-to-approach.md",
"002-design-rate-limiter.md",
"003-design-tiny-url.md",
"004-design-twitter.md",
"005-design-discord.md",
"006-design-you-tube.md",
"007-design-google-drive.md",
"008-design-google-maps.md",
"009-design-key-value-store.md",
"010-design-distributed-queue.md",
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
  <source src="http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/system-design/interviews/{file}" type="video/mp4">
</video>
"""
    f = open(filename,"a")
    f.write(s)
    f.close()
