# Fostex T50RP Mk2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.5; 32 5.1; 35 4.5; 37 4.2; 40 4.0; 42 3.8; 45 3.7; 49 3.6; 52 3.5; 56 3.5; 59 3.6; 64 3.6; 68 3.5; 73 3.5; 78 3.5; 83 3.4; 89 3.2; 95 3.0; 102 2.7; 109 2.4; 117 2.0; 125 1.3; 134 0.7; 143 0.4; 153 0.3; 164 0.5; 175 0.5; 188 0.1; 201 0.0; 215 0.1; 230 0.2; 246 0.3; 263 0.4; 282 0.5; 301 0.6; 323 0.7; 345 0.9; 369 1.0; 395 1.0; 423 1.1; 452 1.0; 484 0.8; 518 0.8; 554 0.7; 593 0.1; 635 0.4; 679 2.5; 726 3.1; 777 2.6; 832 2.1; 890 1.2; 952 0.5; 1019 -0.3; 1090 -1.2; 1167 -1.6; 1248 -1.6; 1336 -1.4; 1429 -0.4; 1529 -0.6; 1636 -1.2; 1751 -1.0; 1873 0.3; 2004 2.5; 2145 4.6; 2295 5.5; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50RP Mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.61 | 6.0 dB  |
| Peaking | 81 Hz   | 1.56 | 2.4 dB  |
| Peaking | 753 Hz  | 3.69 | 3.1 dB  |
| Peaking | 1491 Hz | 1.3  | -5.2 dB |
| Peaking | 3120 Hz | 0.66 | 7.7 dB  |
| Peaking | 1832 Hz | 5.26 | -3.0 dB |
| Peaking | 2131 Hz | 1.84 | 2.3 dB  |
| Peaking | 3169 Hz | 2.01 | -1.5 dB |
| Peaking | 6252 Hz | 2.05 | 5.9 dB  |
| Peaking | 7378 Hz | 1.43 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50RP%20Mk2/Fostex%20T50RP%20Mk2.png)