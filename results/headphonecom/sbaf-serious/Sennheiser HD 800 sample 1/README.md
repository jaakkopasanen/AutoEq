# Sennheiser HD 800 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 10 -84; 20 4.6; 22 4.2; 23 4.0; 25 3.6; 26 3.5; 28 3.2; 30 2.9; 32 2.7; 35 2.5; 37 2.3; 40 2.3; 42 2.5; 45 2.8; 49 2.8; 52 2.3; 56 1.8; 59 1.6; 64 1.2; 68 0.6; 73 0.0; 78 -0.4; 83 -0.6; 89 -1.0; 95 -1.1; 102 -1.3; 109 -1.5; 117 -1.8; 125 -1.9; 134 -2.2; 143 -2.5; 153 -2.6; 164 -2.5; 175 -2.6; 188 -2.8; 201 -2.8; 215 -2.8; 230 -2.8; 246 -2.8; 263 -2.8; 282 -2.5; 301 -2.4; 323 -2.3; 345 -2.1; 369 -2.0; 395 -1.9; 423 -1.9; 452 -1.7; 484 -1.5; 518 -1.4; 554 -1.2; 593 -1.0; 635 -0.9; 679 -0.8; 726 -0.6; 777 -0.5; 832 -0.4; 890 -0.3; 952 -0.1; 1019 0.0; 1090 0.5; 1167 1.0; 1248 1.4; 1336 1.9; 1429 1.9; 1529 1.6; 1636 1.3; 1751 1.6; 1873 1.9; 2004 1.8; 2145 1.9; 2295 2.5; 2455 3.2; 2627 3.1; 2811 3.2; 3008 2.8; 3219 2.4; 3444 2.4; 3685 1.2; 3943 -0.5; 4219 -1.3; 4514 -1.2; 4830 -1.0; 5168 -2.1; 5530 -4.8; 5917 -8.4; 6331 -5.9; 6775 -1.6; 7249 0.4; 7756 0.3; 8299 0.0; 8880 -0.7; 9502 -2.0; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 -0.3; 13327 -3.8; 14260 -5.4; 15258 -4.7; 16326 -2.8; 17469 -0.5; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.699975048152863dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.21 | 4.2 dB  |
| Peaking | 162 Hz   | 0.41 | -3.7 dB |
| Peaking | 2388 Hz  | 1.02 | 3.0 dB  |
| Peaking | 5928 Hz  | 5.46 | -9.2 dB |
| Peaking | 14617 Hz | 2.85 | -5.9 dB |
| Peaking | 1328 Hz  | 6.86 | 1.1 dB  |
| Peaking | 3519 Hz  | 3.68 | 1.9 dB  |
| Peaking | 4054 Hz  | 3.43 | -2.8 dB |
| Peaking | 9161 Hz  | 1.68 | 2.3 dB  |
| Peaking | 9442 Hz  | 5.16 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%20sample%201/Sennheiser%20HD%20800%20sample%201.png)