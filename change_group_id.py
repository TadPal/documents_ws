import json

with open("./data.json", "r", encoding="utf-8") as f:
    data_official = json.load(f)
    with open("./data_new.json", "r", encoding="utf-8") as f2:
        data_rewrite = json.load(f2)

        for group in data_official["groups"]:
            for i, change_group in enumerate(data_rewrite["groups"]):
                
                if change_group["name"] == group["name"]:
                    old_id = change_group["id"]

                    for j, membership in enumerate(data_rewrite["memberships"]):

                        if membership["group_id"] == old_id:
                            data_rewrite["memberships"][j]["group_id"] = group["id"]

                    data_rewrite["groups"][i]["id"] = group["id"]
    
    with open("./data_final.json", "w", encoding="utf-8") as w:
        json.dump(data_rewrite, w, indent=4, ensure_ascii=False)