import pygame

import SecondLevel


class Dungeons:
    def __init__(self, hero_x, hero_y, enemy_x, enemy_y, enemy_x2, enemy_y2, enemy_x3, enemy_y3,
                 boss_x, boss_y, portal_x, portal_y):

        # координаты героя
        self.hero_x = hero_x
        self.hero_y = hero_y
        # направление героя
        self.hero_direction = "right"
        # хп героя
        self.hero_hp = 100
        # урон оружия героя
        self.hero_damage = 200
        # кд оружия героя
        self.hero_attack_cooldown = 0
        # опыт героя
        self.hero_xp = 0
        self.hero_attack = False

        # координаты первого моба
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        # хп моба
        self.enemy_hp = 60
        # опыт с моба
        self.enemy_xp = 15
        self.enemy_direction = "left"

        self.enemy_x2 = enemy_x2
        self.enemy_y2 = enemy_y2
        self.enemy_hp2 = 80
        self.enemy_xp2 = 20
        self.enemy_direction2 = "left"

        self.enemy_x3 = enemy_x3
        self.enemy_y3 = enemy_y3
        self.enemy_hp3 = 100
        self.enemy_xp3 = 25
        self.enemy_direction3 = "left"

        # координаты босса
        self.boss_x = boss_x
        self.boss_y = boss_y
        # хп босса
        self.boss_hp = 400
        # опыт с босса
        self.boss_xp = 100
        self.boss_direction = "left"

        # координаты портала
        self.portal_x = portal_x
        self.portal_y = portal_y

        # скорость прыжка
        self.speed_jump = 5
        # флаг прыжка
        self.is_jump = False
        # счётчик прыжка
        self.jump_count = 10

        # загрузка картинок и указание их размеров
        self.first_location_img = pygame.transform.scale(pygame.image.load("../images/background/background_11.png"),
                                                         (1280, 720))
        self.second_location_img = pygame.transform.scale(pygame.image.load("../images/background/background_12.png"),
                                                          (1280, 720))
        self.third_location_img = pygame.transform.scale(pygame.image.load("../images/background/background_13.png"),
                                                         (1280, 720))

        self.enemy_img = pygame.transform.scale(pygame.image.load("../images/enemy/enemy_first.png"), (280, 280))
        # "прямоугольник" противника
        self.enemy_rect1 = self.enemy_img.get_rect()

        self.enemy_img2 = pygame.transform.scale(pygame.image.load("../images/enemy/enemy_second.png"), (130, 280))
        self.enemy_rect2 = self.enemy_img2.get_rect()

        self.enemy_img3 = pygame.transform.scale(pygame.image.load("../images/enemy/enemy_third.png"), (230, 230))
        self.enemy_rect3 = self.enemy_img3.get_rect()

        self.boss_img = pygame.transform.scale(pygame.image.load("../images/Boss/boss_first.png"), (200, 400))
        self.boss_rect = self.boss_img.get_rect()

        self.portal_img = pygame.image.load("../images/Portal/portal.png")

        self.hero_animation_right_1 = pygame.image.load("../images/Hero/hero_animation_right_1.png")
        self.hero_animation_right_2 = pygame.image.load("../images/Hero/hero_animation_right_2.png")
        self.hero_animation_right_3 = pygame.image.load("../images/Hero/hero_animation_right_3.png")

        self.hero_animation_left_1 = pygame.image.load("../images/Hero/hero_animation_left_1.png")
        self.hero_animation_left_2 = pygame.image.load("../images/Hero/hero_animation_left_2.png")
        self.hero_animation_left_3 = pygame.image.load("../images/Hero/hero_animation_left_3.png")

        self.hero_attack_right_1 = pygame.image.load("../images/Hero/hero_atack_right_1.png")
        self.hero_attack_right_2 = pygame.image.load("../images/Hero/hero_atack_right_2.png")
        self.hero_attack_right_3 = pygame.image.load("../images/Hero/hero_atack_right_2.png")
        self.hero_attack_right_4 = pygame.image.load("../images/Hero/hero_atack_right_3.png")
        self.hero_attack_right_5 = pygame.image.load("../images/Hero/hero_atack_right_3.png")

        self.hero_attack_left_1 = pygame.image.load("../images/Hero/hero_atack_left_1.png")
        self.hero_attack_left_2 = pygame.image.load("../images/Hero/hero_atack_left_2.png")
        self.hero_attack_left_3 = pygame.image.load("../images/Hero/hero_atack_left_2.png")
        self.hero_attack_left_4 = pygame.image.load("../images/Hero/hero_atack_left_3.png")
        self.hero_attack_left_5 = pygame.image.load("../images/Hero/hero_atack_left_3.png")

        # список с кадрами для анимации героя направо
        self.walk_right = [self.hero_animation_right_1, self.hero_animation_right_2, self.hero_animation_right_3]
        self.walk_left = [self.hero_animation_left_1, self.hero_animation_left_2, self.hero_animation_left_3]

        self.fight_right = [self.hero_attack_right_1, self.hero_attack_right_2, self.hero_attack_right_3,
                            self.hero_attack_right_4, self.hero_attack_right_5]
        self.fight_left = [self.hero_attack_left_1, self.hero_attack_left_2, self.hero_attack_left_3,
                           self.hero_attack_left_4, self.hero_attack_left_5]

        # счётчик для переключения кадров
        self.count_hero_animation_right = 0
        self.count_hero_animation_left = 0

        self.count_hero_attack_right = 0
        self.count_hero_attack_left = 0

        # фон
        self.background = self.first_location_img

        # список локаций
        self.all_locations_list = [[self.first_location_img, self.second_location_img, self.third_location_img]]
        self.first_level_locations_list = self.all_locations_list[0]
        # счётчик локаций
        self.location = 0

    # атака по мобам
    def enemy_attack(self):

        # если герой рядом с первым мобом и оружие перезарядилось
        if (abs(self.hero_x - self.enemy_x) <= 100 and abs(self.hero_y - self.enemy_y) <= 100
                and self.hero_attack_cooldown <= 0):

            # урон от оружия первому мобу
            self.enemy_hp -= self.hero_damage

            # перезарядка оружия (обновление кд)
            self.hero_attack_cooldown = 0.3

            # если первый моб мёртв
            if self.enemy_hp <= 0:

                # убираем его картинку
                self.enemy_img = None

                # зачисляем опыт игроку за убийство моба
                self.hero_xp += self.enemy_xp

                # обнуление опыта за моба (картинки нет, но как область на экране присутствует,
                # поэтому если не будет обнуления, можно фармить опыт)
                self.enemy_xp = 0

        if (abs(self.hero_x - self.enemy_x2) <= 100 and abs(self.hero_y - self.enemy_y2) <= 100
                and self.hero_attack_cooldown <= 0):

            self.enemy_hp2 -= self.hero_damage
            self.hero_attack_cooldown = 0.3

            if self.enemy_hp2 <= 0:
                self.enemy_img2 = None
                self.hero_xp += self.enemy_xp2
                self.enemy_xp2 = 0

        if (abs(self.hero_x - self.enemy_x3) <= 100 and abs(self.hero_y - self.enemy_y3) <= 100
                and self.hero_attack_cooldown <= 0):

            self.enemy_hp3 -= self.hero_damage
            self.hero_attack_cooldown = 0.3

            if self.enemy_hp3 <= 0:
                self.enemy_img3 = None
                self.hero_xp += self.enemy_xp3
                self.enemy_xp3 = 0

    # атака по боссу
    def boss_attack(self):
        if (abs(self.hero_x - self.boss_x) <= 100 and abs(self.hero_y - self.boss_y) <= 100
                and self.hero_attack_cooldown <= 0):
            self.boss_hp -= self.hero_damage
            self.hero_attack_cooldown = 0.3

            if self.boss_hp <= 0:
                self.boss_img = None
                self.hero_xp += self.boss_xp
                self.boss_xp = 0

    # передвижение героя
    def movement_hero(self):
        keys = pygame.key.get_pressed()

        # если кнопка A зажата
        if keys[pygame.K_a]:

            # героя перемещают на 10 px налево (скорость 10)
            self.hero_x -= 10

            # изменение направления героя
            self.hero_direction = "left"

            # увеличиваем номер картинки из анимации
            self.count_hero_animation_left += 1
            # после последней анимации идет первая
            if self.count_hero_animation_left >= len(self.walk_left):
                self.count_hero_animation_left = 0

        # если не зажата кнопка A
        elif not keys[pygame.K_a]:
            # счётчик приравниваем 0, чтобы отобразить далее первую анимацию, когда герой неподвижен
            self.count_hero_animation_left = 0

        # если кнопка D зажата
        if keys[pygame.K_d]:

            self.hero_x += 10
            self.hero_direction = "right"

            self.count_hero_animation_right += 1
            if self.count_hero_animation_right >= len(self.walk_right):
                self.count_hero_animation_right = 0

        # если не зажата кнопка D
        elif not keys[pygame.K_d]:
            self.count_hero_animation_right = 0

        # если флаг прыжка False
        if not self.is_jump:

            # если зажат пробел
            if keys[pygame.K_SPACE]:

                # изменение флага прыжка
                self.is_jump = True

        else:
            # проверка на то, что герой на полу
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.hero_y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10

    # кд оружия героя
    def attack_cooldown(self):
        if self.hero_attack_cooldown > 0:
            self.hero_attack_cooldown -= 0.01

    def enemy_movement(self):
        if self.enemy_direction == "right":
            self.enemy_x += 1
            if self.enemy_x >= 1100:
                self.enemy_direction = "left"
        else:
            self.enemy_x -= 1
            if self.enemy_x <= 700:
                self.enemy_direction = "right"

        if self.enemy_direction2 == "right":
            self.enemy_x2 += 1
            if self.enemy_x2 >= 1100:
                self.enemy_direction2 = "left"
        else:
            self.enemy_x2 -= 1
            if self.enemy_x2 <= 700:
                self.enemy_direction2 = "right"

        if self.enemy_direction3 == "right":
            self.enemy_x3 += 1
            if self.enemy_x3 >= 1100:
                self.enemy_direction3 = "left"
        else:
            self.enemy_x3 -= 1
            if self.enemy_x3 <= 700:
                self.enemy_direction3 = "right"

    def boss_movement(self):
        if self.boss_direction == "right":
            self.boss_x += 5
            if self.boss_x >= 1100:
                self.boss_direction = "left"
        else:
            self.boss_x -= 5
            if self.boss_x <= 700:
                self.boss_direction = "right"


