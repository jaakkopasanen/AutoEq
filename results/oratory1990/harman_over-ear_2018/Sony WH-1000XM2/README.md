# Sony WH-1000XM2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 10 -84; 20 -6.2; 22 -6.5; 23 -6.7; 25 -6.9; 26 -7.0; 28 -7.2; 30 -7.4; 32 -7.5; 35 -7.6; 37 -7.7; 40 -7.8; 42 -7.8; 45 -7.8; 49 -7.8; 52 -7.7; 56 -7.7; 59 -7.6; 64 -7.6; 68 -7.6; 73 -7.6; 78 -7.7; 83 -7.8; 89 -8.0; 95 -8.2; 102 -8.4; 109 -8.6; 117 -8.8; 125 -8.9; 134 -9.1; 143 -9.1; 153 -9.2; 164 -9.2; 175 -9.2; 188 -9.1; 201 -9.1; 215 -8.9; 230 -8.6; 246 -8.3; 263 -7.9; 282 -7.5; 301 -7.1; 323 -6.6; 345 -6.1; 369 -5.7; 395 -5.2; 423 -4.8; 452 -4.5; 484 -4.2; 518 -4.0; 554 -3.7; 593 -3.4; 635 -3.1; 679 -2.9; 726 -2.3; 777 0.2; 832 0.9; 890 -0.0; 952 0.1; 1019 -0.2; 1090 -1.4; 1167 -3.3; 1248 -5.3; 1336 -6.5; 1429 -7.5; 1529 -8.1; 1636 -8.1; 1751 -7.6; 1873 -6.9; 2004 -6.7; 2145 -6.7; 2295 -6.4; 2455 -6.5; 2627 -7.1; 2811 -7.5; 3008 -6.4; 3219 -4.7; 3444 -4.1; 3685 -4.8; 3943 -6.5; 4219 -6.9; 4514 -6.1; 4830 -5.2; 5168 -6.7; 5530 -10.5; 5917 -9.7; 6331 -5.9; 6775 -4.0; 7249 -5.7; 7756 -6.7; 8299 -5.3; 8880 -1.8; 9502 -0.0; 10167 -0.1; 10879 -2.6; 11640 -7.2; 12455 -10.6; 13327 -10.2; 14260 -6.6; 15258 -3.4; 16326 -3.0; 17469 -4.5; 18692 -6.6; 20000 -9.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.1941799734684522dB` and instead set Global volume in the UI for both channels to **-11**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-1000XM2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.22 | -7.2 dB  |
| Peaking | 217 Hz   | 0.74 | -5.7 dB  |
| Peaking | 1994 Hz  | 1.1  | -7.4 dB  |
| Peaking | 5622 Hz  | 1.77 | -7.7 dB  |
| Peaking | 13032 Hz | 2.6  | -10.8 dB |
| Peaking | 960 Hz   | 1.79 | 8.6 dB   |
| Peaking | 1205 Hz  | 0.79 | -6.0 dB  |
| Peaking | 2016 Hz  | 2.9  | 4.0 dB   |
| Peaking | 9975 Hz  | 5.76 | 4.4 dB   |
| Peaking | 19593 Hz | 1.6  | -8.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20WH-1000XM2/Sony%20WH-1000XM2.png)