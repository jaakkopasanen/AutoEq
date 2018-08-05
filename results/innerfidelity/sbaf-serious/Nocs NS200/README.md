# Nocs NS200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 -8.6; 22 -8.3; 23 -8.2; 25 -8.0; 26 -7.8; 28 -7.6; 30 -7.4; 32 -7.1; 35 -6.8; 37 -6.6; 40 -6.4; 42 -6.2; 45 -5.9; 49 -5.6; 52 -5.4; 56 -5.1; 59 -4.9; 64 -4.7; 68 -4.5; 73 -4.4; 78 -4.4; 83 -4.4; 89 -4.5; 95 -4.8; 102 -5.1; 109 -5.4; 117 -5.7; 125 -6.1; 134 -6.3; 143 -6.4; 153 -6.5; 164 -6.4; 175 -6.3; 188 -6.1; 201 -5.9; 215 -5.6; 230 -5.4; 246 -5.1; 263 -4.8; 282 -4.4; 301 -4.2; 323 -3.8; 345 -3.5; 369 -3.1; 395 -2.8; 423 -2.3; 452 -2.0; 484 -1.7; 518 -1.4; 554 -0.9; 593 -0.4; 635 -0.1; 679 -0.0; 726 0.3; 777 0.5; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.3; 1429 -1.8; 1529 -2.2; 1636 -2.6; 1751 -3.0; 1873 -3.1; 2004 -3.3; 2145 -3.5; 2295 -3.7; 2455 -3.4; 2627 -3.1; 2811 -2.1; 3008 -0.1; 3219 1.7; 3444 3.3; 3685 3.8; 3943 3.4; 4219 1.7; 4514 0.2; 4830 -0.9; 5168 -1.7; 5530 -3.7; 5917 -5.7; 6331 -4.6; 6775 -2.2; 7249 -0.3; 7756 0.2; 8299 0.0; 8880 -0.3; 9502 -0.9; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.4dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.77 | -7.9 dB |
| Peaking | 31 Hz   | 0.58 | -4.7 dB |
| Peaking | 174 Hz  | 0.73 | -6.1 dB |
| Peaking | 2057 Hz | 2.69 | -4.0 dB |
| Peaking | 6004 Hz | 6.5  | -6.4 dB |
| Peaking | 775 Hz  | 3.24 | 1.4 dB  |
| Peaking | 2641 Hz | 4.06 | -1.3 dB |
| Peaking | 2688 Hz | 3.52 | -1.5 dB |
| Peaking | 3652 Hz | 2.78 | 5.2 dB  |
| Peaking | 5024 Hz | 2.88 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS200/Nocs%20NS200.png)