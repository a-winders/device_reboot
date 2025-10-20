import sys
import json

store_list = sys.argv[1]

# Remove brackets and split by comma
parsed_list = store_list.strip('[]').split(',')

# Clean each item by removing whitespace and quotes
parsed_list = [item.strip().strip("'") for item in parsed_list]

# Print as JSON instead of Python list representation
print(json.dumps(parsed_list))