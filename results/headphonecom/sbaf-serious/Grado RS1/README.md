# Grado RS1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.4; 45 4.6; 49 3.7; 52 3.0; 56 2.0; 59 1.3; 64 0.3; 68 -0.5; 73 -1.3; 78 -2.0; 83 -2.4; 89 -2.9; 95 -3.2; 102 -3.5; 109 -3.7; 117 -3.8; 125 -3.8; 134 -3.7; 143 -3.6; 153 -3.5; 164 -3.2; 175 -2.9; 188 -2.8; 201 -2.8; 215 -2.5; 230 -2.3; 246 -2.0; 263 -1.7; 282 -1.3; 301 -0.5; 323 -0.3; 345 -1.6; 369 -1.5; 395 -1.2; 423 -1.0; 452 -0.8; 484 -0.6; 518 -0.5; 554 -0.3; 593 -0.1; 635 0.0; 679 0.2; 726 0.2; 777 0.2; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.1; 1429 -1.8; 1529 -2.5; 1636 -3.9; 1751 -6.9; 1873 -9.4; 2004 -8.5; 2145 -7.7; 2295 -7.0; 2455 -6.2; 2627 -5.1; 2811 -3.9; 3008 -2.4; 3219 -1.1; 3444 0.1; 3685 0.7; 3943 -0.7; 4219 -5.6; 4514 -11.6; 4830 -13.6; 5168 -10.2; 5530 -9.3; 5917 -8.0; 6331 -4.0; 6775 -0.3; 7249 -0.7; 7756 -3.7; 8299 -8.2; 8880 -11.9; 9502 -12.9; 10167 -10.6; 10879 -6.5; 11640 -3.3; 12455 -2.7; 13327 -4.2; 14260 -5.1; 15258 -3.4; 16326 -0.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.54 | 8.0 dB   |
| Peaking | 100 Hz   | 0.65 | -6.3 dB  |
| Peaking | 1978 Hz  | 3.37 | -8.4 dB  |
| Peaking | 8097 Hz  | 0.55 | -7.6 dB  |
| Peaking | 24000 Hz | 1.95 | -10.4 dB |
| Peaking | 3845 Hz  | 3.41 | 10.3 dB  |
| Peaking | 4671 Hz  | 2.47 | -12.5 dB |
| Peaking | 7028 Hz  | 3.77 | 9.7 dB   |
| Peaking | 9315 Hz  | 4.21 | -8.2 dB  |
| Peaking | 14255 Hz | 0.29 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS1/Grado%20RS1.png)