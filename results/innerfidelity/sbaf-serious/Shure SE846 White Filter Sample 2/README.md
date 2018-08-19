# Shure SE846 White Filter Sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.4; 22 -2.4; 23 -2.4; 25 -2.4; 26 -2.4; 28 -2.4; 30 -2.4; 32 -2.4; 35 -2.4; 37 -2.4; 40 -2.4; 42 -2.3; 45 -2.3; 49 -2.3; 52 -2.3; 56 -2.3; 59 -2.3; 64 -2.3; 68 -2.3; 73 -2.3; 78 -2.4; 83 -2.4; 89 -2.5; 95 -2.5; 102 -2.4; 109 -2.3; 117 -2.2; 125 -2.2; 134 -2.1; 143 -2.0; 153 -1.9; 164 -1.8; 175 -1.6; 188 -1.5; 201 -1.3; 215 -1.1; 230 -0.9; 246 -0.8; 263 -0.7; 282 -0.5; 301 -0.4; 323 -0.3; 345 -0.2; 369 -0.1; 395 -0.0; 423 0.2; 452 0.3; 484 0.2; 518 0.3; 554 0.4; 593 0.8; 635 0.8; 679 0.7; 726 0.8; 777 0.9; 832 0.7; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.5; 1529 -1.9; 1636 -2.2; 1751 -2.4; 1873 -2.4; 2004 -2.2; 2145 -1.8; 2295 -0.9; 2455 0.8; 2627 2.6; 2811 4.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.4; 4219 3.5; 4514 3.0; 4830 3.8; 5168 5.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.2; 7756 -0.7; 8299 -1.0; 8880 -0.3; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999259689dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter Sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.19 | -2.5 dB |
| Peaking | 720 Hz  | 0.6  | 1.5 dB  |
| Peaking | 2001 Hz | 1.1  | -4.9 dB |
| Peaking | 3187 Hz | 1.75 | 8.4 dB  |
| Peaking | 5798 Hz | 3.6  | 5.8 dB  |
| Peaking | 60 Hz   | 1.37 | 0.3 dB  |
| Peaking | 96 Hz   | 1.88 | -0.3 dB |
| Peaking | 6665 Hz | 7.9  | 2.1 dB  |
| Peaking | 7961 Hz | 3.86 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20White%20Filter%20Sample%202/Shure%20SE846%20White%20Filter%20Sample%202.png)