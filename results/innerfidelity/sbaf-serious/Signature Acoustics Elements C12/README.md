# Signature Acoustics Elements C12

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 10 -84; 20 -7.3; 22 -7.8; 23 -8.1; 25 -8.5; 26 -8.7; 28 -9.1; 30 -9.3; 32 -9.6; 35 -10.0; 37 -10.2; 40 -10.5; 42 -10.7; 45 -10.8; 49 -11.0; 52 -11.1; 56 -11.3; 59 -11.4; 64 -11.5; 68 -11.7; 73 -11.8; 78 -12.0; 83 -12.3; 89 -12.7; 95 -13.2; 102 -13.6; 109 -14.0; 117 -14.5; 125 -15.0; 134 -15.3; 143 -15.5; 153 -15.6; 164 -15.6; 175 -15.4; 188 -15.2; 201 -15.0; 215 -14.7; 230 -14.3; 246 -14.0; 263 -13.7; 282 -13.2; 301 -12.7; 323 -12.3; 345 -11.7; 369 -11.2; 395 -10.6; 423 -9.9; 452 -9.3; 484 -8.7; 518 -8.0; 554 -7.1; 593 -6.2; 635 -5.3; 679 -4.7; 726 -3.9; 777 -2.9; 832 -2.1; 890 -1.3; 952 -0.6; 1019 0.2; 1090 0.9; 1167 1.6; 1248 2.1; 1336 2.1; 1429 0.9; 1529 -0.5; 1636 -1.7; 1751 -2.0; 1873 -2.5; 2004 -2.7; 2145 -2.4; 2295 -1.9; 2455 -0.8; 2627 0.4; 2811 1.3; 3008 2.4; 3219 3.2; 3444 3.4; 3685 2.6; 3943 1.1; 4219 -1.6; 4514 -3.8; 4830 -5.3; 5168 -6.6; 5530 -8.5; 5917 -9.6; 6331 -8.0; 6775 -5.4; 7249 -3.4; 7756 -2.2; 8299 -2.2; 8880 -3.2; 9502 -4.5; 10167 -4.5; 10879 -1.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.6; 16326 -4.6; 17469 -6.7; 18692 -5.3; 20000 -1.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.0dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Signature Acoustics Elements C12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 6 Hz     | 1.85 | -6.4 dB  |
| Peaking | 63 Hz    | 0.22 | -10.0 dB |
| Peaking | 230 Hz   | 0.6  | -8.7 dB  |
| Peaking | 5914 Hz  | 3.13 | -10.0 dB |
| Peaking | 17828 Hz | 2.04 | -7.3 dB  |
| Peaking | 1261 Hz  | 1.26 | 9.6 dB   |
| Peaking | 1938 Hz  | 0.6  | -13.7 dB |
| Peaking | 3560 Hz  | 0.76 | 18.6 dB  |
| Peaking | 9626 Hz  | 3.68 | -5.6 dB  |
| Peaking | 4576 Hz  | 1.32 | -10.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Signature%20Acoustics%20Elements%20C12/Signature%20Acoustics%20Elements%20C12.png)