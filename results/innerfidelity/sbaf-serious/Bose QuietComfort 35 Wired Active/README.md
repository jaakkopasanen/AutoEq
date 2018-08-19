# Bose QuietComfort 35 Wired Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -1.6; 22 -1.3; 23 -1.3; 25 -1.2; 26 -1.2; 28 -1.3; 30 -1.5; 32 -1.7; 35 -1.9; 37 -2.0; 40 -2.2; 42 -2.2; 45 -2.3; 49 -2.2; 52 -2.2; 56 -2.1; 59 -2.0; 64 -1.9; 68 -1.8; 73 -1.7; 78 -1.8; 83 -1.8; 89 -1.9; 95 -2.0; 102 -2.0; 109 -1.9; 117 -1.8; 125 -1.7; 134 -1.6; 143 -1.6; 153 -1.6; 164 -1.3; 175 -1.2; 188 -1.2; 201 -1.2; 215 -1.0; 230 -0.8; 246 -0.8; 263 -0.6; 282 -0.4; 301 -0.2; 323 -0.1; 345 0.1; 369 0.2; 395 0.4; 423 0.5; 452 0.6; 484 0.5; 518 0.5; 554 0.6; 593 0.8; 635 0.7; 679 0.6; 726 0.5; 777 0.5; 832 0.3; 890 0.0; 952 -0.0; 1019 0.0; 1090 0.2; 1167 0.7; 1248 0.9; 1336 0.2; 1429 0.1; 1529 0.5; 1636 -0.4; 1751 -1.1; 1873 -1.8; 2004 -2.0; 2145 -2.0; 2295 -2.0; 2455 -2.3; 2627 -2.4; 2811 -2.9; 3008 -2.0; 3219 -1.0; 3444 -0.7; 3685 -1.9; 3943 -2.1; 4219 -2.0; 4514 -1.2; 4830 0.7; 5168 4.7; 5530 4.4; 5917 -0.6; 6331 0.1; 6775 1.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.790140417616161dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 44 Hz   |  0.66 | -2.0 dB |
| Peaking | 128 Hz  |  1.17 | -1.3 dB |
| Peaking | 2510 Hz |  2.3  | -2.7 dB |
| Peaking | 4142 Hz |  4.32 | -2.2 dB |
| Peaking | 5309 Hz |  8.69 | 6.6 dB  |
| Peaking | 544 Hz  |  1.75 | 0.8 dB  |
| Peaking | 1446 Hz |  1.73 | 0.9 dB  |
| Peaking | 1874 Hz |  4.88 | -1.4 dB |
| Peaking | 6083 Hz | 12.06 | -2.0 dB |
| Peaking | 7013 Hz |  7.51 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wired%20Active/Bose%20QuietComfort%2035%20Wired%20Active.png)