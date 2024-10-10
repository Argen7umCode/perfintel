import json


category_file = "categories.json"

def get_categories_from_text(text: str) -> list[str]:
    return list(set(category.strip() for category in text.split(',')))

async def save_user_categories(user_id: int, categories: list[str]) -> None:
    try:
        with open(category_file, "r") as f:
            data = json.load(f)
    except json.decoder.JSONDecodeError:
        data = {}

    with open(category_file, "r") as f:
        data = json.load(f)

    data[str(user_id)] = categories
    
    with open(category_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


async def get_user_categories(user_id: int) -> list[str]:
    with open(category_file, "r") as f:
        data = json.load(f)
        return data.get(str(user_id), [])