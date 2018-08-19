# Denon AH-C560R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.1dB
GraphicEQ: 10 -84; 20 -4.9; 22 -5.2; 23 -5.3; 25 -5.6; 26 -5.7; 28 -5.9; 30 -6.1; 32 -6.3; 35 -6.5; 37 -6.6; 40 -6.8; 42 -6.9; 45 -7.1; 49 -7.3; 52 -7.4; 56 -7.6; 59 -7.8; 64 -8.0; 68 -8.1; 73 -8.4; 78 -8.6; 83 -8.8; 89 -9.1; 95 -9.2; 102 -9.4; 109 -9.4; 117 -9.4; 125 -9.5; 134 -9.5; 143 -9.5; 153 -9.5; 164 -9.4; 175 -9.2; 188 -9.1; 201 -8.9; 215 -8.6; 230 -8.3; 246 -8.0; 263 -7.7; 282 -7.2; 301 -6.9; 323 -6.5; 345 -6.0; 369 -5.7; 395 -5.2; 423 -4.6; 452 -4.1; 484 -3.8; 518 -3.4; 554 -2.9; 593 -2.2; 635 -1.8; 679 -1.6; 726 -1.5; 777 -0.9; 832 -0.6; 890 -0.3; 952 -0.1; 1019 -0.0; 1090 0.0; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.2; 1529 -1.5; 1636 -1.7; 1751 -1.9; 1873 -1.8; 2004 -1.8; 2145 -1.9; 2295 -2.1; 2455 -2.3; 2627 -2.9; 2811 -3.6; 3008 -3.9; 3219 -3.8; 3444 -2.9; 3685 -2.8; 3943 -3.1; 4219 -4.8; 4514 -6.4; 4830 -7.6; 5168 -8.6; 5530 -8.9; 5917 -7.6; 6331 -5.5; 6775 -4.1; 7249 -3.5; 7756 -4.3; 8299 -6.2; 8880 -7.0; 9502 -4.9; 10167 -0.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.10396536317512207dB` and instead set Global volume in the UI for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.29 | -5.9 dB |
| Peaking | 148 Hz   | 0.64 | -5.3 dB |
| Peaking | 310 Hz   | 1.01 | -3.0 dB |
| Peaking | 5206 Hz  | 1.45 | -8.1 dB |
| Peaking | 8808 Hz  | 6.37 | -5.8 dB |
| Peaking | 991 Hz   | 2.81 | 1.3 dB  |
| Peaking | 3024 Hz  | 1.06 | -2.1 dB |
| Peaking | 3860 Hz  | 3.57 | 3.2 dB  |
| Peaking | 10682 Hz | 6.54 | 1.4 dB  |
| Peaking | 12939 Hz | 1.99 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)