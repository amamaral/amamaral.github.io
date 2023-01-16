from jinja2 import Environment, FileSystemLoader
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import markdown
import codecs
import os
import re, yaml, pypandoc, datetime

env = Environment(loader=FileSystemLoader('jinja-templates'))
md = markdown.Markdown(extensions=["markdown.extensions.tables"])

# Bibliographic management


class Works():
    def __init__(self):
        self.title = 'Title'
        self.img = 'http://placehold.it/100x100'
        self.abstract = 'Short abstract'
        self.href = '#work_link'
        self.tags = ['']
        self.authors = ''
        self.journal = ''
        self.volume = ''
        self.pages = ''
        self.month = ''
        self.year = -1

with open('papers//bibtex_list.bib') as bibtex_file:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

    works = [Works() for i in range(len(bib_database.entries))]

    for index, entry in enumerate(bib_database.entries):
        works[index].title = entry['title']
        if 'file' in entry.keys():
            filename = entry['file'][1:-8]
            works[index].img = 'papers//thumbnails/' + filename + '.jpg'

        if 'abstract' in entry.keys():
            works[index].abstract = entry['abstract']

        if 'doi' in entry.keys():
            works[index].href = 'http:////dx.doi.org/'+entry['doi']
        elif 'url' in entry.keys():
            works[index].href = entry['url']

        if 'month' in entry.keys():
            works[index].month = entry['month']

        if 'year' in entry.keys():
            works[index].year = entry['year']

        if 'journal' in entry.keys():
            works[index].journal = entry['journal']

        if 'volume' in entry.keys():
            works[index].volume = entry['volume']

        if 'author' in entry.keys():
            works[index].author = entry['author']

        if 'pages' in entry.keys():
            works[index].pages = entry['pages']

    works = sorted(works, key=lambda w: -int(w.year))


class Conferences():
    def __init__(self):
        self.title = 'Title'
        self.img = 'http://placehold.it/100x100'
        self.abstract = 'Short abstract'
        self.href = '#work_link'
        self.tags = ['']
        self.authors = ''
        self.journal = ''
        self.volume = ''
        self.pages = ''
        self.month = ''
        self.year = -1

with open('conferences//bibtex_list.bib') as bibtex_file:
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

    conference_papers = [Conferences() for i in range(len(bib_database.entries))]

    for index, entry in enumerate(bib_database.entries):
        conference_papers[index].title = entry['title']
        if 'file' in entry.keys():
            filename = entry['file'][1:-8]
            conference_papers[index].img = r'conferences/thumbnails/' + filename + '.jpg'

        if 'abstract' in entry.keys():
            conference_papers[index].abstract = entry['abstract']

        if 'doi' in entry.keys():
            conference_papers[index].href = 'http:////dx.doi.org/'+entry['doi']
        elif 'url' in entry.keys():
            conference_papers[index].href = entry['url']

        if 'month' in entry.keys():
            conference_papers[index].month = entry['month']

        if 'year' in entry.keys():
            conference_papers[index].year = entry['year']

        if 'journal' in entry.keys():
            conference_papers[index].journal = entry['journal']

        if 'volume' in entry.keys():
            conference_papers[index].volume = entry['volume']

        if 'author' in entry.keys():
            conference_papers[index].author = entry['author']

        if 'pages' in entry.keys():
            conference_papers[index].pages = entry['pages']

    works = sorted(works, key=lambda w: -int(w.year))

##############
# INDEX.HTML #
##############
index = env.get_template('index_template.html')
featured_works = works[0:4]
index_html = index.render(featured=featured_works)
with codecs.open("index.html", "w", "utf-8") as fh:
    fh.write(index_html)

##############
# ABOUT.HTML #
##############


