import torch


# 1. 创建线性张量
def test01():

    # 1.1 创建指定步长的张量
    # 第一个参数：开始值
    # 第二个参数：结束值
    # 第三个参数：步长
    data = torch.arange(0, 10, 2)
    print(data)

    # 1.2 在指定区间指定元素个数
    # 第一个参数：开始值
    # 第二个参数：结束值
    # 第三个参数：创建元素的个数
    data = torch.linspace(0, 10, 10)
    print(data)


# 2. 创建随机张量
def test02():

    # 2.1 创建随机张量
    data = torch.randn(2, 3)
    print(data)


if __name__ == '__main__':
    test02()