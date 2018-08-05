# Denon AH-C560R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 10 -84; 20 -4.8; 22 -5.1; 23 -5.2; 25 -5.5; 26 -5.6; 28 -5.8; 30 -5.9; 32 -6.0; 35 -6.2; 37 -6.3; 40 -6.4; 42 -6.4; 45 -6.5; 49 -6.6; 52 -6.6; 56 -6.7; 59 -6.7; 64 -6.7; 68 -6.7; 73 -6.8; 78 -7.0; 83 -7.2; 89 -7.5; 95 -7.8; 102 -8.3; 109 -8.7; 117 -9.0; 125 -9.5; 134 -9.8; 143 -10.0; 153 -10.0; 164 -10.0; 175 -9.7; 188 -9.5; 201 -9.3; 215 -9.0; 230 -8.6; 246 -8.3; 263 -7.9; 282 -7.4; 301 -7.1; 323 -6.6; 345 -6.1; 369 -5.8; 395 -5.3; 423 -4.7; 452 -4.2; 484 -3.8; 518 -3.5; 554 -2.9; 593 -2.2; 635 -1.8; 679 -1.6; 726 -1.5; 777 -0.9; 832 -0.6; 890 -0.3; 952 -0.1; 1019 -0.0; 1090 0.0; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.2; 1529 -1.5; 1636 -1.7; 1751 -1.9; 1873 -1.8; 2004 -1.8; 2145 -1.9; 2295 -2.1; 2455 -2.3; 2627 -2.9; 2811 -3.6; 3008 -3.9; 3219 -3.8; 3444 -2.9; 3685 -2.8; 3943 -3.1; 4219 -4.8; 4514 -6.4; 4830 -7.6; 5168 -8.6; 5530 -8.9; 5917 -7.6; 6331 -5.5; 6775 -4.1; 7249 -3.5; 7756 -4.3; 8299 -6.2; 8880 -7.0; 9502 -4.9; 10167 -0.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.6dB` and instead set Global volume in the UI for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 6 Hz     | 1.79 | -4.1 dB |
| Peaking | 31 Hz    | 0.46 | -5.0 dB |
| Peaking | 176 Hz   | 0.56 | -9.3 dB |
| Peaking | 5210 Hz  | 1.5  | -8.2 dB |
| Peaking | 8805 Hz  | 6    | -5.7 dB |
| Peaking | 990 Hz   | 2.13 | 1.4 dB  |
| Peaking | 1679 Hz  | 2.93 | -0.9 dB |
| Peaking | 3140 Hz  | 1.87 | -2.5 dB |
| Peaking | 3783 Hz  | 3.64 | 3.1 dB  |
| Peaking | 11074 Hz | 4.11 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)