# Sony MDR-EX56LP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.4; 22 -7.8; 23 -7.9; 25 -8.3; 26 -8.4; 28 -8.7; 30 -8.9; 32 -9.1; 35 -9.4; 37 -9.5; 40 -9.7; 42 -9.9; 45 -10.0; 49 -10.2; 52 -10.3; 56 -10.5; 59 -10.7; 64 -10.8; 68 -10.9; 73 -11.0; 78 -11.1; 83 -11.1; 89 -11.2; 95 -11.2; 102 -11.1; 109 -11.0; 117 -11.0; 125 -10.9; 134 -10.8; 143 -10.7; 153 -10.5; 164 -10.3; 175 -10.1; 188 -9.8; 201 -9.5; 215 -9.2; 230 -8.9; 246 -8.5; 263 -8.1; 282 -7.8; 301 -7.4; 323 -6.9; 345 -6.5; 369 -6.0; 395 -5.7; 423 -5.4; 452 -5.2; 484 -5.0; 518 -4.7; 554 -4.4; 593 -4.2; 635 -4.1; 679 -4.1; 726 -4.2; 777 -4.4; 832 -4.8; 890 -3.8; 952 -0.7; 1019 -0.2; 1090 -1.3; 1167 -2.4; 1248 -3.3; 1336 -4.3; 1429 -5.2; 1529 -6.1; 1636 -6.8; 1751 -7.5; 1873 -8.1; 2004 -8.4; 2145 -8.5; 2295 -8.1; 2455 -7.3; 2627 -6.0; 2811 -4.8; 3008 -3.3; 3219 -2.2; 3444 -1.3; 3685 -0.0; 3943 2.1; 4219 4.7; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.6; 6331 1.4; 6775 0.2; 7249 0.3; 7756 0.2; 8299 0.0; 8880 -0.7; 9502 -2.9; 10167 -3.9; 10879 -1.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -2.4; 16326 -3.2; 17469 -0.9; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099952559277959dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX56LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.31 | -6.5 dB |
| Peaking | 153 Hz   | 0.34 | -8.5 dB |
| Peaking | 2118 Hz  | 1.42 | -8.9 dB |
| Peaking | 4821 Hz  | 2.53 | 8.4 dB  |
| Peaking | 864 Hz   | 3.63 | -3.7 dB |
| Peaking | 982 Hz   | 4.04 | 5.0 dB  |
| Peaking | 1521 Hz  | 5.07 | -1.1 dB |
| Peaking | 9799 Hz  | 5.74 | -4.3 dB |
| Peaking | 16172 Hz | 4.27 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-EX56LP/Sony%20MDR-EX56LP.png)