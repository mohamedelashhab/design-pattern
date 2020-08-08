from Structual.Composite.Shape import Shape
from Structual.Composite.Group import Group

if __name__ == '__main__':
    s1 = Shape()
    s2 = Shape()
    s3 = Shape()
    s4 = Shape()
    g1 = Group()
    g1.add(s1)
    g1.add(s2)
    g2 = Group()
    g2.add(g1)
    g2.add(s3)
    g2.render()