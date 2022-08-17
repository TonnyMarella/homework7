import os

image = ('JPEG', 'PNG', 'JPG', 'SVG')
video = ('AVI', 'MP4', 'MOV', 'MKV')
document = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
music = ('MP3', 'OGG', 'WAV', 'AMR')
archives = ('ZIP', 'GZ', 'TAR')

test = {
        ('JPEG', 'PNG', 'JPG', 'SVG'): 'images',
        video: 'video',
        document: 'documents',
        music: 'music',
    }

s = 'JPG'

for i, k in test.items():
    if s in i:
        print(k)