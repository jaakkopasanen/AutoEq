# Beyerdynamic DTX 350 m

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.7; 22 4.3; 23 4.1; 25 3.8; 26 3.6; 28 3.3; 30 3.1; 32 2.9; 35 2.6; 37 2.5; 40 2.5; 42 2.5; 45 2.5; 49 2.1; 52 1.7; 56 1.4; 59 1.4; 64 1.4; 68 1.4; 73 1.6; 78 2.1; 83 2.6; 89 2.6; 95 1.9; 102 0.8; 109 -0.2; 117 -1.4; 125 -2.4; 134 -2.7; 143 -2.5; 153 -1.8; 164 -0.3; 175 0.3; 188 1.3; 201 2.6; 215 4.0; 230 5.0; 246 5.2; 263 5.2; 282 4.9; 301 4.6; 323 3.9; 345 2.9; 369 2.1; 395 1.7; 423 1.6; 452 1.4; 484 1.2; 518 0.9; 554 0.9; 593 1.0; 635 0.8; 679 0.5; 726 0.4; 777 0.4; 832 0.2; 890 0.1; 952 0.0; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.2; 1336 0.1; 1429 0.0; 1529 0.0; 1636 -0.2; 1751 -0.6; 1873 -0.6; 2004 -1.2; 2145 -1.3; 2295 -0.8; 2455 -0.2; 2627 0.5; 2811 0.9; 3008 1.7; 3219 2.6; 3444 4.7; 3685 6.0; 3943 3.2; 4219 -1.9; 4514 -1.5; 4830 0.7; 5168 3.1; 5530 3.4; 5917 1.6; 6331 0.3; 6775 -0.4; 7249 -0.5; 7756 -0.3; 8299 -0.9; 8880 -1.6; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.2; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DTX 350 m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.11 | 3.1 dB  |
| Peaking | 139 Hz   | 2.47 | -5.1 dB |
| Peaking | 260 Hz   | 1.64 | 5.4 dB  |
| Peaking | 3576 Hz  | 6.47 | 6.4 dB  |
| Peaking | 24000 Hz | 2.35 | 0.8 dB  |
| Peaking | 19 Hz    | 2.08 | 1.4 dB  |
| Peaking | 2084 Hz  | 5.25 | -1.6 dB |
| Peaking | 4346 Hz  | 9.84 | -3.8 dB |
| Peaking | 5356 Hz  | 6    | 3.9 dB  |
| Peaking | 8718 Hz  | 4.62 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DTX%20350%20m/Beyerdynamic%20DTX%20350%20m.png)