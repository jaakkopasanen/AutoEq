# Phiaton MS 100 BA

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.3; 22 1.2; 23 1.1; 25 1.0; 26 0.9; 28 0.8; 30 0.7; 32 0.7; 35 0.6; 37 0.5; 40 0.4; 42 0.3; 45 0.3; 49 0.2; 52 0.2; 56 0.1; 59 0.0; 64 -0.1; 68 -0.2; 73 -0.3; 78 -0.5; 83 -0.8; 89 -1.2; 95 -1.6; 102 -2.2; 109 -2.7; 117 -3.3; 125 -3.8; 134 -4.3; 143 -4.6; 153 -4.8; 164 -4.9; 175 -5.0; 188 -4.9; 201 -4.9; 215 -4.8; 230 -4.7; 246 -4.6; 263 -4.4; 282 -4.2; 301 -4.0; 323 -3.8; 345 -3.6; 369 -3.4; 395 -3.1; 423 -2.7; 452 -2.4; 484 -2.2; 518 -1.8; 554 -1.4; 593 -0.9; 635 -0.5; 679 -0.4; 726 -0.1; 777 0.2; 832 0.2; 890 0.1; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.0; 1529 -1.3; 1636 -1.6; 1751 -1.7; 1873 -1.5; 2004 -1.2; 2145 -0.7; 2295 0.2; 2455 1.9; 2627 3.2; 2811 4.0; 3008 4.8; 3219 5.2; 3444 5.5; 3685 5.7; 3943 5.9; 4219 5.5; 4514 5.3; 4830 5.8; 5168 6.0; 5530 5.9; 5917 4.4; 6331 1.2; 6775 1.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton MS 100 BA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 0.37 | 1.5 dB  |
| Peaking | 187 Hz  | 0.64 | -5.9 dB |
| Peaking | 1864 Hz | 2.37 | -3.3 dB |
| Peaking | 3900 Hz | 1.11 | 6.6 dB  |
| Peaking | 3 Hz    | 1.9  | 0.8 dB  |
| Peaking | 801 Hz  | 3.37 | 1.0 dB  |
| Peaking | 4247 Hz | 6.23 | -0.7 dB |
| Peaking | 5446 Hz | 4.83 | 3.3 dB  |
| Peaking | 7327 Hz | 1.22 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20MS%20100%20BA/Phiaton%20MS%20100%20BA.png)