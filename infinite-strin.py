import math


def repeatedString(s, n):
    k = s.count("a")*int(n/len(s))
    k += s[:n % len(s)].count("a")
    print(int(k))


repeatedString(
    "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq", 549382313570)
