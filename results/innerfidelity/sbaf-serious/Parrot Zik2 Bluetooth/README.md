# Parrot Zik2 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -11.5; 22 -11.1; 23 -10.9; 25 -10.4; 26 -10.1; 28 -9.5; 30 -9.0; 32 -8.4; 35 -7.7; 37 -7.3; 40 -6.8; 42 -6.4; 45 -6.0; 49 -5.5; 52 -5.2; 56 -4.8; 59 -4.5; 64 -4.0; 68 -3.7; 73 -3.3; 78 -2.9; 83 -2.6; 89 -2.3; 95 -1.9; 102 -1.5; 109 -1.1; 117 -0.7; 125 -0.5; 134 -0.2; 143 0.1; 153 0.2; 164 0.4; 175 0.6; 188 0.8; 201 1.1; 215 1.3; 230 1.5; 246 1.5; 263 1.7; 282 1.9; 301 2.0; 323 2.2; 345 2.5; 369 2.6; 395 2.6; 423 2.8; 452 3.0; 484 3.0; 518 3.0; 554 3.1; 593 3.3; 635 3.5; 679 3.4; 726 3.3; 777 3.0; 832 2.2; 890 1.3; 952 0.6; 1019 -0.2; 1090 -0.5; 1167 -1.0; 1248 -1.9; 1336 -2.5; 1429 -3.5; 1529 -5.0; 1636 -6.7; 1751 -8.0; 1873 -7.8; 2004 -7.5; 2145 -6.8; 2295 -6.0; 2455 -4.5; 2627 -1.9; 2811 0.6; 3008 2.6; 3219 5.7; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 3.6; 5168 0.3; 5530 1.3; 5917 2.0; 6331 3.8; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -5.7; 10167 -7.0; 10879 -6.1; 11640 -4.8; 12455 -3.9; 13327 -3.0; 14260 -1.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000670943735dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Parrot Zik2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.59 | -11.2 dB |
| Peaking | 63 Hz    | 0.93 | -1.3 dB  |
| Peaking | 1904 Hz  | 0.77 | -26.2 dB |
| Peaking | 2889 Hz  | 0.2  | 18.9 dB  |
| Peaking | 10521 Hz | 0.92 | -14.4 dB |
| Peaking | 669 Hz   | 4.69 | 1.1 dB   |
| Peaking | 2491 Hz  | 4.66 | -3.5 dB  |
| Peaking | 3673 Hz  | 1.48 | 2.9 dB   |
| Peaking | 5262 Hz  | 4.88 | -5.5 dB  |
| Peaking | 6611 Hz  | 8.91 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Parrot%20Zik2%20Bluetooth/Parrot%20Zik2%20Bluetooth.png)