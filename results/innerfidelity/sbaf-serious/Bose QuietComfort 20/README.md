# Bose QuietComfort 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.1; 22 2.5; 23 1.8; 25 0.7; 26 0.3; 28 -0.3; 30 -0.6; 32 -0.8; 35 -0.9; 37 -0.8; 40 -0.6; 42 -0.5; 45 -0.3; 49 -0.1; 52 0.1; 56 0.2; 59 0.2; 64 0.1; 68 -0.0; 73 -0.3; 78 -0.6; 83 -0.9; 89 -1.4; 95 -1.7; 102 -2.3; 109 -2.4; 117 -2.7; 125 -2.9; 134 -3.0; 143 -3.1; 153 -3.1; 164 -3.1; 175 -3.0; 188 -3.1; 201 -3.1; 215 -2.9; 230 -2.9; 246 -2.7; 263 -2.7; 282 -2.4; 301 -2.3; 323 -2.3; 345 -2.2; 369 -2.2; 395 -2.2; 423 -2.2; 452 -2.2; 484 -2.1; 518 -2.0; 554 -1.6; 593 -1.2; 635 -1.1; 679 -1.3; 726 -1.1; 777 -0.6; 832 -0.2; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -2.0; 1336 -3.1; 1429 -4.2; 1529 -5.4; 1636 -6.0; 1751 -5.6; 1873 -4.6; 2004 -3.7; 2145 -2.9; 2295 -2.3; 2455 -1.6; 2627 -1.1; 2811 -0.3; 3008 1.1; 3219 2.1; 3444 2.4; 3685 1.4; 3943 -0.5; 4219 -2.5; 4514 -1.8; 4830 1.4; 5168 5.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 2.4; 7249 -2.2; 7756 -2.3; 8299 -0.6; 8880 0.0; 9502 -0.3; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-9.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 167 Hz  | 0.89 | -3.2 dB |
| Peaking | 421 Hz  | 1.66 | -1.6 dB |
| Peaking | 1692 Hz | 2.32 | -6.1 dB |
| Peaking | 3301 Hz | 7.3  | 3.1 dB  |
| Peaking | 5777 Hz | 5.15 | 7.3 dB  |
| Peaking | 64 Hz   | 3.79 | 0.8 dB  |
| Peaking | 960 Hz  | 5.15 | 1.3 dB  |
| Peaking | 4376 Hz | 5.65 | -5.9 dB |
| Peaking | 4792 Hz | 2.12 | 2.7 dB  |
| Peaking | 7539 Hz | 7.58 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)