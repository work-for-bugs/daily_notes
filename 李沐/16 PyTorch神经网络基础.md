# 层和块
## 自定义块
```python {.line-numbers}
class MLP(nn.Module):
    def __init__(self):

    def forward(self, x):
    
net = MLP()
net(x)
```
## 顺序块
```python {.line-numbers}
class MySequential(nn.Module):
    def __init__(self, *args):
        super().__init__()
        for block in args:
            self._modules[block] = block
        
    def forward(self, x):
        for block in self._modules.values():
            x = block(x)
        return x

net = MySequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))
net(x)
```
## 在正向传播函数中执行代码
继承nn.Module类，可以更灵活地构造模型、灵活计算   
比nn.Sequential更灵活   

## 混合搭配各种组合块的方法


# 参数管理
## 目标参数
## 一次性访问所有参数
net[0].named_parameters()   
net.named_parameters()   
## 从嵌套块收集参数

## 参数绑定
net = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), shared, nn.ReLU(), shared, nn.ReLU(), nn.Linear(8, 1))   

# 自定义层

# 读写文件
## 加载和保存张量
torch.save(x, 'x.file')   
x2 = torch.load('x.file')   
## 存储一个张量列表
torch.save([x, y], 'xy.file')   
x2, y2 = torch.load('xy.file')   
## 写入或读取从字符串映射到张量的字典
mydict = {'x': x, 'y': y}   
torch.save(mydict, 'mydict.file')   
mydict2 = torch.load('mydict.file')   
## 保存和加载模型参数
torch.save(net.state_dict(), 'mlp.params')


# QA




