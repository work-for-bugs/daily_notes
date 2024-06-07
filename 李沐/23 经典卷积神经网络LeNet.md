# 手写的数字识别
# MNIST
5万个训练数据 1万个测试数据 图像大小 28\*28 10类    
输入32\*32image    
卷积 5\*5 输出6通道 28\*28     
pooling 输出6通道 14\*14     
卷积 5\*5 输出16通道 10\*10     
pooling 输出16通道 5\*5     
拉成一个向量 输入到全连接层 输出120 再全连接 输出84      
再gauss层 输出     
# 卷积神经网络（LeNet）
nn.Conv2d(输入通道1，输出通道6，kernel_size5，padding填充2)，sigmoid得到非线性     
nn.AvgPool2d(kernel_size2, stride2窗口的移动步幅，默认与kernel_size大小一致，表示不重叠)     
nn.Conv2d(输入通道1，输出通道6，kernel_size5)，sigmoid得到非线性  
nn.AvgPool2d(kernel_size2, stride2)     
nn.Flatten() output shape:torch.Size([1, 16, 5, 5])->torch.Size([1, 400]) nn.Flatten()函数详解及示例https://blog.csdn.net/gx19990824/article/details/127807334          
nn.Linear(16\*5\*5, 120), nn.Sigmoid()
nn.Linear(120, 84), nn.Sigmoid()
nn.Linear(84, 10)
# 训练和评估LeNet-5模型
高宽减半 通道数翻倍     
cnn-explainer cnn可视化    

