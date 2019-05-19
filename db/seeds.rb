# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)


Home.destroy_all
Image.destroy_all

h1=Home.create(cate: 'defense')
h2=Home.create(cate: 'eiffel')
h3=Home.create(cate: 'general')
h4=Home.create(cate: 'invalides')
h5=Home.create(cate: 'louvre')
h6=Home.create(cate: 'moulinrouge')

h1.images << Image.create(name: 'paris_defense_000000.jpg')
h1.images << Image.create(name: 'paris_defense_000002.jpg')
h1.images << Image.create(name: 'paris_defense_000043.jpg')
h1.images << Image.create(name: 'paris_defense_000013.jpg')
h1.images << Image.create(name: 'paris_defense_000030.jpg')


h2.images << Image.create(name: 'paris_eiffel_000000.jpg')
h2.images << Image.create(name: 'paris_eiffel_000086.jpg')
h2.images << Image.create(name: 'paris_eiffel_000028.jpg')
h2.images << Image.create(name: 'paris_eiffel_000022.jpg')
h2.images << Image.create(name: 'paris_eiffel_000051.jpg')

h3.images << Image.create(name: 'paris_general_000001.jpg')
h3.images << Image.create(name: 'paris_general_000009.jpg')
h3.images << Image.create(name: 'paris_general_000010.jpg')
h3.images << Image.create(name: 'paris_general_000021.jpg')
h3.images << Image.create(name: 'paris_general_000023.jpg')

h4.images << Image.create(name: 'paris_invalides_000002.jpg')
h4.images << Image.create(name: 'paris_invalides_000003.jpg')
h4.images << Image.create(name: 'paris_invalides_000004.jpg')
h4.images << Image.create(name: 'paris_invalides_000006.jpg')
h4.images << Image.create(name: 'paris_invalides_000007.jpg')

h5.images << Image.create(name: 'paris_louvre_000000.jpg')
h5.images << Image.create(name: 'paris_louvre_000002.jpg')
h5.images << Image.create(name: 'paris_louvre_000004.jpg')
h5.images << Image.create(name: 'paris_louvre_000008.jpg')
h5.images << Image.create(name: 'paris_louvre_000013.jpg')

h6.images << Image.create(name: 'paris_moulinrouge_000003.jpg')
h6.images << Image.create(name: 'paris_moulinrouge_000004.jpg')
h6.images << Image.create(name: 'paris_moulinrouge_000006.jpg')
h6.images << Image.create(name: 'paris_moulinrouge_000009.jpg')
h6.images << Image.create(name: 'paris_moulinrouge_000010.jpg')
