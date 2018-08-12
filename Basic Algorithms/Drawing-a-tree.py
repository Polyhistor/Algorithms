#Drawing a tree using et3

from et3 import Tree, TreeStyle

t = Tree( "((a,b),c);" )
circular_style = TreeStyle()
circular_style.mode = "c" # draw tree in circular mode
circular_style.scale = 20
t.render("mytree.png", w=183, units="mm", tree_style=circular_style)


# This case is not a major issue or complex problem to be solved, thus there is no big O notation.