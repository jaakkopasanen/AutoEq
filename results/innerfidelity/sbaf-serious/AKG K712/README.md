# AKG K712

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 5.5; 22 4.8; 23 4.5; 25 4.0; 26 3.8; 28 3.4; 30 3.0; 32 2.7; 35 2.3; 37 2.0; 40 1.7; 42 1.5; 45 1.2; 49 1.0; 52 0.8; 56 0.6; 59 0.4; 64 0.2; 68 0.0; 73 -0.2; 78 -0.4; 83 -0.7; 89 -1.0; 95 -1.4; 102 -1.8; 109 -2.1; 117 -2.4; 125 -2.8; 134 -3.0; 143 -3.1; 153 -3.3; 164 -3.7; 175 -3.5; 188 -3.2; 201 -3.2; 215 -3.3; 230 -3.4; 246 -3.5; 263 -3.5; 282 -3.3; 301 -3.1; 323 -2.9; 345 -2.6; 369 -2.5; 395 -2.3; 423 -2.1; 452 -2.0; 484 -1.8; 518 -1.4; 554 -0.9; 593 -0.6; 635 -0.4; 679 -0.4; 726 -0.2; 777 -0.1; 832 -0.3; 890 -0.0; 952 0.1; 1019 -0.0; 1090 0.1; 1167 0.4; 1248 0.4; 1336 -0.1; 1429 -0.8; 1529 -1.7; 1636 -2.6; 1751 -3.6; 1873 -4.5; 2004 -4.9; 2145 -4.7; 2295 -3.9; 2455 -2.2; 2627 0.2; 2811 2.1; 3008 2.7; 3219 2.7; 3444 2.3; 3685 0.8; 3943 -0.8; 4219 -2.7; 4514 -2.9; 4830 -1.9; 5168 -0.3; 5530 0.2; 5917 -0.6; 6331 -1.8; 6775 -3.0; 7249 -4.1; 7756 -4.9; 8299 -5.6; 8880 -5.2; 9502 -1.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.7; 17469 -4.5; 18692 -6.2; 20000 -3.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.54 | 6.6 dB  |
| Peaking | 195 Hz   | 0.64 | -3.8 dB |
| Peaking | 1989 Hz  | 4.14 | -5.5 dB |
| Peaking | 8075 Hz  | 3.3  | -6.0 dB |
| Peaking | 29456 Hz | 2.4  | -7.0 dB |
| Peaking | 1064 Hz  | 2.64 | 0.7 dB  |
| Peaking | 2364 Hz  | 5.15 | -2.8 dB |
| Peaking | 3098 Hz  | 2.61 | 4.1 dB  |
| Peaking | 4377 Hz  | 5.33 | -3.8 dB |
| Peaking | 13385 Hz | 1.34 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K712/AKG%20K712.png)