# Learning-Hub
Frontend only for LMS simple clean easy 
# Electron.js Player Setup

## Prerequisites
Make sure you have the following installed on your system:

- [Node.js](https://nodejs.org/) (Latest LTS version recommended)
- npm (comes with Node.js) or Yarn
- Git (optional, for cloning repositories)

## Installation

1. Clone the repository (if using Git):
   ```sh
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install Electron.js globally (if not installed):
   ```sh
   npm install -g electron
   ```

3. Install project dependencies:
   ```sh
   npm install
   ```
   or using Yarn:
   ```sh
   yarn install
   ```

## Project Structure
```
/project-directory
│── config.json  # Configuration file containing relative path to mainpage.html
│── mainpage.html  # Main HTML file with thumbnails and course links
│── index.js  # Electron main process
│── package.json  # Project metadata and dependencies
│── assets/  # Additional assets (thumbnails, images, etc.)
│── courses/  # Course-specific HTML files
```

## Running the Electron.js App

Start the Electron.js app:
```sh
npm start
```
Or manually using:
```sh
electron .
```

## Config File (config.json)
The `config.json` file should include the relative path to `mainpage.html`:
```json
{
  "mainPage": "./mainpage.html"
}
```

## Handling Course Clicks
The `mainpage.html` file should contain thumbnails that, when clicked, open course-specific HTML pages:
```html
<a href="courses/course1.html" target="_blank">
    <img src="assets/thumbnail1.png" alt="Course 1">
</a>
```

## Using GitHub Markdown
If your courses use GitHub Markdown (`.md` files), you can convert them to HTML inside Electron using `marked.js`:

1. Install `marked`:
   ```sh
   npm install marked
   ```
2. Load and parse Markdown in your Electron renderer:
   ```js
   const fs = require('fs');
   const path = require('path');
   const marked = require('marked');
   
   const mdFilePath = path.join(__dirname, 'courses/course1.md');
   fs.readFile(mdFilePath, 'utf8', (err, data) => {
       if (!err) {
           document.getElementById('content').innerHTML = marked.parse(data);
       }
   });
   ```

## Packaging the App
To build your Electron app into a standalone executable:

1. Install Electron Packager:
   ```sh
   npm install -g electron-packager
   ```
2. Package the app:
   ```sh
   electron-packager . ElectronApp --platform=win32 --arch=x64
   ```
   (Modify `--platform` and `--arch` as needed for different OS)

## Notes
- Ensure that all HTML file paths in `config.json` are relative to the project directory.
- Use DevTools (`Ctrl+Shift+I`) in Electron to debug issues.
- Keep your `config.json` flexible for dynamic content loading.

## Resources
- [Electron Documentation](https://www.electronjs.org/docs)
- [Node.js](https://nodejs.org/en/)
- [Marked.js](https://github.com/markedjs/marked)
- 
