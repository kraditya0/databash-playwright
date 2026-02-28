from playwright.sync_api import sync_playwright

seeds = range(79, 89)
total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://datadash.iitm.ac.in/seeds/{seed}"
        page.goto(url, timeout=60000)

        cells = page.locator("table td").all_text_contents()

        for c in cells:
            try:
                total += float(c)
            except:
                pass

    print("TOTAL:", total)
    browser.close()
