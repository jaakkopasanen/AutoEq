# Beyerdynamic T50p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.7; 32 5.3; 35 4.7; 37 4.2; 40 3.7; 42 3.3; 45 2.9; 49 2.3; 52 1.8; 56 1.1; 59 0.7; 64 1.3; 68 2.0; 73 1.4; 78 0.5; 83 -0.0; 89 -0.5; 95 -0.4; 102 -0.2; 109 -0.3; 117 -0.2; 125 0.2; 134 0.6; 143 1.3; 153 2.6; 164 4.1; 175 3.3; 188 1.2; 201 -0.6; 215 -1.2; 230 -1.5; 246 -2.1; 263 -3.1; 282 -4.6; 301 -5.6; 323 -5.5; 345 -5.1; 369 -4.9; 395 -4.5; 423 -4.4; 452 -4.2; 484 -3.9; 518 -3.5; 554 -3.3; 593 -2.9; 635 -2.6; 679 -2.1; 726 -0.6; 777 -0.6; 832 -0.6; 890 -0.4; 952 -0.2; 1019 0.0; 1090 0.3; 1167 0.5; 1248 0.7; 1336 0.7; 1429 0.5; 1529 0.4; 1636 0.2; 1751 0.1; 1873 0.2; 2004 0.7; 2145 1.6; 2295 2.5; 2455 3.6; 2627 4.4; 2811 4.9; 3008 5.6; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.7; 5917 3.4; 6331 2.5; 6775 2.5; 7249 0.5; 7756 -4.0; 8299 -6.6; 8880 -7.0; 9502 -5.3; 10167 -1.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.0; 17469 -1.8; 18692 -2.5; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.99 | 6.5 dB   |
| Peaking | 169 Hz   | 3.99 | 5.7 dB   |
| Peaking | 357 Hz   | 0.95 | -5.4 dB  |
| Peaking | 4302 Hz  | 0.87 | 7.0 dB   |
| Peaking | 8617 Hz  | 3.32 | -10.1 dB |
| Peaking | 95 Hz    | 4.65 | -0.8 dB  |
| Peaking | 401 Hz   | 6.65 | 0.4 dB   |
| Peaking | 1881 Hz  | 4.1  | -1.7 dB  |
| Peaking | 2812 Hz  | 3.9  | 1.2 dB   |
| Peaking | 18350 Hz | 3.3  | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T50p/Beyerdynamic%20T50p.png)