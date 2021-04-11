import tkinter as tk



G = {
    (1,1) : [None, None, (2,1), None],
    (1,2) : [None, None, None, None],
    (1,3) : [None, (1,4), (2,3), None],
    (1,4) : [None, (1,3), (1,5), (2,4)],
    (1,5) : [None, None, (1,4), (2,5)],
    (1,6) : [None, (1,7), (2,6), None],
    (1,7) : [None, (1,6), None, (1,8)],
    (1,8) : [None, None, (1,7), (2,8)],
    (2,1) : [(1,1), (2,2), None, None],
    (2,2) : [None, (2,1), (2,3), (3,2)],
    (2,3) : [(1,3), None, None, (2,2)],
    (2,4) : [(1,4), None, (3,4), None],
    (2,5) : [(1,5), (2,6), None, None],
    (2,6) : [(1,6), (2,4), (2,6), (3,6)],
    (2,7) : [None, None, (2,6), (3,7)],
    (2,8) : [(1,8), None, (3,8), None],
    (3,1) : [None, None, None, None],
    (3,2) : [(2,2), None, (4,2), None],
    (3,3) : [None, None, None, None],
    (3,4): [(2,4), (3,5), None, None],
    (3,5) : [None, (3,6), None, (3,4)],
    (3,6) : [(2,6), (3,7), (4,6), (3,5)],
    (3,7) : [(2,7), None, (4,7), (3,6)],
    (3,8) : [(2,8), None, (4,8), None],
    (4,1) : [None, None, None, None],
    (4,2) : [(3,2), (4,3), None, None],
    (4,3) : [None, (4,4), None, (4,2)],
    (4,4) : [None, None, None, (4,3)],
    (4,5) : [None, (4,6), None, None],
    (4,6) : [(4,5), None, None, (3,6)],
    (4,7) : [(3,7), (4,8), None, None],
    (4,8) : [(3,8), None, None, (4,7)]

}

liste_visite = [
    None
]

def labyrinthe(graph, cellule, recherche):
    liste_visite.append(cellule)

    if recherche in graph[cellule]:
        liste_visite.append(recherche)
        return liste_visite[1:liste_visite.index(recherche)+1]

    for i in range(len(graph[cellule])):


        if graph[cellule][i] not in liste_visite:
            labyrinthe(graph, graph[cellule][i], recherche)
        
        if recherche in graph[cellule]:
            liste_visite.append(recherche)
            return
    return liste_visite[1:liste_visite.index(recherche)+1]






def taille(graph):
    max_x = 0
    max_y = 0

    for i in graph:
        if max_x < i[1]:
            max_x = i[1]

        if max_y < i[0]:
            max_y = i[0]
    return max_x, max_y



root= tk.Tk()
C=tk.Canvas(root, width=802, height=402, bg="ivory")

def dessiner(G):
    largeur, longueur = taille(G)
    largeur_cellule = 800/largeur
    longueur_cellule= 400/longueur
    x = 2
    y = 2
    for i in G:
        if G[i][0] == None:     #Nord
            C.create_line(x, y, x + largeur_cellule, y)

        if G[i][2] == None:     #Sud
            C.create_line(x, y + longueur_cellule, x + largeur_cellule, y + longueur_cellule)

        if G[i][1] == None:     #Est
            C.create_line(x + largeur_cellule, y, x + largeur_cellule, y + longueur_cellule)

        if G[i][3] == None:     #Ouest
            C.create_line(x, y, x, y + longueur_cellule)

        if x >= 700:                #permet de passer a la ligne suivant quand arrivé au bout
            x = 2
            y += longueur_cellule
        else:
            x += largeur_cellule    #case suivante


def dessine_chemin(graph, cellule, recherche):
    largeur, longueur = taille(G)
    largeur_trait = 800/largeur
    longueur_trait= 400/longueur

    chemin = labyrinthe(graph, cellule, recherche)
    for i in range(len(chemin)-1):
        x1 = largeur_trait*chemin[i][1] - largeur_trait/2
        y1 = longueur_trait*chemin[i][0] - longueur_trait/2
        x2 = largeur_trait*chemin[i][1] - largeur_trait/2
        y2 = longueur_trait*chemin[i][0] - longueur_trait/2

        if chemin[i][1] < chemin[i+1][1]:
            x2 = x1+largeur_trait

                           #si la cellule est a droite ou a gauche
        elif chemin[i][1] > chemin[i+1][1]:
            x2 = x1-largeur_trait

        if chemin[i][0] < chemin[i+1][0]:
            y2 = y1+largeur_trait         
                  #si la cellule est a droite ou a gauche
        elif chemin[i][0] > chemin[i+1][0]:
            y2 = y1-largeur_trait
        if i == len(chemin)-2:
            C.create_line(x1, y1, x2, y2, fill = 'SpringGreen2', arrow = 'last',  arrowshape = [15, 20, 15])
        else:
            tracer_trait(x1, y1, x2, y2, )
def tracer_trait(x1, y1, x2, y2):
    C.create_line(x1, y1, x2, y2, fill = 'SpringGreen2')

dessiner(G)
dessine_chemin(G, (1,1), (4,7))
C.pack()
root.mainloop()


