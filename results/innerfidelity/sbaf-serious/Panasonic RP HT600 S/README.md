# Panasonic RP HT600 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.7; 22 1.5; 23 0.9; 25 -0.1; 26 -0.6; 28 -1.3; 30 -2.0; 32 -2.5; 35 -3.1; 37 -3.4; 40 -3.7; 42 -3.8; 45 -3.9; 49 -3.9; 52 -3.9; 56 -3.8; 59 -3.7; 64 -3.6; 68 -3.5; 73 -3.4; 78 -3.4; 83 -3.4; 89 -3.4; 95 -3.6; 102 -3.8; 109 -3.8; 117 -3.8; 125 -4.2; 134 -4.6; 143 -4.9; 153 -5.1; 164 -5.1; 175 -4.9; 188 -5.0; 201 -5.2; 215 -5.2; 230 -5.1; 246 -5.2; 263 -5.3; 282 -5.3; 301 -5.3; 323 -5.3; 345 -5.3; 369 -5.4; 395 -5.3; 423 -5.2; 452 -5.2; 484 -5.4; 518 -5.5; 554 -5.3; 593 -4.9; 635 -4.6; 679 -4.4; 726 -4.0; 777 -3.5; 832 -2.7; 890 -1.5; 952 -0.4; 1019 0.1; 1090 0.1; 1167 -0.1; 1248 -1.2; 1336 -3.0; 1429 -4.6; 1529 -6.0; 1636 -6.5; 1751 -6.2; 1873 -5.6; 2004 -3.8; 2145 -2.4; 2295 -1.4; 2455 -0.1; 2627 1.2; 2811 2.4; 3008 3.3; 3219 3.7; 3444 4.0; 3685 3.9; 3943 5.8; 4219 6.0; 4514 3.8; 4830 3.7; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -2.1; 8880 -6.1; 9502 -6.2; 10167 -1.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP HT600 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 211 Hz  | 0.26 | -5.3 dB |
| Peaking | 1746 Hz | 3.12 | -6.9 dB |
| Peaking | 3787 Hz | 1.31 | 4.9 dB  |
| Peaking | 5979 Hz | 2.8  | 5.0 dB  |
| Peaking | 9045 Hz | 4.99 | -8.3 dB |
| Peaking | 18 Hz   | 1.44 | 4.6 dB  |
| Peaking | 39 Hz   | 0.88 | -2.8 dB |
| Peaking | 89 Hz   | 0.9  | 1.4 dB  |
| Peaking | 874 Hz  | 0.79 | -2.5 dB |
| Peaking | 1029 Hz | 2.4  | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Panasonic%20RP%20HT600%20S/Panasonic%20RP%20HT600%20S.png)