# Plugged Crown

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.1; 22 0.8; 23 0.7; 25 0.4; 26 0.3; 28 0.1; 30 -0.1; 32 -0.3; 35 -0.5; 37 -0.7; 40 -0.9; 42 -1.0; 45 -1.2; 49 -1.3; 52 -1.5; 56 -1.6; 59 -1.7; 64 -1.9; 68 -2.0; 73 -2.1; 78 -2.1; 83 -2.1; 89 -2.1; 95 -2.3; 102 -3.3; 109 -4.2; 117 -5.0; 125 -5.8; 134 -6.3; 143 -6.5; 153 -6.7; 164 -6.4; 175 -6.8; 188 -7.3; 201 -7.4; 215 -7.3; 230 -6.9; 246 -7.0; 263 -7.2; 282 -7.0; 301 -6.9; 323 -6.5; 345 -5.9; 369 -5.2; 395 -4.5; 423 -3.2; 452 -2.2; 484 -1.8; 518 -0.9; 554 0.6; 593 1.9; 635 2.9; 679 3.3; 726 3.4; 777 2.9; 832 2.0; 890 1.1; 952 0.4; 1019 -0.0; 1090 -0.2; 1167 -0.9; 1248 -1.1; 1336 -1.1; 1429 -1.1; 1529 -1.0; 1636 -1.5; 1751 -2.1; 1873 -2.1; 2004 -1.6; 2145 -0.9; 2295 -0.1; 2455 1.0; 2627 1.7; 2811 2.6; 3008 3.8; 3219 4.6; 3444 5.6; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plugged Crown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 317 Hz  | 1.35 | -4.2 dB |
| Peaking | 170 Hz  | 0.83 | -6.2 dB |
| Peaking | 683 Hz  | 2.32 | 5.0 dB  |
| Peaking | 1829 Hz | 1.55 | -3.3 dB |
| Peaking | 4285 Hz | 1.12 | 7.2 dB  |
| Peaking | 13 Hz   | 0.7  | 1.7 dB  |
| Peaking | 48 Hz   | 2.04 | -0.7 dB |
| Peaking | 7720 Hz | 1.04 | -1.5 dB |
| Peaking | 6348 Hz | 3.48 | 3.9 dB  |
| Peaking | 7492 Hz | 3.29 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Plugged%20Crown/Plugged%20Crown.png)