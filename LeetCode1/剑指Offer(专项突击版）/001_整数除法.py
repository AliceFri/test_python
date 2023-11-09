class Solution:
    def divide(self, a: int, b: int) -> int:
        if b == 1:
            return a
        bFuShu = False
        iFuShu = 0
        if a < 0:
            a = -a
            iFuShu += 1
        if b < 0:
            b = -b
            iFuShu += 1
        if iFuShu == 1:
            bFuShu = True

        iRet = 0

        while a >= b:

            iSub = b
            iAdd = 1
            # 用减法代替除法, 减去的值*2， 得到的结果*2 指数减
            # tcp慢启动也是该原理!!!!!!!!!!!!!!!!!!!!!!!!
            while a >= iSub + iSub:
                iSub += iSub
                iAdd += iAdd
            a -= iSub
            iRet += iAdd

        iRet = iRet if not bFuShu else -iRet
        if iRet >= 2 ** 31:
            return 2 ** 31 - 1
        return iRet