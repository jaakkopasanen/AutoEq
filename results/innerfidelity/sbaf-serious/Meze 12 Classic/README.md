# Meze 12 Classic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 1.2; 22 0.7; 23 0.4; 25 -0.1; 26 -0.3; 28 -0.6; 30 -0.9; 32 -1.1; 35 -1.4; 37 -1.6; 40 -1.9; 42 -2.1; 45 -2.3; 49 -2.5; 52 -2.6; 56 -2.8; 59 -2.9; 64 -3.0; 68 -3.2; 73 -3.5; 78 -3.7; 83 -3.9; 89 -4.3; 95 -4.7; 102 -5.3; 109 -5.7; 117 -6.1; 125 -6.7; 134 -7.0; 143 -7.3; 153 -7.4; 164 -7.4; 175 -7.3; 188 -7.2; 201 -7.0; 215 -6.7; 230 -6.5; 246 -6.2; 263 -5.9; 282 -5.5; 301 -5.2; 323 -4.7; 345 -4.4; 369 -4.0; 395 -3.5; 423 -3.0; 452 -2.6; 484 -2.3; 518 -1.9; 554 -1.4; 593 -0.8; 635 -0.4; 679 -0.0; 726 0.4; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.8; 1529 -2.4; 1636 -2.8; 1751 -3.2; 1873 -3.5; 2004 -3.9; 2145 -4.2; 2295 -4.3; 2455 -3.8; 2627 -2.9; 2811 -1.5; 3008 0.3; 3219 2.0; 3444 3.3; 3685 3.3; 3943 2.7; 4219 1.3; 4514 0.1; 4830 -0.1; 5168 0.8; 5530 1.6; 5917 3.0; 6331 4.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 12 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 412 Hz  | 1.38 | -1.1 dB |
| Peaking | 173 Hz  | 0.53 | -7.6 dB |
| Peaking | 2129 Hz | 0.84 | -9.4 dB |
| Peaking | 3449 Hz | 3.78 | 4.6 dB  |
| Peaking | 1903 Hz | 0.29 | 5.0 dB  |
| Peaking | 12 Hz   | 0.56 | 2.0 dB  |
| Peaking | 39 Hz   | 1.57 | -1.2 dB |
| Peaking | 4765 Hz | 6.66 | -1.5 dB |
| Peaking | 6458 Hz | 4.78 | 4.6 dB  |
| Peaking | 8149 Hz | 1.44 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2012%20Classic/Meze%2012%20Classic.png)