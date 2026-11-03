# Popula o banco com categorias, posts, usuarios e comentarios do blog.
# Nao sobrescreve o que ja existe. Execute com:
#   python manage.py shell -c "exec(open('populate_db.py', encoding='utf-8').read())"
from datetime import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone

from blog.models import Category, Comment, Post

User = get_user_model()

CATEGORIES = {
    'Futebol de Salão': 'Jogos de futsal: quadra, ritmo intenso e a base de tudo o que aprendi com a bola.',
    'Futebol Society': 'Jogos de futebol 7 na grama sintética, a modalidade em que mais levantei troféus.',
    'Futebol de Campo': 'Jogos de campo, com gramado grande e jogo mais cadenciado.',
    'Viagens': 'Campeonatos disputados fora de São Paulo e as experiências que vieram com eles.',
    'Conquistas': 'Títulos e momentos em que erguemos o troféu.',
}

USERNAMES = [
    'pai_do_rafael',
    'colega_de_time',
    'atletica_poli',
    'tecnico_poli',
    'namorada_do_rafael',
    'mae_do_rafael',
    'amigo_do_time',
]


def when(year, month, day, hour=20, minute=0):
    return timezone.make_aware(datetime(year, month, day, hour, minute))


IMAGES_URL = (
    'https://raw.githubusercontent.com/rafamussi/blog-pessoal-futebol/main/static/images/posts/'
)


def figure(filename, alt, caption):
    return (
        f'<figure><img src="{IMAGES_URL}{filename}" alt="{alt}">'
        f'<figcaption>{caption}</figcaption></figure>'
    )


