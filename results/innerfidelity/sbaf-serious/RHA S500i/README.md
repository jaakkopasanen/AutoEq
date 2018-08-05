# RHA S500i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 4.5; 22 3.8; 23 3.6; 25 3.2; 26 3.0; 28 2.8; 30 2.6; 32 2.4; 35 2.2; 37 2.1; 40 2.0; 42 1.9; 45 1.7; 49 1.6; 52 1.5; 56 1.4; 59 1.3; 64 1.1; 68 1.0; 73 1.0; 78 0.8; 83 0.4; 89 0.1; 95 -0.3; 102 -0.8; 109 -1.2; 117 -1.7; 125 -2.1; 134 -2.4; 143 -2.9; 153 -3.0; 164 -3.0; 175 -2.9; 188 -2.8; 201 -2.8; 215 -2.6; 230 -2.3; 246 -2.2; 263 -2.0; 282 -1.8; 301 -1.6; 323 -1.4; 345 -1.1; 369 -0.9; 395 -0.7; 423 -0.4; 452 -0.2; 484 -0.1; 518 0.1; 554 0.4; 593 0.8; 635 0.8; 679 0.8; 726 0.8; 777 0.9; 832 0.8; 890 0.6; 952 0.3; 1019 -0.2; 1090 -0.7; 1167 -1.2; 1248 -1.6; 1336 -2.2; 1429 -2.9; 1529 -3.6; 1636 -4.3; 1751 -4.7; 1873 -5.1; 2004 -5.5; 2145 -6.3; 2295 -7.2; 2455 -8.1; 2627 -9.6; 2811 -10.6; 3008 -8.6; 3219 -5.3; 3444 -2.0; 3685 -0.1; 3943 0.7; 4219 -0.0; 4514 -0.6; 4830 -0.4; 5168 0.3; 5530 0.2; 5917 -0.5; 6331 -2.6; 6775 -5.1; 7249 -6.6; 7756 -6.1; 8299 -4.7; 8880 -2.8; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 -0.0; 12455 -1.6; 13327 -3.5; 14260 -3.9; 15258 -2.2; 16326 -0.1; 17469 0.0; 18692 -0.0; 20000 -3.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.0dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA S500i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.18 | 3.8 dB  |
| Peaking | 169 Hz   | 1.13 | -3.5 dB |
| Peaking | 2535 Hz  | 1.91 | -9.7 dB |
| Peaking | 13907 Hz | 2.14 | -3.6 dB |
| Peaking | 27960 Hz | 3.21 | -2.6 dB |
| Peaking | 745 Hz   | 2.2  | 1.2 dB  |
| Peaking | 2906 Hz  | 5.99 | -5.4 dB |
| Peaking | 1637 Hz  | 1.84 | -3.8 dB |
| Peaking | 4422 Hz  | 0.37 | 3.8 dB  |
| Peaking | 7372 Hz  | 2.45 | -9.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20S500i/RHA%20S500i.png)