import matplotlib.pyplot as plt



chord = \
[[0.992716247547708,0.0675299444931347],
[0.971311753165686,0.0774685947998831],
[0.926464241127163,0.0935597429155711],
[0.887732298912074,0.107284545720129],
[0.840846263599073,0.123848962898043],
[0.792940966648832,0.139940111013731],
[0.754209024433744,0.152245106631610],
[0.704265204209025,0.169282792871750],
[0.658398430533262,0.184900671925212],
[0.613550918494739,0.197205667543091],
[0.551375958623150,0.211403739409874],
[0.482066167290886,0.224182004089980],
[0.441295701801320,0.228914694712241],
[0.344465846263599,0.227968156587789],
[0.249674514000357,0.205251241600935],
[0.189538077403246,0.178748174116272]]
twist = \
[[0.188525000000000,0.267420715740471],
[0.998830357142857,0.110935408786733],
[0.974337500000000,0.112349432644748],
[0.925351785714286,0.114706139074775],
[0.877386607142857,0.118476869362816],
[0.822277678571429,0.122718940936864],
[0.725326785714286,0.131674425370963],
[0.757983928571429,0.129317718940937],
[0.633478571428571,0.143929298807099],
[0.670217857142857,0.138744544661042],
[0.576328571428572,0.151470759383183],
[0.516116964285714,0.162311608961303],
[0.436515178571429,0.182107942973523],
[0.381406250000000,0.195776840267675],
[0.295681250000000,0.230184754146058],
[0.326297321428571,0.216515856851906],
[0.264044642857143,0.246210357870236],
[0.225264285714286,0.264121326738435],
[0.209956250000000,0.269306080884492]]


r1 = [_[0] for _ in chord]
c  = [_[1] for _ in chord]
r2 = sorted([_[0] for _ in twist])
beta = sorted([_[1] for _ in twist])

# plt.plot(r1,c)
# plt.show()
# plt.close()

plt.plot(r2,beta)
plt.show()
plt.close()