class CV_personal_info:
    def __init__(self, name='My name', sub_text='some description',
                 address='My address', phone='(555) 5555-5555',
                 email='my_mail@server.com', facebook='',
                 linkedin='', twitter='', googlescholar='', researchgate='',
                 orcid=''):
        self.name = name
        self.sub_text = sub_text
        self.address = address
        self.phone = phone
        self.email = email
        self.facebook = facebook
        self.linkedin = linkedin
        self.twitter = twitter
        self.googlescholar = googlescholar
        self.researchgate = researchgate
        self.orcid = orcid


class CV_entry():
    def __init__(self, period, title, entity, description):
        self.period = period
        self.title = title
        self.entity = entity
        self.description = description

personal = CV_personal_info('Anderson Monteiro Amaral',
                            """For a short CV,
                            <a href="http://lattes.cnpq.br">click here</a>.<br>
                            For a full scientific CV, <a href="http://lattes.cnpq.br/1832322110328811">
                            click here</a>.""",
                            """R. Prof. Moraes Rego, 1235 <br>50670-901, Cidade
                            universitária <br>Recife - PE - Brazil""",
                            '+55 (81) 2126-2258; +55 (81) 2126-2204',
                            'andersonamaral(at)df(dot)ufpe(dot)br',
                            'http://www.facebook.com/andersonmonteiroamaral',
                            '', #linkedin
                            'http://twitter.com/amaral_am',
                            'https://scholar.google.com.br/citations?hl=pt-BR&user=eEP-tGAAAAAJ',
                            'https://www.researchgate.net/profile/Anderson_Amaral',
                            'http://www.orcid.org/0000-0001-5706-9744')

academic = []
academic.append(CV_entry("2012 - 2016", "Ph.D. in physics",
                         """Universidade Federal de Pernambuco, UFPE, Recife,
                         Brazil""",
                         """Title: <a href'#link-to-thesis'>Transverse optical phenomena with
                         Gaussian beams and optical vortices</a> (in English) <br>
                         Advisor: Cid Bartolomeu de Araújo <br>
                         Co-advisor: Edilson Lucena Falcão Filho <br>
                         Scholarship: Conselho Nacional de Desenvolvimento
                         Científico e Tecnológico (CNPq)"""))
academic.append(CV_entry("2010 - 2012",
                         "M.Sc. in physics",
                         """Universidade Federal de Pernambuco, UFPE, Recife,
                         Brazil""", """Title: <a href'#link-to-thesis'>Plasmonic
                         nanostructures for nonlinear optics applications</a>
                         (in Portuguese) <br>
                         Advisor: Cid Bartolomeu de Araújo <br>
                         Co-advisor: Edilson Lucena Falcão Filho <br>
                         Scholarship: Conselho Nacional de Desenvolvimento
                         Científico e Tecnológico (CNPq)"""))
academic.append(CV_entry("2006 - 2010",
                         "B.Sc. in physics",
                         "Universidade de Brasília, UnB, Brasília, Brazil",
                         """Advisor: Sebastião William da Silva <br>
                         Scholarship: Conselho Nacional de Desenvolvimento
                         Científico e Tecnológico (CNPq)"""))

scientific = []
scientific.append(CV_entry("",
                           "Angular momentum of light and optical vortices",
                           "Fundamentals and applications",
                           """
                           A well known property of light is that it can
                           possess linear momentum. Pressure from light
                           radiation can be observed, for example, in optical
                           tweezers, where a light beam manipulates small
                           particles. If this linear momentum rotates around a
                           point, it means that there is a non-zero angular
                           momentum of light around that point."""))
scientific.append(CV_entry("",
                           "Nonlinear optics",
                           "Manipulation of light with light",
                           """
                           It is usually observed that light propagation
                           through materials can be described as a linear
                           phenomenon (i.e., the 'output is proportional to the
                           input'). However this approximation breaks down for
                           a sufficiently strong light source, and a large
                           variety of phenomena can be observed. In the
                           nonlinear optics regime, light interacts with light
                           at the nonlinear material."""))
