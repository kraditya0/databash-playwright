from playwright.sync_api import sync_playwright

seeds = list(range(79, 89))
total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://seed{seed}.datadash.iitm.ac.in/"
        page.goto(url)

        cells = page.locator("table td").all_text_contents()

        for c in cells:
            try:
                total_sum += float(c)
            except:
                pass

    print("TOTAL:", total_sum)
    browser.close()
