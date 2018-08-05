# Klipsch X-10i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.5; 22 -1.6; 23 -1.6; 25 -1.7; 26 -1.7; 28 -1.8; 30 -1.8; 32 -1.8; 35 -1.7; 37 -1.7; 40 -1.7; 42 -1.7; 45 -1.7; 49 -1.8; 52 -1.8; 56 -1.8; 59 -1.8; 64 -1.9; 68 -2.0; 73 -2.0; 78 -2.0; 83 -2.1; 89 -2.4; 95 -2.8; 102 -3.2; 109 -3.6; 117 -4.1; 125 -4.6; 134 -5.0; 143 -5.3; 153 -5.4; 164 -5.5; 175 -5.4; 188 -5.3; 201 -5.2; 215 -5.0; 230 -4.8; 246 -4.7; 263 -4.5; 282 -4.2; 301 -4.0; 323 -3.6; 345 -3.2; 369 -3.0; 395 -2.7; 423 -2.3; 452 -2.1; 484 -1.9; 518 -1.6; 554 -1.2; 593 -0.7; 635 -0.4; 679 -0.2; 726 -0.0; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.6; 1529 -1.9; 1636 -1.9; 1751 -1.8; 1873 -1.6; 2004 -1.4; 2145 -1.4; 2295 -1.2; 2455 -1.2; 2627 -1.3; 2811 -1.5; 3008 -0.4; 3219 1.7; 3444 4.4; 3685 5.9; 3943 6.0; 4219 6.0; 4514 5.7; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.1; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X-10i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.8  | -1.6 dB |
| Peaking | 184 Hz  | 0.7  | -5.6 dB |
| Peaking | 2781 Hz | 3.5  | -4.1 dB |
| Peaking | 1762 Hz | 2.14 | -2.6 dB |
| Peaking | 4408 Hz | 1.24 | 7.3 dB  |
| Peaking | 776 Hz  | 2.31 | 1.1 dB  |
| Peaking | 3617 Hz | 7.83 | 2.0 dB  |
| Peaking | 415 Hz  | 2    | -0.5 dB |
| Peaking | 6153 Hz | 2.82 | 6.0 dB  |
| Peaking | 6500 Hz | 1.19 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20X-10i/Klipsch%20X-10i.png)