const puppeteer = require('puppeteer');
const express = require('express');

const app = express();
app.use(express.static('.')); // serve current directory
const server = app.listen(3000);

(async () => {
    const browser = await puppeteer.launch({
        headless: false,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
//            '--window-size=1000,1080'  // width,height
        ],
        defaultViewport: null  // Use full window size
    });
    const pages = await browser.pages();
    const page = pages[0];
    await page.goto('http://localhost:3000/index.html');
})();
