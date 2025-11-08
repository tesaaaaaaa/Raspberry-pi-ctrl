from flask import Flask
import RPi.GPIO as GPIO
# https://www.indoorcorgielec.com/resources/raspberry-pi/python-gpio/
# https://qiita.com/koooooo/items/e5fa77f98e6ce5c05776

# RaspberryPI model 3b+
app = Flask(__name__)
PinNumber = 17

MOTOR_A1 = 26
MOTOR_A2 = 19
MOTOR_B1 = 13
MOTOR_B2 = 12
# GPIOのピン番号モードを設定 (BCMモード)
GPIO.setmode(GPIO.BCM)

# 指定したピンを出力モードに設定




def setup():
    GPIO.setup(MOTOR_A1, GPIO.OUT)
    GPIO.setup(MOTOR_A2, GPIO.OUT)
    GPIO.setup(MOTOR_B1, GPIO.OUT)
    GPIO.setup(MOTOR_B2, GPIO.OUT)



@app.route('/fw')
def taiya_fw():
    GPIO.output(PinNumber, 1) # 出力 ここでは3.3Vにする
    GPIO.output(MOTOR_A1,GPIO.HIGH)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.HIGH)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    return "LED is ON"

@app.route('/bk')
def taiya_bk():
    GPIO.output(PinNumber, 1) # 出力 ここでは3.3Vにする
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)
    return "LED is ON"

@app.route('/lt')
def taiya_lt():
    GPIO.output(PinNumber, 1) # 出力 ここでは3.3Vにする
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.HIGH)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    return "LED is ON"

@app.route('/rt')
def taiya_rt():
    GPIO.output(PinNumber, 1) # 出力 ここでは3.3Vにする
    GPIO.output(MOTOR_A1,GPIO.HIGH)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)
    return "LED is ON"

@app.route('/st')
def taiya_st():
    GPIO.output(PinNumber, 0) # 出力 ここでは3.3Vにする
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    return "LED is OFF"

@app.route('/off')
def led_off():
    GPIO.output(PinNumber, 0) # 出力 ここでは0Vにする
    return "LED is OFF"

if __name__ == '__main__':
    try:
        setup()

        app.run(host='0.0.0.0', port=8800)
    finally:
        # プログラム終了時にGPIOをクリーンアップ
        print("\nCleaning up GPIO...")
        GPIO.cleanup()