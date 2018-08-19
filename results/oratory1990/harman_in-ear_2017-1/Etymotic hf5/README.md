# Etymotic hf5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.9; 40 5.8; 42 5.7; 45 5.6; 49 5.4; 52 5.3; 56 5.1; 59 5.0; 64 4.6; 68 4.4; 73 4.1; 78 3.8; 83 3.5; 89 3.1; 95 3.0; 102 2.4; 109 1.9; 117 2.1; 125 1.7; 134 1.2; 143 1.0; 153 0.8; 164 0.7; 175 0.5; 188 0.4; 201 0.3; 215 0.2; 230 0.1; 246 0.0; 263 0.0; 282 -0.0; 301 -0.0; 323 0.1; 345 0.2; 369 0.3; 395 0.2; 423 0.2; 452 0.2; 484 0.2; 518 0.3; 554 0.4; 593 0.5; 635 0.5; 679 0.6; 726 0.7; 777 0.8; 832 0.7; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.1; 1336 -1.1; 1429 -1.0; 1529 -0.7; 1636 -0.4; 1751 -0.1; 1873 0.3; 2004 0.8; 2145 1.4; 2295 1.9; 2455 2.3; 2627 2.6; 2811 2.9; 3008 3.2; 3219 3.4; 3444 3.6; 3685 3.8; 3943 4.0; 4219 4.3; 4514 4.8; 4830 5.6; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -2.1; 14260 -11.1; 15258 -16.5; 16326 -14.5; 17469 -7.1; 18692 -0.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.18 | 6.2 dB   |
| Peaking | 150 Hz   | 0.69 | -2.7 dB  |
| Peaking | 1381 Hz  | 3.08 | -1.8 dB  |
| Peaking | 4936 Hz  | 0.97 | 5.9 dB   |
| Peaking | 15636 Hz | 2.87 | -18.9 dB |
| Peaking | 4375 Hz  | 4.8  | -1.4 dB  |
| Peaking | 6634 Hz  | 2.09 | 3.3 dB   |
| Peaking | 7499 Hz  | 2.59 | -4.3 dB  |
| Peaking | 12904 Hz | 3.33 | 4.6 dB   |
| Peaking | 14336 Hz | 5.67 | -5.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20hf5/Etymotic%20hf5.png)