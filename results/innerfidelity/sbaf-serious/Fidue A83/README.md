# Fidue A83

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.3; 23 -1.4; 25 -1.7; 26 -1.8; 28 -2.0; 30 -2.1; 32 -2.3; 35 -2.4; 37 -2.5; 40 -2.6; 42 -2.6; 45 -2.7; 49 -2.7; 52 -2.7; 56 -2.8; 59 -2.8; 64 -2.9; 68 -2.9; 73 -3.0; 78 -3.1; 83 -3.2; 89 -3.6; 95 -4.0; 102 -4.4; 109 -4.8; 117 -5.2; 125 -5.6; 134 -5.9; 143 -6.1; 153 -6.1; 164 -6.2; 175 -5.9; 188 -5.8; 201 -5.6; 215 -5.3; 230 -4.9; 246 -4.6; 263 -4.3; 282 -3.9; 301 -3.6; 323 -3.2; 345 -2.6; 369 -2.5; 395 -2.1; 423 -1.5; 452 -1.2; 484 -1.0; 518 0.0; 554 0.5; 593 0.8; 635 1.1; 679 1.0; 726 1.2; 777 1.3; 832 1.2; 890 0.9; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.4; 1248 -2.4; 1336 -3.6; 1429 -5.0; 1529 -6.2; 1636 -7.1; 1751 -7.2; 1873 -6.6; 2004 -5.6; 2145 -4.7; 2295 -4.1; 2455 -3.8; 2627 -4.1; 2811 -4.3; 3008 -1.8; 3219 1.2; 3444 4.7; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.6; 6331 3.7; 6775 -0.0; 7249 -5.0; 7756 -8.5; 8299 -10.3; 8880 -10.0; 9502 -7.9; 10167 -4.3; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A83 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 164 Hz   | 0.49 | -6.2 dB  |
| Peaking | 1691 Hz  | 1.29 | -15.7 dB |
| Peaking | 2761 Hz  | 1.74 | -14.2 dB |
| Peaking | 3296 Hz  | 0.39 | 17.7 dB  |
| Peaking | 8443 Hz  | 1.89 | -19.6 dB |
| Peaking | 32 Hz    | 1.7  | -1.5 dB  |
| Peaking | 4737 Hz  | 3.53 | -2.0 dB  |
| Peaking | 6238 Hz  | 1.98 | 2.9 dB   |
| Peaking | 7269 Hz  | 5.89 | -3.8 dB  |
| Peaking | 16362 Hz | 1.53 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A83/Fidue%20A83.png)