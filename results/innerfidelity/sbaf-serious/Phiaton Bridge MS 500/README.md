# Phiaton Bridge MS 500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.5; 22 3.0; 23 2.8; 25 2.4; 26 2.2; 28 1.9; 30 1.7; 32 1.4; 35 1.1; 37 1.0; 40 0.8; 42 0.6; 45 0.5; 49 0.3; 52 0.1; 56 0.0; 59 0.0; 64 -0.0; 68 -0.1; 73 -0.3; 78 -0.4; 83 -0.4; 89 -0.3; 95 -0.2; 102 0.1; 109 0.3; 117 -0.0; 125 -0.2; 134 -0.0; 143 0.3; 153 0.8; 164 1.6; 175 1.9; 188 2.4; 201 3.1; 215 3.8; 230 4.6; 246 5.2; 263 5.7; 282 6.0; 301 6.0; 323 5.7; 345 5.6; 369 5.3; 395 5.0; 423 4.6; 452 4.2; 484 3.6; 518 3.0; 554 2.7; 593 2.4; 635 1.9; 679 1.6; 726 1.3; 777 0.9; 832 0.5; 890 0.7; 952 0.6; 1019 -0.2; 1090 -0.4; 1167 -0.3; 1248 -0.3; 1336 -0.2; 1429 0.2; 1529 0.7; 1636 0.5; 1751 -0.3; 1873 -0.1; 2004 1.2; 2145 2.7; 2295 4.1; 2455 5.6; 2627 6.0; 2811 6.0; 3008 5.3; 3219 4.0; 3444 3.0; 3685 2.3; 3943 1.8; 4219 2.9; 4514 4.5; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge MS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.92 | 3.2 dB  |
| Peaking | 318 Hz   | 1.21 | 6.4 dB  |
| Peaking | 2685 Hz  | 3.36 | 6.1 dB  |
| Peaking | 5688 Hz  | 1.83 | 7.0 dB  |
| Peaking | 7988 Hz  | 2.11 | -2.2 dB |
| Peaking | 104 Hz   | 1.34 | -0.8 dB |
| Peaking | 536 Hz   | 2.43 | 0.6 dB  |
| Peaking | 1140 Hz  | 3.43 | -1.2 dB |
| Peaking | 1813 Hz  | 9.27 | -1.5 dB |
| Peaking | 24000 Hz | 1.89 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Bridge%20MS%20500/Phiaton%20Bridge%20MS%20500.png)