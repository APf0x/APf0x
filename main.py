import requests
import markdown


def fetch_daily_quote():
    response = requests.get('https://zenquotes.io/api/today')
    
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data[0]['q']
    else:
        return None

with open("README.md", 'r') as file:
    markdown_content = file.read()


daily_quote = fetch_daily_quote()

if daily_quote:

    html_content = markdown.markdown(markdown_content)
    

    html_content = html_content.replace('<!-- Daily Quote Placeholder -->', f'<blockquote>{daily_quote}</blockquote>')
    

    modified_markdown = markdown.markdown(html_content)



    

    with open("README.md", 'w') as file:
        file.write(modified_markdown)
