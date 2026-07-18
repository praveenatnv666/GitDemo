import playwright
from playwright.sync_api import sync_playwright

url = "https://reqres.in"
Key_value = "free_user_3En5rQAZsQEuyZWkgFUK8ngsU5A"
payload = {
    "name": "John1",
    "job": "QA Engineer"
}


def get_api(p):
    page = p.request.new_context(base_url=url)
    response = page.get("api/users", params={"page": 2}, headers={"x-api-key": Key_value})
    print(response.json())
    print(response.status)

def post_api(p):
    page = p.request.new_context(base_url = url)
    response = page.post("api/users",headers={"x-api-key": Key_value}, data=payload)
    print(response.json())
    print(response.status)

def main():
    with sync_playwright() as p:
        get_api(p)
        post_api(p)

if __name__ == "__main__":
    main()