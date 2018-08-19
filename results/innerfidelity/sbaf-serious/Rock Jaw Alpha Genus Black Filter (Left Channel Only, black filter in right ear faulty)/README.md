# Rock Jaw Alpha Genus Black Filter (Left Channel Only, black filter in right ear faulty)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 10 -84; 20 0.4; 22 -0.2; 23 -0.4; 25 -0.8; 26 -1.0; 28 -1.4; 30 -1.7; 32 -2.0; 35 -2.4; 37 -2.6; 40 -2.9; 42 -3.1; 45 -3.4; 49 -3.7; 52 -3.9; 56 -4.2; 59 -4.4; 64 -4.7; 68 -4.9; 73 -5.2; 78 -5.5; 83 -5.7; 89 -6.0; 95 -6.3; 102 -6.4; 109 -6.5; 117 -6.6; 125 -6.8; 134 -6.9; 143 -6.9; 153 -7.0; 164 -6.9; 175 -6.8; 188 -6.7; 201 -6.6; 215 -6.4; 230 -6.1; 246 -5.9; 263 -5.7; 282 -5.3; 301 -5.1; 323 -4.8; 345 -4.4; 369 -4.1; 395 -3.8; 423 -3.3; 452 -2.9; 484 -2.7; 518 -2.3; 554 -1.8; 593 -1.2; 635 -0.8; 679 -0.7; 726 -0.3; 777 0.1; 832 0.2; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.7; 1248 -1.1; 1336 -1.8; 1429 -2.5; 1529 -3.4; 1636 -4.2; 1751 -4.7; 1873 -5.1; 2004 -5.3; 2145 -5.5; 2295 -5.6; 2455 -5.5; 2627 -5.2; 2811 -4.0; 3008 -2.2; 3219 -0.2; 3444 1.7; 3685 2.0; 3943 1.1; 4219 -1.1; 4514 -3.2; 4830 -5.0; 5168 -7.6; 5530 -9.6; 5917 -6.2; 6331 -2.2; 6775 0.4; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -0.3; 9502 -1.9; 10167 -3.4; 10879 -2.7; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.195183675724848dB` and instead set Global volume in the UI for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Jaw Alpha Genus Black Filter (Left Channel Only, black filter in right ear faulty) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 96 Hz    | 0.55 | -5.3 dB |
| Peaking | 234 Hz   | 0.84 | -4.1 dB |
| Peaking | 2098 Hz  | 2.16 | -6.2 dB |
| Peaking | 5449 Hz  | 4.41 | -8.2 dB |
| Peaking | 11808 Hz | 3.69 | -2.1 dB |
| Peaking | 2724 Hz  | 5.83 | -2.6 dB |
| Peaking | 3656 Hz  | 4.09 | 4.3 dB  |
| Peaking | 5609 Hz  | 2.04 | -4.4 dB |
| Peaking | 6597 Hz  | 1.62 | 4.0 dB  |
| Peaking | 10003 Hz | 7.15 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Rock%20Jaw%20Alpha%20Genus%20Black%20Filter%20(Left%20Channel%20Only,%20black%20filter%20in%20right%20ear%20faulty)/Rock%20Jaw%20Alpha%20Genus%20Black%20Filter%20(Left%20Channel%20Only,%20black%20filter%20in%20right%20ear%20faulty).png)