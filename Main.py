from xmnlp import XmNLP

xm = XmNLP()


# 分词
def doc_seg(_doc):
    print('分词', xm.seg(_doc))


# 词性分析
def doc_tag(_doc):
    print('词性', list(xm.tag(_doc)))


# 纠错
def doc_checker(_doc):
    print('纠错', xm.checker(_doc))


# 摘要
def doc_keyphrase(_doc):
    print('摘要')
    for sentence in xm.keyphrase(_doc):
        for word in sentence:
            print(word, end='')
        print()


# 情感分析
def doc_sentiment(_doc):
    print('情感', xm.sentiment(_doc))


# 关键词词频
def doc_keyword(_doc):
    print('词频')
    for item in xm.keyword(_doc):
        print('{0:10s} {1:15f}'.format(item[0], item[1]))


# Main method
if __name__ == '__main__':
    doc = """
人生来得突然去也匆匆,在不断感受着幸福和快乐的同时也不断接受困难和挫折,在不断创造成功与希望的同时也不断接受着失败与折磨.
这是一段短暂而漫长的旅程,它丰富多采也荆棘丛生.
然而,知道这段旅程短暂的人才活得如此精彩,才更加珍惜生命,鏖战不停地与时间赛跑,才会有结实而雄厚的事业,有了困难和挫折才会使人不段完善自己的榜样,正如“河里没有岩石怎能激起美丽的浪花”,所以,不必对困境疑惑,它是人生的一大收获.
人嘛总得相信,有生就有死,有欢喜就有悲伤,有从逢就有离别,有成功就有失败,有暴雨必然会有晴天,就让它顺其自然吧.
    """

    doc_keyword(doc)
