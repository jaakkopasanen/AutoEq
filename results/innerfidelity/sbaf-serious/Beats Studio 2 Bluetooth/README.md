# Beats Studio 2 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.8; 37 5.6; 40 5.3; 42 5.1; 45 5.0; 49 4.9; 52 4.8; 56 4.7; 59 4.7; 64 4.7; 68 4.6; 73 4.4; 78 4.3; 83 4.1; 89 3.8; 95 3.6; 102 3.4; 109 3.2; 117 3.1; 125 2.9; 134 2.8; 143 2.8; 153 2.9; 164 3.0; 175 3.2; 188 3.3; 201 3.5; 215 3.8; 230 4.1; 246 4.3; 263 4.7; 282 5.2; 301 5.5; 323 5.9; 345 6.0; 369 6.0; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 6.0; 554 6.0; 593 5.0; 635 3.6; 679 2.4; 726 1.1; 777 0.3; 832 -0.3; 890 -0.6; 952 -0.5; 1019 0.3; 1090 1.3; 1167 0.8; 1248 0.4; 1336 0.4; 1429 1.0; 1529 1.5; 1636 2.0; 1751 2.7; 1873 3.7; 2004 4.5; 2145 5.1; 2295 5.4; 2455 5.8; 2627 5.6; 2811 5.0; 3008 4.2; 3219 2.2; 3444 1.2; 3685 1.2; 3943 1.8; 4219 3.7; 4514 5.8; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio 2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.15 | 6.0 dB  |
| Peaking | 526 Hz  | 3.36 | 4.2 dB  |
| Peaking | 332 Hz  | 1.36 | 5.2 dB  |
| Peaking | 2372 Hz | 2.3  | 5.8 dB  |
| Peaking | 5399 Hz | 2.37 | 6.6 dB  |
| Peaking | 871 Hz  | 3.5  | -2.2 dB |
| Peaking | 3571 Hz | 7.13 | -1.9 dB |
| Peaking | 2050 Hz | 0.21 | 0.4 dB  |
| Peaking | 6507 Hz | 6.85 | 2.7 dB  |
| Peaking | 7687 Hz | 1.83 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Studio%202%20Bluetooth/Beats%20Studio%202%20Bluetooth.png)