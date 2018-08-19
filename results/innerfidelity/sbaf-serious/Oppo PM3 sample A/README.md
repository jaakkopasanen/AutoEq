# Oppo PM3 sample A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.9; 22 0.8; 23 0.8; 25 0.8; 26 0.8; 28 0.8; 30 0.8; 32 0.8; 35 0.8; 37 0.8; 40 0.8; 42 0.9; 45 0.9; 49 0.9; 52 0.9; 56 0.9; 59 0.9; 64 0.9; 68 0.8; 73 0.8; 78 0.7; 83 0.6; 89 0.5; 95 0.2; 102 0.2; 109 0.3; 117 0.4; 125 0.5; 134 0.6; 143 0.4; 153 -0.1; 164 0.6; 175 1.2; 188 0.8; 201 0.6; 215 0.6; 230 1.0; 246 1.4; 263 1.7; 282 2.2; 301 2.5; 323 2.6; 345 2.6; 369 2.4; 395 2.2; 423 2.0; 452 1.7; 484 1.3; 518 1.0; 554 1.0; 593 0.9; 635 0.8; 679 0.6; 726 0.5; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.3; 1336 -0.8; 1429 -1.3; 1529 -1.8; 1636 -2.6; 1751 -3.3; 1873 -3.8; 2004 -3.3; 2145 -3.0; 2295 -3.0; 2455 -2.4; 2627 -1.6; 2811 -0.6; 3008 0.5; 3219 0.9; 3444 0.9; 3685 1.4; 3943 1.9; 4219 1.9; 4514 2.4; 4830 4.6; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.098269946750707dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 1.77 | -0.8 dB |
| Peaking | 37 Hz   | 0.77 | 1.6 dB  |
| Peaking | 351 Hz  | 1.23 | 2.6 dB  |
| Peaking | 1961 Hz | 2.12 | -4.1 dB |
| Peaking | 5537 Hz | 2.41 | 6.8 dB  |
| Peaking | 844 Hz  | 3.89 | 0.4 dB  |
| Peaking | 2572 Hz | 4.38 | -1.4 dB |
| Peaking | 3046 Hz | 2.04 | 1.2 dB  |
| Peaking | 6579 Hz | 5.74 | 3.0 dB  |
| Peaking | 7210 Hz | 1.79 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3%20sample%20A/Oppo%20PM3%20sample%20A.png)