
import wikipedia
import webbrowser
import json
import time

wikipedia.set_lang("en")


def save_article(title, url, content):
    article = {
        "title": title,
        "url": url,
        "content": content
    }

    with open("article.json", "w", encoding="utf-8") as file:
        json.dump(article, file, ensure_ascii=False, indent=4)

    print("Article saved successfully!")


def random_wiki():
    while True:
        try:
            title = wikipedia.random(pages=1)
            page = wikipedia.page(title, auto_suggest=False)

            content = page.content


            if not content.strip():
                print("Empty article. Trying another...")
                continue

            print("\n" + "=" * 70)
            print(f"TITLE: {page.title}")
            print(f"URL: {page.url}")
            print("=" * 70)

            webbrowser.open(page.url)

            save_article(page.title, page.url, content)

            return content

        except wikipedia.exceptions.DisambiguationError:
            print("Disambiguation encountered. Trying another article...")

        except wikipedia.exceptions.PageError:
            print("Invalid page. Trying another article...")

        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")
            print("Trying another article...")
            time.sleep(2)


get_new = True
while True:
    if get_new == True:
        content = random_wiki()
        get_new = False

    what_to_do = input()

    if what_to_do == "New Article":
        content = random_wiki()
        time.sleep(5)

    elif what_to_do == "Exit":
        break

    else:
        if content and what_to_do in content:
            print("ALLOWED")
        else:
            print("DENIED")
