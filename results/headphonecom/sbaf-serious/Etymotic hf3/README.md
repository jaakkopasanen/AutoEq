# Etymotic hf3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.8; 37 5.7; 40 5.4; 42 5.3; 45 5.1; 49 4.8; 52 4.7; 56 4.4; 59 4.1; 64 3.9; 68 3.7; 73 3.3; 78 3.0; 83 2.8; 89 2.6; 95 2.4; 102 2.2; 109 2.0; 117 1.8; 125 1.6; 134 1.2; 143 1.0; 153 0.8; 164 0.7; 175 0.6; 188 0.5; 201 0.4; 215 0.4; 230 0.4; 246 0.3; 263 0.3; 282 0.4; 301 0.4; 323 0.5; 345 0.7; 369 0.8; 395 1.0; 423 0.9; 452 1.0; 484 1.0; 518 1.1; 554 1.3; 593 1.5; 635 1.6; 679 1.5; 726 1.6; 777 1.5; 832 1.2; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.5; 1336 -2.1; 1429 -2.7; 1529 -3.3; 1636 -3.8; 1751 -3.9; 1873 -4.0; 2004 -3.8; 2145 -3.6; 2295 -3.1; 2455 -2.4; 2627 -1.4; 2811 -0.1; 3008 1.5; 3219 3.3; 3444 4.8; 3685 5.5; 3943 5.3; 4219 4.5; 4514 4.1; 4830 4.7; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.44 | 6.1 dB  |
| Peaking | 846 Hz  | 0.8  | 4.7 dB  |
| Peaking | 2268 Hz | 0.44 | -7.7 dB |
| Peaking | 3586 Hz | 1.61 | 10.3 dB |
| Peaking | 5781 Hz | 2.26 | 7.4 dB  |
| Peaking | 117 Hz  | 1.1  | 0.6 dB  |
| Peaking | 162 Hz  | 0.99 | -0.7 dB |
| Peaking | 389 Hz  | 3.97 | 0.4 dB  |
| Peaking | 6587 Hz | 9.13 | 1.2 dB  |
| Peaking | 7536 Hz | 5.5  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf3/Etymotic%20hf3.png)