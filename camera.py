import pygame
class Camera:
    def __init__(self, cam_width, cam_height,display_w,display_h):

        self.display_w =display_w
        self.display_h = display_h
        self.width = cam_width
        self.height = cam_height
        self.camera = pygame.Rect(0, 0, self.width, self.height)

    def apply(self,entity):
        """returns new rectangle that is shifted by this amount"""
        return entity.rect.move(self.camera.topleft)

    def update(self,target):
        """camera follows a sprite"""
        print (self.width)
        print (self.height)
        # x = -target.rect.x + int(self.display_w/2)
        # y = -target.rect.y + int(self.display_h/2)
        x = -target.rect.x + int(self.display_w / 2)
        y = -target.rect.y + int(self.display_h / 2)
        self.camera = pygame.Rect(x,y,self.width,self.height)

        # x =min(0,x)
        # y=min(0,y)
        # x = max(-(self.width - self.display_w),x)
        # y = max(-(self.height-self.display_h),y)
        # self.camera=pygame.Rect(x,y,self.width,self.height)