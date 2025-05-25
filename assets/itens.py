# File made by: Davi

from assets.things import Char

class Itens:
    tavern = [
        {"nome": "Pocao de Vida", "preco": 5},
        {"nome": "Pocao de Ataque", "preco": 3},
    ]

    blacksmith = [
        {"nome": "Espada de Madeira", "preco": 5, "dano": 0.5},
        {"nome": "Espada de Prata", "preco": 10, "dano": 1.0},
        {"nome": "Espada de Ouro", "preco": 20, "dano": 2.0},
        {"nome": "Espada de Platina", "preco": 40, "dano": 3.0},
        {"nome": "Espada de Diamante", "preco": 60, "dano": 4.5},
    ]



class Village:
    village_names = ["Eldoria", "Brumária", "Calthera"]

class Flashback:
    flashbacks = [
        # PRESENTE
        "Aton na praia sente o desconforto no ar. Há algo errado, mesmo num lugar tão pacífico.",
        "Enquanto treina com soldados, um deles comenta baixinho: 'Esse é o tal de Skalice... ouvi dizer que matou o próprio comandante.'",
        "Durante a primeira noite na taverna, Aton acorda suando frio — não por um pesadelo, mas por não ter sonhado com nada.",
        "Um garoto se aproxima e pergunta se Aton já matou alguém. Aton apenas abaixa os olhos e finge não ouvir.",
        "Enquanto caminha pelas ruas de Eldoria, percebe olhares. Alguns o admiram, outros o evitam. Ele já está marcado ali.",
        "Na primeira batalha de treino, Aton segura o golpe no último instante. Algo dentro dele hesitou — e ele não sabe por quê.",
        "Durante o jantar com os fazendeiros, ouve histórias sobre paz. Ele tenta sorrir, mas sente que está em um mundo que não entende mais.",
        "Ao observar as montanhas distantes, Aton sussurra: 'Será que algum dia volto pra casa?'. Ninguém responde.",

        # PASSADO
        "Skalice em chamas. Gritos, fumaça, o aço contra o aço. Aton tenta proteger os civis, mas chega tarde demais.",
        "O jovem aprendiz cai durante um treino. Aton, impaciente, ignora seu pedido de ajuda. Dias depois, o menino está morto.",
        "Um salão escuro. Nobres de Skalice cochicham sobre alianças com mercenários. Aton escuta — e escolhe o silêncio.",
        "A neve cobre um campo de batalha. Aton segura um corpo sem vida: era seu companheiro mais antigo.",
        "A mulher de cabelos castanhos entrega a ele um colar. 'Se for, não volte sem alma.' Ele parte mesmo assim.",
        "Aton desperta coberto de sangue. Ele mesmo matou um prisioneiro que implorava por perdão. Não foi justiça. Foi raiva.",
        "Chamas cercam a vila. Aton carrega uma criança ferida enquanto vozes gritam seu nome.",
        "Durante o treinamento, um companheiro chora. Aton o manda calar. Depois, descobre que o rapaz perdeu toda a família.",

        # FUTURO
        "Diante de um trono vazio, Aton hesita. Um dia, ele sentará ali. Mas com quais sacrifícios?",
        "Uma voz de criança ecoa: 'Papai, você voltou?' Aton olha em volta. Ele não tem filhos. Ainda.",
        "No reflexo de sua espada, vê-se mais velho, cansado, cercado por túmulos. Todos nomes que ele não conseguiu salvar.",
        "Caminhando pela feira de Vargrid, ouve gritos. É uma revolta. No meio da multidão, alguém grita: 'Aton traiu Skalice!'",
        "Durante um sonho, acorda em uma cela. Guardas o observam com medo. Um aviso ecoa: 'O futuro não te perdoa.'",
        "Diante do espelho d água em Várdann, vê a si mesmo como rei. Atrás, seu reino queimava.",
        "Aton caminha por um campo destruído — reconhece a armadura no chão. Era sua. Mas ele nunca esteve ali... ainda.",
        "Em uma fortaleza distante, alguém lê um livro. Na capa: 'Crônicas do Redentor de Skalice'. Mas Aton nunca escreveu isso."
    ]


class Enemy:
    enemies = {
    "Slime": {
        "hp": 80,
        "attack": 1.0,
        "mana": 20,
        "spells": [],
        "boss": False,
        "drop": "Bola de slime"
    },
    "Dragão Jovem": {
        "hp": 250,
        "attack": 4.0,
        "mana": 100,
        "spells": ["Sopro de Fogo"],
        "boss": True,
        "drop": "Escama de dragao"
    },
    "Lobo Feroz": {
        "hp": 120,
        "attack": 2.5,
        "mana": 0,
        "spells": [],
        "boss": False,
        "drop": "Garra de lobo"
    },
    "Fênix": {
        "hp": 200,
        "attack": 3.0,
        "mana": 150,
        "spells": ["Chama da Ressurreição"],
        "boss": True,
        "drop": "Pluma de fenix"
    },
    "Elemental de Fogo": {
        "hp": 150,
        "attack": 3.5,
        "mana": 120,
        "spells": ["Onda de Chamas", "Bola de Fogo"],
        "boss": False,
        "drop": "Essencia de fogo"
    },
    "Rei Slime": {
        "hp": 300,
        "attack": 5.0,
        "mana": 50,
        "spells": ["Divisão de Slime"],
        "boss": True,
        "drop": "Bola de slime"
    },
    "Dragonete": {
        "hp": 150,
        "attack": 2.0,
        "mana": 50,
        "spells": [],
        "boss": False,
        "drop": "Escama de dragao"
    },
    "Lobo Alfa": {
        "hp": 180,
        "attack": 3.5,
        "mana": 0,
        "spells": [],
        "boss": True,
        "drop": "Garra de lobo"
    },
    "Espírito das Chamas": {
        "hp": 130,
        "attack": 2.8,
        "mana": 100,
        "spells": ["Bola de Fogo"],
        "boss": False,
        "drop": "Essencia de fogo"
    }
}
