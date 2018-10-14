# Grado SR225i Comfy Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.0; 41 3.9; 45 3.0; 49 2.3; 54 1.4; 60 0.8; 66 0.2; 72 -0.4; 79 -0.8; 87 -1.3; 96 -1.7; 106 -1.9; 116 -1.9; 128 -2.0; 141 -2.0; 155 -1.9; 170 -1.8; 187 -1.7; 206 -1.5; 227 -1.2; 249 -1.0; 274 -0.7; 302 -0.8; 332 -0.7; 365 -0.4; 402 -0.3; 442 -0.1; 486 -0.1; 535 0.0; 588 0.3; 647 0.4; 712 0.3; 783 0.5; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -1.5; 1526 -2.8; 1678 -3.6; 1846 -4.8; 2031 -8.8; 2234 -9.3; 2457 -5.9; 2703 -3.5; 2973 -1.7; 3270 -0.2; 3597 -1.3; 3957 0.2; 4353 2.1; 4788 1.7; 5267 0.3; 5793 3.0; 6373 2.8; 7010 0.0; 7711 -1.3; 8482 -2.4; 9330 -2.5; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Comfy Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 0.77 | 6.7 dB   |
| Peaking | 111 Hz  | 0.71 | -2.8 dB  |
| Peaking | 2156 Hz | 2.91 | -10.1 dB |
| Peaking | 6473 Hz | 1.16 | 3.9 dB   |
| Peaking | 8283 Hz | 2.33 | -5.2 dB  |
| Peaking | 797 Hz  | 1.42 | 0.8 dB   |
| Peaking | 1522 Hz | 7.25 | -1.0 dB  |
| Peaking | 5177 Hz | 3.23 | 2.0 dB   |
| Peaking | 5226 Hz | 8.02 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Comfy%20Pads/Grado%20SR225i%20Comfy%20Pads.png)