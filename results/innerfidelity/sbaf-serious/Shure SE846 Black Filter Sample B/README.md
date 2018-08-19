# Shure SE846 Black Filter Sample B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.1; 23 -5.1; 25 -5.1; 26 -5.1; 28 -5.1; 30 -5.0; 32 -5.0; 35 -5.0; 37 -4.9; 40 -4.9; 42 -4.9; 45 -4.9; 49 -4.8; 52 -4.8; 56 -4.8; 59 -4.8; 64 -4.8; 68 -4.8; 73 -4.8; 78 -4.8; 83 -4.8; 89 -4.9; 95 -4.9; 102 -4.8; 109 -4.7; 117 -4.6; 125 -4.5; 134 -4.4; 143 -4.3; 153 -4.2; 164 -4.0; 175 -3.8; 188 -3.6; 201 -3.5; 215 -3.2; 230 -3.0; 246 -2.9; 263 -2.7; 282 -2.5; 301 -2.3; 323 -2.1; 345 -1.9; 369 -1.7; 395 -1.6; 423 -1.3; 452 -1.1; 484 -1.1; 518 -0.9; 554 -0.6; 593 -0.2; 635 -0.1; 679 0.0; 726 0.2; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.3; 1336 -0.5; 1429 -0.7; 1529 -0.8; 1636 -0.8; 1751 -0.6; 1873 -0.2; 2004 0.3; 2145 0.9; 2295 1.6; 2455 3.2; 2627 4.7; 2811 5.9; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999859593dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black Filter Sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.34 | -4.7 dB |
| Peaking | 125 Hz  | 0.46 | -3.8 dB |
| Peaking | 3129 Hz | 2.53 | 5.0 dB  |
| Peaking | 5519 Hz | 1.33 | 6.8 dB  |
| Peaking | 8064 Hz | 1.88 | -2.9 dB |
| Peaking | 800 Hz  | 1.86 | 1.0 dB  |
| Peaking | 1803 Hz | 0.94 | -1.4 dB |
| Peaking | 2626 Hz | 5.55 | 2.0 dB  |
| Peaking | 4050 Hz | 4.92 | 1.2 dB  |
| Peaking | 5218 Hz | 9.14 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20Black%20Filter%20Sample%20B/Shure%20SE846%20Black%20Filter%20Sample%20B.png)