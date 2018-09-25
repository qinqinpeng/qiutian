import csv
import json

data = [{"id": "00001",
         "name": "小明",
         "职业": "B站UP主"},
        {"id": "00002",
         "name": "叽叽",
         "职业": "第五人格UP"},
        {"id": "00003",
         "name": "蛋喵",
         "职业": "星露谷UP"}
        ]
with open("info.json", "a", encoding="utf-8") as file:
    file.write(json.dumps(data, indent=4, ensure_ascii=False))

with open("info.csv", "w", encoding="utf-8", newline="") as csvfile: # 加上newline=""是为了
    # 除去空行，否则在生成的csv文件中，每一行数据后面都有空行
    write = csv.writer(csvfile, delimiter=",")  # writer()初始化写入对象， 用writerow()传入每一行数据
    write.writerow(["id", "name", "职业"])
    write.writerows([["00001", "ming", "teacher"],
                     ["00002", "ming", "teacher"],
                     ["00003", "ming", "teacher"]])
    # 可以直接传字典
    # with open("info.csv", "w") as csvfile:
    #     fieldnames = ['id', 'name', '职业']
    #     write = csv.DictWriter(csvfile, fieldnames=fieldnames) # 初始化一个字典对象
    #     write.writeheader()   # 写入表格的头信息
    #     write.writerow({"id": "00001",
    #      "name": "小明",
    #      "职业": "B站UP主"})
    #     write.writerow({"id": "00002",
    #      "name": "叽叽",
    #      "职业": "第五人格UP"})
    #     write.writerow({"id": "00003",
    #      "name": "蛋喵",
    #      "职业": "星露谷UP"})
with open("info.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
