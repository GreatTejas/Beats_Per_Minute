import sys
import threading
import math
def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        
        
        
        s = list(map(int, input().split()))
        ok = True
        for i in range(1, n):
            if p[i-1] % p[i] != 0:
                ok = False
                break
        for i in range(n-1):
            if s[i+1] % s[i] != 0:
                ok = False
                break
        if not ok:
            print("No")
            continue
        p_prev = 0
        
        
        s_next = 0  
        for i in range(n):
            l = p[i] // math.gcd(p[i], s[i]) * s[i]
            if math.gcd(p_prev, l) != p[i]:
                ok = False
                break
            s_next = s[i+1] if i+1 < n else 0
            if math.gcd(l, s_next) != s[i]:
                ok = False
                break
            p_prev = p[i]
        print("Yes" if ok else "No")
if __name__ == "__main__":
    threading.Thread(target=main).start()
