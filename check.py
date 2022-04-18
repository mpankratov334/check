from r2point import R2Point
"""
Принимает координаты четырёх точек на плоскости,  последовательно задающих два отрезка.
Возвращает None, если отрезки не пересекаются или пересекаются в бесконечном
множестве точек, иначе возвращает точку персечения отрезков.
"""

def check(ax, ay, bx, by, x1, y1, x2, y2):
    
    # назовём первый отрезок AB, второй 1-2
    # Нахождение уравнений прямх, содержащих отрезки.
    dx, dy = ax - bx, ay - by
    c = ay * dx - ax * dy
    dy12, dx12 = y1 - y2, x1 - x2
    c12 = y1 * dx12 - x1 * dy12
    # уравнение прямой 1-2: {dx12}y = {dy12}x + {c12} (1)
    # уравнение прямой a-b: {dx}y = {dy}x + {c} (2)
    
    # проверка системы из уравний (1) и (2) на совместимость
    # (если детерминант равен нулю - система не имеет решений в действительных
    # числах, иначе имеет, притом ровно одно)
    determinant = dx12 * dy - dx * dy12
    
    # если прямые пересекаются
    if determinant != 0:
        #p_x и p_y - координаты пересечения двух прямых
        if dy == 0:
            p_y = c / dx
            p_x = (p_y * dx12 - c12) / dy12
        
            # проверка точки пересечения прямых на пренадлежность
            # к обоим отрезкам
            if ( min(x1, x2) <= p_x <= max(x1, x2) and
                min(y1, y2) <= p_y <= max(y1, y2) and
                min(ax, bx) <= p_x <= max(bx, ax) and
                min(by, ay) <= p_y <= max(by, ay) ):
                return R2Point(p_x, p_y)
            return None
        
        if dy12 == 0:
            p_y = c12 / dx12
            p_x = (p_y * dx - c) / dy
            # проверка точки пересечения прямых на пренадлежность
            # к обоим отрезкам

            if ( min(x1, x2) <= p_x <= max(x1, x2) and
                min(y1, y2) <= p_y <= max(y1, y2) and
                min(ax, bx) <= p_x <= max(bx, ax) and
                min(by, ay) <= p_y <= max(by, ay)):
                return R2Point(p_x, p_y)
            return None
        
        p_y = (c12 * dy - c * dy12) / determinant
        p_x = (p_y * dx - c) / dy
         # проверка точки пересечения прямых на пренадлежность
         # к обоим отрезкам
        if (min(x1, x2) <= p_x <= max(x1, x2) and
            min(y1, y2) <= p_y <= max(y1, y2) and
            min(ax, bx) <= p_x <= max(bx, ax) and
            min(by, ay) <= p_y <= max(by, ay)):
            return R2Point(p_x, p_y)
    return None

if __name__ == '__main__':
    while True:
        A = R2Point()
        B = R2Point()
        p1 = R2Point()
        p2 = R2Point()
        print(type(check(A.x, A.y, B.x, B.y, p1.x, p1.y, p2.x, p2.y)))
