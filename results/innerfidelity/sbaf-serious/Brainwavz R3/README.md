# Brainwavz R3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.3; 22 4.0; 23 3.9; 25 3.8; 26 3.7; 28 3.6; 30 3.4; 32 3.3; 35 3.2; 37 3.1; 40 3.0; 42 2.9; 45 2.8; 49 2.7; 52 2.7; 56 2.5; 59 2.4; 64 2.3; 68 2.2; 73 1.9; 78 1.7; 83 1.4; 89 1.0; 95 0.5; 102 -0.2; 109 -0.7; 117 -1.3; 125 -2.0; 134 -2.5; 143 -2.8; 153 -3.1; 164 -3.3; 175 -3.4; 188 -3.3; 201 -3.4; 215 -3.3; 230 -3.2; 246 -3.2; 263 -3.1; 282 -3.0; 301 -2.9; 323 -2.7; 345 -2.6; 369 -2.4; 395 -2.2; 423 -1.9; 452 -1.7; 484 -1.6; 518 -1.4; 554 -1.0; 593 -0.6; 635 -0.4; 679 -0.3; 726 -0.1; 777 0.2; 832 0.2; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 0.5; 1336 -0.3; 1429 -0.8; 1529 -1.0; 1636 -1.3; 1751 -2.0; 1873 -1.9; 2004 -2.0; 2145 -1.6; 2295 -0.3; 2455 2.1; 2627 4.7; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 4.3; 4830 5.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz R3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.3  | 4.2 dB  |
| Peaking | 81 Hz   | 0.99 | 3.0 dB  |
| Peaking | 163 Hz  | 0.51 | -4.6 dB |
| Peaking | 3335 Hz | 2.51 | 6.3 dB  |
| Peaking | 5540 Hz | 2.45 | 5.9 dB  |
| Peaking | 866 Hz  | 1.67 | 0.9 dB  |
| Peaking | 2006 Hz | 2.26 | -3.4 dB |
| Peaking | 2696 Hz | 5.97 | 3.7 dB  |
| Peaking | 6535 Hz | 7.04 | 2.3 dB  |
| Peaking | 7826 Hz | 2.47 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20R3/Brainwavz%20R3.png)