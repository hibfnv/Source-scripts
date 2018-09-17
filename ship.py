import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen   # 初始化飞船并设置其初始位置
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')   # 加载图片
        self.rect = self.image.get_rect()   # 获取当前图片坐标位置
        self.screen_rect = screen.get_rect()  # 屏幕当前图片外接矩形坐标位置
        self.rect.centerx = self.screen_rect.centerx   # 获取当前x轴中心点位置，将每艘飞船放置于底部中央
        self.rect.bottom = self.screen_rect.bottom    # 获取当前底部坐标位置，即y轴坐标位置
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)   # 在指定位置绘制飞船
