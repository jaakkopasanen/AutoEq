# Ultrasone HFi-780

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.9; 64 5.7; 68 5.7; 73 5.9; 78 5.9; 83 5.9; 89 5.9; 95 5.7; 102 5.7; 109 5.8; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 6.0; 201 6.0; 215 6.0; 230 5.9; 246 4.9; 263 4.1; 282 2.7; 301 1.3; 323 0.2; 345 -0.3; 369 -0.5; 395 -1.0; 423 -1.2; 452 -1.1; 484 -1.0; 518 -0.7; 554 -0.2; 593 0.1; 635 0.3; 679 0.6; 726 0.6; 777 0.6; 832 0.5; 890 0.3; 952 0.1; 1019 -0.1; 1090 0.3; 1167 0.6; 1248 -0.3; 1336 -1.1; 1429 -1.6; 1529 -1.9; 1636 -2.0; 1751 -1.8; 1873 -1.5; 2004 -1.3; 2145 2.8; 2295 6.0; 2455 4.6; 2627 3.2; 2811 3.0; 3008 2.8; 3219 2.5; 3444 1.5; 3685 1.3; 3943 2.4; 4219 5.1; 4514 5.3; 4830 4.0; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -1.7; 10167 -2.8; 10879 -0.9; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFi-780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 66 Hz   | 0.21 | 6.7 dB   |
| Peaking | 1151 Hz | 0.23 | -1.9 dB  |
| Peaking | 2353 Hz | 6.13 | 6.7 dB   |
| Peaking | 5694 Hz | 1.07 | 8.3 dB   |
| Peaking | 8707 Hz | 1.33 | -4.4 dB  |
| Peaking | 20 Hz   | 2.05 | 1.1 dB   |
| Peaking | 229 Hz  | 1.02 | 8.5 dB   |
| Peaking | 338 Hz  | 0.56 | -10.7 dB |
| Peaking | 661 Hz  | 0.52 | 5.9 dB   |
| Peaking | 1690 Hz | 2.28 | -3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFi-780/Ultrasone%20HFi-780.png)