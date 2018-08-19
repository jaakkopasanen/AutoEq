# Phiaton Chord MS530 Bluetooth

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.0; 22 3.4; 23 3.1; 25 2.7; 26 2.5; 28 2.1; 30 1.8; 32 1.5; 35 1.2; 37 1.0; 40 0.8; 42 0.6; 45 0.5; 49 0.2; 52 0.0; 56 -0.1; 59 -0.1; 64 -0.2; 68 -0.3; 73 -0.6; 78 -0.7; 83 -0.7; 89 -0.8; 95 -0.8; 102 -0.8; 109 -0.5; 117 -0.4; 125 -0.3; 134 0.1; 143 0.6; 153 0.9; 164 0.8; 175 1.6; 188 2.0; 201 1.9; 215 1.9; 230 2.0; 246 2.2; 263 2.7; 282 3.1; 301 3.3; 323 3.5; 345 3.6; 369 3.5; 395 3.4; 423 3.4; 452 3.3; 484 3.0; 518 2.8; 554 2.8; 593 2.9; 635 2.8; 679 2.5; 726 2.2; 777 2.0; 832 1.6; 890 1.2; 952 0.6; 1019 -0.1; 1090 -0.6; 1167 -1.1; 1248 -1.5; 1336 -2.0; 1429 -2.4; 1529 -1.3; 1636 0.1; 1751 -2.7; 1873 -2.2; 2004 -1.3; 2145 -0.0; 2295 1.0; 2455 2.4; 2627 3.9; 2811 5.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999259689dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 Bluetooth ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.09 | 4.0 dB  |
| Peaking | 100 Hz  | 1.01 | -1.8 dB |
| Peaking | 423 Hz  | 0.46 | 3.8 dB  |
| Peaking | 1632 Hz | 0.97 | -5.3 dB |
| Peaking | 3736 Hz | 0.89 | 7.9 dB  |
| Peaking | 1934 Hz | 7.73 | -1.1 dB |
| Peaking | 2909 Hz | 3.64 | 1.4 dB  |
| Peaking | 3806 Hz | 2.93 | -1.3 dB |
| Peaking | 6278 Hz | 2.43 | 5.3 dB  |
| Peaking | 7394 Hz | 1.53 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530%20Bluetooth/Phiaton%20Chord%20MS530%20Bluetooth.png)