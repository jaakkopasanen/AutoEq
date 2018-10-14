# Ultrasone HFI-450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.8; 72 4.9; 79 3.8; 87 3.3; 96 2.8; 106 1.9; 116 1.6; 128 1.4; 141 1.5; 155 1.5; 170 2.2; 187 1.9; 206 1.9; 227 1.6; 249 1.1; 274 0.3; 302 -0.8; 332 -1.6; 365 -1.8; 402 -1.6; 442 -1.6; 486 -1.5; 535 -1.1; 588 -0.2; 647 0.2; 712 0.2; 783 0.4; 861 0.2; 947 0.0; 1042 -0.0; 1146 -0.1; 1261 -0.3; 1387 -0.1; 1526 -0.6; 1678 -0.5; 1846 -0.5; 2031 0.5; 2234 1.5; 2457 2.9; 2703 4.2; 2973 4.4; 3270 4.6; 3597 4.7; 3957 6.0; 4353 5.9; 4788 1.4; 5267 1.1; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 -0.7; 11289 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.5  | 6.7 dB  |
| Peaking | 220 Hz  | 2.25 | 1.8 dB  |
| Peaking | 369 Hz  | 1.57 | -2.4 dB |
| Peaking | 3574 Hz | 1.79 | 5.7 dB  |
| Peaking | 6162 Hz | 5.87 | 5.5 dB  |
| Peaking | 64 Hz   | 5.53 | 1.2 dB  |
| Peaking | 1862 Hz | 1.97 | -2.5 dB |
| Peaking | 2490 Hz | 1.3  | 2.1 dB  |
| Peaking | 3398 Hz | 7.27 | -2.3 dB |
| Peaking | 9484 Hz | 3.37 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-450/Ultrasone%20HFI-450.png)