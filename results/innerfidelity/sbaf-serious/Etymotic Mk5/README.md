# Etymotic Mk5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 5.8; 89 5.4; 95 4.9; 102 4.3; 109 3.8; 117 3.2; 125 2.7; 134 2.2; 143 1.9; 153 1.7; 164 1.5; 175 1.4; 188 1.3; 201 1.3; 215 1.4; 230 1.4; 246 1.3; 263 1.4; 282 1.6; 301 1.6; 323 1.7; 345 1.7; 369 1.8; 395 1.7; 423 1.9; 452 2.0; 484 1.9; 518 1.9; 554 2.1; 593 2.2; 635 2.2; 679 2.0; 726 1.9; 777 1.8; 832 1.4; 890 0.9; 952 0.5; 1019 -0.2; 1090 -0.8; 1167 -1.4; 1248 -2.0; 1336 -2.8; 1429 -3.7; 1529 -4.6; 1636 -5.3; 1751 -5.8; 1873 -6.1; 2004 -6.3; 2145 -6.3; 2295 -6.1; 2455 -5.2; 2627 -4.0; 2811 -2.8; 3008 -1.3; 3219 -0.4; 3444 -0.3; 3685 -0.8; 3943 -0.7; 4219 -0.0; 4514 1.6; 4830 2.9; 5168 3.5; 5530 3.1; 5917 2.9; 6331 3.1; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Mk5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.41 | 6.7 dB  |
| Peaking | 654 Hz  | 0.91 | 2.5 dB  |
| Peaking | 2273 Hz | 2.7  | -3.8 dB |
| Peaking | 1713 Hz | 1.47 | -5.2 dB |
| Peaking | 5615 Hz | 2.18 | 4.0 dB  |
| Peaking | 15 Hz   | 0.99 | 1.8 dB  |
| Peaking | 38 Hz   | 1.15 | -1.1 dB |
| Peaking | 83 Hz   | 2.2  | 1.3 dB  |
| Peaking | 149 Hz  | 2.19 | -0.9 dB |
| Peaking | 8428 Hz | 5.48 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20Mk5/Etymotic%20Mk5.png)