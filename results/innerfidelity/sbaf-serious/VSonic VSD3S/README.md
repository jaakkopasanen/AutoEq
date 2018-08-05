# VSonic VSD3S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 1.0; 22 0.6; 23 0.4; 25 0.2; 26 0.0; 28 -0.2; 30 -0.3; 32 -0.5; 35 -0.6; 37 -0.7; 40 -0.9; 42 -0.9; 45 -1.0; 49 -1.1; 52 -1.2; 56 -1.2; 59 -1.2; 64 -1.4; 68 -1.5; 73 -1.6; 78 -1.7; 83 -2.0; 89 -2.3; 95 -2.7; 102 -3.2; 109 -3.6; 117 -4.1; 125 -4.6; 134 -5.1; 143 -5.3; 153 -5.4; 164 -5.5; 175 -5.4; 188 -5.4; 201 -5.3; 215 -5.1; 230 -4.9; 246 -4.7; 263 -4.5; 282 -4.2; 301 -4.0; 323 -3.8; 345 -3.5; 369 -3.3; 395 -3.0; 423 -2.7; 452 -2.4; 484 -2.3; 518 -2.0; 554 -1.6; 593 -1.1; 635 -0.9; 679 -0.7; 726 -0.5; 777 -0.1; 832 -0.0; 890 -0.0; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.1; 1248 0.2; 1336 0.1; 1429 -0.1; 1529 -0.3; 1636 -0.3; 1751 -0.1; 1873 0.3; 2004 0.7; 2145 1.1; 2295 1.6; 2455 2.3; 2627 2.7; 2811 3.1; 3008 3.9; 3219 4.4; 3444 5.0; 3685 4.8; 3943 4.0; 4219 2.0; 4514 0.6; 4830 -0.4; 5168 -1.3; 5530 -2.4; 5917 -2.1; 6331 -0.2; 6775 1.4; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -2.4; 9502 -4.4; 10167 -4.6; 10879 -3.0; 11640 -0.8; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 137 Hz  | 2.08 | -1.3 dB |
| Peaking | 204 Hz  | 0.63 | -4.9 dB |
| Peaking | 3424 Hz | 1.77 | 5.2 dB  |
| Peaking | 5374 Hz | 4.39 | -3.6 dB |
| Peaking | 9950 Hz | 4.69 | -5.5 dB |
| Peaking | 16 Hz   | 0.31 | 1.4 dB  |
| Peaking | 36 Hz   | 0.99 | -1.3 dB |
| Peaking | 843 Hz  | 2.02 | 0.8 dB  |
| Peaking | 1542 Hz | 0.16 | -0.2 dB |
| Peaking | 7017 Hz | 7.17 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD3S/VSonic%20VSD3S.png)