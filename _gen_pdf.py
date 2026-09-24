"""pyppeteer 渲染 → PDF (v3 输出到新文件名)"""
import asyncio, os
from pyppeteer import launch

OUT = r'C:\Users\64549\.minimax\金融财富公司成立\invest-brochure-v7.pdf'

async def main():
    browser = await launch(
        headless=True,
        args=['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage'],
        executablePath=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1200, 'height': 1600})

    src = r'C:\Users\64549\.minimax\金融财富公司成立\website\invest-brochure.html'
    await page.goto(f'file:///{src}', {'waitUntil': 'networkidle0', 'timeout': 30000})
    await asyncio.sleep(3)

    await page.pdf({
        'path': OUT,
        'format': 'A4',
        'landscape': False,
        'printBackground': True,
        'margin': {'top': '16mm', 'bottom': '16mm', 'left': '16mm', 'right': '16mm'}
    })
    await browser.close()
    print(f'OK: {OUT}')
    print(f'Size: {os.path.getsize(OUT)} bytes')

asyncio.run(main())



