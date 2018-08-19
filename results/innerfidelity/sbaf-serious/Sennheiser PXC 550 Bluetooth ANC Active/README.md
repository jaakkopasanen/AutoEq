# Sennheiser PXC 550 Bluetooth ANC Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.7; 22 4.1; 23 3.5; 25 2.7; 26 2.4; 28 2.1; 30 2.1; 32 2.1; 35 2.2; 37 2.3; 40 2.5; 42 2.6; 45 2.8; 49 3.0; 52 3.1; 56 3.3; 59 3.4; 64 3.5; 68 3.6; 73 3.6; 78 3.6; 83 3.5; 89 3.3; 95 3.1; 102 2.7; 109 2.6; 117 2.4; 125 2.1; 134 1.8; 143 1.6; 153 1.5; 164 1.6; 175 1.8; 188 1.8; 201 1.9; 215 2.1; 230 2.4; 246 2.6; 263 2.8; 282 3.2; 301 3.4; 323 3.5; 345 3.6; 369 3.5; 395 3.4; 423 3.3; 452 3.2; 484 2.9; 518 2.6; 554 2.6; 593 2.6; 635 2.5; 679 2.2; 726 2.0; 777 2.0; 832 1.5; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -0.5; 1248 0.3; 1336 -1.1; 1429 -1.6; 1529 -2.1; 1636 -2.6; 1751 -1.8; 1873 -0.7; 2004 -0.9; 2145 -0.5; 2295 0.1; 2455 1.1; 2627 2.5; 2811 3.1; 3008 3.6; 3219 4.2; 3444 4.3; 3685 2.6; 3943 3.5; 4219 6.0; 4514 5.0; 4830 -2.1; 5168 -3.4; 5530 1.6; 5917 4.2; 6331 4.8; 6775 3.9; 7249 1.3; 7756 -0.4; 8299 -2.6; 8880 -4.3; 9502 -4.4; 10167 -2.1; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099993182728349dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Bluetooth ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 40 Hz    |  0.06 | 3.0 dB  |
| Peaking | 3557 Hz  |  2.52 | 4.5 dB  |
| Peaking | 6482 Hz  |  4.86 | 6.2 dB  |
| Peaking | 9434 Hz  |  2.06 | -6.8 dB |
| Peaking | 10796 Hz |  2.56 | 3.9 dB  |
| Peaking | 173 Hz   |  0.9  | -4.7 dB |
| Peaking | 210 Hz   |  0.47 | 3.5 dB  |
| Peaking | 1558 Hz  |  2.28 | -3.1 dB |
| Peaking | 4384 Hz  |  8.64 | 5.1 dB  |
| Peaking | 5001 Hz  | 10.49 | -6.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Bluetooth%20ANC%20Active/Sennheiser%20PXC%20550%20Bluetooth%20ANC%20Active.png)