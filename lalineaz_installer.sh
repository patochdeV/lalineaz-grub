#!/bin/bash
# Vérifier les droits d'administrateur
if [[ $EUID -ne 0 ]]; then
echo "Veuillez exécuter ce script en tant qu'administrateur (sudo)"
exit 1
fi
# Cloner le référentiel GitHub
git clone --depth 1 https://github.com/patochdeV/lalineaz-grub.git /tmp/lalineaz-grub

# Copier le dossier grub-lalineaz dans /usr/share/grub/themes/
sudo cp -r /tmp/lalineaz-grub/grub-lalineaz /usr/share/grub/themes/

# Mettre à jour le fichier /etc/default/grub
sudo sed -i 's/^GRUB_THEME=.*/GRUB_THEME="\/usr\/share\/grub\/themes\/grub-lalineaz"/' /etc/default/grub

# Mettre à jour la configuration GRUB2
sudo update-grub

# Supprimer le référentiel cloné temporairement
rm -rf /tmp/lalineaz-grub

