with open("src/components/Header.tsx", "r") as f:
    text = f.read()
text = text.replace("Let&apos;s talk</p>", "Resume</p>", 1)
text = text.replace("Let's talk", "Let&apos;s talk")
text = text.replace("Don't see", "Don&apos;t see")
with open("src/components/Header.tsx", "w") as f:
    f.write(text)
