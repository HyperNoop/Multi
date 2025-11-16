# Multi
C'est un langage de programation qui peut aceuillir 7 langue.
# 🌍 Multi Programming Language

**Multi** est un langage de programmation révolutionnaire qui permet aux développeurs du monde entier de coder dans leur langue maternelle. Le code peut être automatiquement traduit entre différentes langues tout en préservant sa logique.

## ✨ Caractéristiques

- 🌐 **Multilingue** - Codez en français, anglais, espagnol, japonais, et plus
- 🔄 **Traduction automatique** - Convertissez votre code entre langues instantanément
- 🚀 **Simple et intuitif** - Syntaxe claire et facile à apprendre
- 💼 **Prêt pour l'entreprise** - Idéal pour les équipes internationales
- 🆓 **Open Source** - Licence MIT, gratuit pour tous

## 📦 Installation

### Avec pip (recommandé)
```bash
pip install multi-lang
```

### Depuis le code source
```bash
git clone https://github.com/votre-username/multi-lang.git
cd multi-lang
python setup.py install
```

### Installation manuelle
```bash
# Télécharger multi.py
wget https://raw.githubusercontent.com/votre-username/multi-lang/main/multi.py

# Rendre exécutable
chmod +x multi.py

# Créer un alias (optionnel)
alias multi='python3 /chemin/vers/multi.py'
```

## 🚀 Démarrage Rapide

### Votre premier programme

Créez un fichier `hello.multi`:
```multi
// En français
variable nom = "Alice"
afficher "Bonjour"
afficher nom
```

Exécutez-le:
```bash
multi run hello.multi --lang fr
```

Sortie:
### Le même programme en anglais
```multi
// In English
variable name = "Alice"
print "Hello"
print name
```
```bash
multi run hello.multi --lang en
```

### Traduction automatique

Traduisez votre code du français vers l'anglais:
```bash
multi translate hello.multi --from fr --to en --output hello_en.multi
```

## 📚 Exemples

### Variables et Types
```multi
// Français
variable texte = "Hello"
variable nombre = 42
variable decimal = 3.14
variable vrai_ou_faux = vrai
variable liste = [1, 2, 3, 4, 5]
```

### Fonctions
```multi
// Français
fonction addition(a, b) {
    retourner a + b
}

variable resultat = addition(10, 5)
afficher resultat  // 15
```

### Conditions
```multi
// Français
variable age = 20

si age >= 18 {
    afficher "Majeur"
} sinon {
    afficher "Mineur"
}
```

### Boucles
```multi
// Français
pour i dans [1, 2, 3, 4, 5] {
    afficher i
}

variable compteur = 0
tant_que compteur < 5 {
    afficher compteur
    compteur = compteur + 1
}
```

### Exemple Complet: Calculatrice
```multi
// Français
fonction calculer_moyenne(notes) {
    variable somme = 0
    pour note dans notes {
        somme = somme + note
    }
    retourner somme / longueur(notes)
}

variable mes_notes = [15, 18, 12, 16, 14]
variable moyenne = calculer_moyenne(mes_notes)

afficher "Moyenne:"
afficher moyenne  // 15
```

## 🌐 Langues Supportées

| Langue | Code | Exemple |
|--------|------|---------|
| 🇫🇷 Français | `fr` | `variable x = 10` |
| 🇬🇧 English | `en` | `variable x = 10` |
| 🇪🇸 Español | `es` | `variable x = 10` |
| 🇯🇵 日本語 | `ja` | `変数 x = 10` |
| 🇩🇪 Deutsch | `de` | `variable x = 10` |
| 🇵🇹 Português | `pt` | `variavel x = 10` |
| 🇰🇷 한국어 | `ko` | `변수 x = 10` |

## 📖 Documentation Complète

### Commandes CLI
```bash
# Exécuter un fichier
multi run <fichier> [--lang <langue>]

# Mode interactif (REPL)
multi repl [--lang <langue>]

# Traduire un fichier
multi translate <fichier> --from <lang> --to <lang> [--output <fichier>]

# Afficher l'aide
multi help

# Afficher la version
multi version
```

### Mots-clés (Français)

| Mot-clé | Description | Exemple |
|---------|-------------|---------|
| `variable` | Déclarer une variable | `variable x = 10` |
| `constante` | Déclarer une constante | `constante PI = 3.14` |
| `fonction` | Déclarer une fonction | `fonction add(a, b) { }` |
| `si` | Condition if | `si x > 0 { }` |
| `sinon` | Condition else | `sinon { }` |
| `pour` | Boucle for | `pour i dans [1,2,3] { }` |
| `tant_que` | Boucle while | `tant_que x < 10 { }` |
| `retourner` | Retourner une valeur | `retourner x + y` |
| `afficher` | Afficher dans la console | `afficher "Hello"` |
| `vrai` | Booléen true | `variable ok = vrai` |
| `faux` | Booléen false | `variable ko = faux` |

### Opérateurs

| Opérateur | Description |
|-----------|-------------|
| `+` | Addition |
| `-` | Soustraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulo |
| `==` | Égalité |
| `!=` | Différent |
| `<` | Inférieur |
| `>` | Supérieur |
| `<=` | Inférieur ou égal |
| `>=` | Supérieur ou égal |
| `et` / `and` | ET logique |
| `ou` / `or` | OU logique |
| `non` / `not` | NON logique |

## 🔧 Mode Interactif (REPL)

Lancez le mode interactif:
```bash
multi repl --lang fr
```
## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment vous pouvez aider:

1. Fork le projet
2. Créez une branche (`git checkout -b feature/amazing-feature`)
3. Committez vos changements (`git commit -m 'Add amazing feature'`)
4. Push vers la branche (`git push origin feature/amazing-feature`)
5. Ouvrez une Pull Request

### Domaines d'amélioration

- [ ] Ajouter plus de langues
- [ ] Bibliothèque standard (HTTP, fichiers, etc.)
- [ ] IDE graphique
- [ ] Support des classes et objets avancés
- [ ] Optimisation du compilateur
- [ ] Documentation interactive
- [ ] Package manager

## 📝 Roadmap

### Version 1.0 (Actuelle) ✅
- Interpréteur de base
- Support de 7+ langues
- Traduction automatique
- CLI complet

### Version 1.1 (Prochaine)
- [ ] Classes et objets
- [ ] Gestion d'exceptions avancée
- [ ] Import de modules
- [ ] Bibliothèque standard basique

### Version 2.0 (Future)
- [ ] Compilateur optimisé
- [ ] IDE web intégré
- [ ] Débogueur graphique
- [ ] Package manager
- [ ] Documentation interactive

## 🐛 Bugs Connus

- Les caractères Unicode dans les identifiants peuvent causer des problèmes
- Les boucles imbriquées profondes peuvent être lentes
- Pas de support des imports de modules (à venir)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteurs

- **Votre Nom** - *Créateur initial* - [VotreGitHub](https://github.com/votre-username)

## 🙏 Remerciements

- Inspiré par la nécessité de briser les barrières linguistiques en programmation
- Merci à la communauté open source
- Merci à tous les contributeurs

## 📞 Contact

- GitHub: [@HyperNoop](https://github.com/HyperNoop)

## ⭐ Supportez le Projet

Si vous aimez Multi, donnez-nous une ⭐ sur GitHub !

---

**Multi** - *Programmation sans frontières* 🌍✨
