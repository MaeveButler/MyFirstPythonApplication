import pygame, sys, math, datetime

windowMargin = 30
windowWidth = 600
windowHeight = windowWidth
windowCenter = windowWidth/2, windowHeight/2
clockMarginWidth = 20
secondColor = (200, 200, 200)
minuteColor = (200, 200, 200)
hourColor = (200, 200, 200)
clockMarginColor = (130, 130, 130)
clockBackgroundColor = (40, 40, 40)
backgroundColor = (0, 0, 0)
hourCursorLenght = windowWidth/2.0-windowMargin-140
minuteCursorLenght = windowWidth/2.0-windowMargin-40
secondCursorLenght = windowWidth/2.0-windowMargin-10

virtualSpeed = 1
useVirtualTimer = False

#test

def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((windowWidth, windowHeight))#, pygame.HWSURFACE | pygame.DOUBLEBUFF);
    pygame.display.set_caption('Analog Clock');

    while True:
        handleEvents()
        screen.fill(backgroundColor)

        drawBackground()
        drawCurrentTime()
        drawForeground()

        pygame.display.flip()
        pygame.time.delay(10)


def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit(0)

def drawBackground():
    screen.fill(backgroundColor)
    pygame.draw.ellipse(screen, clockMarginColor, (windowMargin,\
        windowMargin, windowWidth-2*windowMargin,\
        windowWidth-2*windowMargin))
    pygame.draw.ellipse(screen, clockBackgroundColor,\
       (windowMargin+clockMarginWidth/2,\
        windowMargin+clockMarginWidth/2,\
        windowWidth-(windowMargin+clockMarginWidth/2)*2,\
        windowWidth-(windowMargin+clockMarginWidth/2)*2))

def drawForeground():
    pygame.draw.ellipse(screen, clockMarginColor,\
        (windowWidth/2.0-9, windowHeight/2.0-9, 18, 18))

def drawCursor(color, width, lenght, position, scale):
    end = getCirclePoint(position, scale, lenght);
    pygame.draw.line(screen, color, windowCenter, end, width)

def drawCurrentTime():
    if useVirtualTimer:
        global hour, minute, second, micro
        timeGoesOn()
    else:
        now = datetime.datetime.now()
        micro = now.microsecond
        hour = now.hour
        minute = now.minute
        second = now.second

    drawCursor(hourColor, 15, hourCursorLenght, hour+minute/60.0, 12)
    drawCursor(minuteColor, 8, minuteCursorLenght, minute+second/60.0, 60)
    drawCursor(secondColor, 3, secondCursorLenght, second+micro/1000000.0, 60)

hour = 0
minute = 0
second = 0
micro = 0
def timeGoesOn():
    global hour, minute, second, micro
    micro += virtualSpeed
    if micro >= 2:
        second += 1
        micro %= 2
    if second > 60:
        minute += 1
        second %= 60
    if minute > 60:
        hour += 1
        minute %= 60
    if hour > 12:
        hour %= 12

def getCursorPositionDegree(position, scale):
    cursorOffset = -90
    degrees = 360 / scale * position + cursorOffset
    return degrees

def gradToBogenmass(degrees):
    return degrees/180.0*math.pi

def getCirclePoint(position, scale, cursorLenght):
    degrees = getCursorPositionDegree(position, scale)
    bogenmass = gradToBogenmass(degrees)
    xPos = round(math.cos(bogenmass)*cursorLenght+windowCenter[0])
    yPos = round(math.sin(bogenmass)*cursorLenght+windowCenter[1])
    return (xPos, yPos)


if __name__ == '__main__':
        main()