# 道歉程序 💔 — 我错了，能见见面吗？

一个可爱的道歉交互页面，按钮会逃跑，追到就原谅你 ❤️

## ✨ 功能

- 🏃 **逃跑按钮** —「原谅我吧」鼠标悬停会躲开
- 😢 **表情变化** — 追越多次越委屈，最终心软
- 💖 **爱心彩带** — 原谅后全屏粒子动画
- 📱 **移动端适配** — 手机也能玩

## 🚀 部署

### 方式一：Vercel（推荐，主链接）

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

手动部署：

```bash
# 安装 Vercel CLI
npm i -g vercel

# 在项目目录登录并部署
cd apology-app
vercel --prod
```

部署后会获得 `https://<项目名>.vercel.app` 链接。

### 方式二：GitHub Pages（备用链接）

1. 在 GitHub 创建仓库，推送代码
2. Settings → Pages → Source: `Deploy from branch`
3. Branch: `main` → `/static`
4. 获得 `https://<你的名字>.github.io/<仓库名>` 链接

## 📁 项目结构

```
apology-app/
├── backend/
│   └── main.py              # FastAPI 服务器（Vercel）
├── frontend/
│   └── index.html           # 道歉主页面（内嵌 CSS/JS）
├── static/
│   └── index.html           # GitHub Pages 独立版本
├── vercel.json              # Vercel 部署配置
└── README.md
```

## 🎮 玩法

1. 打开链接看到委屈表情 😢
2. 写一段道歉留言
3. 尝试点击「原谅我吧 🙏」— 但按钮会逃跑！
4. 追得越久，表情越委屈 😰 → 😭
5. 追到 15 次后按钮投降 😅
6. 原谅成功！💖 满屏爱心庆祝

## 🛠 本地开发

```bash
# 安装依赖
cd backend
pip install -r requirements.txt

# 启动
cd ..
uvicorn backend.main:app --reload

# 打开 http://localhost:8000
```

## 📄 许可证

MIT
