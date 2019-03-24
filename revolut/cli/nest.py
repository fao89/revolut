import argparse
import json
import textwrap
import sys

from revolut.use_cases.json_parser import ParseJson


example = textwrap.dedent(
    '''
        examples: 
                 python nest.py --filename input.json currency country city

                 cat input.json | python nest.py currency country city
    '''
)
parser = argparse.ArgumentParser(description='Process JSON files',
                                 epilog=example, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('nest', metavar='Nest', type=str, nargs='+',
               help='nesting levels for the dict')
parser.add_argument('--filename', nargs='?', type=argparse.FileType('rb'), default=sys.stdin)
args = parser.parse_args()

if args.filename.name == '<stdin>':
    json_stream = args.filename.detach()
    data = json_stream.read()
else:
    data = args.filename.read()

loaded_json = json.loads(data)
convert = ParseJson(loaded_json, args.nest)
convert.parse()

print(json.dumps(convert.output, indent=4, sort_keys=True))