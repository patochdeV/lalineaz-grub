# lineaz-grub-
Reprise d'un theme existant sur gnome-look qui n'a plus l'air suivi dans le but de le rendre utilisable et rendre l'installation facile .

0 : Installation paquet Git pour telecharger directement avec des commandes "git clone"

    sudo apt install git-all 

1 : Cloner le référentiel GitHub lalineaz-grub dans /usr/share/grub/themes/lalineaz-grub.

    sudo git clone --depth 1 https://github.com/patochdeV/lalineaz-grub.git /usr/share/grub/themes/lalineaz-grub

2: Ouvrez le fichier /etc/default/grub dans un éditeur de texte 

    sudo nano /etc/default/grub

3: Ajoutez ou modifiez la ligne GRUB_THEME avec le nom du dossier cloné .

    GRUB_THEME="/usr/share/grub/themes/lalineaz-grub/linea_grub/theme.txt"

4: Enregistrez et quittez le fichier de configuration.

    CTRL+x

5: Mettez à jour la configuration GRUB2 pour appliquer les modifications :

    sudo update-grub

lalineaz-grub est maintenant prêt à être utilisé après la prochaine réinitialisation de votre système.



- en cours de test une installation en script shell et via installer :
- 
(shell)

  ajout du script " lalineaz_installer.sh " au depot 

  1 : Rendez le script exécutable : chmod +x lalineaz_installer.sh

  2 : Exécutez le script avec les privilèges d'administrateur (sudo) : sudo ./lalineaz_installer.sh

  (installer)

  python grub_lalineaz_setup.py

  

