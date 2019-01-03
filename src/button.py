import pygame.font
import pygame


class Button():
    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        pygame.init()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #设置按钮的尺寸和其它属性
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 50)
        self.text_color = (255, 255,255)
        #print(pygame.font.get_fonts())
        self.font = pygame.font.SysFont("arial", 48)
        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center  =self.screen_rect.center

        #按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染成图像， 并将其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)