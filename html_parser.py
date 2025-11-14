import re

html = input()

title_pattern = r"<title>(.*?)</title>"
title_match = re.search(title_pattern, html)
title = title_match.group(1) if title_match else ""

body_pattern = r"<body>(.*?)</body>"
body_match = re.search(body_pattern, html, re.DOTALL)

if body_match:
    body_content = body_match.group(1)


    content = re.sub(r"<[^>]*>", "", body_content)

    content = content.replace("\\n", "")

    content = re.sub(r"\s+", " ", content).strip()
else:
    content = ""

print(f"Title: {title}")
print(f"Content: {content}")