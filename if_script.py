def age_check():
    if age >= 20:                          # 条件式１
        print("成人です")                  
    elif age >= 18:                        # 条件式２、条件式１がFalseの場合に実行
        print("成人ですが飲酒はできません")  
    elif age >= 6:                         # 条件式３，条件式１、２がFalseの場合に実行
        print("子どもです")
    else:                                  # 条件式４、上記条件の全てがFalseとなる場合に実行
        print("乳児・幼児です")
    
age = 5
age_check()