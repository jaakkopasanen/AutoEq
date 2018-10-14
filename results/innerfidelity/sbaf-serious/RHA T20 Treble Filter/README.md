# RHA T20 Treble Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 -5.0; 23 -5.3; 25 -5.5; 28 -5.8; 31 -5.9; 34 -6.0; 37 -6.1; 41 -6.2; 45 -6.2; 49 -6.2; 54 -6.2; 60 -6.3; 66 -6.3; 72 -6.3; 79 -6.3; 87 -6.4; 96 -6.4; 106 -6.2; 116 -6.0; 128 -5.9; 141 -5.6; 155 -5.4; 170 -5.0; 187 -4.6; 206 -4.2; 227 -3.7; 249 -3.3; 274 -2.8; 302 -2.3; 332 -1.9; 365 -1.4; 402 -0.9; 442 -0.4; 486 -0.2; 535 0.2; 588 0.8; 647 1.0; 712 1.0; 783 1.2; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.8; 1261 -1.7; 1387 -3.2; 1526 -4.3; 1678 -3.3; 1846 -0.2; 2031 -2.5; 2234 -3.6; 2457 -5.0; 2703 -6.3; 2973 -5.8; 3270 -4.2; 3597 -3.3; 3957 -4.9; 4353 -9.2; 4788 -10.9; 5267 -4.8; 5793 1.2; 6373 4.2; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 -0.6; 16529 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.7dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Treble Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.42 | -5.7 dB  |
| Peaking | 112 Hz  | 0.95 | -3.5 dB  |
| Peaking | 208 Hz  | 1.59 | -2.2 dB  |
| Peaking | 2688 Hz | 1.89 | -5.8 dB  |
| Peaking | 4628 Hz | 6.24 | -11.5 dB |
| Peaking | 748 Hz  | 1.78 | 1.8 dB   |
| Peaking | 1563 Hz | 3.05 | -4.2 dB  |
| Peaking | 1861 Hz | 6.01 | 3.6 dB   |
| Peaking | 5057 Hz | 6.25 | -2.9 dB  |
| Peaking | 6351 Hz | 4.34 | 6.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Treble%20Filter/RHA%20T20%20Treble%20Filter.png)