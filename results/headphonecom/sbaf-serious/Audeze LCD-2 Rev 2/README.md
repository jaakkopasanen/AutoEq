# Audeze LCD-2 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 10 -84; 20 -3.5; 22 -3.5; 23 -3.5; 25 -3.5; 26 -3.5; 28 -3.4; 30 -3.4; 32 -3.3; 35 -3.3; 37 -3.3; 40 -3.4; 42 -3.3; 45 -3.3; 49 -3.1; 52 -2.9; 56 -3.3; 59 -3.9; 64 -4.1; 68 -4.1; 73 -4.0; 78 -3.9; 83 -3.7; 89 -3.6; 95 -3.6; 102 -3.6; 109 -3.5; 117 -3.3; 125 -3.3; 134 -3.3; 143 -3.3; 153 -3.4; 164 -3.4; 175 -3.4; 188 -3.6; 201 -3.5; 215 -3.5; 230 -3.4; 246 -3.1; 263 -3.1; 282 -3.2; 301 -3.1; 323 -2.7; 345 -2.3; 369 -2.2; 395 -2.3; 423 -2.2; 452 -2.3; 484 -2.5; 518 -2.6; 554 -2.4; 593 -2.3; 635 -2.3; 679 -2.5; 726 -2.3; 777 -2.2; 832 -2.2; 890 -1.7; 952 -0.7; 1019 0.1; 1090 0.6; 1167 1.4; 1248 0.7; 1336 -0.1; 1429 -1.0; 1529 -1.8; 1636 -2.3; 1751 -2.6; 1873 -1.1; 2004 -0.3; 2145 -0.1; 2295 -1.4; 2455 -0.4; 2627 1.0; 2811 0.8; 3008 0.7; 3219 0.6; 3444 2.0; 3685 2.9; 3943 3.8; 4219 3.4; 4514 2.7; 4830 1.0; 5168 0.2; 5530 0.0; 5917 -0.2; 6331 0.2; 6775 0.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -2.5; 18692 -3.8; 20000 -3.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.3dB` and instead set Global volume in the UI for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.21 | -3.0 dB |
| Peaking | 189 Hz   | 0.33 | -2.9 dB |
| Peaking | 700 Hz   | 3.14 | -1.3 dB |
| Peaking | 4004 Hz  | 3.74 | 4.1 dB  |
| Peaking | 18980 Hz | 2.01 | -4.3 dB |
| Peaking | 1165 Hz  | 5.43 | 2.4 dB  |
| Peaking | 1666 Hz  | 4.69 | -2.6 dB |
| Peaking | 5780 Hz  | 4.71 | -0.7 dB |
| Peaking | 7081 Hz  | 6.88 | 1.4 dB  |
| Peaking | 24000 Hz | 3.22 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)