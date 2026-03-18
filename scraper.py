from typing import Dict, Any
from playwright.sync_api import sync_playwright  # type: ignore
import json

def scrape_ekantipur():
    data: Dict[str, Any] = {
        "entertainment_news": [],
        "cartoon_of_the_day": {}
    }

    print("Starting Playwright to scrape Ekantipur...")
    with sync_playwright() as p:
        # Launching Chromium. We use headless=False to observe visually and for your recording.
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Task 1: Extract Entertainment News
        print("Navigating to the Entertainment section...")
        page.goto('https://ekantipur.com/entertainment', wait_until='networkidle')
        
        # Wait for the article containers
        page.wait_for_selector('.category-inner-wrapper')
        articles = page.locator('.category-inner-wrapper').all()
        
        # We need the top 5 articles
        print("Extracting top 5 entertainment articles...")
        for art in articles[:5]:
            try:
                title_loc = art.locator('.category-description h2')
                title = title_loc.text_content().strip() if title_loc.count() > 0 else "Unknown Title"
                
                author_loc = art.locator('.category-description .author-name')
                author = author_loc.text_content().strip() if author_loc.count() > 0 else None
                
                img_loc = art.locator('.category-image img')
                image_url = None
                if img_loc.count() > 0:
                    image_url = img_loc.first.get_attribute('data-src') or img_loc.first.get_attribute('src')
                
                data["entertainment_news"].append({
                    "title": title,
                    "image_url": image_url,
                    "category": "मनोरञ्जन",
                    "author": author
                })
            except Exception as e:
                print(f"Error scraping an article: {e}")

        # Task 2: Extract Cartoon of the Day
        print("Navigating to homepage to extract the Cartoon of the Day...")
        page.goto('https://ekantipur.com', wait_until='networkidle')
        
        try:
            # The 'व्यंग्य चित्र' (Cartoon of the Day) is present in the .cartoon-slider section
            page.wait_for_selector('.cartoon-slider')
            cartoon_section = page.locator('.cartoon-slider')
            
            # There is usually a slider; we get the active slide
            active_slide = cartoon_section.locator('.swiper-slide-active')
            if active_slide.count() > 0:
                img_el = active_slide.locator('img')
                if img_el.count() > 0:
                    image_url = img_el.get_attribute('data-src') or img_el.get_attribute('src')
                    title = img_el.get_attribute('alt')
                    
                    # Usually, the alt tag says something like 'कान्तिपुर दैनिकमा आज प्रकाशित अविनको कार्टुन'
                    author = "अविन" if title and "अविन" in title else "Unknown"
                    if not title:
                        title = "व्यंग्य चित्र"
                        
                    data["cartoon_of_the_day"] = {
                        "title": title,
                        "image_url": image_url,
                        "author": author
                    }
        except Exception as e:
            print(f"Error scraping cartoon: {e}")

        browser.close()

    # Save data to JSON with UTF-8 encoding for Nepali texts
    print("Saving extracted data to output.json...")
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("Scraping completed successfully!")

if __name__ == "__main__":
    scrape_ekantipur()
