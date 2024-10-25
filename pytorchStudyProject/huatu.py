import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc
import numpy as np
import pandas as pd


# 绘制折线图
# epochs = np.arange(1, 11)
# accuracy = [0.60, 0.65, 0.70, 0.75, 0.80, 0.82, 0.85, 0.87, 0.88, 0.90]
# plt.plot(epochs, accuracy, marker='o', linestyle='-', color='b', label='Model Accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.title('Model Accuracy Over Epochs')
# plt.legend()
# plt.grid(True)
# plt.show()


# 使用Seaborn绘制折线图
# data = pd.DataFrame({
#     'Epochs': np.arange(1, 11),
#     'Accuracy': [0.60, 0.65, 0.70, 0.75, 0.80, 0.82, 0.85, 0.87, 0.88, 0.90]
# })
# sns.lineplot(x='Epochs', y='Accuracy', data=data, marker='o')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.title('Model Accuracy Over Epochs')
# plt.grid(True)
# plt.show()


# sns.set(style='whitegrid')
# epochs = np.arange(1, 21)
#
#
# accuracy_model1 = [0.60, 0.65, 0.70, 0.75, 0.78, 0.80, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93, 0.94, 0.95]
#
#
# accuracy_model2 = [0.58, 0.63, 0.68, 0.73, 0.76, 0.79, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93, 0.94]
# data = pd.DataFrame({
#     'Epochs': epochs,
#     'Model 1': accuracy_model1,
#     'Model 2': accuracy_model2
# })
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='Epochs', y='Model 1', data=data, marker='o', color='blue', label='Model 1')
# sns.lineplot(x='Epochs', y='Model 2', data=data, marker='s', color='green', label='Model 2')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.title('Model Accuracy Comparison Over Epochs')
# plt.legend()
# plt.grid(True)
# plt.show()


# 绘制柱状图
# models = ['SVM', 'RF', 'Autoencoder', 'CNN', 'LSTM', 'DeepLog', 'Ours']
# accuracies = [0.76, 0.80, 0.82, 0.83, 0.85, 0.87, 0.91]
# plt.bar(models, accuracies, color=['silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'gray'])
# plt.xlabel('Models')
# plt.ylabel('Recall')
# plt.title('Recall Comparison of Different Models')
# plt.show()


def xiaorongshiyanduibi():

    # 消融实验对比柱状图
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于支持显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    models = ['完整模型', '移除VAE', '移除K-means', '替换Transformer']
    precision = [0.95, 0.88, 0.89, 0.91]
    recall = [0.91, 0.81, 0.84, 0.86]
    accuracy = [0.95, 0.88, 0.89, 0.88]
    f1_score = [0.92, 0.84, 0.86, 0.88]

    # 设置柱状图的位置
    x = np.arange(len(models))  # 模型配置数量
    width = 0.2  # 每个柱形条的宽度

    # 创建图表
    plt.figure(figsize=(10, 6))

    # 透明度配置
    alpha_dim = 0.5  # 非完整模型的透明度

    # 绘制“完整模型”的柱状图
    plt.bar(x[0] - 1.5*width, precision[0], width, label='Precision', alpha=1)
    plt.bar(x[0] - 0.5*width, recall[0], width, label='Recall', alpha=1)
    plt.bar(x[0] + 0.5*width, accuracy[0], width, label='Accuracy', alpha=1)
    plt.bar(x[0] + 1.5*width, f1_score[0], width, label='F1-Score', alpha=1)

    # 绘制其他模型的柱状图，使用半透明效果
    plt.bar(x[1:] - 1.5*width, precision[1:], width, alpha=alpha_dim)
    plt.bar(x[1:] - 0.5*width, recall[1:], width, alpha=alpha_dim)
    plt.bar(x[1:] + 0.5*width, accuracy[1:], width, alpha=alpha_dim)
    plt.bar(x[1:] + 1.5*width, f1_score[1:], width, alpha=alpha_dim)
    # 设置标题和标签
    plt.title('消融研究结果对比')
    plt.xlabel('模型配置')
    plt.ylabel('性能指标值')

    # 设置X轴刻度位置和标签
    plt.xticks(x, models)

    # 显示图例
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()  # 自动调整布局以防止重叠

    rects1 = plt.bar(x - width - width / 2, precision, width, label='Precision')
    rects2 = plt.bar(x - width / 2, recall, width, label='Recall')
    rects3 = plt.bar(x + width / 2, accuracy, width, label='Accuracy')
    rects4 = plt.bar(x + width + width / 2, f1_score, width, label='F1-Score')
    plt.bar_label(rects1, padding=3)  # 更加简单好用的api
    plt.bar_label(rects2, padding=3)
    plt.bar_label(rects3, padding=3)
    plt.bar_label(rects4, padding=3)

    # 设置y轴范围
    plt.ylim(0.7, 1.0)

    # 显示图表
    plt.show()

xiaorongshiyanduibi()

def roc():
    # 假设你有真实标签和两种模型的预测概率
    y_true = [0, 1, 1, 0, 1, 0, 1, 0, 1, 0]  # 真实标签

    # 模型1的预测概率（自适应聚类前）
    y_scores_before = [0.1, 0.4, 0.35, 0.2, 0.8, 0.3, 0.6, 0.4, 0.7, 0.1]

    # 模型2的预测概率（自适应聚类后）
    y_scores_after = [0.2, 0.5, 0.4, 0.3, 0.9, 0.4, 0.7, 0.5, 0.8, 0.2]

    # 计算ROC曲线和AUC
    fpr_before, tpr_before, _ = roc_curve(y_true, y_scores_before)
    roc_auc_before = auc(fpr_before, tpr_before)

    fpr_after, tpr_after, _ = roc_curve(y_true, y_scores_after)
    roc_auc_after = auc(fpr_after, tpr_after)

    # 绘制ROC曲线
    plt.figure(figsize=(10, 6))
    plt.plot(fpr_before, tpr_before, color='blue', lw=2, label=f'Before Clustering (AUC = {roc_auc_before:.2f})')
    plt.plot(fpr_after, tpr_after, color='red', lw=2, label=f'After Clustering (AUC = {roc_auc_after:.2f})')
    plt.plot([0, 1], [0, 1], color='grey', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve - Adaptive Clustering Impact')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()
