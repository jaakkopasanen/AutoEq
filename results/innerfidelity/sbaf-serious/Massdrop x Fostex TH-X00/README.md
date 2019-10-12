# Massdrop x Fostex TH-X00
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 10 -84; 20 1.0; 22 0.3; 23 0.0; 25 -0.4; 26 -0.6; 28 -0.9; 30 -1.1; 32 -1.3; 35 -1.4; 37 -1.4; 40 -1.5; 42 -1.5; 45 -1.5; 49 -1.5; 52 -1.5; 56 -1.4; 59 -1.4; 64 -1.4; 68 -1.5; 73 -1.6; 78 -1.8; 83 -1.9; 89 -2.1; 95 -2.2; 102 -2.4; 109 -2.4; 117 -2.4; 125 -2.5; 134 -2.6; 143 -2.6; 153 -2.6; 164 -2.4; 175 -2.3; 188 -2.2; 201 -2.1; 215 -1.7; 230 -1.3; 246 -1.1; 263 -0.9; 282 -0.7; 301 -0.5; 323 -0.3; 345 -0.1; 369 0.1; 395 0.3; 423 0.6; 452 0.9; 484 0.8; 518 0.7; 554 0.8; 593 0.9; 635 1.3; 679 1.3; 726 1.0; 777 1.2; 832 1.2; 890 0.6; 952 0.2; 1019 -0.0; 1090 -0.0; 1167 0.0; 1248 0.0; 1336 -0.3; 1429 -0.6; 1529 -1.0; 1636 -1.1; 1751 -0.9; 1873 -0.7; 2004 -0.3; 2145 0.2; 2295 0.7; 2455 1.5; 2627 2.1; 2811 2.5; 3008 3.5; 3219 3.7; 3444 5.6; 3685 4.7; 3943 4.0; 4219 3.2; 4514 2.6; 4830 2.5; 5168 1.4; 5530 1.0; 5917 1.2; 6331 1.7; 6775 2.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -1.0; 10879 -0.4; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.2dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 1.46 | -1.1 dB |
| Peaking | 134 Hz   | 0.75 | -2.7 dB |
| Peaking | 559 Hz   | 1.46 | 1.4 dB  |
| Peaking | 3619 Hz  | 2.14 | 5.1 dB  |
| Peaking | 809 Hz   | 5.97 | 0.8 dB  |
| Peaking | 1710 Hz  | 2.13 | -1.5 dB |
| Peaking | 2628 Hz  | 3.97 | 0.7 dB  |
| Peaking | 6743 Hz  | 7.26 | 2.2 dB  |
| Peaking | 10269 Hz | 5.47 | -1.1 dB |

![](./Massdrop%20x%20Fostex%20TH-X00.png)