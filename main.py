import pygame
import time
import threading
import bird  #
import pillar  #
import start_and_end  #
import score


def move_background(screen, background1, background2, b):
    screen.blit(background1, (b, 0))
    screen.blit(background2, (b + 800, 0))


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 526))
    background1 = pygame.image.load("./image/background.png")
    background2 = pygame.image.load("./image/background.png")
    ground1 = pygame.image.load("./image/ground.png")
    ground2 = pygame.image.load("./image/ground.png")
    title_obj = start_and_end.Title(screen)
    bird_obj = bird.Bird(screen)  # 创建鸟对象
    pillar_obj = pillar.Create(screen)  # 创建柱子对象
    pillar_obj.cre()  # 创建柱子对象
    tap_obj = start_and_end.Tap(screen)  # 创建tap提示对象
    start_button_obj = start_and_end.Startbutton(screen)
    b = 0  # 移动背景用的数字
    # 窗口名字
    pygame.display.set_caption('flappy bird')
    score_num = score.Score()
    score_num.score()
    while True:
        # 小鸟跳
        bird_obj.jump()
        # 移动背景
        b -= bird.Bird.b
        move_background(screen, background1, background2, b)
        if b < -800:
            b = 0
        # 小鸟死
        bird_obj.check_die(bird_obj)
        # 显示标题
        title_obj.display()
        # 显示柱子
        pillar_obj.display()
        # 显示地面
        move_background(screen, ground1, ground2, b)
        # 显示小鸟
        bird_obj.display()
        # 开始按钮
        try:
            start_button_obj.display()
            if bird_obj.start_flag:
                del start_button_obj
        except UnboundLocalError:
            pass
        # 显示tap提示
        try:
            if bird_obj.down_speed:
                del tap_obj
            elif bird_obj.start_flag:
                tap_obj.display()
        except UnboundLocalError:
            pass
        # 刷新
        pygame.display.update()
        # 帧数
        clock = pygame.time.Clock()
        clock.tick(200)


if __name__ == '__main__':
    main()

"""
注释:
python版本为python3.6
需要安装pygame模块
此为初级版本,留以学习
"""