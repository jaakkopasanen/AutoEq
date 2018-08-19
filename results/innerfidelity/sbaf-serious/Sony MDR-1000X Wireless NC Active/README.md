# Sony MDR-1000X Wireless NC Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 10 -84; 20 -5.8; 22 -5.5; 23 -5.3; 25 -5.1; 26 -4.9; 28 -4.7; 30 -4.5; 32 -4.3; 35 -4.1; 37 -4.0; 40 -3.8; 42 -3.8; 45 -3.7; 49 -3.8; 52 -3.8; 56 -3.9; 59 -3.9; 64 -4.1; 68 -4.3; 73 -4.5; 78 -4.7; 83 -5.0; 89 -5.3; 95 -5.6; 102 -5.8; 109 -5.9; 117 -6.0; 125 -6.2; 134 -6.3; 143 -6.3; 153 -6.3; 164 -6.1; 175 -5.7; 188 -5.6; 201 -5.3; 215 -4.8; 230 -4.3; 246 -4.0; 263 -4.3; 282 -4.3; 301 -4.0; 323 -3.4; 345 -2.6; 369 -2.0; 395 -1.7; 423 -2.0; 452 -2.5; 484 -2.7; 518 -2.9; 554 -1.9; 593 -0.7; 635 -1.0; 679 -2.6; 726 -3.2; 777 -0.8; 832 -0.1; 890 -0.6; 952 -0.4; 1019 0.1; 1090 1.2; 1167 2.8; 1248 1.5; 1336 1.6; 1429 -0.5; 1529 -1.9; 1636 -2.8; 1751 -5.3; 1873 -5.6; 2004 -5.5; 2145 -5.4; 2295 -3.7; 2455 -2.2; 2627 -0.5; 2811 -0.6; 3008 -1.9; 3219 -2.4; 3444 -2.6; 3685 -2.7; 3943 -5.4; 4219 -7.2; 4514 -6.4; 4830 -4.0; 5168 -4.0; 5530 -6.7; 5917 -7.5; 6331 -5.9; 6775 -1.7; 7249 -1.4; 7756 -3.0; 8299 -4.9; 8880 -5.7; 9502 -4.8; 10167 -3.0; 10879 -1.5; 11640 -0.7; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.962923419995787dB` and instead set Global volume in the UI for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wireless NC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.68 | -5.4 dB |
| Peaking | 141 Hz   | 0.52 | -6.0 dB |
| Peaking | 1936 Hz  | 4.6  | -5.6 dB |
| Peaking | 5542 Hz  | 0.96 | -5.8 dB |
| Peaking | 24000 Hz | 2.28 | -4.4 dB |
| Peaking | 1059 Hz  | 0.91 | -1.2 dB |
| Peaking | 1183 Hz  | 3.39 | 4.6 dB  |
| Peaking | 7170 Hz  | 6.09 | 5.5 dB  |
| Peaking | 9099 Hz  | 1.66 | -4.6 dB |
| Peaking | 11346 Hz | 1.37 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wireless%20NC%20Active/Sony%20MDR-1000X%20Wireless%20NC%20Active.png)