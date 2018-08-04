# Parrot Zik2 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -11.5; 22 -11.1; 23 -10.9; 25 -10.4; 26 -10.1; 28 -9.5; 30 -8.9; 32 -8.4; 35 -7.6; 37 -7.2; 40 -6.6; 42 -6.3; 45 -5.8; 49 -5.3; 52 -4.9; 56 -4.4; 59 -4.1; 64 -3.5; 68 -3.1; 73 -2.6; 78 -2.1; 83 -1.8; 89 -1.5; 95 -1.2; 102 -1.0; 109 -0.7; 117 -0.5; 125 -0.5; 134 -0.3; 143 -0.1; 153 -0.0; 164 0.1; 175 0.4; 188 0.6; 201 0.9; 215 1.1; 230 1.4; 246 1.4; 263 1.6; 282 1.8; 301 2.0; 323 2.2; 345 2.5; 369 2.6; 395 2.6; 423 2.8; 452 2.9; 484 3.0; 518 2.9; 554 3.1; 593 3.3; 635 3.5; 679 3.4; 726 3.3; 777 3.0; 832 2.2; 890 1.3; 952 0.6; 1019 -0.2; 1090 -0.5; 1167 -1.0; 1248 -1.9; 1336 -2.5; 1429 -3.5; 1529 -5.0; 1636 -6.7; 1751 -8.0; 1873 -7.8; 2004 -7.5; 2145 -6.8; 2295 -6.0; 2455 -4.5; 2627 -1.9; 2811 0.6; 3008 2.6; 3219 5.7; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 3.6; 5168 0.3; 5530 1.3; 5917 2.0; 6331 3.8; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -5.7; 10167 -7.0; 10879 -6.1; 11640 -4.8; 12455 -3.9; 13327 -3.0; 14260 -1.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Parrot Zik2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.65 | -10.6 dB |
| Peaking | 41 Hz    | 0.67 | -1.8 dB  |
| Peaking | 1903 Hz  | 0.8  | -25.3 dB |
| Peaking | 2853 Hz  | 0.21 | 17.8 dB  |
| Peaking | 10474 Hz | 0.96 | -14.0 dB |
| Peaking | 2773 Hz  | 4.94 | -1.6 dB  |
| Peaking | 2408 Hz  | 6.35 | -3.1 dB  |
| Peaking | 3458 Hz  | 1.66 | 3.1 dB   |
| Peaking | 5276 Hz  | 5.23 | -5.3 dB  |
| Peaking | 6621 Hz  | 8.79 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Parrot%20Zik2%20Bluetooth/Parrot%20Zik2%20Bluetooth.png)