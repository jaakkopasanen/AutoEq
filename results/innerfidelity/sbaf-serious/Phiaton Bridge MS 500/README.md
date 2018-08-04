# Phiaton Bridge MS 500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 3.5; 22 3.0; 23 2.8; 25 2.4; 26 2.3; 28 2.0; 30 1.7; 32 1.5; 35 1.2; 37 1.1; 40 0.9; 42 0.8; 45 0.7; 49 0.5; 52 0.4; 56 0.4; 59 0.4; 64 0.5; 68 0.5; 73 0.4; 78 0.3; 83 0.4; 89 0.5; 95 0.6; 102 0.7; 109 0.7; 117 0.2; 125 -0.2; 134 -0.2; 143 0.1; 153 0.5; 164 1.3; 175 1.7; 188 2.2; 201 2.9; 215 3.7; 230 4.5; 246 5.1; 263 5.6; 282 6.0; 301 5.9; 323 5.7; 345 5.6; 369 5.3; 395 4.9; 423 4.6; 452 4.2; 484 3.6; 518 3.0; 554 2.7; 593 2.4; 635 1.9; 679 1.6; 726 1.3; 777 0.9; 832 0.5; 890 0.7; 952 0.6; 1019 -0.2; 1090 -0.4; 1167 -0.3; 1248 -0.3; 1336 -0.2; 1429 0.2; 1529 0.7; 1636 0.5; 1751 -0.3; 1873 -0.1; 2004 1.2; 2145 2.7; 2295 4.1; 2455 5.6; 2627 6.0; 2811 6.0; 3008 5.3; 3219 4.0; 3444 3.0; 3685 2.3; 3943 1.8; 4219 2.9; 4514 4.5; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge MS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.37 | 3.2 dB  |
| Peaking | 6 Hz    | 1.54 | -0.2 dB |
| Peaking | 320 Hz  | 1.21 | 6.3 dB  |
| Peaking | 2699 Hz | 3.19 | 6.2 dB  |
| Peaking | 5459 Hz | 2.41 | 6.6 dB  |
| Peaking | 137 Hz  | 3.58 | -1.6 dB |
| Peaking | 809 Hz  | 0.1  | 0.3 dB  |
| Peaking | 1832 Hz | 7.24 | -1.6 dB |
| Peaking | 1137 Hz | 2.69 | -1.4 dB |
| Peaking | 8365 Hz | 3.64 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Bridge%20MS%20500/Phiaton%20Bridge%20MS%20500.png)