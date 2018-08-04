# Grado SR60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.3; 32 4.7; 35 3.8; 37 3.3; 40 2.7; 42 2.3; 45 1.8; 49 1.2; 52 0.9; 56 0.6; 59 0.3; 64 0.1; 68 0.2; 73 0.1; 78 -0.2; 83 -0.4; 89 -0.6; 95 -0.8; 102 -0.9; 109 -1.1; 117 -1.3; 125 -1.4; 134 -1.4; 143 -1.2; 153 -1.2; 164 -1.3; 175 -1.3; 188 -1.1; 201 -0.8; 215 -0.4; 230 -0.9; 246 -1.5; 263 -1.5; 282 -1.2; 301 -1.0; 323 -0.7; 345 -0.5; 369 -0.4; 395 -0.2; 423 0.0; 452 0.1; 484 0.0; 518 0.1; 554 0.3; 593 0.4; 635 0.6; 679 0.4; 726 0.4; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.4; 1429 -2.1; 1529 -2.8; 1636 -3.6; 1751 -4.3; 1873 -4.8; 2004 -5.3; 2145 -5.6; 2295 -5.8; 2455 -5.6; 2627 -5.1; 2811 -3.8; 3008 -1.6; 3219 -0.2; 3444 0.8; 3685 1.5; 3943 0.3; 4219 -2.0; 4514 -6.1; 4830 -7.5; 5168 -4.4; 5530 -3.7; 5917 -2.0; 6331 -0.6; 6775 -2.1; 7249 -4.1; 7756 -5.9; 8299 -7.9; 8880 -8.4; 9502 -5.5; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -1.9; 16326 -1.4; 17469 -0.5; 18692 -0.5; 20000 -2.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.09 | 6.4 dB  |
| Peaking | 136 Hz   | 0.78 | -1.6 dB |
| Peaking | 2163 Hz  | 1.84 | -6.1 dB |
| Peaking | 8443 Hz  | 3.02 | -8.4 dB |
| Peaking | 21088 Hz | 2.06 | -6.0 dB |
| Peaking | 746 Hz   | 1.92 | 1.0 dB  |
| Peaking | 3684 Hz  | 4.4  | 4.0 dB  |
| Peaking | 4725 Hz  | 5.63 | -7.7 dB |
| Peaking | 10912 Hz | 4.21 | 2.2 dB  |
| Peaking | 15568 Hz | 5.19 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR60/Grado%20SR60.png)