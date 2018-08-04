# Denon AH-D1100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -6.7; 22 -7.2; 23 -7.5; 25 -7.9; 26 -8.1; 28 -8.4; 30 -8.7; 32 -8.9; 35 -9.3; 37 -9.4; 40 -9.6; 42 -9.8; 45 -9.9; 49 -10.1; 52 -10.3; 56 -10.4; 59 -10.5; 64 -10.7; 68 -10.7; 73 -10.8; 78 -10.8; 83 -10.8; 89 -10.8; 95 -10.7; 102 -10.6; 109 -10.5; 117 -10.9; 125 -11.8; 134 -13.0; 143 -13.3; 153 -12.6; 164 -11.8; 175 -11.4; 188 -12.3; 201 -12.2; 215 -11.9; 230 -11.1; 246 -10.1; 263 -9.1; 282 -7.7; 301 -6.1; 323 -4.4; 345 -2.6; 369 -0.8; 395 0.9; 423 2.5; 452 3.4; 484 3.4; 518 2.8; 554 2.2; 593 1.5; 635 0.7; 679 -0.0; 726 -0.4; 777 -0.5; 832 -0.6; 890 -0.4; 952 -0.2; 1019 0.2; 1090 0.4; 1167 0.5; 1248 0.6; 1336 0.4; 1429 -0.1; 1529 -0.9; 1636 -1.6; 1751 -2.5; 1873 -3.1; 2004 -3.1; 2145 -2.5; 2295 -1.3; 2455 0.4; 2627 1.9; 2811 3.8; 3008 5.0; 3219 2.9; 3444 1.1; 3685 5.0; 3943 6.0; 4219 5.6; 4514 0.3; 4830 -0.6; 5168 0.9; 5530 0.7; 5917 3.8; 6331 3.6; 6775 2.3; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -2.0; 9502 -3.3; 10167 -3.8; 10879 -3.2; 11640 -0.7; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 2 Hz     | 1.92 | -5.8 dB  |
| Peaking | 48 Hz    | 0.49 | -10.3 dB |
| Peaking | 143 Hz   | 1.6  | -8.1 dB  |
| Peaking | 226 Hz   | 2.76 | -7.7 dB  |
| Peaking | 3871 Hz  | 3.47 | 5.8 dB   |
| Peaking | 472 Hz   | 3.38 | 5.4 dB   |
| Peaking | 1964 Hz  | 3.46 | -3.8 dB  |
| Peaking | 2887 Hz  | 7.62 | 4.4 dB   |
| Peaking | 6283 Hz  | 6.94 | 4.3 dB   |
| Peaking | 10079 Hz | 3.8  | -4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)