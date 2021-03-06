import pandas as pd


text_value_dict = {'Coarse':['Conglomerates: 21±3',
                             'Breccias: 19±5',
                             'N.a.',
                             'Crystalline Limestone: 12±3',
                             'N.a.',
                             'N.a.',
                             'Marble: 9±3',
                             'N.a.',
                             'Migmatite: 29±3',
                             'Gneiss: 28±5',
                             'Granite: 32±3',
                             'Granodiorite: 29±3',
                             'Gabbro: 27±3',
                             'Norite: 20±5',
                             'Porphyrites: 20±5',
                             'N.a.',
                             'N.a.',
                             'Agglomerate: 19±5 '],
                 'Medium':['Sandstones: 17±4',
                             'N.a.',
                             'N.a.',
                             'Sparitic limestones: 10±2',
                             'Gypsum: 8±2',
                             'N.a.',
                             'Hornfels: 19±4',
                             'Metasandstones: 19±3',
                             'Amphibolites: 26±6',
                             'Schists: 12±3',
                             'Diorite: 25±5',
                             'N.a.',
                             'Dolerite: 16±5',
                             'N.a.',
                             'N.a.',
                             'Rhyolite: 25±5',
                             'Andesite: 25±5',
                             'Breccia: 19±5'],
                    'Fine':['Siltstones: 7±2',
                                'Graywakes: 18±3',
                                'N.a.',
                                'Micritic Limestones: 9±2',
                                'Anhydrite: 12±2',
                                'N.a.',
                                'Quarzites: 20±3',
                                'N.a.',
                                'N.a.',
                                'Phyllites: 7±3',
                                'N.a.',
                                'N.a.',
                                'N.a.',
                                'N.a.',
                                'Diabase: 15±5',
                                'Dacite: 25±3',
                                'Basalt: 25±5',
                                'Tuff: 13±5'],
                    'Very fine':['Claystones: 4±2',
                                'Shales: 6±2',
                                'Marls: 7±2',
                                'Dolomites: 9±3',
                                'N.a.',
                                'Chalk: 7±2',
                                'N.a.',
                                'N.a.',
                                'N.a.',
                                'Slates: 7±4',
                                'N.a.',
                                'N.a.',
                                'N.a.',
                                'N.a.',
                                'Peridotite: 25±5',
                                'Obsidian: 19±3',
                                'N.a.',
                                'N.a.']}
index = ['Sedimentary','Sedimentary','Sedimentary','Sedimentary','Sedimentary','Sedimentary','Metamorphic','Metamorphic','Metamorphic','Metamorphic','Igneous','Igneous','Igneous','Igneous','Igneous','Igneous','Igneous','Igneous']
value_dict = {'Coarse':['Conglomerates: 21±3','Breccias: 19±5','Crystalline Limestone: 12±3','N.a.','N.a.','Marble: 9±3','N.a.','Migmatite: 29±3','Gneiss: 28±5','Granite: 32±3','Granodiorite: 29±3','Gabbro: 27±3','Norite: 20±5','Porphyrites: 20±5','N.a.','Agglomerate: 19±5 ']}

text_values_df = pd.DataFrame(text_value_dict,index=index)

print(text_values_df.loc['Sedimentary','Coarse'])
