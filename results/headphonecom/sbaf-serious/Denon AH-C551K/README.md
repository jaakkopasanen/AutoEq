# Denon AH-C551K

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.1dB
GraphicEQ: 10 -84; 20 -10.5; 22 -10.6; 23 -10.7; 25 -10.8; 26 -10.8; 28 -10.9; 30 -10.9; 32 -10.9; 35 -10.8; 37 -10.7; 40 -10.6; 42 -10.6; 45 -10.6; 49 -10.5; 52 -10.4; 56 -10.3; 59 -10.2; 64 -10.3; 68 -10.2; 73 -10.1; 78 -10.0; 83 -10.0; 89 -10.1; 95 -10.2; 102 -10.4; 109 -10.6; 117 -10.8; 125 -11.0; 134 -11.0; 143 -11.0; 153 -10.8; 164 -10.3; 175 -10.0; 188 -10.5; 201 -10.4; 215 -9.8; 230 -9.3; 246 -8.7; 263 -8.2; 282 -7.5; 301 -7.0; 323 -6.3; 345 -5.6; 369 -5.0; 395 -4.5; 423 -3.8; 452 -3.2; 484 -2.8; 518 -2.3; 554 -1.6; 593 -1.0; 635 -0.5; 679 -0.3; 726 0.0; 777 0.5; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.1; 1336 -1.6; 1429 -2.4; 1529 -3.6; 1636 -4.6; 1751 -5.5; 1873 -6.1; 2004 -6.7; 2145 -7.4; 2295 -8.2; 2455 -9.2; 2627 -10.8; 2811 -11.9; 3008 -10.7; 3219 -7.9; 3444 -5.3; 3685 -3.9; 3943 -3.9; 4219 -5.6; 4514 -7.5; 4830 -9.1; 5168 -10.8; 5530 -12.7; 5917 -11.7; 6331 -8.7; 6775 -7.0; 7249 -7.2; 7756 -9.3; 8299 -11.4; 8880 -10.4; 9502 -5.6; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.5; 15258 -2.9; 16326 -0.5; 17469 0.0; 18692 0.0; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.1dB` and instead set Global volume in the UI for both channels to **-11**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C551K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.19 | -10.6 dB |
| Peaking | 192 Hz   | 0.85 | -6.6 dB  |
| Peaking | 2564 Hz  | 2.02 | -9.4 dB  |
| Peaking | 6256 Hz  | 1.17 | -10.3 dB |
| Peaking | 23995 Hz | 2.13 | -8.7 dB  |
| Peaking | 3898 Hz  | 3.88 | 5.2 dB   |
| Peaking | 5842 Hz  | 1.04 | -4.6 dB  |
| Peaking | 6813 Hz  | 3.67 | 8.0 dB   |
| Peaking | 8745 Hz  | 3.71 | -8.1 dB  |
| Peaking | 10285 Hz | 2.22 | 6.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C551K/Denon%20AH-C551K.png)