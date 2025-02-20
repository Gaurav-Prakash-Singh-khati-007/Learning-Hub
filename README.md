# 🚀 Electron Course App

This is an **Electron.js app** that loads courses dynamically from `config.json`. Clicking on a thumbnail opens a new course page.

---

## 📁 Project Structure

```
📂 YourProject
│── 📂 assets
│   ├── 🖼️ thumbnail.png
│   ├── 🖼️ icon.png
│── 📂 pages
│   ├── 📄 course1.html
│   ├── 📄 course2.html
│── 📂 scripts
│   ├── 📄 preload.js
│── 📄 main.js
│── 📄 mainpage.html
│── 📄 config.json
│── 📄 package.json
```

---

## 🚀 Installation Guide

### 1️⃣ Install Node.js (If Not Installed)
- Download and install **Node.js** from [nodejs.org](https://nodejs.org/)
- Verify installation:
  ```sh
  node -v
  npm -v
  ```

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/your-electron-app.git
cd your-electron-app
```

### 3️⃣ Install Dependencies
```sh
npm install
```

### 4️⃣ Run the App
```sh
npx electron .
```
OR  
```sh
electron .
```

---

## 📜 config.json (Dynamic HTML Loader)

```json
{
  "mainPage": "mainpage.html"
}
```

---

## 📄 main.js (Electron Main File)

```javascript
const { app, BrowserWindow, Tray, Menu } = require("electron");
const path = require("path");
const fs = require("fs");

let mainWindow;
let tray = null;

// Load config
const configPath = path.join(app.getPath("userData"), "config.json");
if (!fs.existsSync(configPath)) {
  fs.writeFileSync(configPath, JSON.stringify({ mainPage: "mainpage.html" }, null, 2));
}
const config = JSON.parse(fs.readFileSync(configPath, "utf-8"));

app.whenReady().then(() => {
  createMainWindow();
  
  tray = new Tray(path.join(__dirname, "assets/icon.png"));
  const trayMenu = Menu.buildFromTemplate([
    { label: "Show App", click: () => mainWindow.show() },
    { label: "Quit", role: "quit" },
  ]);
  tray.setContextMenu(trayMenu);
});

function createMainWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, "scripts/preload.js"),
    },
  });

  const mainPagePath = path.join(__dirname, config.mainPage);
  mainWindow.loadURL(`file://${mainPagePath}`);

  mainWindow.on("closed", () => (mainWindow = null));
}

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});
```

---

## 📄 mainpage.html (Course Page with Thumbnails)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Course Dashboard</title>
    <script>
        function openCourse(page) {
            window.location.href = page;
        }
    </script>
</head>
<body>
    <h1>Courses</h1>
    <img src="assets/thumbnail.png" width="200" onclick="openCourse('pages/course1.html')" />
    <img src="assets/thumbnail.png" width="200" onclick="openCourse('pages/course2.html')" />
</body>
</html>
```

---

## 🎯 Additional Electron Commands

### Build Electron App (Windows)
```sh
npx electron-packager . YourAppName --platform=win32 --arch=x64 --out=dist
```

### For Mac
```sh
npx electron-packager . YourAppName --platform=darwin --arch=x64 --out=dist
```

### For Linux
```sh
npx electron-packager . YourAppName --platform=linux --arch=x64 --out=dist
```

---

### 🎉 Now your Electron app is ready! 🚀

