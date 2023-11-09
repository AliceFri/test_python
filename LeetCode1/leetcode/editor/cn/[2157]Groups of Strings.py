# You are given a 0-indexed array of strings words. Each string consists of 
# lowercase English letters only. No letter occurs more than once in any string of 
# words. 
# 
#  Two strings s1 and s2 are said to be connected if the set of letters of s2 
# can be obtained from the set of letters of s1 by any one of the following 
# operations: 
# 
#  
#  Adding exactly one letter to the set of the letters of s1. 
#  Deleting exactly one letter from the set of the letters of s1. 
#  Replacing exactly one letter from the set of the letters of s1 with any 
# letter, including itself. 
#  
# 
#  The array words can be divided into one or more non-intersecting groups. A 
# string belongs to a group if any one of the following is true: 
# 
#  
#  It is connected to at least one other string of the group. 
#  It is the only string present in the group. 
#  
# 
#  Note that the strings in words should be grouped in such a manner that a 
# string belonging to a group cannot be connected to a string present in any other 
# group. It can be proved that such an arrangement is always unique. 
# 
#  Return an array ans of size 2 where: 
# 
#  
#  ans[0] is the maximum number of groups words can be divided into, and 
#  ans[1] is the size of the largest group. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["a","b","ab","cde"]
# Output: [2,3]
# Explanation:
# - words[0] can be used to obtain words[1] (by replacing 'a' with 'b'), and 
# words[2] (by adding 'b'). So words[0] is connected to words[1] and words[2].
# - words[1] can be used to obtain words[0] (by replacing 'b' with 'a'), and 
# words[2] (by adding 'a'). So words[1] is connected to words[0] and words[2].
# - words[2] can be used to obtain words[0] (by deleting 'b'), and words[1] (by 
# deleting 'a'). So words[2] is connected to words[0] and words[1].
# - words[3] is not connected to any string in words.
# Thus, words can be divided into 2 groups ["a","b","ab"] and ["cde"]. The size 
# of the largest group is 3.  
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["a","ab","abc"]
# Output: [1,3]
# Explanation:
# - words[0] is connected to words[1].
# - words[1] is connected to words[0] and words[2].
# - words[2] is connected to words[1].
# Since all strings are connected to each other, they should be grouped 
# together.
# Thus, the size of the largest group is 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 2 * 10⁴ 
#  1 <= words[i].length <= 26 
#  words[i] consists of lowercase English letters only. 
#  No letter occurs more than once in words[i]. 
#  
#  Related Topics 位运算 并查集 字符串 👍 43 👎 0
from typing import List
from collections import defaultdict, Counter