POSTS = [
    {
        'title': 'Enfrentei o craque Endrick',
        'posted_at': when(2016, 4, 3),
        'categories': ['Futebol Society', 'Viagens'],
        'content': (
            '<p>Na <strong>GO Cup</strong>, em Goiânia, o <strong>Playball</strong> '
            'enfrentou o <strong>Palmeiras</strong>, considerada a melhor base do país. '
            'Do outro lado estava o Endrick, hoje estrela do Real Madrid e da Seleção Brasileira.</p>'
            + figure('endrick-go-cup.jpg', 'Rafael em campo na GO Cup', 'Playball x Palmeiras, GO Cup (2016)')
            + '<p>Apesar da goleada por <strong>6 x 1</strong>, foi uma baita experiência jogar '
            'contra jogadores que viriam a se tornar estrelas do futebol profissional. '
            'E eu fiquei feliz por ter conseguido marcar um gol na partida.</p>'
        ),
        'comments': [],
    },
    {
        'title': 'Marquei meu primeiro hat-trick',
        'posted_at': when(2018, 9, 22),
        'categories': ['Futebol de Salão'],
        'content': (
            '<p>Pelo <strong>Campeonato Estadual de Futebol de Salão</strong>, o '
            '<strong>Lausanne</strong> venceu o <strong>Penha</strong> por <strong>3 x 2</strong>, '
            'e os três gols foram meus.</p>'
            + figure('hat-trick-lausanne.jpg', 'Rafael com a medalha do Lausanne', 'Lausanne, Campeonato Estadual de Futebol de Salão (2018)')
            + '<p>Abrimos o placar em uma jogada de lateral, mas tomamos a virada. Depois, meu amigo '
            'me deixou na cara do gol e eu empatei o jogo. No fim, fiz um golaço de falta, '
            'completei o hat-trick e garanti a vitória.</p>'
            '<p>Depois do jogo, meus amigos brincaram me entrevistando e perguntando qual música eu '
            'queria que tocasse no Fantástico. Uma curiosidade: meu pai, que sempre ia aos jogos, '
            'não foi a esse. Desde então, o pessoal brinca que ele não pode mais ir.</p>'
        ),
        'comments': [
            (
                'pai_do_rafael',
                when(2018, 9, 22, 21, 30),
                'Parabéns, filho! Três gols e uma vitória justo no jogo que eu não fui. '
                'Já está decidido: nos próximos eu fico em casa, não mexo em time que está ganhando! '
                'Muito orgulho de você.',
            ),
            (
                'colega_de_time',
                when(2018, 9, 23, 9, 10),
                'Que golaço de falta! A virada deu um susto, mas o time não desistiu. '
                'A entrevista para o Fantástico já está marcada, hein, craque!',
            ),
        ],
    },
    {
        'title': 'Fomos campeões da Floripa Cup',
        'posted_at': when(2019, 12, 7),
        'categories': ['Futebol de Campo', 'Viagens', 'Conquistas'],
        'content': (
            '<p>O <strong>Opportunity Brazil</strong> venceu o <strong>Gideão</strong> por '
            '<strong>2 x 0</strong> na final da <strong>Floripa Cup</strong>, disputada em pleno '
            'estádio da Ressacada, casa do Avaí.</p>'
            + figure('floripa-cup-campeao.jpg', 'Rafael com o troféu da Floripa Cup', 'Opportunity Brazil, campeão da Floripa Cup (2019)')
            + '<p>Chovia muito forte na hora do jogo, o que deixou a partida mais truncada. Em um '
            'escanteio, marcamos o primeiro gol, e no finalzinho, em um contra-ataque, fiz o '
            'segundo para encerrar a decisão. Terminei como artilheiro do campeonato e erguendo o troféu.</p>'
            '<p>Um fato curioso: nesse time joguei ao lado do André Luiz, joia do Corinthians que '
            'acabou convocado para a Seleção Brasileira. Na época ele jogava de lateral esquerdo; hoje '
            'é o volante do nosso país.</p>'
        ),
        'comments': [
            (
                'mae_do_rafael',
                when(2019, 12, 7, 21, 0),
                'Que orgulho, filho! Final em estádio de profissional, debaixo daquela chuva toda, '
                'e ainda artilheiro e campeão. Você merece cada conquista.',
            ),
            (
                'amigo_do_time',
                when(2019, 12, 8, 10, 20),
                'Artilheiro e campeão na Ressacada! E ainda jogando ao lado do futuro volante da '
                'Seleção. Que time era aquele!',
            ),
        ],
    },
    {
        'title': 'Poli FC campeã da Copa Bixo',
        'posted_at': when(2024, 5, 4),
        'categories': ['Futebol de Campo', 'Conquistas'],
        'content': (
            '<p>No meu primeiro campeonato pela faculdade, o <strong>Poli FC</strong> chegou à final '
            'da <strong>Copa Bixo</strong> contra a forte equipe da <strong>EEFE USP</strong>.</p>'
            + figure('copa-bixo-poli-fc.jpg', 'Time do Poli FC com as medalhas', 'Poli FC, campeã da Copa Bixo (2024)')
            + '<p>Logo no início do segundo tempo, um colega de time cobrou uma falta cruzando na área e eu '
            'fiz o gol, abrindo o placar. Estava tudo '
            'certo até que, no finalzinho, sofremos o gol de empate e a partida terminou em '
            '<strong>1 x 1</strong>, levando a decisão para os pênaltis.</p>'
            '<p>Garanti a minha cobrança e, depois de seis cobranças para cada lado, o nosso goleiro '
            'defendeu. Vencemos por <strong>5 x 4</strong> e nos tornamos campeões.</p>'
        ),
        'comments': [
            (
                'atletica_poli',
                when(2024, 5, 4, 21, 15),
                'Parabéns, Poli FC! Gol logo no início do segundo tempo e título nos pênaltis contra '
                'a EEFE. A Atlética tem muito orgulho de vocês!',
            ),
            (
                'tecnico_poli',
                when(2024, 5, 5, 8, 30),
                'Mesmo depois do empate no fim, o grupo manteve a cabeça no lugar e resolveu nos '
                'pênaltis. O gol no começo do segundo tempo, em cruzamento de falta, foi decisivo. Parabéns, time, e parabéns ao goleiro!',
            ),
            (
                'namorada_do_rafael',
                when(2024, 5, 5, 10, 45),
                'Muito orgulho de você! Primeiro campeonato pela faculdade, gol na final e já campeão. '
                'Você merece demais.',
            ),
        ],
    },
]


categories = {}
for name, description in CATEGORIES.items():
    categories[name], _ = Category.objects.get_or_create(
        name=name, defaults={'description': description}
    )

users = {}
for username in USERNAMES:
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_unusable_password()
        user.save()
    users[username] = user

for data in POSTS:
    post, created = Post.objects.get_or_create(
        title=data['title'],
        defaults={'content': data['content'], 'posted_at': data['posted_at']},
    )
    if created:
        post.categories.set([categories[name] for name in data['categories']])
    for username, posted_at, text in data['comments']:
        Comment.objects.get_or_create(
            post=post,
            author=users[username],
            defaults={'text': text, 'posted_at': posted_at},
        )

print(
    f'{Category.objects.count()} categorias, {Post.objects.count()} posts e '
    f'{Comment.objects.count()} comentários no banco.'
)
