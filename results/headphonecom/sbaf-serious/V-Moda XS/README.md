# V-Moda XS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 -5.0; 22 -5.4; 23 -5.5; 25 -5.8; 26 -5.9; 28 -6.2; 30 -6.3; 32 -6.5; 35 -6.6; 37 -6.7; 40 -6.8; 42 -6.8; 45 -6.9; 49 -6.9; 52 -7.0; 56 -7.1; 59 -7.1; 64 -7.1; 68 -7.2; 73 -7.3; 78 -7.3; 83 -7.2; 89 -7.1; 95 -6.7; 102 -6.7; 109 -6.9; 117 -6.8; 125 -6.9; 134 -6.8; 143 -6.7; 153 -6.5; 164 -6.1; 175 -5.6; 188 -5.3; 201 -4.9; 215 -4.5; 230 -5.0; 246 -4.7; 263 -3.7; 282 -2.6; 301 -1.7; 323 -0.8; 345 -0.3; 369 0.1; 395 0.6; 423 1.1; 452 1.4; 484 1.8; 518 2.0; 554 2.4; 593 2.6; 635 2.5; 679 2.5; 726 2.4; 777 2.1; 832 1.6; 890 1.0; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.0; 1248 -1.3; 1336 -1.4; 1429 -1.5; 1529 -1.7; 1636 -1.7; 1751 -1.6; 1873 -1.6; 2004 -2.0; 2145 -1.8; 2295 -1.7; 2455 -2.1; 2627 -2.4; 2811 -3.1; 3008 -2.8; 3219 -2.2; 3444 -1.0; 3685 1.4; 3943 3.2; 4219 4.3; 4514 2.3; 4830 0.5; 5168 2.9; 5530 4.7; 5917 4.9; 6331 3.6; 6775 0.5; 7249 0.3; 7756 0.2; 8299 -0.3; 8880 -1.2; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.980903809176908dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda XS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.5  | -7.2 dB |
| Peaking | 135 Hz   | 1.43 | -4.4 dB |
| Peaking | 234 Hz   | 4.39 | -2.9 dB |
| Peaking | 5699 Hz  | 4.24 | 5.3 dB  |
| Peaking | 24000 Hz | 2.4  | 2.2 dB  |
| Peaking | 15 Hz    | 1.73 | -1.5 dB |
| Peaking | 616 Hz   | 1.52 | 3.5 dB  |
| Peaking | 2563 Hz  | 0.73 | -2.9 dB |
| Peaking | 4092 Hz  | 5.07 | 5.7 dB  |
| Peaking | 8827 Hz  | 8.88 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20XS/V-Moda%20XS.png)