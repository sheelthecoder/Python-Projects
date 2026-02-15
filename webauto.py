import webbrowser as wb

def webauto():
    chrome_path = '"C:\Program Files (x86)\Google\Chrome\Application" %s'
    URLS = (
        "google.com",
        "github.com",
        "youtube.com"
    )
    for url in URLS:
        print("Opening :"+url)
        wb.get(chrome_path).open(url)
        
webauto()
        