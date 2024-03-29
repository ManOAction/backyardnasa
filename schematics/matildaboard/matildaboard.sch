EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Matilda_CustomLibrary:AdaBrk_Si7021 U1
U 1 1 5E5717AE
P 4200 2650
F 0 "U1" V 4665 2733 50  0000 C CNN
F 1 "AdaBrk_Si7021" V 4574 2733 50  0000 C CNN
F 2 "MatildaCustom:Adafruit_Si7021_Breakout" H 4200 3350 50  0001 C CNN
F 3 "" H 4200 3350 50  0001 C CNN
	1    4200 2650
	0    1    -1   0   
$EndComp
Text GLabel 4650 1150 3    50   Input ~ 0
3.3V
Text GLabel 4750 1150 3    50   Input ~ 0
GND
Text GLabel 4850 1150 3    50   Input ~ 0
Logic_1
Text GLabel 4950 1150 3    50   Input ~ 0
Logic_2
Text GLabel 5050 1150 3    50   Input ~ 0
Logic_3
Text GLabel 5150 1150 3    50   Input ~ 0
Logic_4
Text GLabel 5250 1150 3    50   Input ~ 0
Logic_5
Text GLabel 4450 1150 3    50   Input ~ 0
SDA
Text GLabel 4550 1150 3    50   Input ~ 0
SCL
Text GLabel 4500 2450 2    50   Input ~ 0
SDA
Text GLabel 4500 2550 2    50   Input ~ 0
SCL
Text GLabel 5100 4650 0    50   Input ~ 0
Logic_1
Text GLabel 5100 4500 0    50   Input ~ 0
Logic_2
Text GLabel 5100 4350 0    50   Input ~ 0
Logic_3
Text GLabel 5100 4200 0    50   Input ~ 0
Logic_4
Text GLabel 5100 4050 0    50   Input ~ 0
Logic_5
NoConn ~ 5650 2050
NoConn ~ 5350 2050
NoConn ~ 4500 2750
NoConn ~ 5100 3900
$Comp
L power:GND #PWR0101
U 1 1 5E583DD6
P 7350 1050
F 0 "#PWR0101" H 7350 800 50  0001 C CNN
F 1 "GND" H 7350 900 50  0000 C CNN
F 2 "" H 7350 1050 50  0001 C CNN
F 3 "" H 7350 1050 50  0001 C CNN
	1    7350 1050
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0102
U 1 1 5E58422F
P 7350 750
F 0 "#PWR0102" H 7350 600 50  0001 C CNN
F 1 "+3.3V" H 7365 923 50  0000 C CNN
F 2 "" H 7350 750 50  0001 C CNN
F 3 "" H 7350 750 50  0001 C CNN
	1    7350 750 
	1    0    0    -1  
$EndComp
Text GLabel 7350 1050 0    50   Input ~ 0
GND
Text GLabel 7350 750  0    50   Input ~ 0
3.3V
$Comp
L Matilda_CustomLibrary:Matilda_Battery_Cell BT1
U 1 1 5E58F4BD
P 7350 950
F 0 "BT1" H 7468 1046 50  0000 L CNN
F 1 "Matilda_Battery_Cell" H 7468 955 50  0000 L CNN
F 2 "Battery:Battery_Panasonic_CR2032-VS1N_Vertical_CircularHoles" V 7350 1010 50  0001 C CNN
F 3 "~" V 7350 1010 50  0001 C CNN
	1    7350 950 
	1    0    0    -1  
$EndComp
$Comp
L Matilda_CustomLibrary:Adafruit_Breakout_DRV8833 A1
U 1 1 5E5962E7
P 5500 4000
F 0 "A1" H 5500 3225 50  0000 C CNN
F 1 "Adafruit_Breakout_DRV8833" H 5500 3134 50  0000 C CNN
F 2 "MatildaCustom:Adafruit_Breakout_DRV8833" H 5700 3200 50  0001 L CNN
F 3 "https://www.pololu.com/product/2982" H 5600 3700 50  0001 C CNN
	1    5500 4000
	1    0    0    -1  
$EndComp
$Comp
L Matilda_CustomLibrary:Woo_StepUp_MT3608 U2
U 1 1 5E5978DE
P 5500 2500
F 0 "U2" H 5778 2521 50  0000 L CNN
F 1 "Woo_StepUp_MT3608" H 5778 2430 50  0000 L CNN
F 2 "MatildaCustom:Woo_StepUp_MT3608" H 5500 3550 50  0001 C CNN
F 3 "" H 5500 3550 50  0001 C CNN
	1    5500 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 3000 5400 3000
Wire Wire Line
	5400 3000 5400 3400
Wire Wire Line
	5350 3000 5350 3200
Wire Wire Line
	5350 3200 5600 3200
Wire Wire Line
	5600 3200 5600 3400
Text GLabel 4500 2850 2    50   Input ~ 0
3.3V
Text GLabel 4500 2650 2    50   Input ~ 0
GND
Text GLabel 5100 3600 0    50   Input ~ 0
3.3V
Text GLabel 5100 3750 0    50   Input ~ 0
GND
NoConn ~ 5900 3900
NoConn ~ 5900 3750
$Comp
L Connector:Conn_01x09_Female J1
U 1 1 5E59EDE1
P 4850 950
F 0 "J1" V 5015 930 50  0000 C CNN
F 1 "Conn_01x09_Female" V 4924 930 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x09_P2.54mm_Vertical" H 4850 950 50  0001 C CNN
F 3 "~" H 4850 950 50  0001 C CNN
	1    4850 950 
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Conn_01x04_Female J2
U 1 1 5E5A5861
P 6800 4200
F 0 "J2" H 6828 4176 50  0000 L CNN
F 1 "Conn_01x04_Female" H 6828 4085 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 6800 4200 50  0001 C CNN
F 3 "~" H 6800 4200 50  0001 C CNN
	1    6800 4200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5900 4500 6600 4500
Wire Wire Line
	6600 4500 6600 4400
Wire Wire Line
	5900 4350 6600 4350
Wire Wire Line
	6600 4350 6600 4300
Wire Wire Line
	5900 4200 6600 4200
Wire Wire Line
	5900 4050 6600 4050
Wire Wire Line
	6600 4050 6600 4100
$EndSCHEMATC
