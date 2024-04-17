# lineaz-grub-
reprise d'un theme existant sur gnome-look mais que je n'arrive pas a installer et qui n'a plus l'air suivi dans le but de le rendre utilisable et instalable facilement


1 : Cloner le référentiel GitHub lalineaz-grub dans /usr/share/grub/themes/lalineaz-grub.

         sudo git clone --depth 1 https://github.com/patochdeV/lalineaz-grub.git /usr/share/grub/themes/lalineaz-grub

2: Ouvrez le fichier /etc/default/grub dans un éditeur de texte 

         sudo nano /etc/default/grub

3: Ajoutez ou modifiez la ligne GRUB_THEME avec le nom du dossier cloné .

         GRUB_THEME="/usr/share/grub/themes/lalineaz-grub"

4: Enregistrez et quittez le fichier de configuration.

         CTRL+x

5: Mettez à jour la configuration GRUB2 pour appliquer les modifications :

        sudo update-grub

lalineaz-grub est maintenant prêt à être utilisé après la prochaine réinitialisation de votre système.

