import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://hidr.com.np/"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def check_link(url, timeout=10):
    if not url:
        return "SKIP", "Empty href"
    if url.startswith(("mailto:", "tel:", "javascript:", "#")):
        return "SKIP", "Non-HTTP link"
    try:
        response = requests.head(
            url,
            allow_redirects=True,
            timeout=timeout
        )

        # Some servers do not properly support HEAD.
        if response.status_code == 405:
            response = requests.get(
                url,
                allow_redirects=True,
                timeout=timeout,
                stream=True
            )

        if response.status_code < 400:
            return "PASS", f"HTTP {response.status_code}"

        return "FAIL", f"HTTP {response.status_code}"

    except requests.exceptions.Timeout:
        return "FAIL", "Request timeout"

    except requests.exceptions.ConnectionError:
        return "FAIL", "Connection error"

    except requests.exceptions.RequestException as error:
        return "FAIL", str(error)


def test_all_links(driver):
    driver.get(BASE_URL)
    # Wait until the page is loaded and at least one link is available.
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "a"))
    )
    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) > 0, "No links found on the webpage."
    print(f"\nTotal links found: {len(links)}")

    broken_links = []
    valid_links = []
    skipped_links = []
    # Extract hrefs first because the page can change while checking links.
    hrefs = []
    for link in links:
        href = link.get_attribute("href")

        if href and href not in hrefs:
            hrefs.append(href)

    print(f"Unique links to check: {len(hrefs)}")
    for index, url in enumerate(hrefs, start=1):
        status, message = check_link(url)
        print(f"{index}. {url} --> {status} ({message})")

        if status == "PASS":
            valid_links.append(url)

        elif status == "FAIL":
            broken_links.append(
                {
                    "url": url,
                    "reason": message
                }
            )
        elif status == "SKIP":
            skipped_links.append(url)
    print("\n========== LINK TEST SUMMARY ==========")
    print(f"Total links       : {len(hrefs)}")
    print(f"Valid links       : {len(valid_links)}")
    print(f"Broken links      : {len(broken_links)}")
    print(f"Skipped links     : {len(skipped_links)}")
    if broken_links:
        print("\n========== BROKEN LINKS ==========")

        for broken in broken_links:
            print(
                f"{broken['url']} --> {broken['reason']}"
            )
    # Actual pytest condition.
    assert not broken_links, (
        f"Found {len(broken_links)} broken link(s)."
    )