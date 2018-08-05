# Westone W2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.9; 22 1.8; 23 1.7; 25 1.7; 26 1.6; 28 1.6; 30 1.6; 32 1.7; 35 1.6; 37 1.6; 40 1.5; 42 1.5; 45 1.5; 49 1.4; 52 1.4; 56 1.4; 59 1.4; 64 1.3; 68 1.2; 73 1.1; 78 1.0; 83 0.7; 89 0.3; 95 -0.1; 102 -0.6; 109 -1.1; 117 -1.6; 125 -2.2; 134 -2.5; 143 -2.8; 153 -3.1; 164 -3.3; 175 -3.3; 188 -3.4; 201 -3.4; 215 -3.4; 230 -3.1; 246 -3.1; 263 -3.1; 282 -3.0; 301 -2.7; 323 -2.5; 345 -2.3; 369 -2.0; 395 -2.0; 423 -1.6; 452 -1.4; 484 -1.2; 518 -1.0; 554 -0.6; 593 -0.2; 635 0.1; 679 0.2; 726 0.4; 777 0.7; 832 0.7; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.6; 1529 -2.0; 1636 -2.4; 1751 -2.5; 1873 -2.4; 2004 -2.3; 2145 -1.9; 2295 -1.0; 2455 0.5; 2627 2.2; 2811 4.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.7; 5168 5.6; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.44 | 1.8 dB  |
| Peaking | 76 Hz   | 1.54 | 1.4 dB  |
| Peaking | 192 Hz  | 0.75 | -3.9 dB |
| Peaking | 1977 Hz | 1.72 | -5.9 dB |
| Peaking | 3710 Hz | 0.88 | 7.7 dB  |
| Peaking | 781 Hz  | 2.16 | 1.4 dB  |
| Peaking | 2961 Hz | 8.72 | 1.9 dB  |
| Peaking | 2261 Hz | 0.14 | -0.4 dB |
| Peaking | 6237 Hz | 2.83 | 5.6 dB  |
| Peaking | 7161 Hz | 1.45 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20W2/Westone%20W2.png)