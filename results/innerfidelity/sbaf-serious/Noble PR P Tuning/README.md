# Noble PR P Tuning

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 3.7; 22 3.6; 23 3.5; 25 3.4; 26 3.3; 28 3.2; 30 3.1; 32 3.0; 35 2.8; 37 2.7; 40 2.6; 42 2.5; 45 2.4; 49 2.1; 52 1.9; 56 1.7; 59 1.6; 64 1.3; 68 1.1; 73 0.8; 78 0.5; 83 0.2; 89 -0.1; 95 -0.4; 102 -0.7; 109 -0.8; 117 -1.0; 125 -1.3; 134 -1.5; 143 -1.6; 153 -1.8; 164 -1.9; 175 -2.0; 188 -2.1; 201 -2.2; 215 -2.1; 230 -2.2; 246 -2.1; 263 -2.1; 282 -2.0; 301 -1.9; 323 -1.9; 345 -1.8; 369 -1.6; 395 -1.6; 423 -1.3; 452 -1.1; 484 -1.0; 518 -0.8; 554 -0.5; 593 -0.1; 635 0.0; 679 0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.2; 952 0.0; 1019 -0.1; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.0; 1529 -1.3; 1636 -1.5; 1751 -1.5; 1873 -1.3; 2004 -1.2; 2145 -1.1; 2295 -1.1; 2455 -0.7; 2627 -0.2; 2811 0.7; 3008 2.5; 3219 3.9; 3444 4.8; 3685 4.4; 3943 2.5; 4219 -0.8; 4514 -3.3; 4830 -5.1; 5168 -6.6; 5530 -8.3; 5917 -8.5; 6331 -7.4; 6775 -6.4; 7249 -6.1; 7756 -6.8; 8299 -7.6; 8880 -6.5; 9502 -3.3; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.6; 17469 -0.3; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.955111361763682dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble PR P Tuning ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.36 | 3.6 dB  |
| Peaking | 194 Hz   | 0.63 | -2.5 dB |
| Peaking | 3570 Hz  | 3.65 | 7.6 dB  |
| Peaking | 5691 Hz  | 1.8  | -8.8 dB |
| Peaking | 8377 Hz  | 4.74 | -5.7 dB |
| Peaking | 803 Hz   | 2.1  | 1.0 dB  |
| Peaking | 1864 Hz  | 1.4  | -1.4 dB |
| Peaking | 3085 Hz  | 7.89 | 1.5 dB  |
| Peaking | 10837 Hz | 4.5  | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noble%20PR%20P%20Tuning/Noble%20PR%20P%20Tuning.png)