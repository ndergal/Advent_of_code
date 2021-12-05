class Position:
    def __init__(self, horizontal: int, depth: int) -> None:
        self.__horizontal = horizontal
        self.__depth = depth

    @property
    def horizontal(self) -> int:
        return self.__horizontal

    @horizontal.setter
    def horizontal(self, horizontal) -> None:
        self.__horizontal = horizontal

    @property
    def depth(self) -> int:
        return self.__depth

    @depth.setter
    def depth(self, depth) -> None:
        self.__depth = depth

class Submarine:

    def forward(self,x) -> None:
        raise NotImplementedError
    
    def down(self,x) -> None:
        raise NotImplementedError

    def up(self,x) -> None:
        raise NotImplementedError

    @property
    def position(self) -> Position:
        raise NotImplementedError
    

class BasicSubmarine(Submarine):

    def __init__(self) -> None:
        self.__position = Position(0,0)

    def forward(self,x) -> None:
        self.__position.horizontal += x
    
    def down(self,x) -> None:
        self.__position.depth += x

    def up(self,x) -> None:
        self.__position.depth -= x

    @property
    def position(self) -> Position:
        return Position(self.__position.horizontal,self.__position.depth)

class AimingSubmarine(Submarine):
    
    def __init__(self):
        self.__position = Position(0,0)
        self.__aim = 0

    def forward(self,x) -> None:
        self.__position.horizontal  += x
        self.__position.depth += (self.__aim * x)
    
    def down(self,x) -> None:
        self.__aim += x

    def up(self,x) -> None:
        self.__aim -= x

    @property
    def position(self) -> Position:
        return Position(self.__position.horizontal,self.__position.depth)
    

class SubmarineCommandProcessor:
    __submarine: Submarine

    def __init__(self, submarine: Submarine) -> None:
        self.__submarine = submarine

    def process(self, command: str, value: int) -> bool:
        match command:
            case "forward":
                self.__submarine.forward(value)
                return True
            case "down":
                self.__submarine.down(value)
                return True
            case "up":
                self.__submarine.up(value)
                return True
            case _: 
                return False

