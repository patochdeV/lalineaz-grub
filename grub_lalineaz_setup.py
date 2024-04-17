from installer import Archive
import os

def install_lalineaz_grub_theme():
    # Télécharger le thème GRUB2 lalineaz-grub
theme_archive = Archive('https://github.com/patochdeV/lalineaz-grub/archive/refs/heads/main.tar.gz')
    theme_archive.download()

    # Extraire l'archive téléchargée
theme_archive.extract()

    # Copier le dossier grub-lalineaz dans /usr/share/grub/themes/
theme_folder_path = os.path.join('/usr', 'share', 'grub', 'themes')
    theme_folder_name = 'grub-lalineaz'
theme_destination_path = os.path.join(theme_folder_path, theme_folder_name)

    os.makedirs(theme_destination_path, exist_ok=True)

    for file_name in os.listdir(theme_archive.path):
        file_source_path = os.path.join(theme_archive.path, file_name)
        file_destination_path = os.path.join(theme_destination_path, file_name)
        os.symlink(file_source_path, file_destination_path)

    # Mettre à jour le fichier /etc/default/grub
grub_config_file = '/etc/default/grub'
with open(grub_config_file, 'r') as file:
        grub_config = file.read()

    grub_config = grub_config.replace('GRUB_THEME=', 'GRUB_THEME="' + theme_destination_path + '"\n')

    with open(grub_config_file, 'w') as file:
        file.write(grub_config)

    # Mettre à jour la configuration GRUB2
os.system('sudo update-grub')

# Appeler la fonction d'installation du thème
install_lalineaz_grub_theme()

