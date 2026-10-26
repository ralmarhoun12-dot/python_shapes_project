import math

REPEAT = int(input("Enter repeat count: "))


def is_inside_heart(x, y):
    return (x**2 + y**2 - 1) ** 3 - x**2 * y**3 <= 0


def star_points():
    points = []
    for i in range(10):
        angle = math.pi / 2 + i * math.pi / 5
        radius = 1 if i % 2 == 0 else 0.4
        points.append((math.cos(angle) * radius, math.sin(angle) * radius))
    return points


STAR = star_points()


def is_inside_star(x, y):
    inside = False
    for i in range(len(STAR)):
        x1, y1 = STAR[i]
        x2, y2 = STAR[(i + 1) % len(STAR)]
        if (y1 > y) != (y2 > y):
            if x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
                inside = not inside
    return inside


def draw_shape(is_inside, char):
    rows = []
    for r in range(13, -14, -1):
        y = r / 10
        row = ""
        for c in range(-30, 31):
            x = c / 20
            row += char if is_inside(x, y) else " "
        rows.append(row.rstrip())
    return "\n".join(rows)


def main():
    for _ in range(REPEAT):
        print(draw_shape(is_inside_heart, "*"))
        print(draw_shape(is_inside_star, "#"))
        print("Latifa is amazing!")


if __name__ == "__main__":
    main()
