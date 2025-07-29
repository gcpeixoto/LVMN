import json

def extract_outline_from_ipynb(ipynb_path, output_path=None):
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    outline_lines = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            for line in cell['source']:
                if line.lstrip().startswith('#'):
                    outline_lines.append(line.rstrip('\n'))

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f_out:
            for line in outline_lines:
                f_out.write(line + '\n')
        print(f"Outline saved to {output_path}")
    else:
        print('\n'.join(outline_lines))


# Usage:
file = "../ipynb/aula-07-fatoracao-lu.ipynb"
extract_outline_from_ipynb(file, 'outline.txt')