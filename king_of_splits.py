with open("content.html") as f:
    content = f.read()

listings = content.split('aria-label="full details of ')[1:]

for listing in listings:
    title = listing.split('"')[0]

    company_name = listing.split('data-testid="company-name"')[1]
    company_name = company_name.split('<')[0]
    company_name = company_name.split('">')[1]

    location = listing.split('data-testid="text-location"')[1]
    location = location.split('<')[0]
    location = location.split('">')[1]

    print(f"Title : {title}")
    print(f"Company name : {company_name}")
    print(f"Location : {location}")