import requests

BASE_URL = "http://127.0.0.1:8000/api"


class NewsAPIClient:
    def __init__(self):
        self.session = requests.Session()

    def login(self, username, password):
        url = "http://127.0.0.1:8000/api/token/"
        response = self.session.post(url, json={
            "username": username,
            "password": password
        })

        data = response.json()

        if "access" in data:
            self.session.headers.update({
                "Authorization": f"Bearer {data['access']}"
            })
            return "LOGIN SUCCESS"

        return data

    def get_news(self):
        return self.session.get(f"{BASE_URL}/news/").json()

    def create_news(self, title, summary, content):
        return self.session.post(f"{BASE_URL}/news/", json={
            "title": title,
            "summary": summary,
            "content": content
        }).json()

    def update_news(self, news_id, **kwargs):
        return self.session.patch(
            f"{BASE_URL}/news/{news_id}/",
            json=kwargs
        ).json()

    def delete_news(self, news_id):
        return self.session.delete(
            f"{BASE_URL}/news/{news_id}/"
        ).status_code


if __name__ == "__main__":
    client = NewsAPIClient()

    print(client.login("admin", "Dimamiller2005"))

    print("ALL NEWS:")
    print(client.get_news())

    print("\nCREATE NEWS:")
    print(client.create_news(
        "Новость из клиента",
        "тест API клиента",
        "Создано через requests"
    ))