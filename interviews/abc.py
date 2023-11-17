
import glob

files = glob.glob("*.md")
files.sort()

for f in files:
    filename = f.split(".")[0]
    content = ""
    with open(f) as file:
        content = file.read()
        content = content.replace(
            "/images/interviews", "http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/interviews")
    with open(f,'w') as file:
        file.write(content)
    