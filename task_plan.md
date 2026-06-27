# 道歉程序 (Apology App) — 任务计划

## 目标
用 Python 写一个道歉程序，部署到 Vercel 和 GitHub Pages，分享链接即用。

## 架构决策

```
GitHub Pages（纯静态）            Vercel（主部署）
    └── 备份链接                      └── 分享主链接
    └── standalone.html                └── Python FastAPI 后端
                                       └── HTML/CSS/JS 前端
                                       └── API（原谅记录）
```

| 平台 | 运行内容 | 能力 |
|------|---------|------|
| Vercel | Python FastAPI + 前端 | 完整功能 |
| GitHub Pages | 纯静态 HTML | 基础展示 |

## 阶段

| 阶段 | 描述 | 状态 |
|------|------|------|
| 1 | 项目初始化 & 结构设计 | ✅ complete |
| 2 | Python FastAPI 后端开发 | ✅ complete |
| 3 | 道歉程序前端开发（HTML/CSS/JS） | ✅ complete |
| 4 | Vercel 部署配置 | ✅ complete |
| 5 | GitHub Pages 静态版本 | ✅ complete |
| 6 | 测试 & 发布 | ✅ complete |

## 创建的文件

| 文件 | 用途 |
|------|------|
| `backend/main.py` | FastAPI 应用入口 |
| `backend/requirements.txt` | Python 依赖 |
| `vercel.json` | Vercel 部署配置 |
| `frontend/index.html` | 道歉主页面（内嵌 CSS/JS） |
| `static/index.html` | GitHub Pages 独立版本 |
| `README.md` | 项目说明 + 部署指南 |
