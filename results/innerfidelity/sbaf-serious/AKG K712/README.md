# AKG K712

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 5.5; 22 4.8; 23 4.5; 25 4.0; 26 3.8; 28 3.3; 30 3.0; 32 2.6; 35 2.2; 37 1.9; 40 1.6; 42 1.3; 45 1.1; 49 0.7; 52 0.5; 56 0.2; 59 0.0; 64 -0.3; 68 -0.6; 73 -0.9; 78 -1.2; 83 -1.5; 89 -1.8; 95 -2.1; 102 -2.4; 109 -2.5; 117 -2.6; 125 -2.9; 134 -2.9; 143 -2.9; 153 -3.1; 164 -3.5; 175 -3.2; 188 -3.0; 201 -3.1; 215 -3.2; 230 -3.3; 246 -3.4; 263 -3.4; 282 -3.2; 301 -3.1; 323 -2.8; 345 -2.6; 369 -2.4; 395 -2.3; 423 -2.1; 452 -2.0; 484 -1.8; 518 -1.4; 554 -0.9; 593 -0.6; 635 -0.4; 679 -0.4; 726 -0.2; 777 -0.1; 832 -0.3; 890 -0.0; 952 0.1; 1019 -0.0; 1090 0.1; 1167 0.4; 1248 0.4; 1336 -0.1; 1429 -0.8; 1529 -1.7; 1636 -2.6; 1751 -3.6; 1873 -4.5; 2004 -4.9; 2145 -4.7; 2295 -3.9; 2455 -2.2; 2627 0.2; 2811 2.1; 3008 2.7; 3219 2.7; 3444 2.3; 3685 0.8; 3943 -0.8; 4219 -2.7; 4514 -2.9; 4830 -1.9; 5168 -0.3; 5530 0.2; 5917 -0.6; 6331 -1.8; 6775 -3.0; 7249 -4.1; 7756 -4.9; 8299 -5.6; 8880 -5.2; 9502 -1.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.7; 17469 -4.5; 18692 -6.2; 20000 -3.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.551930942246704dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.71 | 5.8 dB  |
| Peaking | 186 Hz   | 0.55 | -3.6 dB |
| Peaking | 1990 Hz  | 4.16 | -5.5 dB |
| Peaking | 8072 Hz  | 3.3  | -6.0 dB |
| Peaking | 18816 Hz | 2.41 | -7.0 dB |
| Peaking | 985 Hz   | 2.06 | 0.7 dB  |
| Peaking | 2337 Hz  | 5.19 | -2.8 dB |
| Peaking | 3084 Hz  | 2.62 | 4.1 dB  |
| Peaking | 4319 Hz  | 5.38 | -3.8 dB |
| Peaking | 11164 Hz | 2.95 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K712/AKG%20K712.png)