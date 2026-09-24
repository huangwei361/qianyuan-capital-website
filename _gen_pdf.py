"""用 pyppeteer 真实渲染 invest-brochure.html → PDF"""
import asyncio
from pyppeteer import launch
import os

OUT = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure.pdf'

async def main():
    browser = await launch(
        headless=True,
        args=['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage'],
        executablePath=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1600, 'height': 1200})

    # 加载本地 HTML（用 file:// 避免网络问题）
    src = r'C:\Users\64549\.minimax\金融财富公司成立\website\invest-brochure.html'
    await page.goto(f'file:///{src}', {'waitUntil': 'networkidle0', 'timeout': 30000})
    # 给 JS/CSS 时间渲染
    await asyncio.sleep(3)

    # 用 page.pdf() 生成（更可靠）
    await page.pdf({
        'path': OUT,
        'format': 'A4',
        'landscape': True,
        'printBackground': True,
        'margin': {'top': '10mm', 'bottom': '10mm', 'left': '10mm', 'right': '10mm'}
    })
    await browser.close()
    print(f'OK: {OUT}')
    print(f'Size: {os.path.getsize(OUT)} bytes')

asyncio.run(main())