import os
import urllib.parse

def genera_indice(root_dir=".", output_file="INDEX.md"):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Indice Automatico dei Contenuti\n\n")

        # Esplora tutte le cartelle e sottocartelle
        for subdir, dirs, files in sorted(os.walk(root_dir)):
            # Salta la cartella di git e le cartelle nascoste
            if '.git' in subdir or os.path.basename(subdir).startswith('.'):
                continue

            # Calcola l'indentazione in base alla profondità della cartella
            livello = subdir.replace(root_dir, '').count(os.sep)
            indentazione_cartella = '  ' * livello
            nome_cartella = os.path.basename(subdir)

            if nome_cartella and nome_cartella != '.':
                f.write(f"{indentazione_cartella}- **📂 {nome_cartella}/**\n")

            indentazione_file = '  ' * (livello + 1)
            
            for file in sorted(files):
                # Ignora lo script stesso e l'indice che stiamo creando
                if file in [output_file, 'genera_indice.py', 'README.md'] or file.startswith('.'):
                    continue
                
                # Crea il percorso relativo e codifica gli spazi per i link URL
                percorso_relativo = os.path.relpath(os.path.join(subdir, file), root_dir)
                percorso_relativo = percorso_relativo.replace('\\', '/') # Fix per chi usa Windows
                percorso_url = urllib.parse.quote(percorso_relativo)
                
                f.write(f"{indentazione_file}- [📄 {file}](./{percorso_url})\n")

if __name__ == "__main__":
    genera_indice()
    print("Indice generato con successo nel file INDEX.md!")