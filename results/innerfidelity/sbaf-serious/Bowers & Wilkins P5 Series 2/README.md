# Bowers & Wilkins P5 Series 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 10 -84; 20 -6.5; 22 -7.0; 23 -7.2; 25 -7.6; 26 -7.8; 28 -8.1; 30 -8.3; 32 -8.5; 35 -8.7; 37 -8.8; 40 -8.9; 42 -9.0; 45 -9.1; 49 -9.3; 52 -9.3; 56 -9.4; 59 -9.5; 64 -9.7; 68 -9.7; 73 -9.8; 78 -9.9; 83 -9.9; 89 -10.0; 95 -10.1; 102 -10.0; 109 -10.1; 117 -10.0; 125 -9.9; 134 -9.7; 143 -9.6; 153 -9.6; 164 -9.4; 175 -8.9; 188 -8.8; 201 -8.6; 215 -8.2; 230 -7.6; 246 -7.0; 263 -6.1; 282 -5.1; 301 -4.4; 323 -4.0; 345 -3.1; 369 -1.9; 395 -0.8; 423 0.5; 452 1.5; 484 2.5; 518 3.4; 554 4.0; 593 4.4; 635 4.3; 679 3.8; 726 3.3; 777 2.9; 832 2.1; 890 1.4; 952 0.6; 1019 -0.2; 1090 -0.9; 1167 -1.7; 1248 -2.7; 1336 -3.7; 1429 -4.9; 1529 -6.0; 1636 -6.5; 1751 -6.9; 1873 -7.0; 2004 -6.8; 2145 -6.4; 2295 -6.1; 2455 -5.1; 2627 -3.7; 2811 -2.0; 3008 -1.1; 3219 -0.7; 3444 0.2; 3685 -0.4; 3943 -1.5; 4219 -2.9; 4514 -3.6; 4830 -3.5; 5168 -2.9; 5530 -2.6; 5917 -1.3; 6331 -0.4; 6775 1.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.0; 17469 -1.1; 18692 -1.6; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.545341642498066dB` and instead set Global volume in the UI for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 Series 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -4.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.3  | -7.5 dB |
| Peaking | 199 Hz   | 0.44 | -7.3 dB |
| Peaking | 581 Hz   | 0.95 | 8.6 dB  |
| Peaking | 1795 Hz  | 1.26 | -7.9 dB |
| Peaking | 2385 Hz  | 4.95 | -1.7 dB |
| Peaking | 3515 Hz  | 1.8  | 3.8 dB  |
| Peaking | 4569 Hz  | 2.01 | -4.8 dB |
| Peaking | 6971 Hz  | 6.32 | 3.2 dB  |
| Peaking | 18629 Hz | 2.45 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5%20Series%202/Bowers%20&%20Wilkins%20P5%20Series%202.png)