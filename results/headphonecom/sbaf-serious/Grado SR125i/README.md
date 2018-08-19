# Grado SR125i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.7; 56 5.0; 59 4.4; 64 3.4; 68 2.7; 73 1.8; 78 1.2; 83 0.6; 89 0.0; 95 -0.4; 102 -0.7; 109 -0.9; 117 -1.1; 125 -1.1; 134 -1.1; 143 -1.0; 153 -1.0; 164 -0.9; 175 -0.8; 188 -0.7; 201 -0.6; 215 -0.4; 230 -0.2; 246 -0.1; 263 0.2; 282 0.7; 301 0.5; 323 -0.3; 345 -0.2; 369 0.1; 395 0.1; 423 0.2; 452 0.3; 484 0.3; 518 0.5; 554 0.6; 593 0.5; 635 0.7; 679 0.7; 726 0.7; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.5; 1429 -2.3; 1529 -3.1; 1636 -3.9; 1751 -4.5; 1873 -5.3; 2004 -5.7; 2145 -6.1; 2295 -6.2; 2455 -5.3; 2627 -4.7; 2811 -3.3; 3008 -2.6; 3219 -1.8; 3444 -1.5; 3685 -1.6; 3943 -1.9; 4219 -1.7; 4514 -3.8; 4830 -5.1; 5168 -4.4; 5530 -7.9; 5917 -6.7; 6331 -6.1; 6775 -6.8; 7249 -6.1; 7756 -6.2; 8299 -8.0; 8880 -10.0; 9502 -9.9; 10167 -6.4; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.2; 18692 -3.3; 20000 -8.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 64 Hz    | 0.25 | 11.0 dB  |
| Peaking | 110 Hz   | 0.55 | -11.0 dB |
| Peaking | 2102 Hz  | 1.94 | -6.3 dB  |
| Peaking | 5978 Hz  | 2.05 | -6.4 dB  |
| Peaking | 9099 Hz  | 3.88 | -9.9 dB  |
| Peaking | 833 Hz   | 1.25 | 1.3 dB   |
| Peaking | 1496 Hz  | 0.15 | -0.6 dB  |
| Peaking | 3624 Hz  | 2.55 | 1.4 dB   |
| Peaking | 11851 Hz | 3.32 | 2.2 dB   |
| Peaking | 19786 Hz | 3.07 | -8.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR125i/Grado%20SR125i.png)