# leetcode submit region begin(Prohibit modification and deletion)
def parse(s):
    ret = 0
    for c in s:
        ret |= 1 << (ord(c) - 97)
    return ret


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        words = [parse(s) for s in words]

        f = list(range(len(words)))

        def find(i):
            if i != f[i]:
                f[i] = find(f[i])
            return f[i]

        def join(i, j):
            fi, fj = find(i), find(j)
            fj = find(j)
            if fi > fj:
                fi, fj = fj, fi
            f[fj] = fi

        st = set(words)
        mp, dl = {}, {}
        for i, s in enumerate(words):
            if s in mp:
                join(i, mp[s])
            else:
                mp[s] = i
            for k in range(26):
                if s & (1 << k):
                    s1 = s ^ (1 << k)
                    if s1 in mp and s1 in st:
                        join(mp[s1], i)
                    else:
                        mp[s1] = i
                    if s1 in dl:
                        join(dl[s1], i)
                    else:
                        dl[s1] = i

        g = Counter(map(find, range(len(words))))
        return [len(g), max(g.values())]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().groupStrings(["a", "b", "ab", "cde"]))
    print(Solution().groupStrings(["umeihvaq","ezflcmsur","ynikwecaxgtrdbu","u","q","gwrv","ftcuw","ocdgslxprzivbja","zqrktuepxs","cpqolvnwxz","geqis","xgfdazthbrolci","vwnrjqzsoepa","udzckgenvbsty","lpqcw","nekpvchqfgdo","iapjhxvdrmwetz","gw","waxokchnmifsruj","vqp","vbpkij","ufjvbstzh","swiu","knslbdcahfrox","ctofplkhednmv","g","zk","idretzjbpl","pxqdauys","mfgrqaktbzpv","vdtq","wyxjrcie","kl","jpcdzmli","oth","yumdawhfbskcjo","rvfksqhu","swemnvjpg","rnl","zgd","rmzdbcsqht","ure","qlusoaxprtebn","zkbmvtpya","jszxuwevfidkm","smlft","cpwugmbzfsqr","cblkjevhp","iyfnozaulex","qvlok","wsgm","du","awyplckj","aey","ycsjqnt","vtoqzsyx","ejqixsmrdhlofyp","kvlmurbzjg","lysdahgpwmrcn","af","jkezhdu","etjzqiyghdnovm","ycwdfnluoke","kwshbx","pyvaznljqwes","xakinu","e","zjexfgvhtabwcy","thuvwlnjkbxym","jorzeslpidmhubq","wnr","qzdv","qeovrbmwzgpdh","jkioenptaygfubh","bvndzxijope","cudizhjntbes","rnhzitpqoexwb","ihezcmfqouyl","q","mwtsdjqn","hrmc","hxaocbyikluvqsf","d","vgwjzuaondbcm","ibqxltf","rzyhguptmesqo","ruwgy","jvprwhtzuf","aupngodjexkiw","yhijelwpvtsrbqc","gtick","koilywcfbs","elv","dehxzlitskq","ptvbkql","msfxyjahlzo","oslxzfwrpmtyh","gypuchkwa","rsqij","tw","igbcylqfhtmjkr","nryhzjgi","pw","bnfairow","xjzrf","olxfypjtmrncuv","ifhue","akcvofuyzwbj","tvhxfeuiykpwbsz","wnrztclfpm","ozvypnfwrqg","cwkgr","gjyzrucplbsfe","pdtzmfoy","wehd","bnvqhcmg","uyw","sgynxljqbf","tvxbq","wcmguioelbdrkvx","okvtyexuj","hjbc","uidcswzm","jemtkvshizaub","rmb","jpgnqdemzcxa","dmalekhiyj","akocedu","rlpqufcv","r","lohgs","xapnorj","cdb","icopdtzxy","xcrflvojqgpkwt","rp","yv","u","atdxqeilhkg","olfvmrgkb","rplxskabvtqmhw","n","rldswkyoujmfxpn","rvgejzdusoya","hvoft","wskgmjchz","luagnzkj","ywe","i","wcqtsk","umpvywknjbxacsd","ynavjpcrgq","jyftmklci","xfol","zh","kut","zvawyielscotkn","p","wykpqdjoz","uabtpxkvq","uabtifwhrvxc","sdcamqup","srghwfptloxvke","sfdywtx","tuohnxzjqmac","pwxjyhdurnfz","axgfcuqtiyhjz","rwqpyh","bmoznqavicdgp","jcu","vnkc","jpb","nvfqyahjkul","radpctwixygb","pvjmk","s","dzyqjbwucne","mgh","ivc","eaqc","yjimsadtcwbgk","lo","ayirlsfevtwpnd","wcsk","xlvejy","kcjrqf","a","ixsdga","vk","cqxyfotziwrvl","zmxboiewhfdjlnr","kdpwngf","zyretijxpw","ncw","ljw","mrxeciy","aqwcofnjypsgi","byuvhj","ukidyqzhxgowmc","cpqsmu","auwmcrpdisbzokg","pxgwmvfq","azgljrsyeqwxfic","xmlgpdrzwqe","emgdcqntjpwrf","hrwq","zmjkx","npabcide","dvlfxnt","kilqsvmborf","lvsxjnbimhpzfow","sqcym","tcjmkwq","yugkwdzvmteon","pq","nklmb","azqcnodkimtxve","ovpcfe","uqkcwjimbvdyx","xvdazh","xk"]))
