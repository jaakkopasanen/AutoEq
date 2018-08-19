# Signature Acoustics Elements C12

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 -7.4; 22 -7.9; 23 -8.2; 25 -8.6; 26 -8.8; 28 -9.2; 30 -9.5; 32 -9.8; 35 -10.3; 37 -10.6; 40 -10.9; 42 -11.1; 45 -11.4; 49 -11.7; 52 -11.9; 56 -12.2; 59 -12.5; 64 -12.8; 68 -13.1; 73 -13.4; 78 -13.7; 83 -13.9; 89 -14.2; 95 -14.6; 102 -14.7; 109 -14.7; 117 -14.8; 125 -15.0; 134 -15.0; 143 -15.1; 153 -15.1; 164 -15.0; 175 -14.9; 188 -14.7; 201 -14.6; 215 -14.3; 230 -14.0; 246 -13.7; 263 -13.4; 282 -13.0; 301 -12.6; 323 -12.2; 345 -11.6; 369 -11.1; 395 -10.6; 423 -9.8; 452 -9.2; 484 -8.7; 518 -8.0; 554 -7.1; 593 -6.2; 635 -5.3; 679 -4.7; 726 -3.8; 777 -2.9; 832 -2.1; 890 -1.3; 952 -0.6; 1019 0.2; 1090 0.9; 1167 1.6; 1248 2.1; 1336 2.1; 1429 0.9; 1529 -0.5; 1636 -1.7; 1751 -2.0; 1873 -2.5; 2004 -2.7; 2145 -2.4; 2295 -1.9; 2455 -0.8; 2627 0.4; 2811 1.3; 3008 2.4; 3219 3.2; 3444 3.4; 3685 2.6; 3943 1.1; 4219 -1.6; 4514 -3.8; 4830 -5.3; 5168 -6.6; 5530 -8.5; 5917 -9.6; 6331 -8.0; 6775 -5.4; 7249 -3.4; 7756 -2.2; 8299 -2.2; 8880 -3.2; 9502 -4.5; 10167 -4.5; 10879 -1.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.6; 16326 -4.6; 17469 -6.7; 18692 -5.3; 20000 -1.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.563088052860216dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Signature Acoustics Elements C12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.3  | -11.0 dB |
| Peaking | 185 Hz   | 0.7  | -7.9 dB  |
| Peaking | 398 Hz   | 1.33 | -5.1 dB  |
| Peaking | 5922 Hz  | 3.09 | -10.0 dB |
| Peaking | 17827 Hz | 2.04 | -7.3 dB  |
| Peaking | 1268 Hz  | 1.61 | 7.7 dB   |
| Peaking | 1983 Hz  | 0.7  | -9.5 dB  |
| Peaking | 3559 Hz  | 0.92 | 12.7 dB  |
| Peaking | 4612 Hz  | 1.87 | -7.9 dB  |
| Peaking | 9689 Hz  | 4.69 | -4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Signature%20Acoustics%20Elements%20C12/Signature%20Acoustics%20Elements%20C12.png)