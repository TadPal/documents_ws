import json

with open("./systemdata_Users.json", "r", encoding="utf-8") as f:
    data_official = json.load(f)
    with open("./systemdata_membership.json", "r", encoding="utf-8") as f2:
        data_rewrite = json.load(f2)

        for user in data_official["users"]:
            for i, change_user in enumerate(data_rewrite["users"]):
                
                if change_user["email"] == user["email"]:
                    old_id = change_user["id"]

                    for j, membership in enumerate(data_rewrite["memberships"]):

                        if membership["user_id"] == old_id:
                            data_rewrite["memberships"][j]["user_id"] = user["id"]

                    data_rewrite["users"][i]["id"] = user["id"]
    
    with open("./systemdata_memberships_new.json", "w", encoding="utf-8") as w:
        json.dump(data_rewrite, w, indent=4, ensure_ascii=False)