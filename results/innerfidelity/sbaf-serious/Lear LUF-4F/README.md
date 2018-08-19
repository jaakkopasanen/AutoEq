# Lear LUF-4F

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.4; 22 1.1; 23 1.0; 25 0.8; 26 0.7; 28 0.5; 30 0.3; 32 0.1; 35 -0.1; 37 -0.2; 40 -0.4; 42 -0.6; 45 -0.8; 49 -1.0; 52 -1.2; 56 -1.4; 59 -1.6; 64 -1.9; 68 -2.1; 73 -2.3; 78 -2.6; 83 -2.8; 89 -3.0; 95 -3.2; 102 -3.3; 109 -3.2; 117 -3.2; 125 -3.2; 134 -3.1; 143 -2.9; 153 -2.6; 164 -2.3; 175 -1.8; 188 -1.4; 201 -1.0; 215 -0.5; 230 0.0; 246 0.4; 263 0.8; 282 1.1; 301 1.4; 323 1.5; 345 1.7; 369 1.8; 395 1.8; 423 1.9; 452 1.9; 484 1.8; 518 1.7; 554 1.9; 593 2.0; 635 1.9; 679 1.8; 726 1.6; 777 1.6; 832 1.3; 890 0.9; 952 0.5; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.9; 1336 -2.7; 1429 -3.8; 1529 -4.8; 1636 -5.6; 1751 -6.2; 1873 -6.5; 2004 -6.6; 2145 -6.6; 2295 -6.3; 2455 -5.4; 2627 -4.0; 2811 -2.4; 3008 -0.4; 3219 0.3; 3444 -0.1; 3685 -0.1; 3943 0.9; 4219 3.9; 4514 6.0; 4830 6.0; 5168 2.3; 5530 -0.3; 5917 0.6; 6331 1.8; 6775 1.8; 7249 0.4; 7756 -2.7; 8299 -4.0; 8880 -2.0; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999640354261135dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear LUF-4F ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 125 Hz  |  0.71 | -5.5 dB |
| Peaking | 357 Hz  |  0.28 | 3.2 dB  |
| Peaking | 1901 Hz |  1.38 | -8.2 dB |
| Peaking | 4590 Hz |  4.02 | 7.2 dB  |
| Peaking | 8316 Hz |  8.11 | -4.7 dB |
| Peaking | 22 Hz   |  1.75 | 1.5 dB  |
| Peaking | 2434 Hz |  6.52 | -1.3 dB |
| Peaking | 3110 Hz |  7.79 | 2.1 dB  |
| Peaking | 5482 Hz | 11.25 | -2.3 dB |
| Peaking | 6592 Hz |  7.43 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lear%20LUF-4F/Lear%20LUF-4F.png)