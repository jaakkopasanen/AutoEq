# Bowers & Wilkins P5 Series 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 -6.5; 22 -7.0; 23 -7.2; 25 -7.6; 26 -7.7; 28 -8.0; 30 -8.3; 32 -8.5; 35 -8.6; 37 -8.7; 40 -8.8; 42 -8.9; 45 -9.0; 49 -9.0; 52 -9.1; 56 -9.1; 59 -9.1; 64 -9.1; 68 -9.1; 73 -9.1; 78 -9.1; 83 -9.1; 89 -9.2; 95 -9.4; 102 -9.5; 109 -9.7; 117 -9.8; 125 -9.9; 134 -9.9; 143 -9.8; 153 -9.8; 164 -9.7; 175 -9.1; 188 -9.0; 201 -8.7; 215 -8.3; 230 -7.8; 246 -7.1; 263 -6.2; 282 -5.1; 301 -4.5; 323 -4.0; 345 -3.1; 369 -2.0; 395 -0.8; 423 0.5; 452 1.5; 484 2.5; 518 3.4; 554 4.0; 593 4.4; 635 4.3; 679 3.8; 726 3.3; 777 2.9; 832 2.1; 890 1.4; 952 0.6; 1019 -0.2; 1090 -0.9; 1167 -1.7; 1248 -2.7; 1336 -3.7; 1429 -4.9; 1529 -6.0; 1636 -6.5; 1751 -6.9; 1873 -7.0; 2004 -6.8; 2145 -6.4; 2295 -6.1; 2455 -5.1; 2627 -3.7; 2811 -2.0; 3008 -1.1; 3219 -0.7; 3444 0.2; 3685 -0.4; 3943 -1.5; 4219 -2.9; 4514 -3.6; 4830 -3.5; 5168 -2.9; 5530 -2.6; 5917 -1.3; 6331 -0.4; 6775 1.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.0; 17469 -1.1; 18692 -1.6; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.0dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Series 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 5 Hz     | 1.79 | -5.8 dB |
| Peaking | 35 Hz    | 0.41 | -7.2 dB |
| Peaking | 178 Hz   | 0.49 | -8.7 dB |
| Peaking | 588 Hz   | 1.01 | 8.0 dB  |
| Peaking | 1797 Hz  | 1.27 | -7.9 dB |
| Peaking | 2415 Hz  | 4.55 | -1.8 dB |
| Peaking | 3566 Hz  | 1.64 | 4.0 dB  |
| Peaking | 4534 Hz  | 2.01 | -5.1 dB |
| Peaking | 6910 Hz  | 6.48 | 3.1 dB  |
| Peaking | 29043 Hz | 2.44 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Series%202/Bowers%20&%20Wilkins%20P5%20Series%202.png)