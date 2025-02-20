const { app, BrowserWindow, Tray, Menu } = require("electron");
const path = require("path");
const fs = require("fs");

let mainWindow;
let tray = null;

// Path for config.json
const configPath = path.join(__dirname, "config.json");

// Ensure config.json exists with default settings
if (!fs.existsSync(configPath)) {
  const defaultConfig = {
    mainPage: path.join(__dirname, "mainpage.html"), // ✅ Set correct HTML file
  };
  fs.writeFileSync(configPath, JSON.stringify(defaultConfig, null, 2));
}

// Load config.json
let config;
try {
  config = JSON.parse(fs.readFileSync(configPath, "utf-8"));
} catch (error) {
  console.error("Error reading config.json:", error);
  app.quit();
}

app.whenReady().then(() => {
  createMainWindow();

  // Setup system tray
  tray = new Tray(path.join(__dirname, "icon.png"));
  const trayMenu = Menu.buildFromTemplate([
    { label: "Show App", click: () => mainWindow.show() },
    { label: "Quit", role: "quit" },
  ]);
  tray.setContextMenu(trayMenu);

  tray.on("click", () => {
    if (mainWindow && mainWindow.isMinimized()) {
      mainWindow.restore();
    }
    mainWindow.show();
    mainWindow.focus();
  });
});

function createMainWindow() {
  mainWindow = new BrowserWindow({
    fullscreen: true, // ✅ Open window in full-screen mode
    webPreferences: {
      nodeIntegration: false, // 🚫 No Node.js access for security
      contextIsolation: true, // ✅ Prevents global context pollution
      enableRemoteModule: false, // ✅ Disables remote module for security
      sandbox: true, // ✅ Runs the renderer process in a secure sandbox
    },
  });

  // ✅ Construct correct file path
  const mainPagePath = `file://${config.mainPage}`;
  console.log("Loading page:", mainPagePath);

  mainWindow.loadURL(mainPagePath);

  mainWindow.on("minimize", (event) => {
    event.preventDefault();
    mainWindow.hide();
  });

  mainWindow.on("closed", () => {
    mainWindow = null;
  });
}

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});
