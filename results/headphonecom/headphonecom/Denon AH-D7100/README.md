# Denon AH-D7100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -11.3; 22 -11.3; 23 -11.3; 25 -11.3; 26 -11.3; 28 -11.2; 30 -11.1; 32 -11.0; 35 -10.9; 37 -10.8; 40 -10.6; 42 -10.4; 45 -10.2; 49 -9.9; 52 -9.6; 56 -8.9; 59 -8.4; 64 -7.9; 68 -8.1; 73 -8.4; 78 -8.6; 83 -8.9; 89 -9.6; 95 -10.2; 102 -10.3; 109 -10.1; 117 -10.0; 125 -9.8; 134 -9.4; 143 -9.0; 153 -8.6; 164 -7.0; 175 -6.8; 188 -6.2; 201 -4.9; 215 -3.4; 230 -1.4; 246 0.9; 263 3.0; 282 5.0; 301 5.9; 323 6.0; 345 6.0; 369 5.5; 395 5.0; 423 4.6; 452 4.3; 484 3.8; 518 3.4; 554 2.9; 593 2.4; 635 1.8; 679 1.5; 726 1.2; 777 1.0; 832 0.8; 890 0.5; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.2; 1248 -0.1; 1336 0.0; 1429 0.1; 1529 -0.1; 1636 -0.4; 1751 -0.4; 1873 -0.3; 2004 0.2; 2145 1.1; 2295 2.5; 2455 4.1; 2627 5.4; 2811 5.6; 3008 5.4; 3219 5.6; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.6; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -2.8; 9502 -1.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.59 | -10.6 dB |
| Peaking | 146 Hz  | 0.56 | -10.9 dB |
| Peaking | 318 Hz  | 1.15 | 12.2 dB  |
| Peaking | 4490 Hz | 0.94 | 7.0 dB   |
| Peaking | 8920 Hz | 3.65 | -4.6 dB  |
| Peaking | 1939 Hz | 2.06 | -2.8 dB  |
| Peaking | 1133 Hz | 3.94 | -0.8 dB  |
| Peaking | 2626 Hz | 2.3  | 3.4 dB   |
| Peaking | 5296 Hz | 1.16 | -1.5 dB  |
| Peaking | 6096 Hz | 4.05 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Denon%20AH-D7100/Denon%20AH-D7100.png)