fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
must = ['jen', 'vlad']
for m in must:
    if m in fav_lang.keys():
        print("{}, thanks for your voice".format(m.title()))
    else:
        print("Hey " + m.title() + ' you must voted!')