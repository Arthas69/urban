from time import sleep


class User(object):
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname


class UrTube(object):
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, username, password):
        for user in self.users:
            if user.nickname == username and user.password == hash(password):
                self.current_user = user
                print(f"Вы вошли как {username}")
                return
        print("Неверный логин или пароль")

    def register(self, username, password, age):
        for user in self.users:
            if user.nickname == username:
                print(f"Пользователь {username} уже существует")
                return
        user = User(username, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, prompt=None):
        if not prompt:
            return self.videos
        found = []
        for video in self.videos:
            if prompt in video:
                found.append(video)
        return found
    
    def watch_video(self, video_name):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video == video_name:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for i in range(1, video.duration + 1):
                    print(i, end=' ')
                    sleep(1)
                print("Конец видео")


class Video(object):
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __contains__(self, other):
        return other.lower() in self.title.lower()

    def __eq__(self, other):
        return self.title == other


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
