# Findings — 道歉程序

## 架构研究

### 部署限制
- **GitHub Pages**: 仅支持静态文件。不能运行 Python/Node 后端。
  - 解决方案：部署纯前端 HTML 版本作为备份链接。
- **Vercel**: 支持 Python 运行时（Serverless Functions）。
  - Python 3.9+ 可用，通过 `vercel.json` 配置路由。
  - FastAPI 通过 `asgi` 适配器运行。

### 主流道歉程序功能
1. 「对不起」大标题 + 可爱风格
2. 输入框：写下道歉内容
3. 「原谅我吧」按钮 — 鼠标悬停会逃跑（经典设计）
4. 爱心/花瓣/彩带动画效果
5. 点击原谅后显示成功动画
6. 可选的背景音乐

### 技术选型
- **后端框架**: FastAPI（轻量，异步，Vercel 友好）
- **前端**: 原生 HTML/CSS/JS（零依赖，加载快）
- **静态部署**: 单文件 HTML（便于分享）
- **字体**: Google Fonts 或系统字体
