# coding: UTF-8
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["test1","ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ","test"]
# source=["test1","test2"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    #python2の場合 word =raw_input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}は見つかりません".format(word))

if __name__ == "__main__":
    search()
