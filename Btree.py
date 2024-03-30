from Node import Node
import subprocess
import bisect

def indice(val, l):
    """
    Effectue une recherche de 'val' dans la liste triée 'l'. 
    
    Cette fonction renvoie l'indice de 'val' dans 'l' si 'val' est trouvée. 
    Si 'val' n'est pas trouvée, elle renvoie l'indice où 'val' pourrait être 
    insérée pour maintenir 'l' triée.
    
    Paramètres :
    val : La valeur à rechercher.
    l : Liste triée dans laquelle effectuer la recherche.
    
    Contraintes :
    La liste 'l' doit être triée.
    La valeur 'val' doit être de type comparable aux éléments de 'l'.
    
    Retourne :
    L'indice de 'val' dans 'l' si trouvée ; sinon, l'indice où 'val' devrait être insérée.
    """
    for i in range(len(l)):
        if l[i] >= val:
            return i
    return len(l)

class Btree:
    def __init__(self, root, k):
        """
        Initialise un nouvel arbre B avec un nœud racine et un facteur de ramification.

        Paramètres:
        root (Node): Le nœud racine de l'arbre B.
        k (int): Le facteur de ramification de l'arbre B.
        """
        self.k = k
        self.root = root

    def print_tree(self,  node=None, indent="", last=True):
        """
        Affiche l'arbre B

        Paramètres:
        node: Le nœud à partir duquel commencer l'affichage. Si None, commence à la racine de l'arbre.
        indent: La chaîne de caractères utilisée pour l'indentation, indiquant le niveau actuel dans l'arbre.
        last: Indique si le nœud est le dernier enfant de son parent.
        """
        if node is None:
            node = self.root
        prefix = indent + ("└── " if last else "├── ")
        print(prefix + ", ".join(str(key) for key in node.get_keys()))
        indent += "    " if last else "|   "
        children = node.get_children()
        for i, child in enumerate(children, start=1):
            next_last = i == len(children)
            self.print_tree(child, indent, next_last)

    def search(self, key):
        """
        Recherche une clé dans l'arbre B.

        Paramètres:
        key: La clé à rechercher dans l'arbre.

        Retourne:
        bool: True si la clé est trouvée, False sinon.
        """
        if(self.root.is_leaf()):
            return self.root.find_key(key)
        else:
            i = 0
            while i < len(self.root.get_keys()):
                if(key == self.root.get_keys()[i]):
                    return True
                elif (key < self.root.get_keys()[i]):
                    return Btree(self.root.get_children()[i], self.k).search(key)
                else:
                    i+=1
            return Btree(self.root.get_children()[-1], self.k).search(key)
        
    def is_linear(self):
        """
        Retourne une représentation linéaire des clés de l'arbre B.

        Retourne:
        list: Liste des clés de l'arbre en ordre croissant.
        """
        result = []
        if(self.root.is_leaf()):
            return self.root.get_keys()
        else:
            result += Btree(self.root.get_children()[0], self.k).is_linear()
            i = 0
            while i < len(self.root.get_keys()):
                result.append(self.root.get_keys()[i])
                result += Btree(self.root.get_children()[i+1], self.k).is_linear()
                i+=1
        return result
    
    def is_balanced(self):
        """
        Vérifie si l'arbre B est équilibré.

        Retourne:
        bool: True si l'arbre est équilibré, False sinon.
        """
        def check_node(node):
            if node.is_leaf():
                return True
            if len(node.children)!=len(node.keys)+1:
                return False
            for child in node.children:
                if not check_node(child):
                    return False
            return True

        return check_node(self.root)

    def is_covered(self):
        """
        Vérifie si chaque nœud de l'arbre B respecte les propriétés de couverture d'un arbre B d'ordre k.
        Pour un arbre B non-feuille, chaque nœud doit avoir au moins k//2 clés et au plus k clés, et 
        k//2 + 1 enfants au minimum et k + 1 enfants au maximum.

        Retourne:
        bool: True si toutes les propriétés de couverture sont respectées pour chaque nœud, False sinon.
        """
        if(self.root.is_leaf()):
            return self.k//2 <= len(self.root.get_keys()) <= self.k
        cond1 = False
        cond2 = False
        if self.root.get_parent() == None :
            cond1 = 0 <= len(self.root.get_keys()) <= self.k
            cond2 = 0 <= len(self.root.get_children()) <= self.k+1
        else :
            cond1 = self.k//2 <= len(self.root.get_keys()) <= self.k
            cond2 = self.k//2+1 <= len(self.root.get_children()) <= self.k+1

        children_is_covered = all(Btree(child, self.k).is_covered() for child in self.root.get_children())
        return cond1 and cond2 and children_is_covered

    def is_btree(self):
        """
        Vérifie si l'arbre actuel est un arbre B valide

        Retourne:
        bool: True si l'arbre est un arbre B valide, False sinon.
        """
        return self.is_balanced and self.is_covered and self.is_linear()==sorted(self.is_linear())

    def insert(self, key):
        """
        Insère une clé dans l'arbre B.

        Arguments:
        key: La clé à insérer dans l'arbre B.
		"""
        root = self.root
        if (self.search(key)):
            #print("Cette valeur existe déjà.")
            return
        elif (len(root.get_keys()) == self.k):
            self._insert_nonfull(root, key)
            if (len(root.get_keys()) > self.k):
                new_root = Node()        
                new_root.insert_child(self.root, 0)
                self._split_child(new_root, 0)   
                self.root = new_root
        else:
            self._insert_nonfull(root, key)
        
    def _insert_nonfull(self, node, key):
        """
        Insère une clé 'key' dans un nœud 'node' qui n'est pas plein.

		Arguments:
		node: Le nœud où insérer la clé.
        key: La clé à insérer.
        """
        i = len(node.get_keys())-1
        if node.leaf:
            node.insert_key(key)
        else:
            if self.k!=2:
                idx = indice(key, node.keys)
                if len(node.children[idx].keys) == self.k :
                    self._split_child(node, idx)
                    if key > node.keys[idx]:        
                        idx +=1
                self._insert_nonfull(node.children[idx], key)
            else:
                idx = indice(key, node.keys)
                self._insert_nonfull(node.children[idx], key)
                if len(node.children[idx].keys) > self.k :
                    self._split_child(node, idx)

    def _split_child(self, parent_node, child_index):
        """
        Divise le nœud enfant plein à l'indice 'child_index' du nœud 'parent'

		Arguments:
		parent_node: Le nœud parent contenant le nœud enfant à diviser
        child_index: L'indice du nœud enfant à diviser dans la liste des enfants du parent
        """
        to_split = parent_node.children[child_index]
        new_node = Node()
        parent_node.insert_child(new_node, child_index+1)
                    
        idx = indice(to_split.keys[self.k//2], parent_node.keys)
        parent_node.keys.insert(idx, to_split.keys[self.k//2])
        new_node.keys = to_split.keys[self.k//2+1:]
        to_split.keys = to_split.keys[0: self.k//2]
        
        if not to_split.is_leaf():
            new_node.leaf = False
            new_node.children = to_split.children[self.k//2+1:]
            to_split.children = to_split.children[:self.k//2+1]

    def insert_liste(self, liste):
        """
        Inserer les element de la liste liste  dans l'arbre b 
        Paramètres :
        liste : la liste des valeurs a inserer successivement  
        Contraintes :
        aucune
        """
        for i in liste :
            self.insert(i)

    def explore_tree(self, filename="mon_arbre.dot"):
        """
        Crée un fichier .dot à partir de notre arbre

        Arguments:
        filename: Nom du fichier .dot à créer
        """
        res = 'digraph "parfait3" { \nnode [fontname="DejaVu-Sans"]\n' 
        res += self.root.liste_nodes()
        res += self.root.list_arcs()
        res += "}"

        with open(filename, "w") as file:
            file.write(res)

        return res
    
    def convert_dot_to_png(self, dot_filename, png_filename="mon_arbre.png"):
        """
        Utilise Graphviz pour convertir un fichier .dot en un fichier .png.

        Arguments:
        dot_filename: Le chemin du fichier .dot à convertir.
        png_filename: Le chemin du fichier .png à créer.
        """
        try:
            subprocess.run(["dot", "-Tpng", dot_filename, "-o", png_filename], check=True)
            print(f"Fichier '{png_filename}' créé avec succès dans la racine du projet.\nOuvrez l'image pour voir le résultat.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la conversion du fichier: {e}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
