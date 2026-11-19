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
