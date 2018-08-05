# Bowers & Wilkins P7 Wireless Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.2; 22 2.6; 23 2.3; 25 1.8; 26 1.6; 28 1.3; 30 1.0; 32 0.7; 35 0.4; 37 0.2; 40 -0.0; 42 -0.1; 45 -0.3; 49 -0.4; 52 -0.5; 56 -0.5; 59 -0.6; 64 -0.6; 68 -0.7; 73 -0.8; 78 -0.9; 83 -0.9; 89 -1.2; 95 -1.5; 102 -1.7; 109 -1.9; 117 -2.1; 125 -2.3; 134 -2.5; 143 -2.8; 153 -2.9; 164 -3.1; 175 -2.7; 188 -2.6; 201 -2.7; 215 -2.6; 230 -2.4; 246 -2.2; 263 -1.9; 282 -1.3; 301 -0.6; 323 -0.0; 345 0.2; 369 0.5; 395 0.7; 423 0.7; 452 0.7; 484 0.6; 518 0.6; 554 0.7; 593 0.9; 635 0.9; 679 0.7; 726 0.6; 777 0.6; 832 0.3; 890 0.1; 952 -0.1; 1019 0.2; 1090 0.5; 1167 0.2; 1248 -0.1; 1336 -0.6; 1429 -1.3; 1529 -1.8; 1636 -2.3; 1751 -2.6; 1873 -2.5; 2004 -2.0; 2145 -1.8; 2295 -1.9; 2455 -2.0; 2627 -1.4; 2811 -0.1; 3008 3.2; 3219 5.5; 3444 4.5; 3685 2.4; 3943 0.2; 4219 -0.6; 4514 -0.2; 4830 0.2; 5168 1.2; 5530 2.4; 5917 1.5; 6331 2.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 Wireless Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.1  | 2.8 dB  |
| Peaking | 157 Hz  | 1.22 | -3.2 dB |
| Peaking | 2130 Hz | 1.63 | -2.8 dB |
| Peaking | 3249 Hz | 5.49 | 6.9 dB  |
| Peaking | 6590 Hz | 5.06 | 3.8 dB  |
| Peaking | 246 Hz  | 2.84 | -1.5 dB |
| Peaking | 456 Hz  | 0.77 | 1.3 dB  |
| Peaking | 1170 Hz | 4.04 | 0.9 dB  |
| Peaking | 1826 Hz | 1.6  | -1.5 dB |
| Peaking | 2076 Hz | 5.01 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7%20Wireless%20Bluetooth/Bowers%20&%20Wilkins%20P7%20Wireless%20Bluetooth.png)