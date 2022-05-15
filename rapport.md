# 检查第一个词（加入list-word），如果可以组合，查看下一个词，如在dict里且在regle里面，加入list-word，记录词性（第一个词性）
#                                                           如不在dict里，加入list-word
#                                                               如在dict里但不在regle里，输出list-word，清空list-word，从第一步重新开始
# 如果已经有两个dic词并且有mark，那么就输出
# mark: 如果后续有组合mark，那么就代替先前mark
# if 遇到duplicate (list_word)，输出

