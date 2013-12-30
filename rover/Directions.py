class North:
    name = 'north'
    x = 0
    y = 1

    @staticmethod
    def left():
        return West
    
    @staticmethod
    def right():
        return East

class East:
    name = 'east'
    x = 1
    y = 0

    @staticmethod
    def left():
        return North

    @staticmethod
    def right():
        return South

class South:
    name = 'south'
    x = 0
    y = -1

    @staticmethod
    def left():
        return East

    @staticmethod
    def right():
        return West

class West:
    name = 'west'
    x = -1
    y = 0

    @staticmethod
    def left():
        return South

    @staticmethod
    def right():
        return North