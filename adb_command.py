import os

"""
파이썬을 이용하여 adb명령어를 사용하고, 디바이스 화면에 탭, 스와이프, 사각형을 스와이프하는 파일
"""

#pc에 연결된 디바이스의 첫번째 아이디 추출하여 DEVICE_ID에 담는다.
DEVICE_ID = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()

def screen_tap(device_id, x, y):
    """  adb를 사용한 안드로이드 디바이스에 탭 하는 함수
    Args:
            device_id: 디바이스 아이디를 입력
            x: 탭하려는 x 좌표
            y: 탭하려는 y 좌표
    Returns:
            함수 실행 후 adb 명령어 실행한 내용과 터미널에서 명령어 실행 후 나온 출력문을 리턴해준다.
    """
    command = ["adb", "-s" , device_id, "shell", "input", "tap", str(x), str(y)]
    result = os.popen(' '.join(command)).read()
    return ' '.join(command), result

def screen_swipe(device_id, x, x1, y, y1):
    """  adb를 사용한 안드로이드 디바이스에 스와이프 하는 함수
    Args:
            device_id: 디바이스 아이디를 입력
            x: 스와이프 시작점의 x 좌표
            x1: 스와이프 끝점의 x 좌표
            y: 스와이프 시작점의 y 좌표
            y1: 스와이프 끝점의  Y 좌표
    Returns:
            함수 실행 후 adb 명령어 실행한 내용과 터미널에서 명령어 실행 후 나온 출력문을 리턴해준다.
    """
    command = ["adb", "-s" , device_id, "shell", "input", "swipe", str(x), str(y), str(x1), str(y1)]
    result = os.popen(' '.join(command)).read()
    return ' '.join(command), result

def screen_square(x, y, size):
    """  screen_swipe를 사용하여 안드로이드 디바이스 화면에 사각형을 그리는 함수
    Args:            
            x: 시작점의 x 좌표
            y: 시작점의 y 좌표
            size: 한변의 길이
    Returns:
            리턴하지 않는다.
    """
    global DEVICE_ID
    in_list = [[x,y] for i in range(5)]
    add_list = [[0,0], [size, 0], [size, size], [0, size], [0,0]]
    result = [[a[0]+b[0],a[1]+b[1]] for a,b in zip(in_list, add_list)]
    
    for i in range(len(result)-1):
        p = result[i] + result[i+1]
        screen_swipe(DEVICE_ID, p[0], p[2], p[1], p[3])


if __name__ == '__main__':
    screen_swipe(DEVICE_ID, 400, 900, 600, 1200)
    
    screen_tap(DEVICE_ID, 700, 1600)
    
    screen_square(420, 315, 500)