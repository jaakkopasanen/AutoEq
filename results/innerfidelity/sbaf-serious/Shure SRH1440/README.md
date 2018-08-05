# Shure SRH1440

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.7; 83 5.2; 89 4.6; 95 4.0; 102 3.4; 109 2.9; 117 2.3; 125 1.7; 134 1.2; 143 0.7; 153 0.4; 164 0.3; 175 0.2; 188 -0.1; 201 -0.1; 215 -0.1; 230 -0.1; 246 -0.1; 263 -0.0; 282 0.0; 301 0.1; 323 0.1; 345 0.3; 369 0.3; 395 0.4; 423 0.7; 452 0.9; 484 0.9; 518 0.9; 554 1.2; 593 1.3; 635 1.8; 679 1.9; 726 1.4; 777 1.3; 832 0.8; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.7; 1248 -1.1; 1336 -1.6; 1429 -2.3; 1529 -3.2; 1636 -4.1; 1751 -4.9; 1873 -5.4; 2004 -5.5; 2145 -5.9; 2295 -6.0; 2455 -5.9; 2627 -5.6; 2811 -6.2; 3008 -6.2; 3219 -6.3; 3444 -6.4; 3685 -6.1; 3943 -5.8; 4219 -5.6; 4514 -4.9; 4830 -3.4; 5168 -1.8; 5530 -0.5; 5917 0.2; 6331 1.1; 6775 1.5; 7249 0.4; 7756 -1.8; 8299 -4.6; 8880 -7.0; 9502 -7.4; 10167 -5.2; 10879 -1.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1440 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.55 | 6.9 dB  |
| Peaking | 772 Hz   | 1.3  | 2.6 dB  |
| Peaking | 3011 Hz  | 0.61 | -7.0 dB |
| Peaking | 6454 Hz  | 2.16 | 5.3 dB  |
| Peaking | 9163 Hz  | 4.02 | -7.9 dB |
| Peaking | 18 Hz    | 1.04 | 2.6 dB  |
| Peaking | 41 Hz    | 1.05 | -1.7 dB |
| Peaking | 76 Hz    | 1.61 | 2.0 dB  |
| Peaking | 170 Hz   | 1.33 | -1.4 dB |
| Peaking | 11754 Hz | 4.98 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1440/Shure%20SRH1440.png)