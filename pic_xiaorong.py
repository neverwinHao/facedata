import matplotlib.pyplot as plt

# 数据
articles = ['SFMNet(CVPR 2023)', 'SCTANet', 'DCNN(PR2023)']
psnr = [27.42, 27.28, 26.68]
ssim = [0.8036, 0.7932, 0.7741]
plt.figure(figsize=(8, 6))

for i in range(len(articles)):
    plt.plot(psnr[i], ssim[i], marker='o', label=articles[i])

plt.xlabel('PSNR')
plt.ylabel('SSIM')
plt.title('SPARD Net')
plt.legend()

plt.grid(True)
plt.show()
