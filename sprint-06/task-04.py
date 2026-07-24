import json


def find(file, key):
    with open(file, 'r') as f:
        data = json.load(f)

    results = []

    def traverse(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == key:
                    if isinstance(v, list):
                        for item in v:
                            if isinstance(item, (dict, list)):
                                traverse(item)
                            elif item not in results:
                                results.append(item)
                    elif isinstance(v, dict):
                        traverse(v)
                    else:
                        if v not in results:
                            results.append(v)
                else:
                    traverse(v)
        elif isinstance(node, list):
            for item in node:
                traverse(item)

    traverse(data)
    return results