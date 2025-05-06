import ckan.plugins.toolkit as tk
import ckanext.ckanstrageapi.logic.schema as schema

import os
import requests

@tk.side_effect_free
def ckanstrageapi_get_sum(context, data_dict):
    tk.check_access(
        "ckanstrageapi_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.ckanstrageapi_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }

def ckanStrageCatalogData(context, data_dict):
    # パラメータ取得
    file_id = data_dict.get("file_id")
    file_type = data_dict.get("file_type")
    token = data_dict.get("token")

    if not file_id or not file_type or not token:
        raise tk.ValidationError("Missing required parameters")

    # 外部APIのURL例
    url = f"https://example.com/api/download?file_id={file_id}&type={file_type}"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # 外部APIにリクエスト
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise tk.ValidationError(f"Failed to download file: {response.status_code}")

    # 保存先パス（※要調整）
    save_dir = "/srv/app/downloads"
    os.makedirs(save_dir, exist_ok=True)

    file_path = os.path.join(save_dir, f"{file_id}_{file_type}.bin")

    # ファイル保存
    with open(file_path, "wb") as f:
        f.write(response.content)

    return {
        "message": "File downloaded successfully",
        "path": file_path
    }

def get_actions():
    return {
        'ckanstrageapi_get_sum': ckanstrageapi_get_sum,
    }
