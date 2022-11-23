import models

def get_users_in_bytes():
    user1 = models.zhukov.Zhukov()
    userDenis = models.ignatev.Ignatev()
    userIvan = models.ivan.Ivan()
    userIvanova = models.ivanova.Ivanova()
    userSergeeva = models.sergeeva.Sergeeva()
    userShchegolskiy = models.shchegolskiy.Shchegolskiy()
    userEgor = models.sobinin.Sobinin()
    userAndrew = models.logwinow.Logwinow()
    userMatvey = models.zhuravskiy.Zhuravskiy()

    result = bytes('Users:', 'utf-8')
    result += bytes(user1.full_name, 'utf-8')
    result += bytes(userDenis.full_name, 'utf-8')
    result += bytes(userIvan.full_name, 'utf-8')
    result += bytes(userIvanova.full_name, 'utf-8')
    result += bytes(userSergeeva.full_name, 'utf-8')
    result += bytes(userShchegolskiy.full_name, 'utf-8')
    result += bytes(userEgor.full_name, 'utf-8')
    result += bytes(userAndrew.full_name, 'utf-8')
    result += bytes(userMatvey.full_name, 'utf-8')

    return result