# Beats Powerbeats2 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.5; 22 -0.6; 23 -0.7; 25 -0.8; 26 -0.9; 28 -0.9; 30 -1.0; 32 -1.1; 35 -1.2; 37 -1.2; 40 -1.3; 42 -1.4; 45 -1.5; 49 -1.6; 52 -1.7; 56 -1.7; 59 -1.8; 64 -2.0; 68 -2.1; 73 -2.3; 78 -2.5; 83 -2.7; 89 -2.9; 95 -3.2; 102 -3.4; 109 -3.5; 117 -3.6; 125 -3.9; 134 -4.1; 143 -4.2; 153 -4.4; 164 -4.4; 175 -4.3; 188 -4.4; 201 -4.5; 215 -4.4; 230 -4.3; 246 -4.3; 263 -4.3; 282 -4.1; 301 -4.0; 323 -3.8; 345 -3.7; 369 -3.5; 395 -3.4; 423 -3.1; 452 -2.8; 484 -2.8; 518 -2.5; 554 -2.1; 593 -1.6; 635 -1.4; 679 -1.2; 726 -0.9; 777 -0.4; 832 -0.3; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.4; 1336 0.4; 1429 0.3; 1529 0.3; 1636 0.3; 1751 0.4; 1873 0.7; 2004 1.2; 2145 1.7; 2295 2.5; 2455 3.7; 2627 4.8; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.5; 4514 4.0; 4830 3.2; 5168 3.3; 5530 3.4; 5917 3.1; 6331 2.3; 6775 1.2; 7249 -0.3; 7756 -1.6; 8299 -2.5; 8880 -2.4; 9502 -1.4; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.3; 15258 -3.4; 16326 -4.0; 17469 -3.5; 18692 -3.3; 20000 -4.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999814356dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats2 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 68 Hz    | 0.29 | -0.9 dB |
| Peaking | 174 Hz   | 0.62 | -3.5 dB |
| Peaking | 386 Hz   | 1.08 | -1.7 dB |
| Peaking | 3493 Hz  | 1.34 | 6.8 dB  |
| Peaking | 18849 Hz | 0.54 | -3.8 dB |
| Peaking | 1862 Hz  | 3.06 | -0.9 dB |
| Peaking | 2712 Hz  | 6.81 | 1.2 dB  |
| Peaking | 5980 Hz  | 4.44 | 1.8 dB  |
| Peaking | 8358 Hz  | 3.36 | -3.1 dB |
| Peaking | 12275 Hz | 2.56 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Powerbeats2%20Bluetooth/Beats%20Powerbeats2%20Bluetooth.png)