from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('jinja-templates'))

# Add tags!


class Works():
    def __init__(self):
        self.title = 'Title'
        self.img = 'http://placehold.it/100x100'
        self.abstract = 'Short abstract'
        self.href = '#work_link'

##############
# INDEX.HTML #
##############

index = env.get_template('index_template.html')
featured_works = [Works() for i in range(3)]
index_html = index.render(featured=featured_works)
with open("index.html", "w") as fh:
    fh.write(index_html)

##############
# ABOUT.HTML #
##############


class CV_personal_info:
    def __init__(self, name='My name', sub_text='some description',
                 address='My address', phone='(555) 5555-5555',
                 email='my_mail@server.com', facebook='',
                 linkedin='', twitter='', googlescholar='', researchgate=''):
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


class CV_entry():
    def __init__(self, period, title, entity, description):
        self.period = period
        self.title = title
        self.entity = entity
        self.description = description

personal = CV_personal_info('Anderson Monteiro Amaral',
                            """For a short CV,
                            <a href="http://lattes.cnpq.br">click here</a>.<br>
                            For a full CV, <a href="http://lattes.cnpq.br/1832322110328811">
                            click here</a>.""",
                            """R. Prof. Moraes Rego, 1235 <br>50670-901, Cidade
                            universitária <br>Recife - PE - Brazil""",
                            '+55 (81) 2126-2258; +55 (81) 2126-2204',
                            'anderson.amaral@outlook.com',
                            'http://www.facebook.com/andersonmonteiroamaral',
                            '#linkedin',
                            'http://twitter.com/amaral_am',
                            '#google-plus')

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
scientific.append(CV_entry("2012 - Today",
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
scientific.append(CV_entry("2010 - Today",
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
scientific.append(CV_entry("2010 - 2012", "Plasmonics",
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
with open("about.html", "w") as fh:
    fh.write(about_html)

###############
# USEFUL.HTML #
###############

useful = env.get_template('useful_template.html')
useful_html = useful.render()
with open("useful.html", "w") as fh:
    fh.write(useful_html)
