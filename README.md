# B-Tree

#### Complexité des algorithmes :

- search(self, key) :
  - Complexité en temps: O(log⁡k(n)) où n est le nombre total de clés et k est le facteur.
  - Explication:
    - À chaque étape, la méthode élimine environ la moitié des nœuds restants en choisissant le bon sous-arbre.
    - La hauteur d'un arbre B est O(log⁡k n), où n est le nombre total de clés et k est le facteur.
    - À chaque niveau de l'arbre, un nombre constant d'opérations est effectué (comparaisons et choix du sous-arbre suivant).
    - Par conséquent, la complexité totale est proportionnelle à la hauteur de l'arbre.
- is_linear(self) :
  - Complexité en temps: O(n)
  - Explication:
    - Cette méthode parcourt chaque nœud de l'arbre pour construire une liste linéaire des clés.
    - Chaque clé dans l'arbre est visitée exactement une fois.
    - Puisque le nombre total de clés dans l'arbre est n, la complexité en temps est linéaire par rapport au nombre de clés.
- is_balanced(self) :
  - Complexité en temps: O(n)
  - Explication:
    - La méthode vérifie si chaque sous-arbre de l'arbre B est équilibré.
    - Pour ce faire, elle parcourt tous les nœuds de l'arbre.
    - Bien que la hauteur de l'arbre soit O(log⁡k n), chaque nœud (et donc chaque clé) doit être visité pour vérifier si le sous-arbre est équilibré.
    - La complexité est donc linéaire par rapport au nombre total de clés dans l'arbre.
- is_covred(self) :
  - Complexité en temps: O(n)
  - Explication:
    - Cette méthode vérifie si chaque nœud respecte les propriétés des arbres B en termes de nombre de clés et d'enfants.
    - La vérification nécessite un parcours de tous les nœuds pour examiner leurs propriétés. Comme chaque nœud est visité une fois, la complexité est linéaire par rapport au nombre total de nœuds dans l'arbre, soit O(n).
- is_btree(self) :
  - Complexité en temps: O(n)
  - Explication:
    - Cette méthode vérifie si l'arbre actuel satisfait à toutes les conditions d'un arbre B valide.
    - Pour valider un arbre B, il est nécessaire de parcourir tous les nœuds et de vérifier ces propriétés.
- insert(self) :
  - Complexité en temps: O(logk(n))
  - Explication:
    - Si le nœud a de l'espace, l'insertion est immédiate; sinon, une scission est nécessaire, mais reste limitée en nombre grâce à la hauteur logarithmique de l'arbre.
    - À chaque étape, un nombre fixe d'opérations assure l'insertion et la gestion des scissions.

#### Procédure d'éxecution du projet:

- Toutes nos méthodes sont implémentées et téstées dans Btree.py et Node.py et pour les éxécuter, on lance la commande suivante dans la racine du projet: `python3 Btree.py` et `python3 Node.py`, si aprés l'éxecution rien ne s'affiche sur la console donc tout les tests sont éxecutés avec succés.
- En plus de ça on a crée un exemple de B-Tree dans Main.py avec des test plus approfondis pour chaqu'une des méthodes principales avec un affichage plus clair, pour éxecuter le main il faut se trouver dans la racine du projet et lancé la commande: `python3 Main.py`

#### Lien Uml :

- Le lien de l'Uml est [ici](https://lucid.app/lucidchart/cebac901-f2a1-4598-9ad9-aecc0c582ab5/edit?viewport_loc=-2085%2C-164%2C2219%2C1108%2C0_0invitationId=inv_77a8c4b0-db7e-4e99-8f9f-669c7454a042)
