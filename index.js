const puppeteer = require('puppeteer');
const express = require('express');
const fs = require('fs');
const path = require('path');
const chokidar = require('chokidar');

const configPath = path.join(__dirname, 'window-size.json');

function loadWindowSize() {
    try {
        if (fs.existsSync(configPath)) {
            return JSON.parse(fs.readFileSync(configPath, 'utf8'));
        }
    } catch (err) {
        console.error('Error loading config:', err);
    }
    return { width: 1920, height: 1080 };
}

(async () => {
    const app = express();
    app.use(express.static(__dirname));
    const server = app.listen(3000, () => {
        console.log('Server running on http://localhost:3000');
    });

    const windowSize = loadWindowSize();
    const browser = await puppeteer.launch({
        headless: false,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            `--window-size=${windowSize.width},${windowSize.height}`
        ],
        defaultViewport: null
    });

    const pages = await browser.pages();
    const page = pages[0];

    const client = await browser.target().createCDPSession();

    await page.exposeFunction('saveWindowSize', async () => {
        try {
            const { windowId } = await client.send('Browser.getWindowForTarget', {
                targetId: page.target()._targetId
            });
            const { bounds } = await client.send('Browser.getWindowBounds', { windowId });
            fs.writeFileSync(configPath, JSON.stringify({
                width: bounds.width,
                height: bounds.height
            }, null, 2));
        } catch (err) {
            console.error('Error saving config:', err);
        }
    });

    await page.evaluateOnNewDocument(() => {
        let resizeTimeout;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(() => {
                window.saveWindowSize();
            }, 500);
        });
    });

    await page.goto('http://localhost:3000/index.html');

    // File watching with better debugging
    console.log('Setting up file watcher...');
    console.log('Watching directory:', __dirname);

    const watcher = chokidar.watch(__dirname, {
        ignored: [
            /(^|[\/\\])\../,  // dotfiles
            /node_modules/,
            /window-size\.json$/,
            path.basename(__filename)  // ignore the main script itself
        ],
        persistent: true,
        ignoreInitial: true,
        awaitWriteFinish: {
            stabilityThreshold: 100,
            pollInterval: 100
        }
    });

    watcher
        .on('ready', () => {
            console.log('File watcher ready');
            const watched = watcher.getWatched();
            console.log('Watching files:', Object.keys(watched).map(dir =>
                watched[dir].map(file => path.join(dir, file))
            ).flat());
        })
        .on('change', async (filepath) => {
            console.log(`\n[${new Date().toLocaleTimeString()}] File changed: ${filepath}`);
            console.log('Reloading page...');
            try {
                await page.reload({ waitUntil: 'networkidle0' });
                console.log('Page reloaded successfully');
            } catch (err) {
                console.error('Error reloading page:', err);
            }
        })
        .on('error', error => console.error('Watcher error:', error));

    browser.on('disconnected', () => {
        console.log('Browser disconnected, cleaning up...');
        watcher.close();
        server.close();
    });
})();