import sys
line = sys.stdin.readline
# h1,m1,s1,h2,m2,s2=0,0,0,0,0,0
# def tictoc():
#     global n,m,h1,h2,m1,m2,s1,s2
#     s1+=n/m
#     s2+=1

#     if 60<=s1:
#         m1+=s1//60
#         s1=s1%60
#         if 60<=m1:
#             h1+=m1//60
#             m1=m1%60
#             if 12<=h1:
#                 h1=h1%12
#     if 0>s1:
#         m1+=s1//60
#         s1=60-(-s1%60)
#         if s1==60:
#             s1=0
#         if 0>m1:
#             h1+=m1//60
#             m1=60-(-m1%60)
#             if m1==60:
#                 m1=0
#             if 0>h1:
#                 h1=12-(-h1%12)
#                 if h1==12:
#                     h1=0
#     if 60<=s2:
#         m2+=s2//60
#         s2=s2%60
#         if 60<=m2:
#             h2+=m2//60
#             m2=m2%60
#             if 12<=h2:
#                 h2=h2%12


n,m=map(int,line().split())

print(int(abs(n/m-1)*2))
# cnt=0
# tick=0
# tictoc()
# while True:
#     # print(h1,m1,s1,':',h2,m2,s2)
#     if tick==3600*24:
#         break
#     if h1==h2 and m1==m2 and s1==s2:
#         cnt+=1
#     tictoc()
#     tick+=1
# print(cnt)