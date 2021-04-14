# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
#
#  实现词典类 WordDictionary ：
#
#
#  WordDictionary() 初始化词典对象
#  void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
#  bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回 false 。word 中可能包含一些 '
# .' ，每个 . 都可以表示任何一个字母。
#
#
#
#
#  示例：
#
#
# 输入：
# ["WordDictionary","addWord","addWord","addWord","search","search","search","se
# arch"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
#
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#
#
#  提示：
#
#
#  1 <= word.length <= 500
#  addWord 中的 word 由小写英文字母组成
#  search 中的 word 由 '.' 或小写英文字母组成
#  最多调用 50000 次 addWord 和 search
#
#  Related Topics 深度优先搜索 设计 字典树 回溯算法
#  👍 233 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = dict()

    def addWord(self, word: str) -> None:
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = dict()
            tree = tree[a]
        tree["#"] = "#"

    def search(self, word: str) -> bool:
        def helper(word, tree):
            if not word:
                return True if "#" in tree else False

            if word[0] == ".":
                for a in tree:
                    if a == "#": continue
                    if helper(word[1:], tree[a]): return True
                else:
                    return False
            else:
                if word[0] not in tree:
                    return False
                else:
                    return helper(word[1:], tree[word[0]])

        return helper(word, self.lookup)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# leetcode submit region end(Prohibit modification and deletion)
