# Sony MDR-1R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.5; 35 4.9; 37 4.5; 40 3.9; 42 3.6; 45 3.1; 49 2.6; 52 2.3; 56 1.9; 59 1.7; 64 1.4; 68 1.1; 73 0.7; 78 0.3; 83 -0.1; 89 -0.4; 95 -0.7; 102 -0.9; 109 -1.4; 117 -1.4; 125 -1.2; 134 -0.9; 143 -0.9; 153 -1.6; 164 -1.7; 175 0.0; 188 -0.7; 201 -1.2; 215 -1.4; 230 -1.3; 246 -0.9; 263 -0.7; 282 -0.3; 301 0.5; 323 1.2; 345 2.1; 369 3.0; 395 3.5; 423 3.9; 452 4.0; 484 3.7; 518 3.5; 554 3.4; 593 3.2; 635 2.7; 679 2.0; 726 2.0; 777 2.0; 832 1.4; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.8; 1429 -2.4; 1529 -3.1; 1636 -3.5; 1751 -3.4; 1873 -2.9; 2004 -2.3; 2145 -1.1; 2295 0.2; 2455 2.1; 2627 3.6; 2811 5.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.68 | 6.4 dB  |
| Peaking | 227 Hz  |  0.41 | -2.8 dB |
| Peaking | 462 Hz  |  1.03 | 6.0 dB  |
| Peaking | 1762 Hz |  1.63 | -6.3 dB |
| Peaking | 3748 Hz |  0.88 | 7.6 dB  |
| Peaking | 178 Hz  | 12.77 | 1.4 dB  |
| Peaking | 2948 Hz |  4.05 | 2.1 dB  |
| Peaking | 3535 Hz |  1.54 | -1.4 dB |
| Peaking | 6271 Hz |  2.29 | 5.5 dB  |
| Peaking | 7379 Hz |  1.53 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1R/Sony%20MDR-1R.png)