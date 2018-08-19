# Beats Solo3 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 10 -84; 20 -4.8; 22 -5.1; 23 -5.3; 25 -5.5; 26 -5.6; 28 -5.8; 30 -5.9; 32 -6.0; 35 -6.1; 37 -6.2; 40 -6.3; 42 -6.3; 45 -6.4; 49 -6.5; 52 -6.6; 56 -6.7; 59 -6.8; 64 -6.9; 68 -6.9; 73 -7.0; 78 -7.2; 83 -7.3; 89 -7.5; 95 -7.7; 102 -8.0; 109 -8.1; 117 -8.0; 125 -8.1; 134 -8.2; 143 -8.4; 153 -8.6; 164 -8.4; 175 -8.1; 188 -8.3; 201 -8.2; 215 -7.9; 230 -7.7; 246 -7.3; 263 -6.8; 282 -6.2; 301 -5.7; 323 -5.1; 345 -4.8; 369 -4.3; 395 -3.5; 423 -2.8; 452 -2.6; 484 -2.6; 518 -2.2; 554 -1.6; 593 -0.9; 635 -0.5; 679 -0.2; 726 0.2; 777 0.4; 832 0.4; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.2; 1429 -1.6; 1529 -1.8; 1636 -1.9; 1751 -2.0; 1873 -1.6; 2004 -1.1; 2145 -0.9; 2295 -0.9; 2455 -0.6; 2627 -0.7; 2811 -1.2; 3008 -1.5; 3219 -2.1; 3444 -2.6; 3685 -2.3; 3943 -0.8; 4219 -1.0; 4514 -2.7; 4830 -2.4; 5168 -0.8; 5530 1.2; 5917 1.9; 6331 0.9; 6775 1.0; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.034826328418015dB` and instead set Global volume in the UI for both channels to **-20**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.33 | -5.7 dB |
| Peaking | 140 Hz  | 0.83 | -4.4 dB |
| Peaking | 251 Hz  | 1.18 | -4.0 dB |
| Peaking | 1665 Hz | 3.46 | -1.9 dB |
| Peaking | 3498 Hz | 2.75 | -2.4 dB |
| Peaking | 492 Hz  | 3.06 | -0.7 dB |
| Peaking | 770 Hz  | 2.61 | 1.3 dB  |
| Peaking | 4823 Hz | 6.04 | -3.6 dB |
| Peaking | 5718 Hz | 2.47 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo3%20Bluetooth/Beats%20Solo3%20Bluetooth.png)