class Object():
    def __init__(self, image, pos_x, pos_y):
        self.image = image
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))


class ObjectList():
    def __init__(self):
        self.list = []

    def add(self, object):
        self.list.append(object)

    def update_ob(self, speed):  # for obstacles
        for obstacle in self.list:
            obstacle.update(speed)
        for i in reversed(range(len(self.list))):
            if self.list[i].pos_x < - self.list[i].image.get_width():
                del self.list[i]

    def update_cl(self):  # for cloud
        for cloud in self.list:
            cloud.update()
        for i in reversed(range(len(self.list))):
            if self.list[i].pos_x < - self.list[i].image.get_width():
                del self.list[i]

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        for object in self.list:
            yield object

    def draw(self, screen):
        for object in self.list:
            object.draw(screen)
