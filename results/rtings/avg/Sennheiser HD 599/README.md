# Sennheiser HD 599

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 0.0; 23 4.3; 25 3.8; 28 3.1; 31 2.6; 34 2.1; 37 1.7; 41 1.3; 45 0.9; 49 0.5; 54 0.0; 60 -0.6; 66 -1.2; 72 -1.7; 79 -2.1; 87 -2.7; 96 -3.2; 106 -3.7; 116 -4.2; 128 -4.6; 141 -4.9; 155 -5.0; 170 -5.0; 187 -4.9; 206 -4.6; 227 -4.3; 249 -4.0; 274 -3.8; 302 -3.6; 332 -3.4; 365 -3.2; 402 -2.9; 442 -2.7; 486 -2.5; 535 -2.3; 588 -2.0; 647 -1.4; 712 -0.9; 783 -0.5; 861 -0.3; 947 -0.1; 1042 0.1; 1146 0.4; 1261 0.7; 1387 1.2; 1526 2.1; 1678 2.3; 1846 1.4; 2031 0.0; 2234 -0.4; 2457 0.4; 2703 -0.3; 2973 -1.9; 3270 -3.2; 3597 -2.8; 3957 -2.8; 4353 -4.3; 4788 -2.9; 5267 -1.3; 5793 -1.4; 6373 0.1; 7010 1.7; 7711 0.3; 8482 -1.2; 9330 -1.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.7; 18182 -6.1; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 599 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 599 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.29 | 5.8 dB  |
| Peaking | 164 Hz   | 0.44 | -5.2 dB |
| Peaking | 1576 Hz  | 2.21 | 2.7 dB  |
| Peaking | 4014 Hz  | 1.98 | -3.8 dB |
| Peaking | 19187 Hz | 2.05 | -8.2 dB |
| Peaking | 18 Hz    | 0.2  | 0.2 dB  |
| Peaking | 6165 Hz  | 4.56 | -1.5 dB |
| Peaking | 6810 Hz  | 4.26 | 2.9 dB  |
| Peaking | 8788 Hz  | 9.27 | -2.1 dB |
| Peaking | 15394 Hz | 3.01 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20599/Sennheiser%20HD%20599.png)