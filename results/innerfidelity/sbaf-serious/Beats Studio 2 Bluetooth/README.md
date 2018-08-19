# Beats Studio 2 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.7; 37 5.5; 40 5.2; 42 5.0; 45 4.8; 49 4.7; 52 4.5; 56 4.4; 59 4.3; 64 4.1; 68 4.0; 73 3.7; 78 3.5; 83 3.3; 89 3.1; 95 2.8; 102 2.8; 109 2.8; 117 2.9; 125 2.9; 134 2.9; 143 3.0; 153 3.1; 164 3.2; 175 3.4; 188 3.5; 201 3.7; 215 4.0; 230 4.2; 246 4.4; 263 4.8; 282 5.2; 301 5.5; 323 6.0; 345 6.0; 369 6.0; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 6.0; 554 6.0; 593 5.0; 635 3.6; 679 2.4; 726 1.1; 777 0.3; 832 -0.3; 890 -0.6; 952 -0.5; 1019 0.3; 1090 1.3; 1167 0.8; 1248 0.4; 1336 0.4; 1429 1.0; 1529 1.5; 1636 2.0; 1751 2.7; 1873 3.7; 2004 4.5; 2145 5.1; 2295 5.4; 2455 5.8; 2627 5.6; 2811 5.0; 3008 4.2; 3219 2.2; 3444 1.2; 3685 1.2; 3943 1.8; 4219 3.7; 4514 5.8; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio 2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.16 | 6.1 dB  |
| Peaking | 319 Hz  | 1.19 | 5.3 dB  |
| Peaking | 522 Hz  | 3.25 | 4.1 dB  |
| Peaking | 2374 Hz | 2.31 | 5.8 dB  |
| Peaking | 5398 Hz | 2.37 | 6.6 dB  |
| Peaking | 878 Hz  | 3.43 | -2.3 dB |
| Peaking | 2008 Hz | 0.2  | 0.4 dB  |
| Peaking | 3588 Hz | 7.1  | -1.9 dB |
| Peaking | 6583 Hz | 6.82 | 2.7 dB  |
| Peaking | 7668 Hz | 1.82 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Studio%202%20Bluetooth/Beats%20Studio%202%20Bluetooth.png)