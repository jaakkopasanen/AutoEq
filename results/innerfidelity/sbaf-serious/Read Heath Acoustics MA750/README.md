# Read Heath Acoustics MA750

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 -5.8; 22 -5.9; 23 -5.9; 25 -5.9; 26 -5.9; 28 -5.9; 30 -5.9; 32 -5.9; 35 -6.0; 37 -6.0; 40 -5.9; 42 -5.9; 45 -5.9; 49 -5.9; 52 -5.9; 56 -5.9; 59 -5.9; 64 -6.0; 68 -6.1; 73 -6.2; 78 -6.3; 83 -6.3; 89 -6.4; 95 -6.6; 102 -6.6; 109 -6.6; 117 -6.5; 125 -6.6; 134 -6.6; 143 -6.6; 153 -6.6; 164 -6.6; 175 -6.4; 188 -6.3; 201 -6.2; 215 -6.1; 230 -5.9; 246 -5.7; 263 -5.6; 282 -5.3; 301 -5.1; 323 -4.8; 345 -4.5; 369 -4.2; 395 -3.9; 423 -3.5; 452 -3.1; 484 -3.0; 518 -2.7; 554 -2.2; 593 -1.6; 635 -1.3; 679 -1.0; 726 -0.7; 777 -0.3; 832 -0.2; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.3; 1248 0.3; 1336 0.3; 1429 0.1; 1529 -0.1; 1636 -0.1; 1751 0.0; 1873 0.3; 2004 0.6; 2145 0.8; 2295 1.1; 2455 1.4; 2627 1.3; 2811 1.0; 3008 0.7; 3219 0.0; 3444 -0.8; 3685 -1.8; 3943 -3.1; 4219 -5.4; 4514 -7.7; 4830 -7.8; 5168 -5.3; 5530 -1.3; 5917 2.1; 6331 4.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -0.4; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -3.2; 15258 -4.4; 16326 -1.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.900740059177974dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read Heath Acoustics MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.18 | -5.9 dB |
| Peaking | 227 Hz   | 0.69 | -3.5 dB |
| Peaking | 4709 Hz  | 4.18 | -9.4 dB |
| Peaking | 6396 Hz  | 4.71 | 6.1 dB  |
| Peaking | 14980 Hz | 4.68 | -5.1 dB |
| Peaking | 470 Hz   | 1.87 | -0.9 dB |
| Peaking | 858 Hz   | 1.06 | 0.8 dB  |
| Peaking | 2608 Hz  | 2.41 | 1.8 dB  |
| Peaking | 4087 Hz  | 4.98 | -1.1 dB |
| Peaking | 24000 Hz | 1.6  | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20Heath%20Acoustics%20MA750/Read%20Heath%20Acoustics%20MA750.png)