if 0:
    scientific.append(CV_entry("To be started", "Quantum optics",
                               "Light at its fundamental levels",
                               """
                               Light from ordinary and intense light sources
                               can be described as a superposition of waves.
                               If the light intensity becomes very small, it
                               can be observed that light comes in small energy
                               packets (detected photons are a 'click' in the
                               detector). In this regime, light behaves very
                               differently from the so-called 'classical
                               regime', and many fundamental aspects of nature
                               can be tested."""))
scientific.append(CV_entry("", "Plasmonics",
                           "Light interaction with metal structures",
                           """
                           Metals can be considered as an ideal gas of
                           free-electrons. If one produces a metallic structure
                           such that the electrons can move from one edge to
                           its opposite during half-optical cycle, its
                           interaction with light becomes resonant. This
                           implies an increased accumulation of charges and an
                           enhancement of the optical electric and magnetic
                           fields. The light becomes confined near the metallic
                           structure. Plasmonics can be used for nonlinear
                           optics and also in sensing applications."""))

about = env.get_template('about_template.html')
about_html = about.render(personal_info=personal, academic_background=academic,
                          science=scientific)
with codecs.open("about.html", "w", "utf-8") as fh:
    fh.write(about_html)

###############
# USEFUL.HTML #
###############

useful = env.get_template('useful_template.html')
useful_html = useful.render()
with codecs.open("useful.html", "w", "utf-8") as fh:
    fh.write(useful_html)

############
# 404.HTML #
############

error404 = env.get_template('404_template.html')
error404_html = error404.render()
with codecs.open("404.html", "w", "utf-8") as fh:
    fh.write(error404_html)

###########################
# under_construction.HTML #
###########################

underConstruction = env.get_template('under_construction_template.html')
underConstruction_html = underConstruction.render()
with codecs.open("under_construction.html", "w", "utf-8") as fh:
    fh.write(underConstruction_html)

###############
# PAPERS.HTML #
###############

papers = env.get_template('papers_template.html')
papers_html = papers.render(papers=works)
with codecs.open("science_papers.html", "w", "utf-8") as fh:
    fh.write(papers_html)

##########################
# CONFERENCE_PAPERS.HTML #
##########################

cpapers = env.get_template('conference_papers_template.html')
cpapers_html = cpapers.render(papers=conference_papers)
with codecs.open("conference_papers.html", "w", "utf-8") as fh:
    fh.write(cpapers_html)

############
# TEACHING #
############

class Courses():
    def __init__(self, title='Title', folder='course_name',
                 abstract='Short abstract'):
        self.title = title
        self.base_folder = folder
        self.abstract = abstract
        self.img = r'/thumbnail.jpg'
        self.href = '#broken_link'
        self.tags = ['']

coursePages = []

coursePages.append(Courses('Guia básico do AVA para docentes', 'Guia_basico_AVA',
                           'Guia básico das funcionalidades do AVA-UFPE para docentes, visando principalmente as necessidades dos docentes da área 2.'))

coursePages.append(Courses('2020.1 - Sensoriamento e controle básico', 'sensoriamento_2020_1',
                           'Sensoriamento e controle básico utilizando a plataforma arduino'))
coursePages.append(Courses('2020.1 - Instrumentação Eletrônica', 'instrumentacao_2020',
                           'Instrumentação Eletrônica para a Física, lidando com conceitos de eletrônica analógica e digital'))
coursePages.append(Courses('Sensoriamento e controle remoto', 'sensoriamento_remoto',
                           'Sensoriamento e controle remoto utilizando a plataforma arduino, python e kivy'))
coursePages.append(Courses('Escola de Instrumentação Eronides 2019', 'Eronides_2019',
                           'Atividades realizadas durante a Escola de Instrumentação Eronides 2019'))
coursePages.append(Courses('Sensoriamento e controle - verão 2019', 'sensoriamento_verao_2019',
                           'Curso de sensoriamento e controle utilizando a plataforma arduino'))
coursePages.append(Courses('Instrumentação eletrônica para a física', 'instrumentacao_fisica',
                           'Curso de instrumentação para a física utilizando eletrônica analógica'))
