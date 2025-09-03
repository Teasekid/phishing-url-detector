"""
generate_dataset.py
------------------
Generates a synthetic dataset of 5000 URLs (phishing and legitimate) and saves to data/urls.csv.
"""
import random
import csv

legit_domains = [
    'google.com', 'paypal.com', 'amazon.com', 'github.com', 'microsoft.com', 'apple.com', 'bankofamerica.com',
    'dropbox.com', 'linkedin.com', 'twitter.com', 'facebook.com', 'wikipedia.org', 'adobe.com', 'netflix.com',
    'reddit.com', 'instagram.com', 'airbnb.com', 'booking.com', 'uber.com', 'spotify.com', 'cloudflare.com',
    'salesforce.com', 'slack.com', 'medium.com', 'trello.com', 'zoom.us', 'shopify.com', 'ebay.com', 'etsy.com',
    'aliexpress.com', 'walmart.com', 'target.com', 'homedepot.com', 'lowes.com', 'bestbuy.com', 'costco.com',
    'wayfair.com', 'overstock.com', 'chewy.com', 'petco.com', 'petsmart.com', 'nike.com', 'adidas.com',
    'underarmour.com', 'puma.com', 'newbalance.com', 'asics.com', 'converse.com', 'vans.com', 'fila.com',
    'skechers.com', 'brooksrunning.com', 'merrell.com', 'columbia.com', 'patagonia.com', 'thenorthface.com',
    'arcteryx.com', 'marmot.com', 'mountaingear.com', 'backcountry.com', 'rei.com', 'ems.com', 'moosejaw.com',
    'campmor.com', 'cabelas.com', 'basspro.com', 'academy.com', 'dickssportinggoods.com', 'hibbett.com',
    'runnings.com', 'fleetfeet.com', 'big5sportinggoods.com', 'scheels.com', 'dunhamssports.com', 'sportsmans.com',
    'ganderoutdoors.com', 'campingworld.com', 'outdoorworld.com', 'orvis.com', 'llbean.com', 'landsend.com',
    'eddiebauer.com', 'canadianoutdoor.com', 'mountainwarehouse.com', 'tog24.com', 'regatta.com', 'craghoppers.com',
    'jackwolfskin.com', 'berghaus.com', 'rab.equipment', 'montane.co.uk', 'sprayway.com', 'keela.co.uk',
    'paramo-clothing.com', 'trekmates.co.uk', 'mountain-equipment.co.uk', 'outdoorresearch.com', 'mammut.com',
    'salewa.com', 'deuter.com', 'osprey.com', 'gregorypacks.com', 'kelty.com', 'granitegear.com', 'mountainsmith.com',
    'highsierra.com', 'eaglecreek.com', 'samsonite.com', 'tumi.com', 'briggs-riley.com', 'travelpro.com', 'delsey.com',
    'antler.co.uk', 'itluggage.com', 'american-tourister.com', 'rocklandluggage.com', 'olympiausa.com',
    'pathfinderluggage.com', 'swissgear.com', 'travelersclub.com', 'kensington.com', 'case-mate.com', 'otterbox.com',
    'speckproducts.com', 'uag.com', 'incipio.com', 'tech21.com', 'griffintechnology.com', 'mophie.com', 'lifeproof.com',
    'pelican.com', 'otterproducts.com', 'caseologycases.com', 'spigen.com', 'ringke.com', 'poeticcases.com',
    'supcase.com', 'amzer.com', 'tridentcase.com', 'ballisticcases.com', 'elementcase.com', 'x-doria.com', 'rokform.com',
    'lunatik.com', 'magpul.com', 'griffin.com', 'moshi.com', 'casecrown.com', 'elago.com', 'kwmobile.com'
]

