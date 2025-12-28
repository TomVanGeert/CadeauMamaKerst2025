from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        cwd = os.getcwd()
        page.goto(f'file://{cwd}/index.html')

        page.focus('#capture-btn')

        box_shadow = page.eval_on_selector('#capture-btn', 'el => window.getComputedStyle(el).boxShadow')
        outline = page.eval_on_selector('#capture-btn', 'el => window.getComputedStyle(el).outline')

        print(f"BASELINE - Box Shadow: {box_shadow}")
        print(f"BASELINE - Outline: {outline}")

        page.screenshot(path='verification/baseline.png')
        browser.close()

if __name__ == "__main__":
    run()