class MediaFile:
    def __init__(self, name, size, created_date, owner):
        self.name = name
        self.size = size
        self.created_date = created_date
        self.owner = owner

    def save(self):  #сохранение файла
        pass

    def delete(self):  #удаление файла
        pass

    def __str__(self):
        return f"Файл:{self.name}, Размер: {self.size}MB, Дата создания: {self.created_date}, Владелец: {self.owner}"

class Audio(MediaFile):
        def __init__(self, name, size, created_date, owner, bitrate):
            super().__init__(name, size, created_date, owner)
            self.bitrate = bitrate
        def play(self):
             print(f"Играет:{self.name}")  #воспроизведение аудио

class Video(MediaFile):
            def __init__(self, name, size, created_date, owner, resolution):
                super().__init__(name, size, created_date, owner)
                self.resolution = resolution
            def change_resolution(self, new_resolition):  #изменение разрешения видео
                 pass
    

class Image(MediaFile):
            def __init__(self, name, size, created_date, owner, pixels):
                super().__init__(name, size, created_date, owner)
                self.pixels = pixels
            def filter( self, filter_name):
                 print (f"К фото {self.name} применен фильтр {filter_name}")  #наложение фильтра на фото

                
                
                #ПРИМЕР
#Создаем аудифайл с именем, размером, датой, владельцом и битрейтом.
song = Audio("song.mp3", 5.2, "2000-01-25", "Kate", 320)

#вызываем методы
song.save()  #метод из базового класса, просто сохранит, ничего не выведет)

song.play()  #метод из класса audio, выведет "Играет: song.mp3"

print(song)  #вызовется магический метод __str__ красиво покажет  данные

#3 
# Класс для работы с облаком 
class CloudStorage:
    def __init__(self, file):
        self.file = file

    def upload(self):
        # Логика загрузки файла в облако
        print(f"Файл {self.file.name} успешно загружен в облако!")

    def download(self):
        # Логика скачивания
        pass

#Ответ на 4 вопрос
#Благодаря способу копирования методов из базового класса, при добавлении новых файлов и классов, много кода  писать не придется.