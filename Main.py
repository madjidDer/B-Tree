from Btree import Btree
from Node import Node
import os
import subprocess

class Test():
    def __init__(self) -> None:
        self.tree = self.init1()
    
    def init1(self):
        n1 = Node()
        n2 = Node()
        n3 = Node()
        n4 = Node()
        n5 = Node()
        n6 = Node()
        n7 = Node()
        n8 = Node()

        n1.set_leaf(False)
        n1.insert_child(n2, 0)
        n1.insert_child(n5, 1)
        
        n2.insert_child(n3, 0)
        n2.insert_child(n4, 1)
        n2.set_leaf(False)
        n2.set_parent(n1)
        
        n3.set_leaf(True)
        n3.set_parent(n2)
        
        n4.set_leaf(True)
        n4.set_parent(n2)
        
        n5.insert_child(n6, 0)
        n5.insert_child(n7, 1)
        n5.insert_child(n8, 2)
        n5.set_leaf(False)
        n5.set_parent(n1)
        
        n6.set_leaf(True)
        n6.set_parent(n5)
        
        n7.set_leaf(True)
        n7.set_parent(n5)
        
        n8.set_leaf(True)
        n8.set_parent(n5)
        
        n1.insert_key(6)
        n2.insert_key(4)
        n3.insert_key(2)
        n4.insert_key(5)
        n5.insert_key(10)
        n5.insert_key(14)
        n6.insert_key(8)
        n7.insert_key(12)
        n8.insert_key(16)
        n8.insert_key(18)

        return Btree(n1,2)
    
    def test1Search(self):
        print("------------------------------Test 1 Recherche:-------------------------------")
        print("Dans notre exemple, on a les valeurs: 2, 4, 5, 6, 8, 10, 12, 14, 16, 18")
        print("20 : "+str(self.tree.search(20)))
        print("11 : "+str(self.tree.search(11)))
        print("4 : "+str(self.tree.search(4)))
        print("12 : "+str(self.tree.search(12)))
        print("6 : "+str(self.tree.search(6)))
        print("4 : "+str(self.tree.search(4)))
        print("10 : "+str(self.tree.search(10)))
        print("14 : "+str(self.tree.search(14)))
        print("2 : "+str(self.tree.search(2)))
        print("18 : "+str(self.tree.search(18)))
        print("8 : "+str(self.tree.search(8)))
        print("16 : "+str(self.tree.search(16)))
        print("5 : "+str(self.tree.search(5)))
        print("0 : "+str(self.tree.search(0)))

    def test2Linearisation(self):
        print("------------------------------Test 2 Linearisation------------------------------")
        print(self.tree.is_linear())
    
    def test3Equilibre(self):
        print("--------------------------------Test 3 Equilibre--------------------------------")
        print("Cet arbre est équilibré : "+str(self.tree.is_balanced()))

    def test4Couverture(self):
        print("--------------------------------Test 4 Couverture--------------------------------")
        print("Cet arbre est couvert : "+str(self.tree.is_covered()))

    def test5RepresentationGraphique(self):
        print("--------------------------Test 5 Representation Graphique--------------------------")
        self.tree.explore_tree("arbre.dot")
        self.tree.convert_dot_to_png("arbre.dot", "arbre.png")

    def test_experimentations_1(self):
        print("-------------------------------------Test 6-------------------------------------")
        tree = Btree(Node(),2)
        tree.insert_liste([2,4,5,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,7,9,11,13])
        list = tree.is_linear()
        assert(len(list)==23)
        assert(list==sorted(list))
        assert(tree.is_btree())
        assert(tree.is_balanced())
        assert(tree.is_covered())
        print("test_experimentations_1 passé avec succès")

    def test_experimentations_2(self):
        print("-------------------------------------Test 7-------------------------------------")
        tree = Btree(Node(),3)
        for i in range(10000):
            tree.insert(i)
        list = tree.is_linear()
        assert(len(list)==10000)
        assert(list==sorted(list))
        assert(tree.is_btree())
        assert(tree.is_balanced())
        assert(tree.is_covered())
        print("test_experimentations_2 passé avec succès")

if __name__ == '__main__':
    Test().test1Search()
    print()
    Test().test2Linearisation()
    print()
    Test().test3Equilibre()
    print()
    Test().test4Couverture()
    print()
    Test().test5RepresentationGraphique()
    print()
    Test().test_experimentations_1()
    print()
    Test().test_experimentations_2()