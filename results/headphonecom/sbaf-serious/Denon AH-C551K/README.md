# Denon AH-C551K

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 10 -84; 20 -10.6; 22 -10.7; 23 -10.8; 25 -10.9; 26 -10.9; 28 -11.0; 30 -11.1; 32 -11.1; 35 -11.1; 37 -11.1; 40 -11.1; 42 -11.1; 45 -11.2; 49 -11.2; 52 -11.2; 56 -11.2; 59 -11.3; 64 -11.6; 68 -11.6; 73 -11.6; 78 -11.6; 83 -11.7; 89 -11.6; 95 -11.6; 102 -11.5; 109 -11.3; 117 -11.2; 125 -11.0; 134 -10.8; 143 -10.6; 153 -10.2; 164 -9.8; 175 -9.5; 188 -10.0; 201 -10.0; 215 -9.5; 230 -9.0; 246 -8.4; 263 -7.9; 282 -7.3; 301 -6.8; 323 -6.2; 345 -5.6; 369 -4.9; 395 -4.4; 423 -3.8; 452 -3.2; 484 -2.7; 518 -2.2; 554 -1.6; 593 -1.1; 635 -0.6; 679 -0.2; 726 0.1; 777 0.4; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.1; 1336 -1.6; 1429 -2.4; 1529 -3.6; 1636 -4.6; 1751 -5.5; 1873 -6.1; 2004 -6.7; 2145 -7.4; 2295 -8.2; 2455 -9.3; 2627 -10.7; 2811 -11.8; 3008 -10.8; 3219 -7.9; 3444 -5.2; 3685 -3.8; 3943 -4.1; 4219 -5.6; 4514 -7.4; 4830 -9.0; 5168 -10.9; 5530 -12.7; 5917 -11.6; 6331 -8.7; 6775 -7.1; 7249 -7.3; 7756 -9.3; 8299 -11.2; 8880 -10.3; 9502 -5.7; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.5; 15258 -2.7; 16326 -0.4; 17469 0.0; 18692 0.0; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.5945006827314859dB` and instead set Global volume in the UI for both channels to **-5**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C551K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.26 | -11.4 dB |
| Peaking | 195 Hz   | 0.84 | -4.9 dB  |
| Peaking | 2564 Hz  | 2.02 | -9.4 dB  |
| Peaking | 6257 Hz  | 1.17 | -10.3 dB |
| Peaking | 24000 Hz | 2.11 | -8.7 dB  |
| Peaking | 3910 Hz  | 3.66 | 5.1 dB   |
| Peaking | 5913 Hz  | 1.05 | -4.9 dB  |
| Peaking | 6778 Hz  | 3.55 | 8.2 dB   |
| Peaking | 8761 Hz  | 3.52 | -8.0 dB  |
| Peaking | 10308 Hz | 2.16 | 6.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C551K/Denon%20AH-C551K.png)