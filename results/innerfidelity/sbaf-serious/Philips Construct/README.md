# Philips Construct

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.1; 22 -1.1; 23 -1.1; 25 -1.1; 26 -1.1; 28 -1.2; 30 -1.2; 32 -1.1; 35 -1.1; 37 -1.0; 40 -0.9; 42 -0.8; 45 -0.7; 49 -0.4; 52 -0.2; 56 0.1; 59 0.4; 64 0.7; 68 0.7; 73 0.6; 78 0.1; 83 -0.6; 89 -1.2; 95 -1.6; 102 -1.6; 109 -1.8; 117 -2.0; 125 -2.3; 134 -2.3; 143 -2.0; 153 -1.5; 164 -0.9; 175 -0.7; 188 -0.1; 201 0.6; 215 1.4; 230 2.3; 246 3.2; 263 4.1; 282 4.9; 301 5.3; 323 5.4; 345 5.0; 369 4.4; 395 3.4; 423 2.3; 452 1.4; 484 0.5; 518 -0.2; 554 -0.5; 593 -0.8; 635 -1.0; 679 -1.1; 726 -1.2; 777 -0.9; 832 -0.8; 890 -0.7; 952 -0.4; 1019 0.2; 1090 0.9; 1167 1.7; 1248 2.5; 1336 3.0; 1429 3.5; 1529 3.9; 1636 4.5; 1751 5.2; 1873 5.9; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Construct ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.7  | -1.3 dB |
| Peaking | 134 Hz  | 1.66 | -2.9 dB |
| Peaking | 316 Hz  | 1.59 | 6.3 dB  |
| Peaking | 724 Hz  | 1.01 | -3.5 dB |
| Peaking | 2836 Hz | 0.53 | 6.9 dB  |
| Peaking | 67 Hz   | 5.09 | 1.2 dB  |
| Peaking | 1899 Hz | 4.23 | 0.9 dB  |
| Peaking | 2862 Hz | 2.08 | -0.9 dB |
| Peaking | 6026 Hz | 1.89 | 5.8 dB  |
| Peaking | 7683 Hz | 1.37 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Construct/Philips%20Construct.png)