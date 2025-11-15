import re

def fix_bib_keys(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Padrão para encontrar chaves com acentos
    pattern = r'@(\w+)\{([^}]*[áéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ][^}]*)\d{4},'
    
    def replace_key(match):
        entry_type = match.group(1)
        key = match.group(2)
        # Remover acentos da chave
        key_fixed = re.sub(r'[áéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ]', lambda m: {
            'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u',
            'â':'a', 'ê':'e', 'î':'i', 'ô':'o', 'û':'u',
            'ã':'a', 'õ':'o', 'ç':'c',
            'Á':'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ú':'U',
            'Â':'A', 'Ê':'E', 'Î':'I', 'Ô':'O', 'Û':'U',
            'Ã':'A', 'Õ':'O', 'Ç':'C'
        }.get(m.group(0), m.group(0)), key)
        return f'@{entry_type}{{{key_fixed}{match.group(0).split(key)[-1]}'
    
    content_fixed = re.sub(pattern, replace_key, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content_fixed)
    
    print("Arquivo corrigido.")

fix_bib_keys('referencias.bib')