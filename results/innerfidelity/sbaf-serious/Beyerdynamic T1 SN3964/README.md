# Beyerdynamic T1 sn3964

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 4.0; 22 3.5; 23 3.3; 25 2.9; 26 2.8; 28 2.4; 30 2.2; 32 2.0; 35 1.7; 37 1.5; 40 1.3; 42 1.1; 45 0.9; 49 0.8; 52 0.7; 56 0.8; 59 1.0; 64 1.1; 68 0.6; 73 -0.2; 78 -0.6; 83 -0.9; 89 -1.3; 95 -1.6; 102 -1.8; 109 -2.0; 117 -2.1; 125 -2.4; 134 -2.6; 143 -2.7; 153 -2.8; 164 -2.9; 175 -2.9; 188 -3.0; 201 -3.0; 215 -2.9; 230 -2.9; 246 -2.8; 263 -2.8; 282 -2.6; 301 -2.5; 323 -2.4; 345 -2.3; 369 -2.1; 395 -1.9; 423 -1.7; 452 -1.6; 484 -1.4; 518 -1.3; 554 -1.1; 593 -0.7; 635 -0.4; 679 -0.1; 726 0.1; 777 0.1; 832 -0.2; 890 -0.4; 952 -0.3; 1019 0.1; 1090 0.4; 1167 1.1; 1248 0.4; 1336 -0.3; 1429 0.3; 1529 0.2; 1636 -0.3; 1751 -0.5; 1873 -1.4; 2004 -1.2; 2145 -0.9; 2295 -2.1; 2455 -1.5; 2627 -1.5; 2811 -1.6; 3008 -0.4; 3219 0.5; 3444 0.8; 3685 -0.2; 3943 -1.1; 4219 -2.0; 4514 -1.9; 4830 -0.0; 5168 4.4; 5530 2.7; 5917 -2.7; 6331 -4.6; 6775 0.1; 7249 -0.8; 7756 -5.0; 8299 -8.0; 8880 -7.9; 9502 -5.1; 10167 -1.5; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.927254903917204dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 sn3964 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 187 Hz   |  0.61 | -3.3 dB |
| Peaking | 2383 Hz  |  3.12 | -1.8 dB |
| Peaking | 5295 Hz  | 13.47 | 5.9 dB  |
| Peaking | 8621 Hz  |  4.07 | -9.0 dB |
| Peaking | 16 Hz    |  0.69 | 4.2 dB  |
| Peaking | 63 Hz    |  3.76 | 1.3 dB  |
| Peaking | 6216 Hz  |  8.53 | -5.2 dB |
| Peaking | 7090 Hz  |  5.14 | 2.3 dB  |
| Peaking | 11359 Hz |  2.6  | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1%20sn3964/Beyerdynamic%20T1%20sn3964.png)