phishing_patterns = [
    'secure-', 'update-', 'verify-', 'login-', 'account-', 'confirm-', 'required-', 'banking-', 'dropbox-', 'appleid-',
    'paypal-', 'facebook-', 'amazon-', 'microsoft-', 'twitter-', 'linkedin-', 'netflix-', 'adobe-', 'reddit-', 'instagram-',
    'airbnb-', 'booking-', 'uber-', 'spotify-', 'cloudflare-', 'salesforce-', 'slack-', 'medium-', 'trello-', 'zoom-',
    'shopify-', 'ebay-', 'etsy-', 'aliexpress-', 'walmart-', 'target-', 'homedepot-', 'lowes-', 'bestbuy-', 'costco-',
    'wayfair-', 'overstock-', 'chewy-', 'petco-', 'petsmart-', 'nike-', 'adidas-', 'underarmour-', 'puma-', 'newbalance-',
    'asics-', 'converse-', 'vans-', 'fila-', 'skechers-', 'brooksrunning-', 'merrell-', 'columbia-', 'patagonia-',
    'thenorthface-', 'arcteryx-', 'marmot-', 'mountaingear-', 'backcountry-', 'rei-', 'ems-', 'moosejaw-', 'campmor-',
    'cabelas-', 'basspro-', 'academy-', 'dickssportinggoods-', 'hibbett-', 'runnings-', 'fleetfeet-', 'big5sportinggoods-',
    'scheels-', 'dunhamssports-', 'sportsmans-', 'ganderoutdoors-', 'campingworld-', 'outdoorworld-', 'orvis-', 'llbean-',
    'landsend-', 'eddiebauer-', 'canadianoutdoor-', 'mountainwarehouse-', 'tog24-', 'regatta-', 'craghoppers-',
    'jackwolfskin-', 'berghaus-', 'rab-', 'montane-', 'sprayway-', 'keela-', 'paramo-', 'trekmates-', 'mountain-equipment-',
    'outdoorresearch-', 'mammut-', 'salewa-', 'deuter-', 'osprey-', 'gregorypacks-', 'kelty-', 'granitegear-',
    'mountainsmith-', 'highsierra-', 'eaglecreek-', 'samsonite-', 'tumi-', 'briggs-riley-', 'travelpro-', 'delsey-',
    'antler-', 'itluggage-', 'american-tourister-', 'rocklandluggage-', 'olympiausa-', 'pathfinderluggage-', 'swissgear-',
    'travelersclub-', 'kensington-', 'case-mate-', 'otterbox-', 'speckproducts-', 'uag-', 'incipio-', 'tech21-',
    'griffintechnology-', 'mophie-', 'lifeproof-', 'pelican-', 'otterproducts-', 'caseologycases-', 'spigen-', 'ringke-',
    'poeticcases-', 'supcase-', 'amzer-', 'tridentcase-', 'ballisticcases-', 'elementcase-', 'x-doria-', 'rokform-',
    'lunatik-', 'magpul-', 'griffin-', 'moshi-', 'casecrown-', 'elago-', 'kwmobile-'
]

suffixes = ['.com', '.net', '.org', '.info', '.co', '.us', '.biz', '.online', '.site', '.top']

phishing_tlds = ['.xyz', '.top', '.online', '.site', '.info', '.biz']

special_chars = ['-', '_', '.', '@', '?', '=', '%']

random.seed(42)

def random_legit_url():
    domain = random.choice(legit_domains)
    scheme = random.choice(['http', 'https'])
    path = '' if random.random() < 0.7 else '/' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(5,15)))
    return f"{scheme}://{domain}{path}"

def random_phishing_url():
    pattern = random.choice(phishing_patterns)
    domain = pattern + random.choice(legit_domains)
    tld = random.choice(phishing_tlds)
    scheme = random.choice(['http', 'https'])
    path = '' if random.random() < 0.5 else '/' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(5,15)))
    # Add special chars, digits, or fake redirects
    extras = ''
    if random.random() < 0.3:
        extras += random.choice(special_chars)
    if random.random() < 0.2:
        extras += str(random.randint(10,99))
    if random.random() < 0.1:
        extras += '//' + random.choice(legit_domains)
    return f"{scheme}://{domain}{extras}{tld}{path}"

def main():
    # Number of new URLs to add per run
    add_count = 1000  # Change this value as needed

    # Read existing URLs
    existing_urls = set()
    existing_data = []
    try:
        with open('data/urls.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if len(row) == 2:
                    url, label = row
                    if url not in existing_urls:
                        existing_urls.add(url)
                        existing_data.append((url, label))
    except FileNotFoundError:
        pass

    new_urls = set()
    new_data = []
    legit_needed = add_count // 2
    phishing_needed = add_count - legit_needed
    while len(new_data) < add_count:
        if legit_needed > 0:
            url = random_legit_url()
            if url not in existing_urls and url not in new_urls:
                new_data.append((url, 'legitimate'))
                new_urls.add(url)
                legit_needed -= 1
        if phishing_needed > 0:
            url = random_phishing_url()
            if url not in existing_urls and url not in new_urls:
                new_data.append((url, 'phishing'))
                new_urls.add(url)
                phishing_needed -= 1

    all_data = existing_data + new_data
    random.shuffle(all_data)
    with open('data/urls.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['url', 'label'])
        writer.writerows(all_data)
    print(f"Added {add_count} new URLs. Total URLs in data/urls.csv: {len(all_data)}")

if __name__ == "__main__":
    main()
