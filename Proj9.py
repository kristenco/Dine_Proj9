import requests

url_ddg = "https://api.duckduckgo.com"
def test_ddg0():
    resp = requests.get(url_ddg + "/?q=presidents%20of%20the%20united%20states&format=json")
    rsp_data = resp.json()
    RelatedTopics = rsp_data.get('RelatedTopics')
    presidents = []
    dupe_names = ["Bush", "Roosevelt", "Adams", "Johnson", "Harrison"]
    good_names = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Van",
                  "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson",
                  "Grant", "Hayes", "Garfield", "Arthur", "Cleveland", "Harrison", "McKinley", "Roosevelt", "Taft",
                  "Wilson", "Harding", "Coolidge", "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon",
                  "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"]
    for i in RelatedTopics:
        for x in i['Text'].split(" "):
            if x in good_names:
                if x == "Van":
                    presidents.append("Van Buren")
                else:
                    presidents.append(x)

        presidents_list = list(dict.fromkeys(presidents))
        for z in dupe_names:
            presidents_list.append(z)
    sorted_presidents_list = sorted(presidents_list)
    for i in sorted_presidents_list:
        print(i)
    assert "Presidents of the United States" in rsp_data["Heading"]

test_ddg0()
