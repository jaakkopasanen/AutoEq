# Polk Audio UltraFit 300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -10.2; 23 -10.2; 25 -10.2; 28 -10.2; 31 -10.2; 34 -10.2; 37 -10.2; 41 -10.3; 45 -10.3; 49 -10.3; 54 -10.4; 60 -10.5; 66 -10.6; 72 -10.7; 79 -10.8; 87 -10.9; 96 -11.0; 106 -10.9; 116 -10.7; 128 -10.6; 141 -10.5; 155 -10.2; 170 -9.9; 187 -9.4; 206 -9.0; 227 -8.4; 249 -7.9; 274 -7.3; 302 -6.6; 332 -6.0; 365 -5.3; 402 -4.7; 442 -3.8; 486 -3.3; 535 -2.6; 588 -1.7; 647 -1.2; 712 -0.8; 783 0.1; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.6; 1387 -1.2; 1526 -1.9; 1678 -2.5; 1846 -2.5; 2031 -2.5; 2234 -2.2; 2457 -0.8; 2703 0.0; 2973 1.2; 3270 2.6; 3597 5.8; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 1.46 | -9.8 dB |
| Peaking | 51 Hz   | 0.29 | -9.4 dB |
| Peaking | 192 Hz  | 0.65 | -4.9 dB |
| Peaking | 2059 Hz | 2    | -3.8 dB |
| Peaking | 4572 Hz | 1.33 | 7.2 dB  |
| Peaking | 848 Hz  | 2.38 | 1.7 dB  |
| Peaking | 2099 Hz | 0.07 | -0.2 dB |
| Peaking | 6318 Hz | 4.13 | 2.9 dB  |
| Peaking | 6755 Hz | 4.06 | 1.2 dB  |
| Peaking | 7431 Hz | 2.08 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%20300/Polk%20Audio%20UltraFit%20300.png)