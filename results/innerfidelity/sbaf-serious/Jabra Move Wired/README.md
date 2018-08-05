# Jabra Move Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.8; 22 -3.9; 23 -4.0; 25 -4.0; 26 -4.1; 28 -4.1; 30 -4.0; 32 -4.0; 35 -3.8; 37 -3.7; 40 -3.4; 42 -3.1; 45 -2.5; 49 -1.5; 52 -1.4; 56 -2.1; 59 -2.5; 64 -2.4; 68 -2.1; 73 -1.5; 78 -0.9; 83 -0.7; 89 -1.4; 95 -2.4; 102 -3.3; 109 -3.9; 117 -3.9; 125 -3.8; 134 -4.3; 143 -4.3; 153 -3.9; 164 -3.2; 175 -3.5; 188 -2.8; 201 -2.0; 215 -1.3; 230 -0.4; 246 -0.3; 263 -1.0; 282 -1.5; 301 -1.9; 323 -2.1; 345 -1.8; 369 -1.8; 395 -1.7; 423 -1.7; 452 -1.8; 484 -2.0; 518 -2.1; 554 -2.1; 593 -2.0; 635 -1.9; 679 -1.7; 726 -1.2; 777 -0.7; 832 -1.3; 890 -1.3; 952 -0.6; 1019 0.3; 1090 0.6; 1167 -0.1; 1248 -0.0; 1336 0.1; 1429 0.1; 1529 0.2; 1636 0.3; 1751 0.9; 1873 1.5; 2004 2.3; 2145 3.0; 2295 3.7; 2455 4.5; 2627 5.1; 2811 4.7; 3008 4.6; 3219 5.4; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 3.5; 4830 5.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Move Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.83 | -4.3 dB |
| Peaking | 135 Hz  | 1.68 | -4.1 dB |
| Peaking | 530 Hz  | 0.91 | -2.1 dB |
| Peaking | 3326 Hz | 1.21 | 5.9 dB  |
| Peaking | 5790 Hz | 3.45 | 4.8 dB  |
| Peaking | 8 Hz    | 1.19 | -0.7 dB |
| Peaking | 1613 Hz | 4.91 | -0.8 dB |
| Peaking | 2358 Hz | 5.53 | 0.9 dB  |
| Peaking | 8403 Hz | 3.7  | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jabra%20Move%20Wired/Jabra%20Move%20Wired.png)