# главная функция, которая выполняется при запуске программы
def main():
    pygame.init()

    # размеры окна приложения
    size = 1280, 720

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    timer_value = 0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Hero & Enemy")

    # указание координат для класса
    dungeons = Dungeons(100, 315, 1000, 350,
                        800, 310, 900, 80, 900, 185,
                        1100, 350)

    # Load the music file
    music_file = "../music/Doom.mp3"
    pygame.mixer.music.load(music_file)

    # Set the music to loop indefinitely
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play(-1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # если кнопка мыши нажата и герой находится на локации до боссов
            if event.type == pygame.MOUSEBUTTONDOWN and dungeons.location != 2:

                # если нажата ЛКМ
                if pygame.mouse.get_pressed()[0]:
                    dungeons.enemy_attack()

                    if dungeons.hero_direction == "right":
                        dungeons.count_hero_attack_right += 1
                        if dungeons.count_hero_attack_right >= len(dungeons.fight_right):
                            dungeons.count_hero_attack_right = 0
                        dungeons.hero_attack = True

                    elif dungeons.hero_direction == "left":
                        dungeons.count_hero_attack_left += 1
                        if dungeons.count_hero_attack_left >= len(dungeons.fight_left):
                            dungeons.count_hero_attack_left = 0
                        dungeons.hero_attack = True

            # если кнопка мыши нажата и герой находится на локации с боссами
            if event.type == pygame.MOUSEBUTTONDOWN and dungeons.location == 2:

                # если нажата ЛКМ
                if pygame.mouse.get_pressed()[0]:
                    dungeons.boss_attack()

                    if dungeons.hero_direction == "right":
                        dungeons.count_hero_attack_right += 1
                        if dungeons.count_hero_attack_right >= len(dungeons.fight_right):
                            dungeons.count_hero_attack_right = 0
                        dungeons.hero_attack = True

                    elif dungeons.hero_direction == "left":
                        dungeons.count_hero_attack_left += 1
                        if dungeons.count_hero_attack_left >= len(dungeons.fight_left):
                            dungeons.count_hero_attack_left = 0
                        dungeons.hero_attack = True

            if event.type == pygame.USEREVENT:
                # Restart the music when it ends
                pygame.mixer.music.play(-1)

        dungeons.movement_hero()
        dungeons.attack_cooldown()
        dungeons.enemy_movement()
        dungeons.boss_movement()

        screen.fill((0, 0, 0))

        # фон
        screen.blit(dungeons.background, (0, 0))

        timer_value += clock.get_time() / 1000
        timer_text = font.render(f"Время: {timer_value:.2f} сек.", True, (196, 0, 0))
        screen.blit(timer_text, (10, 10))

        xp_text = font.render(f"Опыт: {dungeons.hero_xp} xp", True, (0, 233, 0))
        screen.blit(xp_text, (10, 50))

        # Отображение хп противника
        enemy_hp_rect = pygame.Rect(dungeons.enemy_x + 100, dungeons.enemy_y + 10, dungeons.enemy_hp, 10)
        pygame.draw.rect(screen, (255, 0, 0), enemy_hp_rect)

        enemy_hp_rect2 = pygame.Rect(dungeons.enemy_x2 + 30, dungeons.enemy_y2 - 20, dungeons.enemy_hp2, 10)
        pygame.draw.rect(screen, (255, 0, 0), enemy_hp_rect2)

        enemy_hp_rect3 = pygame.Rect(dungeons.enemy_x3 + 70, dungeons.enemy_y3, dungeons.enemy_hp3, 10)
        pygame.draw.rect(screen, (255, 0, 0), enemy_hp_rect3)

        # Отображение хп героя
        hero_hp_rect = pygame.Rect(dungeons.hero_x + 75, dungeons.hero_y + 10, dungeons.hero_hp, 10)
        pygame.draw.rect(screen, (0, 255, 0), hero_hp_rect)

        # если герой повёрнут направо
        if dungeons.hero_direction == "right":
            if dungeons.hero_attack:
                screen.blit(dungeons.fight_right[dungeons.count_hero_attack_right],
                            (dungeons.hero_x, dungeons.hero_y))
                dungeons.hero_attack = False
            else:
                screen.blit(dungeons.walk_right[dungeons.count_hero_animation_right],
                            (dungeons.hero_x, dungeons.hero_y))

        # если герой повёрнут налево
        elif dungeons.hero_direction == "left":
            if dungeons.hero_attack:
                screen.blit(dungeons.fight_left[dungeons.count_hero_attack_left],
                            (dungeons.hero_x, dungeons.hero_y))
                dungeons.hero_attack = False
            else:
                screen.blit(dungeons.walk_left[dungeons.count_hero_animation_left],
                            (dungeons.hero_x, dungeons.hero_y))

        # если хотя бы один из мобов жив
        if dungeons.enemy_img or dungeons.enemy_img2 or dungeons.enemy_img3:

            # если жив первый моб
            if dungeons.enemy_img:
                # отображаем этого моба
                screen.blit(dungeons.enemy_img, (dungeons.enemy_x, dungeons.enemy_y))

            if dungeons.enemy_img2:
                screen.blit(dungeons.enemy_img2, (dungeons.enemy_x2, dungeons.enemy_y2))

            if dungeons.enemy_img3:
                screen.blit(dungeons.enemy_img3, (dungeons.enemy_x3, dungeons.enemy_y3))

        # если все мобы мертвы
        else:
            # герой на локации с боссами
            if dungeons.location == 2:

                # Отображение хп босса
                boss_hp_rect = pygame.Rect(dungeons.boss_x - 100, dungeons.boss_y - 30, dungeons.boss_hp, 10)
                pygame.draw.rect(screen, (255, 0, 255), boss_hp_rect)

                # если герой за левой границей карты
                if dungeons.hero_x < -230:

                    # отображение предыдущей локации
                    dungeons.location -= 1
                    dungeons.background = dungeons.first_level_locations_list[dungeons.location]

                    # отображение героя на правой границе локации
                    dungeons.hero_x = size[0] - 200

                # если босс жив
                if dungeons.boss_img:
                    screen.blit(dungeons.boss_img, (dungeons.boss_x, dungeons.boss_y))

                else:
                    screen.blit(dungeons.portal_img, (dungeons.portal_x, dungeons.portal_y))

                    if dungeons.hero_x < -230:
                        dungeons.location -= 1
                        dungeons.background = dungeons.first_level_locations_list[dungeons.location]
                        dungeons.hero_x = size[0] - 200

                    # если герой в портале
                    elif (dungeons.hero_x < dungeons.portal_x + 100 and dungeons.hero_x + 100 > dungeons.portal_x
                            and dungeons.hero_y < dungeons.portal_y + 100
                            and dungeons.hero_y + 100 > dungeons.portal_y):
                        SecondLevel.main()

            else:
                # если герой в начале локации
                if dungeons.location == 0:
                    dungeons.background = dungeons.first_level_locations_list[dungeons.location]

                    # если герой прошёл правую границу
                    if dungeons.hero_x >= size[0] - 80:

                        # локация меняется на следующую
                        dungeons.location += 1
                        dungeons.background = dungeons.first_level_locations_list[dungeons.location]

                        # отображение героя в начале локации
                        dungeons.hero_x = -100

                else:
                    dungeons.background = dungeons.first_level_locations_list[dungeons.location]

                    # если герой прошёл правую границу
                    if dungeons.hero_x >= size[0] - 80:

                        # локация меняется на следующую
                        dungeons.location += 1
                        dungeons.background = dungeons.first_level_locations_list[dungeons.location]

                        # отображение героя в начале локации
                        dungeons.hero_x = -100

                    # если герой прошел левую границу
                    elif dungeons.hero_x < -230:

                        # локация меняется на предыдущую
                        dungeons.location -= 1
                        dungeons.background = dungeons.first_level_locations_list[dungeons.location]

                        # отображение героя в конце локации
                        dungeons.hero_x = size[0] - 200

        pygame.display.update()

        # фпс
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
