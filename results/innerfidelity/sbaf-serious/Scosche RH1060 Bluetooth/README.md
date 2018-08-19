# Scosche RH1060 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 10 -84; 20 -1.7; 22 -2.5; 23 -2.9; 25 -3.5; 26 -3.8; 28 -4.3; 30 -4.7; 32 -5.1; 35 -5.5; 37 -5.7; 40 -6.0; 42 -6.2; 45 -6.4; 49 -6.7; 52 -6.8; 56 -7.0; 59 -7.2; 64 -7.3; 68 -7.5; 73 -7.6; 78 -7.7; 83 -7.8; 89 -8.0; 95 -8.0; 102 -8.0; 109 -8.0; 117 -7.9; 125 -7.8; 134 -7.7; 143 -7.7; 153 -7.9; 164 -7.6; 175 -6.6; 188 -6.6; 201 -6.5; 215 -6.0; 230 -5.6; 246 -5.5; 263 -4.9; 282 -3.6; 301 -2.6; 323 -1.9; 345 -0.7; 369 0.6; 395 1.9; 423 3.3; 452 3.8; 484 4.1; 518 4.2; 554 4.6; 593 4.6; 635 3.9; 679 2.9; 726 2.1; 777 1.6; 832 1.1; 890 0.7; 952 0.2; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.3; 1336 -0.1; 1429 -0.3; 1529 -0.7; 1636 -1.3; 1751 -1.8; 1873 -1.9; 2004 -1.7; 2145 -1.5; 2295 -1.6; 2455 -1.7; 2627 -1.8; 2811 -2.0; 3008 -2.1; 3219 -2.6; 3444 -2.2; 3685 -1.9; 3943 -1.4; 4219 -0.8; 4514 -1.3; 4830 -2.7; 5168 -1.8; 5530 1.3; 5917 3.1; 6331 4.2; 6775 3.9; 7249 1.3; 7756 -0.7; 8299 -2.0; 8880 -1.2; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.785920213985079dB` and instead set Global volume in the UI for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Scosche RH1060 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.42 | -5.9 dB |
| Peaking | 220 Hz  | 0.5  | -5.7 dB |
| Peaking | 492 Hz  | 1.12 | 8.5 dB  |
| Peaking | 3646 Hz | 0.47 | -2.4 dB |
| Peaking | 6369 Hz | 4.34 | 6.6 dB  |
| Peaking | 3326 Hz | 5.39 | -0.8 dB |
| Peaking | 4441 Hz | 2.84 | 1.4 dB  |
| Peaking | 4909 Hz | 8.01 | -3.0 dB |
| Peaking | 8307 Hz | 5.38 | -2.8 dB |
| Peaking | 9001 Hz | 1.21 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Scosche%20RH1060%20Bluetooth/Scosche%20RH1060%20Bluetooth.png)