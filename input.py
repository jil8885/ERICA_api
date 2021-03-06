import json

def cafe():
    with open('cafe.json') as json_file:
        data = json.load(json_file)

    while True:
        name = input("가게 이름 입력: ")
        if name in data.keys():
            continue
        elif name != "":
            data[name] = {}
            phone = input("전화 번호 입력: ")
            place = input("장소 링크 입력: ")
            if phone:
                data[name]['phone'] = phone
            if place:
                data[name]['place'] = place
        else:
            break

    with open('cafe.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))


def food():
    with open('restaurant.json') as json_file:
        data = json.load(json_file)

    while True:
        name = input("가게 이름 입력: ")
        if name in data.keys():
            continue
        elif name != "":
            data[name] = {}
            phone = input("전화 번호 입력: ")
            place = input("장소 링크 입력: ")
            data[name]['cat'] = input("분류 입력: ")
            data[name]['menu'] = input("메뉴 입력: ")
            if phone:
                data[name]['phone'] = phone
            if place:
                data[name]['place'] = place
        else:
            break

    with open('restaurant.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))
food()
