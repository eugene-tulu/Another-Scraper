from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

def get_job_listings(search_query):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            user_agent="insert agent"
        )
        page = context.new_page()
        page.goto(f"https://companyyyy.com/jobs?q={search_query}")
        page.screenshot(path="screenshot.jpg", full_page=True)
        
        content = page.content()

        soup = BeautifulSoup(content, features="html.parser")

        jobs = []

        listings = soup.select(".resultContent")

        for listing in listings:
            title = listing.select(".jobTitle")[0].get_text()
            company_name = listing.select('[data-testid="company-name"]')[0].get_text()
            location = listing.select('[data-testid="text-location"]')[0].get_text()

            jobs.append({
                "Title": title,
                "Company name": company_name,
                "Location": location
            })
            

            with open("content.html", "w") as f:
                f.write(content)
            
            browser.close()
    return jobs

print(json.dumps(get_job_listings("developer"), indent=4))