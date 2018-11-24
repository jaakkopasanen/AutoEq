# HyperX Cloud Stinger

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.1; 23 -5.4; 25 -5.6; 28 -5.9; 31 -6.1; 34 -6.2; 37 -6.2; 41 -6.2; 45 -6.4; 49 -6.6; 54 -6.6; 60 -6.6; 66 -6.5; 72 -6.3; 79 -6.1; 87 -6.2; 96 -6.3; 106 -6.5; 116 -6.5; 128 -6.4; 141 -6.0; 155 -5.7; 170 -5.1; 187 -4.5; 206 -3.4; 227 -2.3; 249 -1.1; 274 0.2; 302 1.8; 332 3.4; 365 5.2; 402 6.0; 442 6.0; 486 4.7; 535 2.7; 588 0.9; 647 -0.2; 712 -0.6; 783 -0.6; 861 -0.1; 947 0.0; 1042 -0.0; 1146 -0.3; 1261 -1.2; 1387 -2.7; 1526 -4.3; 1678 -5.4; 1846 -5.7; 2031 -6.1; 2234 -5.6; 2457 -5.0; 2703 -4.2; 2973 -3.7; 3270 -1.9; 3597 0.6; 3957 2.0; 4353 1.6; 4788 2.4; 5267 5.0; 5793 2.8; 6373 0.5; 7010 2.1; 7711 0.0; 8482 -4.4; 9330 -6.8; 10263 -2.6; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.0; 18182 -0.9; 20000 -1.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Stinger GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Stinger ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.3  | -6.3 dB |
| Peaking | 148 Hz  | 1.12 | -3.0 dB |
| Peaking | 400 Hz  | 1.99 | 7.8 dB  |
| Peaking | 1980 Hz | 1.9  | -6.8 dB |
| Peaking | 9253 Hz | 6.45 | -7.7 dB |
| Peaking | 690 Hz  | 5.08 | -1.5 dB |
| Peaking | 1559 Hz | 5.94 | -1.8 dB |
| Peaking | 2916 Hz | 2.15 | -7.2 dB |
| Peaking | 3212 Hz | 1.07 | 5.5 dB  |
| Peaking | 5343 Hz | 6.36 | 4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/HyperX%20Cloud%20Stinger/HyperX%20Cloud%20Stinger.png)