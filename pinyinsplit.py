from pygtrie import CharTrie
import copy

"""
Split a Chinese Pinyin phrase into a list of possible permutations of Pinyin words.This is the "example" module.

For example,

>>> from pinyinsplit import PinyinSplit
>>> pys = PinyinSplit()
>>> pys.split('XiangGangDaXue')
[['Xiang', 'Gang', 'Da', 'Xue'], ['Xiang', 'Gang', 'Da', 'Xu', 'e'], ['Xi', 'ang', 'Gang', 'Da', 'Xue'], ['Xi', 'ang', 'Gang', 'Da', 'Xu', 'e']]
"""
class PinyinSplit:
    """Split a Chinese Pinyin phrase into a list of possible permutations of Pinyin words.

    It returns a list of all possible permutations of valid Pinyin words.
    If the Pinyin phrase cannot be exhaustively split into valid Pinyin words, an empty list will be returned.

    >>> from pinyinsplit import PinyinSplit
    >>> pys = PinyinSplit()
    >>> pys.split('shediaoyingxiongchuan')
    [['she', 'diao', 'ying', 'xiong', 'chuan'], ['she', 'diao', 'ying', 'xiong', 'chu', 'an'], ['she', 'di', 'ao', 'ying', 'xiong', 'chuan'], ['she', 'di', 'ao', 'ying', 'xiong', 'chu', 'an']]
    >>> pys.split('shediaoyingxiongchuanxyz')
    []
    
    """
    pylist = [
        'a', 'ai', 'an', 'ang', 'ao',
        'ba', 'bai', 'ban', 'bang', 'bao', 'bei', 'ben', 'beng',
        'bi', 'bian', 'biang', 'biao', 'bie', 'bin', 'bing', 'bo', 'bu',
        'ca', 'cai', 'can', 'cang', 'cao', 'ce', 'cen', 'ceng',
        'cha', 'chai', 'chan', 'chang', 'chao', 'che', 'chen', 'cheng',
        'chi', 'chong', 'chou', 'chu', 'chua', 'chuai', 'chuan', 'chuang', 'chui', 'chun', 'chuo',
        'ci', 'cong', 'cou', 'cu', 'cuan', 'cui', 'cun', 'cuo',
        'da', 'dai', 'dan', 'dang', 'dao', 'de', 'dei', 'den', 'deng',
        'di', 'dia', 'dian', 'diang', 'diao', 'die', 'ding', 'diu',
        'dong', 'dou', 'du', 'duan', 'dui', 'dun', 'duo',
        'e', 'ei', 'en', 'eng', 'er',
        'fa', 'fan', 'fang', 'fei', 'fen', 'feng', 'fiao',
        'fo', 'fou', 'fu', 'ga', 'gai', 'gan', 'gang', 'gao',
        'ge', 'gei', 'gen', 'geng', 'gong', 'gou',
        'gu', 'gua', 'guai', 'guan', 'guang', 'gui', 'gun', 'guo',
        'ha', 'hai', 'han', 'hang', 'hao', 'he', 'hei', 'hen', 'heng',
        'hong', 'hou', 'hu', 'hua', 'huai', 'huan', 'huang', 'hui', 'hun', 'huo',
        'ji', 'jia', 'jian', 'jiang', 'jiao', 'jie', 'jin', 'jing', 'jiong', 'jiu', 'ju', 'juan', 'jue', 'jun',
        'ka', 'kai', 'kan', 'kang', 'kao', 'ke', 'kei', 'ken', 'keng',
        'kong', 'kou', 'ku', 'kua', 'kuai', 'kuan', 'kuang', 'kui', 'kun', 'kuo',
        'la', 'lai', 'lan', 'lang', 'lao', 'le', 'lei', 'leng',
        'li', 'lia', 'lian', 'liang', 'liao', 'lie', 'lin', 'ling', 'liu', 'long', 'lou',
        'lu', 'luan', 'lue', 'lun', 'luo', 'lv', 'lve', 'lvn', 'lü', 'lüe', 'lün',
        'ma', 'mai', 'man', 'mang', 'mao', 'me', 'mei', 'men', 'meng',
        'mi', 'mian', 'miao', 'mie', 'min', 'ming', 'miu', 'mo', 'mou', 'mu',
        'na', 'nai', 'nan', 'nang', 'nao', 'ne', 'nei', 'nen', 'neng',
        'ni', 'nia', 'nian', 'niang', 'niao', 'nie', 'nin', 'ning', 'niu',
        'nong', 'nou', 'nu', 'nuan', 'nue', 'nun', 'nuo', 'nv', 'nve', 'nü', 'nüe', 'ou',
        'pa', 'pai', 'pan', 'pang', 'pao', 'pei', 'pen', 'peng',
        'pi', 'pian', 'piao', 'pie', 'pin', 'ping', 'po', 'pou', 'pu',
        'qi', 'qia', 'qian', 'qiang', 'qiao', 'qie',
        'qin', 'qing', 'qiong', 'qiu', 'qu', 'quan', 'que', 'qun',
        'ran', 'rang', 'rao', 're', 'ren', 'reng', 'ri', 'rong', 'rou',
        'ru', 'rua', 'ruan', 'rui', 'run', 'ruo',
        'sa', 'sai', 'san', 'sang', 'sao', 'se', 'sei', 'sen', 'seng',
        'sha', 'shai', 'shan', 'shang', 'shao', 'she', 'shei', 'shen', 'sheng', 'shi',
        'shong', 'shou', 'shu', 'shua', 'shuai', 'shuan', 'shuang', 'shui', 'shun', 'shuo',
        'si', 'song', 'sou', 'su', 'suan', 'sui', 'sun', 'suo',
        'ta', 'tai', 'tan', 'tang', 'tao', 'te', 'tei', 'teng',
        'ti', 'tian', 'tiao', 'tie', 'ting', 'tong', 'tou',
        'tu', 'tuan', 'tui', 'tun', 'tuo',
        'wa', 'wai', 'wan', 'wang', 'wei', 'wen', 'weng', 'wo', 'wu',
        'xi', 'xia', 'xian', 'xiang', 'xiao', 'xie', 'xin', 'xing', 'xiong', 'xiu', 'xu', 'xuan', 'xue', 'xun',
        'ya', 'yai', 'yan', 'yang', 'yao', 'ye', 'yi', 'yin', 'ying',
        'yo', 'yong', 'you', 'yu', 'yuan', 'yue', 'yun',
        'za', 'zai', 'zan', 'zang', 'zao', 'ze', 'zei', 'zen', 'zeng',
        'zha', 'zhai', 'zhan', 'zhang', 'zhao', 'zhe', 'zhei', 'zhen', 'zheng',
        'zhi', 'zhong', 'zhou', 'zhu', 'zhua', 'zhuai', 'zhuan', 'zhuang', 'zhui', 'zhun', 'zhuo',
        'zi', 'zong', 'zou', 'zu', 'zuan', 'zui', 'zun', 'zuo', 'ê'
    ]

    def __init__(self):
        self.trie = CharTrie()
        for py in self.pylist:
            self.trie[py] = len(py)

    def split(self, phrase):
        phrase_lc = phrase.lower()
        split_list = []
        results = []
        if phrase:
            split_list.append((phrase, phrase_lc, []))
        while split_list:
            pair = split_list.pop()
            phrase = pair[0]
            phrase_lc = pair[1]
            words = pair[2]
            matches = self.trie.prefixes(phrase_lc)
            for match in matches:
                n = match[1]
                word = phrase[:n]
                tail = phrase[n:]
                tail_lc = phrase_lc[n:]
                words_copy = copy.deepcopy(words)
                words_copy.append(word)
                if tail:
                    split_list.append((tail, tail_lc, words_copy))
                else:
                    results.append(words_copy)
        return results

if __name__ == "__main__":
    import doctest
    doctest.testmod()