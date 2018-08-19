# Thinksound ts02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 -7.4; 22 -7.3; 23 -7.4; 25 -7.4; 26 -7.4; 28 -7.5; 30 -7.6; 32 -7.7; 35 -7.8; 37 -7.8; 40 -7.9; 42 -7.9; 45 -8.0; 49 -8.2; 52 -8.3; 56 -8.5; 59 -8.6; 64 -8.7; 68 -8.8; 73 -9.1; 78 -9.3; 83 -9.4; 89 -9.5; 95 -9.7; 102 -9.7; 109 -9.8; 117 -9.8; 125 -9.9; 134 -9.9; 143 -10.0; 153 -10.0; 164 -9.9; 175 -9.8; 188 -9.6; 201 -9.4; 215 -9.1; 230 -8.9; 246 -8.6; 263 -8.2; 282 -7.9; 301 -7.4; 323 -6.9; 345 -6.4; 369 -5.9; 395 -5.4; 423 -4.9; 452 -4.6; 484 -4.2; 518 -3.6; 554 -3.0; 593 -2.4; 635 -1.9; 679 -1.4; 726 -0.9; 777 -0.5; 832 -0.2; 890 0.0; 952 0.2; 1019 -0.0; 1090 0.1; 1167 1.2; 1248 1.1; 1336 0.9; 1429 0.7; 1529 0.5; 1636 0.5; 1751 0.7; 1873 0.9; 2004 1.1; 2145 1.2; 2295 1.4; 2455 1.4; 2627 1.2; 2811 0.9; 3008 0.9; 3219 1.7; 3444 3.0; 3685 4.0; 3943 3.8; 4219 2.4; 4514 1.0; 4830 -0.1; 5168 -1.4; 5530 -4.3; 5917 -8.5; 6331 -6.7; 6775 -2.7; 7249 -0.7; 7756 -0.2; 8299 -1.9; 8880 -4.5; 9502 -5.0; 10167 -1.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.209920288875503dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound ts02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.23 | -7.3 dB |
| Peaking | 154 Hz  | 0.7  | -5.5 dB |
| Peaking | 312 Hz  | 1.18 | -3.4 dB |
| Peaking | 3847 Hz | 1.67 | 4.1 dB  |
| Peaking | 5997 Hz | 3.99 | -9.5 dB |
| Peaking | 1195 Hz | 2.11 | 1.3 dB  |
| Peaking | 2325 Hz | 2.03 | 0.7 dB  |
| Peaking | 2958 Hz | 5.5  | -1.6 dB |
| Peaking | 7428 Hz | 3.62 | 1.8 dB  |
| Peaking | 9128 Hz | 5.56 | -5.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Thinksound%20ts02/Thinksound%20ts02.png)