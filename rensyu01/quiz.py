import random

def shutudai():
    qa = random.choice(qa_list)
    print("じゃじゃん！！",qa["q"])
    return qa["a"]

def kai(a_list):
    kai = input("答えを入力して下さい：")
    print("入力した答えは：", kai)
    if kai in a_list:
        print("正解です。。。")
    else:
        print("不正解です。")


if __name__ == "__main__":
    qa_list =[{"q" : "サザエさんの旦那の名前は？","a": ["ますお","マスオ"]},{"q" : "カツオの妹の名前は？", "a": ["わかめ","ワカメ"]},{"q" : "タラオはカツオから見てどんな関係？", "a": ["甥","おい","甥っ子",""]}]
    a_list = shutudai()
    kai(a_list)

