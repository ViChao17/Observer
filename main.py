from Observable import Observer, Observable


class MySubject(Observable):
    pass


class Observer1(Observer):
    def update(self, obs: Observable, arg):
        print(f'Observer1({self.__class__.__bases__[0].__name__})')


class Observer2(Observer):
    def update(self, obs: Observable, arg):
        print(f'Observer2({self.__class__.__bases__[0].__name__})')


class Observer3(Observer):
    def update(self, obs: Observable, arg):
        print(f'Observer3({self.__class__.__bases__[0].__name__})')


def main():
    o1 = Observer1()
    o2 = Observer2()
    o3 = Observer3()

    sub = MySubject()

    sub.register(o1)
    sub.register(o2)
    sub.register(o3)

    sub.set_changed()
    sub.notify()

    print('ok')


if __name__=='__main__':
    main()
