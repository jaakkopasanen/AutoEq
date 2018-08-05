# Sony MDR-1000X Wireless NC Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 10 -84; 20 -5.8; 22 -5.5; 23 -5.3; 25 -5.0; 26 -4.9; 28 -4.7; 30 -4.4; 32 -4.2; 35 -4.0; 37 -3.9; 40 -3.7; 42 -3.7; 45 -3.6; 49 -3.5; 52 -3.5; 56 -3.5; 59 -3.5; 64 -3.6; 68 -3.7; 73 -3.8; 78 -4.0; 83 -4.2; 89 -4.5; 95 -4.8; 102 -5.2; 109 -5.5; 117 -5.8; 125 -6.2; 134 -6.4; 143 -6.5; 153 -6.5; 164 -6.3; 175 -5.9; 188 -5.8; 201 -5.5; 215 -4.9; 230 -4.4; 246 -4.1; 263 -4.4; 282 -4.4; 301 -4.1; 323 -3.5; 345 -2.7; 369 -2.0; 395 -1.8; 423 -2.1; 452 -2.5; 484 -2.7; 518 -2.9; 554 -1.9; 593 -0.7; 635 -1.0; 679 -2.6; 726 -3.2; 777 -0.8; 832 -0.1; 890 -0.6; 952 -0.4; 1019 0.1; 1090 1.2; 1167 2.8; 1248 1.5; 1336 1.6; 1429 -0.5; 1529 -1.9; 1636 -2.8; 1751 -5.3; 1873 -5.6; 2004 -5.5; 2145 -5.4; 2295 -3.7; 2455 -2.2; 2627 -0.5; 2811 -0.6; 3008 -1.9; 3219 -2.4; 3444 -2.6; 3685 -2.7; 3943 -5.4; 4219 -7.2; 4514 -6.4; 4830 -4.0; 5168 -4.0; 5530 -6.7; 5917 -7.5; 6331 -5.9; 6775 -1.7; 7249 -1.4; 7756 -3.0; 8299 -4.9; 8880 -5.7; 9502 -4.8; 10167 -3.0; 10879 -1.5; 11640 -0.7; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.4dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wireless NC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.62 | -5.4 dB |
| Peaking | 155 Hz   | 0.6  | -6.1 dB |
| Peaking | 1935 Hz  | 4.56 | -5.5 dB |
| Peaking | 5541 Hz  | 0.96 | -5.8 dB |
| Peaking | 24000 Hz | 2.28 | -4.5 dB |
| Peaking | 1184 Hz  | 3.5  | 4.4 dB  |
| Peaking | 11276 Hz | 1.39 | 2.4 dB  |
| Peaking | 986 Hz   | 0.84 | -1.1 dB |
| Peaking | 7237 Hz  | 6.25 | 5.5 dB  |
| Peaking | 9137 Hz  | 1.71 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wireless%20NC%20Active/Sony%20MDR-1000X%20Wireless%20NC%20Active.png)