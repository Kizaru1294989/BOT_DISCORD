from III import BinaryTreeNode
from III import BinaryTree

# arbre binaire

root = BinaryTreeNode("Quel logiciel serveur voulez-vous apprendre Nginx ou Apache2 ?")
left_child = BinaryTreeNode("Voulez-vous apprendre les bases de Nginx ou les concepts avancés ?")
right_child = BinaryTreeNode("Voulez-vous apprendre les bases de Apache2 ou les concepts avancés ?")
nginx_basic = BinaryTreeNode("Vous pouvez commencer par le cours Nginx pour les débutants. Voulez-vous que je vous propose des liens ?")
nginx_advanced = BinaryTreeNode("Vous pouvez consulter le cours Nginx avancé. Voulez-vous que je vous propose des liens ?")
apache_basic = BinaryTreeNode("Vous pouvez commencer par le cours Apache2 pour les débutants. Voulez-vous que je vous propose des liens ?")
apache_advanced = BinaryTreeNode("Vous pouvez consulter le cours Apache2 avancé. Voulez-vous que je vous propose des liens ?")
root.left = left_child
root.right = right_child
left_child.left = nginx_basic
left_child.right = nginx_advanced
right_child.left = apache_basic
right_child.right = apache_advanced

question_tree = BinaryTree(root)