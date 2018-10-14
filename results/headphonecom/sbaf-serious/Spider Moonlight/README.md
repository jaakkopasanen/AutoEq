# Spider Moonlight

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.2; 28 0.7; 31 0.2; 34 -0.2; 37 -0.5; 41 -0.8; 45 -1.1; 49 -1.4; 54 -1.7; 60 -2.0; 66 -2.3; 72 -2.5; 79 -2.8; 87 -3.4; 96 -3.4; 106 -3.6; 116 -4.1; 128 -4.6; 141 -5.0; 155 -5.3; 170 -4.6; 187 -5.1; 206 -4.8; 227 -4.0; 249 -3.1; 274 -1.5; 302 0.3; 332 1.4; 365 1.6; 402 1.0; 442 0.3; 486 -0.2; 535 -0.4; 588 -0.6; 647 -0.2; 712 0.8; 783 0.9; 861 0.4; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.6; 1526 -3.0; 1678 -4.1; 1846 -4.9; 2031 -5.7; 2234 -6.3; 2457 -6.0; 2703 -5.0; 2973 -4.9; 3270 -4.9; 3597 -4.3; 3957 -4.9; 4353 -4.3; 4788 -1.1; 5267 5.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.6; 10263 -3.8; 11289 -1.7; 12418 -3.2; 13660 -5.5; 15026 -1.5; 16529 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider Moonlight ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 142 Hz   | 1.05 | -5.5 dB |
| Peaking | 2200 Hz  | 1.8  | -6.0 dB |
| Peaking | 4324 Hz  | 1.75 | -7.8 dB |
| Peaking | 5542 Hz  | 2.32 | 11.3 dB |
| Peaking | 12704 Hz | 1.39 | -4.3 dB |
| Peaking | 20 Hz    | 2.85 | 2.4 dB  |
| Peaking | 223 Hz   | 3.18 | -2.0 dB |
| Peaking | 344 Hz   | 2.95 | 3.0 dB  |
| Peaking | 805 Hz   | 3.14 | 1.3 dB  |
| Peaking | 16192 Hz | 4.97 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Spider%20Moonlight/Spider%20Moonlight.png)