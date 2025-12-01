from PIL import Image, ImageDraw
import random
import os
def load_image():
    while True:
        filename = input("Введите имя файла изображения (*.jpg):")
        if not filename:
            print("Имя файла не может быть пустым")
            continue

        try:
            img = Image.open(filename)
            print (f"Изображение '{filename}'успешно загружено")
            return img
        except FileNotFoundError:
            print(f"Ошибка! Файл '{filename}'не найден")
        except PermissionError:
            print(f"Ошибка! Нет доступа к файлу '{filename}'")
            print("Проверьте права доступа к файлу.")
        except IsADirectoryError:
             print(f" Ошибка! '{filename}' это папка, а не файл!")
        except Exception as e:

            print(f"✗ Неизвестная ошибка")


        print("Пожалуйста, попробуйте снова.\n")
def print_image_info(img):
    print("Информация от изображении")
    print(f"Размеры:")
    print(f"Ширина: {img.width} пикселей")
    print(f"Высота: {img.height} пикселей")
    print(f"Соотношение сторон: {img.width}:{img.height}")
    print(f"\n Цвет и формат:")
    print(f"Режим цвета: {img.mode}")
    print(f"Глубина цвета: {get_color_depth(img)}")
    if hasattr(img, 'filename'):


        print(f"Имя файла: {os.path.basename(img.filename)}")

    if hasattr(img, 'format'):
        print(f"Формат: {img.format}")
        try:

            if hasattr(img, 'filename') and os.path.exists(img.filename):

                file_size = os.path.getsize(img.filename)
                print(f"\n Файл:")

                print(f"Размер файла: {file_size / 1024:.2f} KB")
        except:
            pass

def get_color_depth(img):
    modes = {
        '1': '1 бит (чёрно-белое)',
        'L': '8 бит (оттенки серого)',
        'P': '8 бит (палитра)',
        'RGB': '24 бита (True Color)',
        'RGBA': '32 бита (True Color + Alpha)',
        'CMYK': '32 бита (Cyan, Magenta, Yellow, Black)',
        'YCbCr': '24 бита (цветовое пространство)',
        'LAB': '24 бита (цветовое пространство)',
        'HSV': '24 бита (Hue, Saturation, Value)'
    }
    return modes.get(img.mode, f'Неизвестный режим: {img.mode}')
def apply_grayscale(img):
    print("Применяем черно-белый фильтр")
    return img.convert('L')
def flip_vertical(img):
    print("Отражаем по вертикали")
    return img.transpose(Image.FLIP_TOP_BOTTOM)


def flip_horizontal(img):
    print("Отражаем по горизонтали")
    return img.transpose(Image.FLIP_LEFT_RIGHT)
def add_random_square(img):
    print(" Добавляем случайный квадрат")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    width, height = img_copy.size
    min_side = min(width, height)

    max_size = min_side // 3

    square_size = random.randint(min_side // 10, max_size)
    x = random.randint(0, width - square_size - 1)
    y = random.randint(0, height - square_size - 1)
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )



    draw.rectangle(
        [x, y, x + square_size, y + square_size],
        fill=color,
        outline=(0, 0, 0),
        width=2
    )


    print(f"Размер квадрата: {square_size}×{square_size} пикселей")
    print(f"Позиция: ({x}, {y})")
    print(f"Цвет: RGB{color}")

    return img_copy
def add_noise(img):
    print("Добавляем шум (10% пикселей)")
    img_copy = img.copy()
    pixels = img_copy.load()
    width, height = img_copy.size
    total_pixels = width * height
    noise_pixels = int(total_pixels * 0.1)
    print(f"Всего пикселей: {total_pixels}")
    print(f"Будет изменено: {noise_pixels} пикселей")

    changed = 0
    for _ in range(noise_pixels):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if img.mode == 'L':
            pixels[x, y] = random.randint(0, 255)

        elif img.mode == 'RGB':

            pixels[x, y] = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )

        elif img.mode == 'RGBA':


            pixels[x, y] = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                255
            )

        else:

            pixels[x, y] = random.choice([0, 255])

        changed += 1

    print(f"Фактически изменено: {changed} пикселей")
    return img_copy

