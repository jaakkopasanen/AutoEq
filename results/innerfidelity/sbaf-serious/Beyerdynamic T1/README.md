# Beyerdynamic T1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 5.4; 22 4.8; 23 4.6; 25 4.1; 26 3.9; 28 3.5; 30 3.2; 32 3.0; 35 2.7; 37 2.5; 40 2.2; 42 2.1; 45 1.8; 49 1.6; 52 1.5; 56 1.7; 59 1.9; 64 1.7; 68 1.1; 73 0.4; 78 -0.0; 83 -0.3; 89 -0.7; 95 -1.0; 102 -1.3; 109 -1.5; 117 -1.6; 125 -1.9; 134 -2.1; 143 -2.2; 153 -2.3; 164 -2.4; 175 -2.5; 188 -2.5; 201 -2.6; 215 -2.5; 230 -2.5; 246 -2.5; 263 -2.5; 282 -2.4; 301 -2.3; 323 -2.2; 345 -2.0; 369 -1.9; 395 -1.8; 423 -1.6; 452 -1.5; 484 -1.3; 518 -1.2; 554 -1.1; 593 -0.8; 635 -0.5; 679 -0.4; 726 -0.3; 777 -0.0; 832 -0.2; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.4; 1167 0.7; 1248 0.5; 1336 0.2; 1429 0.3; 1529 -0.2; 1636 -0.8; 1751 -1.3; 1873 -1.5; 2004 -0.7; 2145 0.2; 2295 -0.4; 2455 -1.0; 2627 -0.6; 2811 -0.8; 3008 0.2; 3219 0.9; 3444 1.0; 3685 0.4; 3943 -0.1; 4219 -0.8; 4514 -0.8; 4830 2.3; 5168 5.9; 5530 2.0; 5917 -3.7; 6331 -5.2; 6775 -0.6; 7249 -2.5; 7756 -6.5; 8299 -9.8; 8880 -10.2; 9502 -7.3; 10167 -2.8; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.041303939534414dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 15 Hz    |  0.59 | 5.7 dB   |
| Peaking | 60 Hz    |  3.38 | 1.6 dB   |
| Peaking | 193 Hz   |  0.56 | -2.8 dB  |
| Peaking | 5170 Hz  | 11.41 | 7.4 dB   |
| Peaking | 8615 Hz  |  3.61 | -11.3 dB |
| Peaking | 1840 Hz  |  3.2  | -3.5 dB  |
| Peaking | 2044 Hz  |  1.09 | 2.6 dB   |
| Peaking | 2488 Hz  |  3.78 | -2.4 dB  |
| Peaking | 6131 Hz  | 12.88 | -5.3 dB  |
| Peaking | 11087 Hz |  5.25 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1/Beyerdynamic%20T1.png)