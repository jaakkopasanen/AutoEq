# Audeo PFE 121 Green Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.7; 23 -1.8; 25 -1.8; 28 -1.9; 31 -2.0; 34 -2.1; 37 -2.3; 41 -2.5; 45 -2.6; 49 -2.8; 54 -3.0; 60 -3.3; 66 -3.5; 72 -3.8; 79 -4.2; 87 -4.5; 96 -5.0; 106 -5.1; 116 -5.3; 128 -5.5; 141 -5.7; 155 -5.8; 170 -5.8; 187 -5.8; 206 -5.7; 227 -5.4; 249 -5.3; 274 -5.0; 302 -4.7; 332 -4.4; 365 -4.0; 402 -3.7; 442 -3.0; 486 -2.6; 535 -2.0; 588 -1.3; 647 -0.8; 712 -0.5; 783 -0.0; 861 0.1; 947 0.0; 1042 0.1; 1146 0.2; 1261 0.3; 1387 0.2; 1526 0.1; 1678 0.4; 1846 1.2; 2031 2.3; 2234 3.2; 2457 4.7; 2703 4.7; 2973 4.2; 3270 4.8; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -2.2; 9330 -4.8; 10263 -2.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.0; 16529 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Green Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 77 Hz    | 0.3  | -2.4 dB |
| Peaking | 203 Hz   | 0.55 | -4.3 dB |
| Peaking | 3521 Hz  | 0.97 | 5.2 dB  |
| Peaking | 5810 Hz  | 2.01 | 4.2 dB  |
| Peaking | 9210 Hz  | 3.57 | -6.4 dB |
| Peaking | 785 Hz   | 3    | 0.8 dB  |
| Peaking | 1662 Hz  | 2.71 | -1.2 dB |
| Peaking | 2618 Hz  | 2.2  | 1.6 dB  |
| Peaking | 3014 Hz  | 5.2  | -2.0 dB |
| Peaking | 15171 Hz | 7.28 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Green%20Filter/Audeo%20PFE%20121%20Green%20Filter.png)