def show_effects_menu():

    print("Выбор эффекта для изображения")
    print("1. Сделать черно-белым")
    print("2. Отразить по вертикали")
    print("3. Отразить по горизонтали")
    print("4. Добавить случайный квадрат")
    print("5. Добавить шум")
    print("6. Вернуться в главное меню")
def apply_effect(img):
    while True:
        show_effects_menu()
        choice = input("\n Выбирете эффект от 1-6:")
        if choice == '1':
            return apply_grayscale(img)
        elif choice == '2':
            return flip_vertical(img)
        elif choice == '3':
            return flip_horizontal(img)
        elif choice == '4':
            return add_random_square(img)
        elif choice == '5':
            return add_noise(img)
        elif choice == '6':
            print("Возвращаемся в главное меню")
            return None
        else:
            print(" Неверный выбор! Пожалуйста, введите число от 1 до 6.")


def save_image(img):
    print("Сохранение изображения")
    formats = {
        'jpg': 'JPEG',
        'jpeg': 'JPEG',
        'png': 'PNG',
        'bmp': 'BMP',
        'gif': 'GIF',
        'tiff': 'TIFF',
        'webp': 'WEBP'
    }
    while True:
        print("\n Введите имя файла для сохранения.")
        print("Поддерживаемые форматы: JPG, PNG, BMP, GIF, TIFF, WEBP")
        filename = input("Имя файла: ")
        if not filename:
            print("Имя файла не может быть пустым!")
            continue
        if '.' not in filename:
            filename += '.jpg'
            print(f"Добавлено расширение .jpg -> {filename}")
        _, ext = os.path.splitext(filename)
        ext = ext.lower()[1:]
        if ext not in formats:
            print(f"Неподдерживаемый формат: .{ext}")
            print(f"Доступные форматы: {', '.join(formats.keys())}")
            continue
        try:
            save_params = {}
            if formats[ext] == 'JPEG':
                save_params['quality'] = 95
            img.save(filename, format=formats[ext], **save_params)
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                print(f"\nУспешно сохранено!")
                print(f"Файл: {filename}")
                print(f"Размер: {file_size / 1024:.2f} KB")
                print(f"Формат: {formats[ext]}")
                return True
            else:
                print("Ошибка!")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")

        print("\nХотите попробовать другое имя?")
        retry = input("Введите 'да' или 'нет': ")

        if retry not in ['да', 'д', 'yes', 'y']:
            print("Сохранение отменено.")
            return False
def show_main_menu():

    print("Главное меню")

    print("1. Применить эффект")
    print("2. Сохранить изображение")
    print("3. Показать информацию об изображении")
    print("4. Выход")
def main():
    print("Редактор Изображений")
    print("Эта программа позволяет:")
    print("Загружать изображения")
    print("Применять различные эффекты")
    print("Сохранять результаты")

    print("\nЗАГРУЗКА ИЗОБРАЖЕНИЯ")

    img = load_image()
    if img is None:
        print("Не удалось загрузить изображение.")
        return
    while True:
        print_image_info(img)
        show_main_menu()
        choice = input("\nВыберите действие (1-4): ")
        if choice == '1':

            result = apply_effect(img)


            if result is not None:
                img = result
                print("\nЭффект успешно применен!")
                print(f"Новые размеры: {img.width}×{img.height}")

        elif choice == '2':

            save_image(img)

        elif choice == '3':

            print("Информация об изображении уже отображена выше.")
            continue

        elif choice == '4':
            print("Выход из программы")

            if hasattr(img, 'filename'):
                print(f"\nТекущее изображение: {os.path.basename(img.filename)}")

            save_before_exit = input("Сохранить перед выходом? (да/нет): ")
            if save_before_exit in ['да','yes']:
                save_image(img)

            print("До свидания!")
            break

        else:
            print(" Неверный выбор! Пожалуйста, введите число от 1 до 4.")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:

        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:

        print(f"\n Критическая ошибка: {type(e).__name__}: {e}")
        print("Программа завершена.")


















