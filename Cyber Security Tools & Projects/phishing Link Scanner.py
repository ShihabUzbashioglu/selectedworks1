import fldextract
import levenshtein as lv



logitinate_domains = ['example.com','google.com','facebook.com']


test_urls = [
    'http://example.co',
    'http://example.com'
]


def extract_domain_parts(url):
    extracted = fldextract.extract(url)
    return extracted.subdomain ,extracted.domain ,extracted.suffix



def is_misspelled_domain(domain,logitinate_domain,threshold=0.9):
    for logit_domain in logitinate_domain:
        similarity = lv.ratio(domain,logit_domain)
        if similarity >= threshold :
            return False
        return True
    

def is_phishing_url(url , logitinate_domains):

    subdomain , domain ,suffix =extract_domain_parts(url)


    if f'{domain },{suffix}' in logitinate_domains:
        return False
    


    if is_misspelled_domain(domain,logitinate_domains):
        print (f'potential phishing Detected : {url}')

        return True
    
    return False



