# Ultimate Ears UE350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -8.6; 23 -8.5; 25 -8.5; 28 -8.6; 31 -8.6; 34 -8.6; 37 -8.5; 41 -8.5; 45 -8.5; 49 -8.5; 54 -8.5; 60 -8.5; 66 -8.6; 72 -8.6; 79 -8.7; 87 -8.8; 96 -8.8; 106 -8.7; 116 -8.5; 128 -8.5; 141 -8.3; 155 -8.0; 170 -7.7; 187 -7.3; 206 -7.0; 227 -6.4; 249 -6.0; 274 -5.4; 302 -4.9; 332 -4.3; 365 -3.7; 402 -3.2; 442 -2.5; 486 -2.1; 535 -1.6; 588 -0.8; 647 -0.5; 712 -0.3; 783 0.2; 861 -0.3; 947 0.2; 1042 -0.0; 1146 -0.6; 1261 -0.7; 1387 -1.4; 1526 -2.0; 1678 -2.3; 1846 -2.0; 2031 -1.6; 2234 -1.0; 2457 0.2; 2703 1.2; 2973 2.9; 3270 4.7; 3597 6.0; 3957 5.8; 4353 4.3; 4788 4.3; 5267 5.5; 5793 5.9; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.19 | -8.3 dB |
| Peaking | 176 Hz  | 0.65 | -4.1 dB |
| Peaking | 1831 Hz | 2.26 | -2.8 dB |
| Peaking | 3662 Hz | 2.34 | 6.0 dB  |
| Peaking | 5819 Hz | 3.24 | 5.7 dB  |
| Peaking | 363 Hz  | 2.21 | -0.6 dB |
| Peaking | 780 Hz  | 1.46 | 1.0 dB  |
| Peaking | 1473 Hz | 5.5  | -0.7 dB |
| Peaking | 8326 Hz | 4.56 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultimate%20Ears%20UE350/Ultimate%20Ears%20UE350.png)