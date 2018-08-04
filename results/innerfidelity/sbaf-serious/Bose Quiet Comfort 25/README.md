# Bose Quiet Comfort 25

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.3; 23 -1.5; 25 -1.6; 26 -1.6; 28 -1.6; 30 -1.4; 32 -1.1; 35 -0.7; 37 -0.5; 40 -0.4; 42 -0.4; 45 -0.5; 49 -0.6; 52 -0.8; 56 -0.9; 59 -1.0; 64 -1.0; 68 -1.0; 73 -0.9; 78 -0.9; 83 -0.8; 89 -0.8; 95 -0.8; 102 -0.9; 109 -1.0; 117 -1.1; 125 -1.3; 134 -1.4; 143 -1.5; 153 -1.5; 164 -1.4; 175 -1.0; 188 -1.0; 201 -1.1; 215 -0.9; 230 -0.7; 246 -0.6; 263 -0.5; 282 -0.4; 301 -0.2; 323 0.0; 345 0.3; 369 0.5; 395 0.7; 423 1.1; 452 1.3; 484 1.4; 518 1.5; 554 1.8; 593 2.0; 635 2.0; 679 1.8; 726 1.8; 777 1.6; 832 1.2; 890 0.7; 952 0.3; 1019 0.1; 1090 0.5; 1167 0.4; 1248 0.3; 1336 -0.6; 1429 -0.5; 1529 -2.1; 1636 -3.4; 1751 -4.7; 1873 -5.7; 2004 -6.1; 2145 -5.4; 2295 -4.7; 2455 -4.1; 2627 -3.6; 2811 -4.1; 3008 -4.9; 3219 -6.0; 3444 -6.1; 3685 -4.7; 3943 -2.4; 4219 0.0; 4514 2.1; 4830 4.4; 5168 5.9; 5530 5.9; 5917 2.2; 6331 0.7; 6775 2.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose Quiet Comfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 133 Hz  | 0.2  | -1.3 dB |
| Peaking | 611 Hz  | 0.87 | 2.8 dB  |
| Peaking | 1989 Hz | 2.54 | -6.0 dB |
| Peaking | 3385 Hz | 2.67 | -6.5 dB |
| Peaking | 5151 Hz | 3.24 | 7.4 dB  |
| Peaking | 23 Hz   | 2.36 | -0.9 dB |
| Peaking | 152 Hz  | 5.14 | -0.5 dB |
| Peaking | 962 Hz  | 4.84 | -1.0 dB |
| Peaking | 1341 Hz | 1.55 | 0.8 dB  |
| Peaking | 1672 Hz | 5.36 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20Quiet%20Comfort%2025/Bose%20Quiet%20Comfort%2025.png)