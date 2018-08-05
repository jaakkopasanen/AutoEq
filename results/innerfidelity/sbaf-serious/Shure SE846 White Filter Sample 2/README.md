# Shure SE846 White Filter Sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -2.4; 22 -2.4; 23 -2.3; 25 -2.3; 26 -2.3; 28 -2.3; 30 -2.2; 32 -2.2; 35 -2.1; 37 -2.0; 40 -1.9; 42 -1.9; 45 -1.7; 49 -1.6; 52 -1.4; 56 -1.3; 59 -1.2; 64 -1.0; 68 -0.9; 73 -0.8; 78 -0.7; 83 -0.8; 89 -0.9; 95 -1.1; 102 -1.3; 109 -1.6; 117 -1.8; 125 -2.2; 134 -2.4; 143 -2.4; 153 -2.4; 164 -2.3; 175 -2.1; 188 -1.9; 201 -1.7; 215 -1.5; 230 -1.3; 246 -1.1; 263 -0.9; 282 -0.7; 301 -0.6; 323 -0.4; 345 -0.3; 369 -0.1; 395 -0.1; 423 0.1; 452 0.3; 484 0.2; 518 0.2; 554 0.4; 593 0.8; 635 0.8; 679 0.7; 726 0.8; 777 0.9; 832 0.7; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.5; 1529 -1.9; 1636 -2.2; 1751 -2.4; 1873 -2.4; 2004 -2.2; 2145 -1.8; 2295 -0.9; 2455 0.8; 2627 2.6; 2811 4.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.4; 4219 3.5; 4514 3.0; 4830 3.8; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.2; 7756 -0.7; 8299 -1.0; 8880 -0.3; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter Sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.72 | -2.4 dB |
| Peaking | 154 Hz  | 1.46 | -2.4 dB |
| Peaking | 1976 Hz | 1.84 | -4.3 dB |
| Peaking | 3233 Hz | 1.84 | 7.2 dB  |
| Peaking | 5803 Hz | 3.65 | 5.8 dB  |
| Peaking | 247 Hz  | 2.93 | -0.3 dB |
| Peaking | 710 Hz  | 1.52 | 1.0 dB  |
| Peaking | 1408 Hz | 3.49 | -0.6 dB |
| Peaking | 6668 Hz | 7.91 | 2.1 dB  |
| Peaking | 7964 Hz | 3.78 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20White%20Filter%20Sample%202/Shure%20SE846%20White%20Filter%20Sample%202.png)