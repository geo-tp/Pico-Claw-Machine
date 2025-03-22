from machine import Pin
import time

# LED
led = Pin("LED", Pin.OUT)

# Aimant
pince = Pin(1, Pin.OUT)

# Moteurs
motorX_gauche = Pin(2, Pin.OUT)
motorX_droite = Pin(3, Pin.OUT)
motorY_gauche = Pin(4, Pin.OUT)
motorY_droite = Pin(5, Pin.OUT)
motorZ_haut = Pin(6, Pin.OUT)
motorZ_bas = Pin(7, Pin.OUT)

# Boutons
btn_pince_haut = Pin(8, Pin.IN, Pin.PULL_UP)
btn_pince_bas = Pin(9, Pin.IN, Pin.PULL_UP)
btn_pince_catch = Pin(10, Pin.IN, Pin.PULL_UP)
btn_grue_gauche = Pin(11, Pin.IN, Pin.PULL_UP)
btn_grue_droite = Pin(12, Pin.IN, Pin.PULL_UP)
btn_grue_haut = Pin(13, Pin.IN, Pin.PULL_UP)
btn_grue_bas = Pin(14, Pin.IN, Pin.PULL_UP)

# Fins de course moteurs
limitX_gauche = Pin(16, Pin.IN, Pin.PULL_UP)
limitY_haut = Pin(17, Pin.IN, Pin.PULL_UP)
limitY_bas = Pin(18, Pin.IN, Pin.PULL_UP)
limitZ_haut = Pin(19, Pin.IN, Pin.PULL_UP)
limitZ_bas = Pin(20, Pin.IN, Pin.PULL_UP)

while True:
    led_state = False

    # Moteurs X (gauche/droite)
    if not btn_grue_gauche.value() and not limitX_gauche.value():
        motorX_gauche.on()
        print("Grue gauche")
        led_state = True
    else:
        motorX_gauche.off()

    if not btn_grue_droite.value():
        motorX_droite.on()
        print("Grue droite")
        led_state = True
    else:
        motorX_droite.off()

    # Moteurs Y (avance/recule)
    if not btn_grue_haut.value() and not limitY_haut.value():
        motorY_gauche.on()
        print("Grue avance")
        led_state = True
    else:
        motorY_gauche.off()

    if not btn_grue_bas.value() and not limitY_bas.value():
        motorY_droite.on()
        print("Grue recule")
        led_state = True
    else:
        motorY_droite.off()

    # Moteurs Z (pince haut/bas)
    if not btn_pince_haut.value() and not limitZ_haut.value():
        motorZ_haut.on()
        print("Pince monte")
        led_state = True
    else:
        motorZ_haut.off()

    if not btn_pince_bas.value() and not limitZ_bas.value():
        motorZ_bas.on()
        print("Pince descend")
        led_state = True
    else:
        motorZ_bas.off()

    # Pince
    if not btn_pince_catch.value():
        pince.on()
        print("Pince attrape")
        led_state = True
    else:
        pince.off()

    # Allumer la LED si au moins un moteur ou la pince
    if led_state:
        led.on()
    else:
        led.off()

    time.sleep(0.01)
