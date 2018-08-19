# Klipsch Image S4i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 -8.7; 22 -8.7; 23 -8.7; 25 -8.7; 26 -8.7; 28 -8.8; 30 -8.8; 32 -8.8; 35 -8.8; 37 -8.8; 40 -8.8; 42 -8.8; 45 -8.9; 49 -9.1; 52 -9.2; 56 -9.3; 59 -9.4; 64 -9.5; 68 -9.7; 73 -9.8; 78 -10.0; 83 -10.1; 89 -10.2; 95 -10.3; 102 -10.3; 109 -10.3; 117 -10.3; 125 -10.4; 134 -10.4; 143 -10.3; 153 -10.2; 164 -10.1; 175 -9.9; 188 -9.7; 201 -9.4; 215 -9.1; 230 -8.8; 246 -8.5; 263 -8.1; 282 -7.7; 301 -7.2; 323 -6.6; 345 -6.1; 369 -5.5; 395 -5.0; 423 -4.5; 452 -3.9; 484 -3.4; 518 -2.8; 554 -2.2; 593 -1.7; 635 -1.2; 679 -0.7; 726 -0.3; 777 -0.0; 832 0.1; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.8; 1336 -1.2; 1429 -1.7; 1529 -2.1; 1636 -2.2; 1751 -2.0; 1873 -1.8; 2004 -1.8; 2145 -1.8; 2295 -1.5; 2455 -1.3; 2627 -1.0; 2811 -0.6; 3008 0.2; 3219 1.6; 3444 3.0; 3685 3.8; 3943 3.3; 4219 1.9; 4514 0.5; 4830 -0.6; 5168 -1.5; 5530 -3.3; 5917 -4.7; 6331 -3.6; 6775 -0.9; 7249 0.7; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -1.2; 10879 -1.8; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.8748634081643587dB` and instead set Global volume in the UI for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S4i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  0.22 | -8.1 dB |
| Peaking | 132 Hz   |  0.62 | -6.2 dB |
| Peaking | 272 Hz   |  1.01 | -3.8 dB |
| Peaking | 3750 Hz  |  5.26 | 4.5 dB  |
| Peaking | 5886 Hz  |  5.29 | -5.2 dB |
| Peaking | 467 Hz   |  1.4  | -1.5 dB |
| Peaking | 1266 Hz  |  0.47 | 3.7 dB  |
| Peaking | 1692 Hz  |  0.93 | -5.4 dB |
| Peaking | 7317 Hz  | 10.41 | 1.4 dB  |
| Peaking | 10630 Hz |  9.12 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S4i/Klipsch%20Image%20S4i.png)