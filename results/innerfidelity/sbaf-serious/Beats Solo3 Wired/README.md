# Beats Solo3 Wired

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 10 -84; 20 -5.7; 22 -5.9; 23 -6.0; 25 -6.1; 26 -6.1; 28 -6.2; 30 -6.2; 32 -6.2; 35 -6.3; 37 -6.3; 40 -6.3; 42 -6.2; 45 -6.2; 49 -6.2; 52 -6.3; 56 -6.2; 59 -6.2; 64 -6.2; 68 -6.2; 73 -6.2; 78 -6.3; 83 -6.3; 89 -6.5; 95 -6.7; 102 -7.2; 109 -7.5; 117 -7.6; 125 -7.9; 134 -8.0; 143 -8.3; 153 -8.4; 164 -8.1; 175 -8.1; 188 -8.2; 201 -7.9; 215 -7.7; 230 -7.3; 246 -7.0; 263 -6.5; 282 -5.9; 301 -5.4; 323 -4.7; 345 -4.3; 369 -3.8; 395 -2.9; 423 -2.3; 452 -2.1; 484 -2.0; 518 -1.8; 554 -1.2; 593 -0.5; 635 -0.1; 679 0.2; 726 0.4; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 -0.4; 1248 -0.6; 1336 -0.9; 1429 -1.3; 1529 -1.5; 1636 -1.7; 1751 -1.8; 1873 -1.4; 2004 -1.0; 2145 -0.9; 2295 -1.0; 2455 -0.8; 2627 -1.0; 2811 -1.5; 3008 -1.8; 3219 -2.4; 3444 -2.7; 3685 -2.0; 3943 -0.4; 4219 -0.8; 4514 -2.5; 4830 -1.9; 5168 0.1; 5530 2.1; 5917 2.6; 6331 1.6; 6775 1.6; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.1; 18692 -0.9; 20000 -1.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.21 | -5.9 dB |
| Peaking | 190 Hz  | 0.87 | -6.1 dB |
| Peaking | 1677 Hz | 4.58 | -1.4 dB |
| Peaking | 4255 Hz | 1.12 | -2.6 dB |
| Peaking | 5961 Hz | 2.8  | 4.1 dB  |
| Peaking | 193 Hz  | 1.99 | 1.8 dB  |
| Peaking | 217 Hz  | 0.99 | -1.4 dB |
| Peaking | 748 Hz  | 2.15 | 1.6 dB  |
| Peaking | 4051 Hz | 2.78 | -2.2 dB |
| Peaking | 3969 Hz | 7.46 | 4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo3%20Wired/Beats%20Solo3%20Wired.png)