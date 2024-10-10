import json
from typing import Mapping


category_file = "records.json"

async def save_user_record(user_id: int, record: Mapping[str, float | int | str]) -> None:
    try:
        with open(category_file, "r") as f:
            data = json.load(f)
    except json.decoder.JSONDecodeError:
        data = []

    with open(category_file, "r") as f:
        data = json.load(f)

    data.append(record)
    
    with open(category_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


async def get_user_recods(user_id: int) -> list[str]:
    with open(category_file, "r") as f:
        data = json.load(f)
        return data.get(str(user_id), [])