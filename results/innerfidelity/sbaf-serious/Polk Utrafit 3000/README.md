# Polk Utrafit 3000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -9.3; 22 -9.3; 23 -9.3; 25 -9.3; 26 -9.3; 28 -9.4; 30 -9.4; 32 -9.4; 35 -9.5; 37 -9.5; 40 -9.6; 42 -9.6; 45 -9.6; 49 -9.7; 52 -9.8; 56 -9.9; 59 -9.9; 64 -10.1; 68 -10.2; 73 -10.3; 78 -10.5; 83 -10.6; 89 -10.8; 95 -10.9; 102 -10.9; 109 -10.9; 117 -10.8; 125 -10.8; 134 -10.8; 143 -10.7; 153 -10.6; 164 -10.5; 175 -10.2; 188 -9.9; 201 -9.7; 215 -9.4; 230 -9.0; 246 -8.7; 263 -8.3; 282 -7.8; 301 -7.4; 323 -7.0; 345 -6.5; 369 -6.0; 395 -5.6; 423 -4.9; 452 -4.4; 484 -4.0; 518 -3.5; 554 -2.9; 593 -2.1; 635 -1.6; 679 -1.2; 726 -0.9; 777 -0.5; 832 -0.4; 890 -0.4; 952 -0.2; 1019 0.2; 1090 0.3; 1167 0.4; 1248 0.5; 1336 0.3; 1429 -0.0; 1529 -0.3; 1636 -0.5; 1751 -0.4; 1873 -0.1; 2004 0.2; 2145 0.6; 2295 1.4; 2455 2.6; 2627 3.6; 2811 4.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.1; 4514 1.7; 4830 0.8; 5168 2.8; 5530 5.6; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999259688dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Utrafit 3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.19 | -8.8 dB |
| Peaking | 147 Hz   | 0.64 | -6.0 dB |
| Peaking | 313 Hz   | 1.13 | -3.1 dB |
| Peaking | 3331 Hz  | 2.19 | 6.7 dB  |
| Peaking | 6037 Hz  | 4.62 | 6.0 dB  |
| Peaking | 1205 Hz  | 1.41 | 1.6 dB  |
| Peaking | 1670 Hz  | 1.36 | -1.7 dB |
| Peaking | 2665 Hz  | 4.52 | 1.1 dB  |
| Peaking | 8168 Hz  | 5.32 | -0.7 dB |
| Peaking | 10582 Hz | 1.98 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Utrafit%203000/Polk%20Utrafit%203000.png)