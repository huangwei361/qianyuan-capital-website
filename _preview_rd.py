"""渲染 quant-rd.html 的 research section 看效果"""
import asyncio, sys, os
sys.stdout.reconfigure(encoding='utf-8')
from pyppeteer import launch

async def main():
    browser = await launch(
        headless=True,
        args=['--no-sandbox', '--disable-gpu'],
        executablePath=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1280, 'height': 900})
    await page.goto('file:///C:/Users/64549/.minimax/金融财富公司成立/website/quant-rd.html#research', {'waitUntil': 'networkidle0', 'timeout': 30000})
    await asyncio.sleep(2)
    await page.screenshot({'path': r'C:\Users\64549\.minimax\金融财富公司成立\website\_preview-rd-research.png', 'fullPage': False})
    await browser.close()

asyncio.run(main())
print('OK')