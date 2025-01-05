import webbrowser
import sys
from colorama import init, Fore, Style

# Initialize Colorama
init()

# ASCII banner
banner = """

 .########...#######..##.....##.####.##....##..######..
 .##.....##.##.....##..##...##...##..###...##.##....##.
 .##.....##.##.....##...##.##....##..####..##.##.......
 .##.....##.##.....##....###.....##..##.##.##.##...####
 .##.....##.##.....##...##.##....##..##..####.##....##.
 .##.....##.##.....##..##...##...##..##...###.##....##.
 .########...#######..##.....##.####.##....##..######..
 


                  DOXING WEBSITE
                  By AnonNews_irc
"""

def print_banner():
    print(Fore.YELLOW + banner + Style.RESET_ALL)

def print_menu():
    sections = {
        "1. La Búsqueda de la Base de Datos": [
            ("Hunter.io Email Finder", "https://hunter.io/email-finder"), 
            ("IntelTechniques", "https://inteltechniques.com/"), 
            ("Have I Been Pwned", "https://haveibeenpwned.com/"), 
            ("EPIEOS", "https://epieos.com"), 
            ("Spokeo", "https://spokeo.com"), 
            ("BeenVerified", "https://beenverified.com"), 
            ("PeopleFinders", "https://peoplefinders.com"), 
            ("Whitepages", "https://whitepages.com"), 
            ("Intelius", "https://intelius.com"), 
            ("Pipl", "https://pipl.com")
        ],
        "2. La Búsqueda de Imagen": [
            ("Yandex Images", "https://yandex.com/images/touch/"), 
            ("FaceCheck.ID", "https://facecheck.id/"), 
            ("Google Lens", "https://lens.google/"), 
            ("Small SEO Tools", "https://smallseotools.com/reverse-image-search/"), 
            ("TinEye", "https://tineye.com"), 
            ("Bing Visual Search", "https://bing.com/images/search"), 
            ("Image Raider", "https://imageraider.com"), 
            ("RevEye", "https://reveye.com"), 
            ("Berify", "https://berify.com"), 
            ("PicPurify", "https://picpurify.com")
        ],
        "3. La Búsqueda de Nombre de Usuario": [
            ("Instant Username", "https://instantusername.com/"), 
            ("Social Searcher", "https://www.social-searcher.com/"), 
            ("Namechk", "https://namechk.com"), 
            ("KnowEm", "https://knowem.com"), 
            ("Usersearch", "https://usersearch.com"), 
            ("Username Check", "https://usernamecheck.com"), 
            ("Pipl", "https://pipl.com"), 
            ("Social Search", "https://socialsearch.com"), 
            ("NameAPI", "https://nameapi.org"), 
            ("NameCheckr", "https://namecheckr.com")
        ],
        "4. La Verificación del Correo Electrónico": [
            ("Hunter.io Email Verifier", "https://hunter.io/email-verifier"), 
            ("VoilaNorbert", "https://voilanorbert.com"), 
            ("FindThat.Email", "https://findthat.email"), 
            ("Snov.io", "https://snov.io"), 
            ("Clearbit", "https://clearbit.com"), 
            ("EmailFinder.io", "https://emailfinder.io"), 
            ("EmailSearch.io", "https://emailsearch.io"), 
            ("ContactOut", "https://contactout.com"), 
            ("AeroLeads", "https://aeroleads.com"), 
            ("FindEmails", "https://findemails.com")
        ],
        "5. La Búsqueda de Geolocalizacion ": [
            ("IPinfo", "https://ipinfo.io"), 
            ("GeoIPTool", "https://geoiptool.com"), 
            ("IPLocation", "https://iplocation.net"), 
            ("WhatIsMyIPAddress", "https://whatismyipaddress.com"), 
            ("IP Geolocation", "https://ipgeolocation.io"), 
            ("MaxMind", "https://maxmind.com"), 
            ("DB-IP", "https://db-ip.com"), 
            ("ipstack", "https://ipstack.com"), 
            ("ipapi", "https://ipapi.co"), 
            ("GeoNames", "https://geonames.org")
        ],
        "6. Los Registros Públicos": [
            ("FamilySearch", "https://familysearch.org"), 
            ("Ancestry", "https://ancestry.com"), 
            ("MyHeritage", "https://myheritage.com"), 
            ("Findmypast", "https://findmypast.com"), 
            ("USGenWeb", "https://usgenweb.org"), 
            ("PublicRecords", "https://publicrecords.com"), 
            ("Radaris", "https://radaris.com"), 
            ("USA People Search", "https://usapeoplesearch.com"), 
            ("CheckMate", "https://checkmate.com"), 
            ("PeopleLooker", "https://peoplelooker.com")
        ],
        "7. Redes Sociales": [
            ("Facebook", "https://facebook.com"), 
            ("Twitter", "https://twitter.com"), 
            ("LinkedIn", "https://linkedin.com"), 
            ("Instagram", "https://instagram.com"), 
            ("Reddit", "https://reddit.com"), 
            ("Tumblr", "https://tumblr.com"), 
            ("Pinterest", "https://pinterest.com"), 
            ("Snapchat", "https://snapchat.com"), 
            ("WhatsApp", "https://whatsapp.com"), 
            ("Flickr", "https://flickr.com")
        ],
        "8. Informacion de Dominio y IP": [
            ("WHOIS Lookup", "https://whois.domaintools.com"), 
            ("IPinfo", "https://ipinfo.io"), 
            ("ARIN WHOIS", "https://whois.arin.net"), 
            ("IPLocation", "https://iplocation.net"), 
            ("MXToolbox", "https://mxtoolbox.com"), 
            ("DNSstuff", "https://dnsstuff.com"), 
            ("DomainBigData", "https://domainbigdata.com"), 
            ("Shodan", "https://shodan.io"), 
            ("Censys", "https://censys.io"), 
            ("IP-Address", "https://ip-address.com")
        ],
        "9. Busqueda de Numero de Telefono": [
            ("TrueCaller", "https://www.truecaller.com"), 
            ("Whitepages", "https://www.whitepages.com"), 
            ("AnyWho", "https://www.anywho.com"), 
            ("SpyDialer", "https://www.spydialer.com"), 
            ("NumLookup", "https://www.numlookup.com"), 
            ("ZLOOKUP", "https://www.zlookup.com"), 
            ("CallerSmart", "https://www.callersmart.com"), 
            ("Pipl", "https://www.pipl.com"), 
            ("ReversePhoneLookup", "https://www.reversephonelookup.com"), 
            ("PhoneNumberLookup", "https://www.phonenumberlookup.com")
        ],
        "10. Direcciones de Criptomonedas": [
            ("Blockchair", "https://blockchair.com"), 
            ("Etherscan", "https://etherscan.io"), 
            ("Blockchain Explorer", "https://www.blockchain.com/explorer"), 
            ("BitcoinScan", "https://bitcoinscan.com"), 
            ("CoinGecko", "https://coingecko.com"), 
            ("CryptoCompare", "https://cryptocompare.com"), 
            ("BlockCypher", "https://www.blockcypher.com"), 
            ("BTCScan", "https://btcscan.org"), 
            ("Chainalysis", "https://chainalysis.com"), 
            ("TokenView", "https://tokenview.com")
        ]
    }

    print(Fore.RED + "Selecciona una Seccion:" + Style.RESET_ALL)
    for key in sections:
        print(Fore.WHITE + key + Style.RESET_ALL)

    try:
        choice = int(input(Fore.RED + "Introduce el Numero de la Seccion: " + Style.RESET_ALL))
        if choice not in range(1, len(sections) + 1):
            raise ValueError

        section_name = list(sections.keys())[choice - 1]
        print(Fore.RED + f"\nWebsites in {section_name}:" + Style.RESET_ALL)
        for idx, (name, _) in enumerate(sections[section_name], start=1):
            print(Fore.GREEN + f"{idx}. {name}" + Style.RESET_ALL)

        website_choice = int(input(Fore.RED + "Selecciona el Numero de tu Opcion: " + Style.RESET_ALL))
        if website_choice not in range(1, len(sections[section_name]) + 1):
            raise ValueError

        url_map = {name: url for (name, url) in sections[section_name]}
        selected_website = list(url_map.keys())[website_choice - 1]
        selected_url = url_map[selected_website]
        
        # Open the URL in the default web browser
        webbrowser.open(selected_url)

    except (ValueError, IndexError):
        print(Fore.YELLOW + "Opcion no Valida. Por Favor,Intentelo de Nuevo" + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    print_banner()
    print_menu()
