# Fischer Audio SBA-03

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.9; 22 4.7; 23 4.6; 25 4.4; 26 4.4; 28 4.3; 30 4.2; 32 4.1; 35 3.9; 37 3.8; 40 3.7; 42 3.6; 45 3.5; 49 3.5; 52 3.4; 56 3.3; 59 3.2; 64 3.1; 68 3.0; 73 2.8; 78 2.6; 83 2.4; 89 1.9; 95 1.4; 102 0.8; 109 0.3; 117 -0.2; 125 -0.9; 134 -1.4; 143 -1.7; 153 -1.9; 164 -2.1; 175 -2.2; 188 -2.2; 201 -2.3; 215 -2.2; 230 -2.2; 246 -2.2; 263 -2.0; 282 -2.0; 301 -1.9; 323 -1.7; 345 -1.6; 369 -1.5; 395 -1.3; 423 -1.0; 452 -0.8; 484 -0.8; 518 -0.6; 554 -0.2; 593 0.1; 635 0.2; 679 0.1; 726 0.3; 777 0.5; 832 0.5; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.7; 1636 -2.1; 1751 -2.3; 1873 -2.5; 2004 -2.7; 2145 -3.2; 2295 -3.9; 2455 -4.2; 2627 -3.9; 2811 -2.0; 3008 1.5; 3219 4.5; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.6; 4514 3.5; 4830 1.2; 5168 -1.1; 5530 -4.6; 5917 -3.4; 6331 0.8; 6775 3.2; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -2.1; 9502 -0.7; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio SBA-03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 26 Hz   |  1.11 | 4.8 dB   |
| Peaking | 62 Hz   |  2.32 | 2.8 dB   |
| Peaking | 2636 Hz |  1.46 | -10.2 dB |
| Peaking | 3451 Hz |  1.56 | 12.3 dB  |
| Peaking | 5548 Hz |  6.99 | -7.5 dB  |
| Peaking | 90 Hz   |  1.75 | 2.0 dB   |
| Peaking | 194 Hz  |  0.65 | -2.7 dB  |
| Peaking | 769 Hz  |  1.86 | 1.1 dB   |
| Peaking | 6763 Hz | 10.5  | 3.2 dB   |
| Peaking | 8787 Hz |  6.42 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20SBA-03/Fischer%20Audio%20SBA-03.png)