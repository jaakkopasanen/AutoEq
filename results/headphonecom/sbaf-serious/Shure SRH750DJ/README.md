# Shure SRH750DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 -3.4; 22 -3.9; 23 -4.1; 25 -4.5; 26 -4.7; 28 -5.1; 30 -5.4; 32 -5.6; 35 -5.9; 37 -6.1; 40 -6.3; 42 -6.5; 45 -6.6; 49 -6.7; 52 -6.7; 56 -6.6; 59 -6.7; 64 -6.9; 68 -7.1; 73 -7.5; 78 -7.5; 83 -7.2; 89 -6.5; 95 -5.5; 102 -4.6; 109 -4.1; 117 -4.8; 125 -6.1; 134 -6.6; 143 -7.2; 153 -7.2; 164 -5.9; 175 -6.0; 188 -6.3; 201 -5.8; 215 -5.0; 230 -4.8; 246 -5.0; 263 -4.2; 282 -3.3; 301 -2.4; 323 -1.5; 345 -0.9; 369 -0.6; 395 -0.3; 423 -0.3; 452 -0.4; 484 -0.6; 518 -0.7; 554 -0.7; 593 -0.7; 635 -0.7; 679 -0.6; 726 -0.4; 777 -0.1; 832 0.3; 890 0.6; 952 0.6; 1019 -0.2; 1090 -0.6; 1167 -0.4; 1248 -0.3; 1336 -0.8; 1429 -1.8; 1529 -2.6; 1636 -3.7; 1751 -5.3; 1873 -6.5; 2004 -7.6; 2145 -8.2; 2295 -7.6; 2455 -6.0; 2627 -4.0; 2811 -2.2; 3008 -0.7; 3219 0.5; 3444 1.0; 3685 0.9; 3943 -0.2; 4219 -3.0; 4514 -3.5; 4830 -0.8; 5168 0.7; 5530 1.4; 5917 5.3; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.0; 8299 -4.6; 8880 -6.8; 9502 -6.7; 10167 -4.4; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.958492719114096dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.51 | -6.9 dB |
| Peaking | 180 Hz  | 1.36 | -4.7 dB |
| Peaking | 2105 Hz | 2.73 | -8.8 dB |
| Peaking | 6310 Hz | 4.62 | 7.2 dB  |
| Peaking | 9104 Hz | 3.77 | -8.1 dB |
| Peaking | 12 Hz   | 1.38 | -0.6 dB |
| Peaking | 385 Hz  | 5.1  | 1.1 dB  |
| Peaking | 913 Hz  | 5.17 | 1.3 dB  |
| Peaking | 3477 Hz | 4.58 | 2.5 dB  |
| Peaking | 4395 Hz | 8.14 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH750DJ/Shure%20SRH750DJ.png)