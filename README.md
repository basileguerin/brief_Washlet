# Résultat assessment : Votre première mission

Chers Solution Leaders, chers Lead Software engineers et chers software engineers...

Le groupe Adecco est très heureux de vous compter parmi ses nouveaux collaborateurs !!! Vous avez tous passé vos tests avec brio (encore bravo !!), maintenant on entre dans le vif du sujet...Parlons de votre première mission !

Votre client s'appelle "Toto", c'est l'un des leaders mondiaux des WC. Son représentant, M.Madoka Kitamura, a besoin de vous pour conquérir le marché sud-américain !

En effet, après un long séjour passé à Tijuana, peu de temps avant son mandat, le président du groupe a eu une idée...intégrer deux nouveaux marchés : la nourriture méxicaine et les produits pharmaceutiques en faisant l'acquisition de deux nouvelles sociétés françaises: 1) la société General Mills, Inc possédant la marque OldElPaso 2) la société Vidal, spécialisée dans la revente de médicaments.

La fusion avec ces nouveaux partenaires génèrait pas moins de 50 millions d'euros supplémentaires au groupe !! Mais, avant cela il doit d'abord convaincre ses actionnaires...C'est là que vous intervenez !

Une assemblée extraordinaire aura lieu ainsi la semaine prochaine. Et M.Kitamura souhaiterait, à cette occasion, présenter une application mobile à ses collègues siégeant au conseil d'administration ! Son futur slogan : "Washlet - Burrito - Lopéramide ...One to rule them all" ! Le departement IT Toto s'occupera de la partie mobile (pour le front-end), il souhaiterait donc que vous réalisiez la partie back-end.

## Description:

Vous réaliserez 3 API ciblant respectivement les WC washlet, les produits Old el paso et les médicaments à base de lopéramide. Pour cela vous vous répartirez en 3 équipes.

1 - Team Washlet

```
Source données:
https://eu.toto.com/fr/produits/washlet
```

Membres
- Kevin : Solution Leader
- Basile : Lead Software Engineer
- Mickaël : Software engineer
- Guinel : Software engineer

2 - Team Burrito

```
Source données:
https://www.oldelpaso.fr/products
```

Membres
- Harold : Solution Leader
- David : Lead Software Engineer
- Slava : Software engineer
- Geoffroy : Software engineer

3 - Team Lopéramide

```
Source données:
https://www.vidal.fr/medicaments/substances/loperamide-5732.html
```

Membres
- Charley : Solution Leader
- Antoine : Lead Software Engineer
- Soraya : Software engineer (Absente)
- Johann : Software engineer
- Amadou : Software engineer

## Objectifs par equipe:

I ) En utilisant les "Sources données", réaliser 5 endpoints pour réaliser des opérations : 1er : endpoint d'ajout de tous les produits 2ème : endpoint d'effacement de tous les produits 3ème : endpoint d'ajout d'un seul produit 4ème : endpoint de modif d'un seul produit 5ème : endpoint d'effacement d'un seul produit

II) Sauvegarder les données en base de données

III) Enregistrer les projets sur github

IV) Déployer chaque API sur le serveur de production Nb : Bruno notre stagiaire sénior a eu la gentillesse de vous préparer le terrain en déployant 3 API de test (avec 2 endpoints : / et /animaux). Il n'a pas fait plus...car il a tout simplement copier-collé un code trouvé sur google sans le comprendre... Il a bien evidemment été remercié !

## Note sur les responsabilités en fonction des postes:

Les SL encadreront les opérations au sein de chaque équipe et veilleront à ce que l'API créee par leur Team corresponde au mieux à la demande du client ainsi qu'à la deadline. Les LSE piloteront les développements d'un point de vue technique, notamment concernant l'utilisation des bonnes technologies et des bonnes pratiques. Les SE, sont spécialisés dans le développement. Ils incarnent le coeur des équipes. Leur force de travail et leur savoir-faire rend possible la réalisation du projet.

NB : Dans le cadre du projet, les SL et LSE feront du développement en plus de leur mission respective (au minimum un endpoint) NB 2 : Les déploiements sur le serveur de prod seront effectués par les SL

## Technologies :

bases de données : mongodb conteneurisation : docker langage back-end : python serveur web : flask webscrapping : beautifulsoup os serveur de prod : windows 10 connexion au serveur de prod : rdp

## Note sur la connexion au serveur de production:

Vous pourrez vous y connecter en rdp grace à son adresse IP, un identifiant + mot de passe qui vous ont été communiqués sur discord. Vous pourrez également requéter vos API respectivement via les ports 666, 667, 668

NB : Une seule personne peut se connecter à la fois (si une 2ème personne se connecte en même temps, cela quitte la session de la première) NB 2 : En production, vous ne devez pas installer d'application supplémentaire. Vous ferez avec les moyens du bord ! ;)

Bien cordialement

Votre contact Adecco
