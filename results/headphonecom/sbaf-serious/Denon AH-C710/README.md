# Denon AH-C710

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 10 -84; 20 -12.1; 22 -12.0; 23 -11.9; 25 -11.8; 26 -11.8; 28 -11.8; 30 -11.7; 32 -11.7; 35 -11.5; 37 -11.4; 40 -11.3; 42 -11.2; 45 -11.1; 49 -10.9; 52 -10.8; 56 -10.6; 59 -10.4; 64 -10.2; 68 -10.1; 73 -9.9; 78 -9.7; 83 -9.6; 89 -9.6; 95 -9.7; 102 -9.8; 109 -10.0; 117 -10.1; 125 -10.4; 134 -10.4; 143 -10.3; 153 -10.2; 164 -9.9; 175 -9.5; 188 -9.2; 201 -8.8; 215 -8.2; 230 -7.8; 246 -7.3; 263 -6.8; 282 -6.3; 301 -5.7; 323 -5.1; 345 -4.6; 369 -4.3; 395 -3.9; 423 -3.3; 452 -2.8; 484 -2.5; 518 -2.1; 554 -1.5; 593 -0.9; 635 -0.6; 679 -0.4; 726 -0.1; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.6; 1336 -1.1; 1429 -1.7; 1529 -2.2; 1636 -2.6; 1751 -2.9; 1873 -3.1; 2004 -3.6; 2145 -4.0; 2295 -4.5; 2455 -5.1; 2627 -5.9; 2811 -6.3; 3008 -5.2; 3219 -3.5; 3444 -1.5; 3685 -0.4; 3943 -0.4; 4219 -2.0; 4514 -3.6; 4830 -4.6; 5168 -5.7; 5530 -8.2; 5917 -10.8; 6331 -8.1; 6775 -4.4; 7249 -2.3; 7756 -1.1; 8299 -1.2; 8880 -2.4; 9502 -4.1; 10167 -4.3; 10879 -1.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.9dB` and instead set Global volume in the UI for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 1.15 | -11.8 dB |
| Peaking | 33 Hz   | 0.3  | -10.1 dB |
| Peaking | 176 Hz  | 0.75 | -6.6 dB  |
| Peaking | 2532 Hz | 2.08 | -5.7 dB  |
| Peaking | 5898 Hz | 3.63 | -10.4 dB |
| Peaking | 835 Hz  | 2.24 | 1.4 dB   |
| Peaking | 1647 Hz | 3.62 | -1.5 dB  |
| Peaking | 7691 Hz | 0.23 | 0.3 dB   |
| Peaking | 7693 Hz | 6.15 | 1.1 dB   |
| Peaking | 9790 Hz | 5.34 | -4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C710/Denon%20AH-C710.png)