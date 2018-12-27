import pygame


class Score(object):
    def __init__(self):
        self.scores = 0

    def score(screen):
        # 定义颜色
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 128)

        # 通过字体文件获得字体对象
        fontObj = pygame.font.Font('./image/flappy_bird.ttf', 50)

        # 配置要显示的文字
        textSurfaceObj = fontObj.render('scores:', True, BLUE, GREEN)

        # 获得要显示的对象的rect
        textRectObj = textSurfaceObj.get_rect()

        # 设置显示对象的坐标
        textRectObj.center = (250, 200)

        # 设置背景
        # screen.fill(WHITE)
        #
        # # 绘制字体
        # screen.blit(textSurfaceObj, textRectObj)


if __name__ == 'main':
    pass