coursePages.append(Courses('Minicurso de arduino', 'minicurso_arduino',
                           'Breve curso de introdução à eletrônica e programação utilizando a plataforma arduino'))
coursePages.append(Courses('Física 1', 'Fisica_1',
                           'Curso de Física Geral 1 ministrado na área 2 - UFPE'))


# Cria as páginas individuais de cada curso
for c in coursePages:
    main_page_body = ''
    base_filename = r'teaching/' + c.base_folder
    c.img = base_filename + c.img
    c.href = base_filename + ".html"
    with codecs.open(base_filename+r'/main.md', "r", "utf-8") as fh:
        main_page_body = md.convert(fh.read())
    main_page_body = main_page_body.replace('<table>','<table class="table">')

    cpage = env.get_template('course_template.html')
    cpage_html = cpage.render(page_body=main_page_body)
    with codecs.open(base_filename+".html", "w", "utf-8") as fh:
        fh.write(cpage_html)

# Cria a página geral da área de ensino
teaching = env.get_template('teaching_template.html')
teaching_html = teaching.render(courses=coursePages)
with codecs.open("teaching.html", "w", "utf-8") as fh:
        fh.write(teaching_html)

########
# BLOG #
########

class post_class():
    def __init__(self):
        self.title = 'default'
        self.author = 'author'
        self.date = '01/01/2001'
        self.last_update = self.date
        self.image = r''
        self.short = 'abstract example'
        self.tags = ['']
        self.status = ''
        self.language = 'En'

        self.href = '#broken_link'

class tags_handler_class():
    def __init__(self):
        self._tags = {}
    def add_tags_from_post(self, post):
        for t in post.tags:
            if t.lower() in self._tags.keys():
                self._tags[t.lower()].append(post)
            else:
                self._tags[t.lower()] = [post]

tags_handler = tags_handler_class()
posts = []

def process_post(config, contents, filename):
    post = post_class()
    for key in config.keys():
        post.__setattr__(key, config[key])

    if filename.endswith('pmd'):
        filename = filename.rstrip('pmd')+'html'
    post.href = filename

    processed_contents = pypandoc.convert(contents,
                                          "html",
                                          format="md",
                                          extra_args=['--mathjax',
                                                      '--highlight-style=tango'])
                                                      #'--self-contained']) Requires a redefinition of the folders... think a bit on how to do this
    ## TODO: Use BeautifulSoup to modify html classes and other tuned properties...
    processed_contents = processed_contents.replace('<table>','<table class="table">')
    processed_contents = processed_contents.replace('<img','<img class="img-responsive"')

    page = env.get_template('blog_template.html')
    page_html = page.render(post=post, page_body=processed_contents)

    with codecs.open(post.href, "w", "utf-8") as fh:
        fh.write(page_html)

    if 'status' in config.keys():
        if config['status'].lower() == 'publish':
            posts.append(post)
            tags_handler.add_tags_from_post(post)


# Search for *.pmd files in the blog folder, and opens them
for file in os.listdir('blog'):
    if file.endswith('.pmd'):
        fullname = os.path.join('blog',file)
        with codecs.open(fullname, "r", "utf-8") as fh:
            contents = fh.read()

            # Get the YAML header at the document beginning
            config = re.search('---\n?(:?.*\n)*?---', contents).group(0)
            contents = contents.replace(config, '').lstrip()
            config = yaml.load(config.strip('---'), Loader=yaml.Loader)

            process_post(config, contents, fullname)


# Reorder posts by post date
posts = sorted(posts, key=lambda w: datetime.datetime.strptime(w.date, r"%d/%m/%Y"), reverse=True)

blog_index       = env.get_template('blog_index_template.html')
blog_index_html  = blog_index.render(posts=posts, tags=tags_handler._tags)

with codecs.open("blog.html", "w", "utf-8") as fh:
    fh.write(blog_index_html)

print('website generation finished!')

#pypandoc.convert(extr)
