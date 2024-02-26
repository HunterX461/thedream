import sys
import urllib.parse

def remove_fuzz_parameter(url):
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    if 'FUZZ' in query_params:
        del query_params['FUZZ']

    new_query_string = urllib.parse.urlencode(query_params, doseq=True)
    new_url = parsed_url._replace(query=new_query_string).geturl()
    return new_url

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        urls_with_fuzz = f.readlines()

    with open(output_file, 'w') as f:
        for url in urls_with_fuzz:
            new_url = remove_fuzz_parameter(url.strip())
            f.write(new_url + '\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python remove_fuzz.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_file(input_file, output_file)