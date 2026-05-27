const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function generateHtml(filePath, content) {
  const lines = content.split('\n');
  const lineCount = lines.length;
  const lineNumbers = Array.from({ length: lineCount }, (_, i) => i + 1).join('\n');
  const escapedContent = escapeHtml(content);
  const escapedPath = escapeHtml(filePath);
  const escapedBasename = escapeHtml(path.basename(filePath));

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${escapedBasename}</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
      font-family: 'Courier New', Courier, monospace;
      background: #1e1e1e;
      color: #d4d4d4;
    }

    header {
      background: #2d2d2d;
      padding: 8px 16px;
      border-bottom: 1px solid #444;
      font-size: 13px;
      color: #9e9e9e;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      flex-shrink: 0;
    }

    header span {
      color: #d4d4d4;
    }

    .viewer {
      display: flex;
      flex: 1;
      overflow: auto;
      font-size: 14px;
      line-height: 1.5;
    }

    .line-numbers {
      position: sticky;
      left: 0;
      background: #2d2d2d;
      color: #858585;
      text-align: right;
      padding: 8px 12px 8px 16px;
      border-right: 1px solid #444;
      user-select: none;
      pointer-events: none;
      white-space: pre;
      z-index: 1;
      flex-shrink: 0;
    }

    .content {
      padding: 8px 16px;
      white-space: pre;
      flex: 1;
      outline: none;
    }
  </style>
</head>
<body>
  <header>File: <span>${escapedPath}</span> &nbsp;|&nbsp; ${lineCount} lines</header>
  <div class="viewer">
    <div class="line-numbers">${lineNumbers}</div>
    <div class="content">${escapedContent}</div>
  </div>
</body>
</html>`;
}

app.get('/', (req, res) => {
  const filePath = req.query.file;

  if (!filePath) {
    return res.status(400).send(`<!DOCTYPE html>
<html><body style="font-family:'Courier New',monospace;padding:20px;background:#1e1e1e;color:#d4d4d4">
  <h2>Text File Viewer</h2>
  <p style="margin-top:12px">Usage: <code style="background:#2d2d2d;padding:2px 6px">/?file=/absolute/path/to/file.txt</code></p>
</body></html>`);
  }

  const resolvedPath = path.resolve(filePath);

  fs.readFile(resolvedPath, 'utf8', (err, content) => {
    if (err) {
      const status = err.code === 'ENOENT' ? 404 : 500;
      return res.status(status).send(`<!DOCTYPE html>
<html><body style="font-family:'Courier New',monospace;padding:20px;background:#1e1e1e;color:#d4d4d4">
  <h2>Error ${status}</h2>
  <p style="margin-top:12px;color:#f48771">${escapeHtml(err.message)}</p>
</body></html>`);
    }
    res.send(generateHtml(resolvedPath, content));
  });
});

app.listen(PORT, () => {
  console.log(`Text file viewer running at http://localhost:${PORT}`);
  console.log(`Usage: http://localhost:${PORT}/?file=/path/to/file.txt`);
});
