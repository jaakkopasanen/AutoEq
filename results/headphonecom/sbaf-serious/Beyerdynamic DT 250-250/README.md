# Beyerdynamic DT 250-250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.6; 83 5.1; 89 4.6; 95 4.2; 102 3.8; 109 3.5; 117 3.1; 125 2.6; 134 2.1; 143 1.8; 153 1.7; 164 1.7; 175 1.3; 188 0.9; 201 0.6; 215 0.4; 230 0.2; 246 0.2; 263 0.2; 282 0.2; 301 0.1; 323 -0.0; 345 -0.1; 369 -0.2; 395 -0.1; 423 0.0; 452 0.3; 484 0.6; 518 0.7; 554 1.0; 593 1.1; 635 1.0; 679 0.9; 726 0.8; 777 0.6; 832 0.5; 890 0.3; 952 0.1; 1019 0.8; 1090 3.3; 1167 2.2; 1248 1.8; 1336 1.3; 1429 0.2; 1529 -1.0; 1636 -1.8; 1751 -2.0; 1873 -2.0; 2004 -1.9; 2145 -2.0; 2295 -2.0; 2455 -2.6; 2627 -2.9; 2811 -2.2; 3008 -1.2; 3219 -0.6; 3444 -1.0; 3685 -1.7; 3943 -1.9; 4219 -2.0; 4514 -1.6; 4830 -0.7; 5168 1.4; 5530 5.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.8; 9502 -4.6; 10167 -4.9; 10879 -2.0; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.44 | 6.7 dB  |
| Peaking | 1156 Hz | 2.89 | 3.7 dB  |
| Peaking | 2784 Hz | 0.56 | -2.6 dB |
| Peaking | 6045 Hz | 3.47 | 8.1 dB  |
| Peaking | 9855 Hz | 5.5  | -5.7 dB |
| Peaking | 77 Hz   | 4.55 | 1.0 dB  |
| Peaking | 619 Hz  | 4.06 | 1.3 dB  |
| Peaking | 3270 Hz | 3.98 | 3.7 dB  |
| Peaking | 3399 Hz | 1.75 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20250-250/Beyerdynamic%20DT%20250-250.png)