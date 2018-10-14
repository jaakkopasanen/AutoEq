# Ultrasone HFI-780

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.8; 66 5.6; 72 5.5; 79 5.7; 87 5.4; 96 5.0; 106 5.0; 116 5.1; 128 5.3; 141 5.3; 155 5.5; 170 6.0; 187 6.0; 206 6.0; 227 5.7; 249 3.9; 274 2.7; 302 1.1; 332 -0.2; 365 -1.0; 402 -1.2; 442 -0.8; 486 -0.5; 535 -0.1; 588 0.5; 647 0.7; 712 0.6; 783 0.7; 861 0.4; 947 0.1; 1042 0.1; 1146 0.2; 1261 -0.2; 1387 -1.0; 1526 -2.2; 1678 -2.9; 1846 -3.1; 2031 -1.5; 2234 3.7; 2457 5.9; 2703 3.6; 2973 3.5; 3270 1.7; 3597 1.2; 3957 2.4; 4353 2.1; 4788 1.3; 5267 2.8; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.5; 10263 -2.3; 11289 -1.7; 12418 -1.5; 13660 -0.4; 15026 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.33 | 6.3 dB  |
| Peaking | 188 Hz   | 1.99 | 4.6 dB  |
| Peaking | 1922 Hz  | 2.34 | -7.9 dB |
| Peaking | 2361 Hz  | 2.27 | 9.2 dB  |
| Peaking | 6049 Hz  | 4.34 | 6.3 dB  |
| Peaking | 372 Hz   | 0.83 | 2.6 dB  |
| Peaking | 387 Hz   | 1.71 | -4.9 dB |
| Peaking | 4112 Hz  | 8.25 | 1.5 dB  |
| Peaking | 10551 Hz | 2.44 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-780/Ultrasone%20HFI-780.png)