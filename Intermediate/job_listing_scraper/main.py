from playwright.sync_api import sync_playwright
from urllib.parse import quote


# -------------------------
# USER INPUT
# -------------------------

job = input("Enter job category: ")
location = input("Enter location: ")


# -------------------------
# OUTPUT FILE
# -------------------------

output_file = open(
    "jobs.txt",
    "w",
    encoding="utf-8"
)


# -------------------------
# PLAYWRIGHT
# -------------------------

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    url = (
        f"https://in.indeed.com/jobs"
        f"?q={quote(job)}"
        f"&l={quote(location)}"
    )

    page.goto(
        url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(3000)

    # -------------------------
    # REJECT COOKIES
    # -------------------------

    reject_button = page.locator(
        "#onetrust-reject-all-handler"
    )

    if reject_button.count() > 0:
        reject_button.click()
        page.wait_for_timeout(1000)

    # -------------------------
    # FIND JOBS
    # -------------------------

    jobs = page.locator("td.resultContent")

    print("Jobs found:", jobs.count())

    output_file.write(
        f"JOB SEARCH: {job}\n"
        f"LOCATION: {location}\n\n"
    )

    # -------------------------
    # SCRAPE JOBS
    # -------------------------

    for i in range(jobs.count()):

        # Re-locate cards because Indeed
        # changes the DOM after clicking
        jobs = page.locator("td.resultContent")
        card = jobs.nth(i)

        # -------------------------
        # BASIC INFORMATION
        # -------------------------

        title_link = card.locator(
            "h3.jobTitle a"
        )

        title = title_link.locator(
            "span"
        ).get_attribute("title")

        company = card.locator(
            '[data-testid="company-name"]'
        ).inner_text()

        job_location = card.locator(
            '[data-testid="text-location"]'
        ).inner_text()

        salary_locator = card.locator(
            '[data-testid="attribute_snippet_testid salary-snippet-container"]'
        )

        if salary_locator.count() > 0:
            salary = salary_locator.inner_text()
        else:
            salary = "Not specified"

        # -------------------------
        # SAVE BASIC INFORMATION
        # -------------------------

        output_file.write("=" * 60 + "\n")
        output_file.write(f"JOB: {title}\n")
        output_file.write(f"COMPANY: {company}\n")
        output_file.write(f"LOCATION: {job_location}\n")
        output_file.write(f"SALARY: {salary}\n")

        # -------------------------
        # FIND VISIBLE JOB TITLE
        # -------------------------

        visible_title = page.locator(
            f'h3.jobTitle span[title="{title}"]:visible'
        ).first

        # -------------------------
        # CLICK JOB
        # -------------------------

        visible_title.click()

        # -------------------------
        # WAIT FOR JOB DETAILS
        # -------------------------

        description_heading = page.locator(
            '[data-testid="vj-job-description-heading"]'
        )

        try:

            description_heading.wait_for(
                state="visible",
                timeout=10000
            )

        except:

            output_file.write(
                "\nDESCRIPTION: Not found\n\n"
            )

            continue

        # -------------------------
        # GET DESCRIPTION
        # -------------------------

        description = page.locator(
            ".simple-job-description-html"
        )

        if description.count() > 0:

            description_text = description.inner_text()

            output_file.write(
                "\nDESCRIPTION:\n"
            )

            output_file.write(
                description_text
            )

            output_file.write("\n\n")

        else:

            output_file.write(
                "\nDESCRIPTION: Not found\n\n"
            )

        # Save immediately
        output_file.flush()

    # -------------------------
    # CLOSE OUTPUT FILE
    # -------------------------

    output_file.close()

    print("\nScraping completed.")
    print("Data saved to jobs.txt")

    # -------------------------
    # KEEP BROWSER OPEN
    # -------------------------

    input("\nPress Enter to close...")

    browser.close()