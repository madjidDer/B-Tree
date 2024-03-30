class Node:
    def __init__(self):
        """
        Constructeur de la classe Node. Initialise un nouveau nœud avec des propriétés par défaut.

        Exemple:
        >>> node = Node()
        >>> isinstance(node, Node)
        True
        """
        self.keys = []       
        self.children = []
        self.parent = None 
        self.leaf = True     

    def insert_key(self, key):
        """
        Insère une nouvelle clé dans le nœud courant.
        
        Paramètres:
        key: La clé à insérer dans le nœud.
        Exemple:
        >>> node = Node()
        >>> node.insert_key(5)
        >>> 5 in node.keys
        True
        """
        self.keys.append(key)
        self.keys.sort()
    
    def delete_key(self, key):
        """
        Supprime une clé spécifiée du nœud courant si elle existe.
        
        Paramètres:
        key: La clé à supprimer du nœud.
        Exemple:
        >>> node = Node()
        >>> node.insert_key(5)
        >>> node.delete_key(5)
        >>> 5 in node.keys
        False
        """
        if key in self.keys:
            self.keys.remove(key)

    def set_parent(self, parent):
        """
        Définit le parent du nœud courant.
        
        Paramètres:
        parent: L'instance de Node à définir comme parent.
        Exemple:
        >>> node = Node()
        >>> parent = Node()
        >>> node.set_parent(parent)
        >>> node.parent == parent
        True
        """
        self.parent = parent
                             
    def insert_child(self, child, i):
        """
        Ajoute un enfant au nœud courant, met à jour le parent de l'enfant, et indique que le nœud n'est plus une feuille.
        
        Paramètres:
        child : L'instance de Node à ajouter en tant qu'enfant.
        i : l'indice ou inserer le child
        Exemple:
        >>> node = Node()
        >>> child = Node()
        >>> node.insert_child(child, 0)
        >>> child in node.children
        True
        >>> node.is_leaf()
        False
        >>> child.get_parent() == node
        True
        """
        self.children.insert(i, child)
        self.leaf = False
        child.set_parent(self)

    def remove_child(self, child):
        """
        Supprime un enfant spécifié du nœud courant, et met à jour le parent de l'enfant supprimé.
        
        Paramètres:
        child: L'instance de Node à supprimer en tant qu'enfant.
        Exemple:
        >>> parent = Node()
        >>> child1 = Node()
        >>> child2 = Node()
        >>> parent.insert_child(child1, 0)
        >>> parent.insert_child(child2, 1)
        >>> parent.remove_child(child1)
        >>> child1 in parent.children
        False
        >>> child1.get_parent() is None
        True
        >>> parent.is_leaf()
        False
        >>> parent.remove_child(child2)
        >>> parent.is_leaf()
        True
        """
        if child in self.children:
            self.children.remove(child)
            if len(self.children)==0 :
                self.leaf = True
            child.set_parent(None)

    def set_leaf(self, leaf):
        """
        Définit si le nœud courant est une feuille.
        
        Paramètres:
        leaf: Un booléen indiquant si le nœud est une feuille (True) ou non (False).
        Exemple:
        >>> node = Node()
        >>> node.set_leaf(False)
        >>> node.leaf
        False
        >>> node.set_leaf(True)
        >>> node.leaf
        True
        """
        self.leaf = leaf

    def find_key(self, key):
        """
        Vérifie si une clé spécifique est présente dans le nœud.
        
        Paramètres:
        key: La clé à rechercher dans le nœud.
        Retourne:
        True si la clé est trouvée, sinon False.
        Exemple:
        >>> node = Node()
        >>> node.insert_key(5)
        >>> node.find_key(5)
        True
        >>> node.find_key(6)
        False
        """
        return key in self.keys
        
    def is_leaf(self):
        """
        Indique si le nœud courant est une feuille.
        
        Paramètres: Aucun.
        Retourne:
        True si le nœud est une feuille, sinon False.
        Exemples:
        >>> n = Node()
        >>> n.is_leaf()
        True
        >>> n.insert_child(Node(), 0)
        >>> n.is_leaf()
        False
        """
        return self.leaf

    def get_keys(self):
        """
        Retourne la liste des clés contenues dans le nœud.
        
        Paramètres: Aucun.
        Retourne:
        Une liste des clés dans le nœud.
        Exemple:
        >>> node = Node()
        >>> node.insert_key(5)
        >>> node.insert_key(3)
        >>> node.get_keys()
        [3, 5]
        """
        return self.keys
    
    def set_keys(self, keys):
        """
        Mets a jour la liste des clés contenues dans le nœud.
        
        Paramètres:
        keys : la nouvelle liste de cles
        Retourne:
        Exemple:
        >>> node = Node()
        >>> node.insert_key(5)
        >>> node.insert_key(3)
        >>> node.set_keys([1, 2])
        >>> node.get_keys()
        [1, 2]
        """
        self.keys = keys

    def get_children(self):
        """
        Retourne la liste des enfants du nœud.
        
        Paramètres: Aucun.
        
        Retourne:
        Une liste des enfants (Node instances) du nœud.
        Exemple:
        >>> parent = Node()
        >>> child1 = Node()
        >>> child2 = Node()
        >>> parent.insert_child(child1, 0)
        >>> parent.insert_child(child2, 1)
        >>> parent.get_children() == [child1, child2]
        True
        """
        return self.children

    def set_children(self, children):
        """
        Mets a jour la liste des children du nœud.
        
        Paramètres:
        children : la nouvelle liste de children
        Retourne:
        Exemple:
        >>> parent = Node()
        >>> child1 = Node()
        >>> child2 = Node()
        >>> child3 = Node()
        >>> parent.insert_child(child1, 0)
        >>> parent.insert_child(child2, 1)
        >>> parent.get_children() == [child1, child2]
        True
        >>> parent.set_children([child3])
        >>> parent.get_children() == [child3]
        True
        """
        self.children = children

    def get_parent(self):
        """
        Retourne le parent du nœud courant.
        
        Paramètres: Aucun.
        Retourne:
        L'instance de Node qui est le parent du nœud courant, ou None si le nœud n'a pas de parent.
        Exemple:
        >>> child = Node()
        >>> parent = Node()
        >>> child.set_parent(parent)
        >>> child.get_parent() == parent
        True
        """
        return self.parent

    def liste_nodes(self):
        """
        fonction interne pour lister les noeuds de l'arbre pour l'affichage
        """
        if(self.is_leaf()):
            return '"'+str(self.keys)+'"'+'\n'
        else:
            res = ""
            for child in self.children:
                res+= '"'+(str(self.keys)) + '"' +"\n"
                res+=child.liste_nodes()
            return res

    def list_arcs(self):
        """
        fonction interne pour lister les arcs de l'arbre pour l'affichage
        """
        if(self.is_leaf()):
            return ""
        else:
            res = ""
            for child in self.children:
                res+= ('"'+str(self.keys) +'"'+ "->"+'"'+str(child.keys)) +'"'+"\n"
                res+=child.list_arcs()
            return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()