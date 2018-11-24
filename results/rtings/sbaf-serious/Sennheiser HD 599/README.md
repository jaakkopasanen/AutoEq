# Sennheiser HD 599

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 0.0; 23 4.6; 25 4.1; 28 3.3; 31 2.6; 34 2.0; 37 1.6; 41 1.1; 45 0.6; 49 0.2; 54 -0.3; 60 -0.9; 66 -1.4; 72 -1.7; 79 -1.9; 87 -2.3; 96 -2.8; 106 -3.3; 116 -3.7; 128 -4.1; 141 -4.3; 155 -4.4; 170 -4.4; 187 -4.3; 206 -4.1; 227 -3.8; 249 -3.4; 274 -3.2; 302 -2.8; 332 -2.5; 365 -2.2; 402 -1.9; 442 -1.6; 486 -1.3; 535 -1.1; 588 -0.9; 647 -0.4; 712 -0.0; 783 -0.0; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.7; 1261 1.0; 1387 1.2; 1526 1.7; 1678 1.9; 1846 1.5; 2031 0.4; 2234 0.1; 2457 0.9; 2703 0.5; 2973 -0.3; 3270 -0.6; 3597 0.4; 3957 -0.4; 4353 -3.0; 4788 -1.3; 5267 1.7; 5793 2.5; 6373 3.9; 7010 2.5; 7711 0.3; 8482 -1.8; 9330 -2.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 599 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 599 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.8  | 5.7 dB  |
| Peaking | 164 Hz   | 0.58 | -4.5 dB |
| Peaking | 1641 Hz  | 1.43 | 2.0 dB  |
| Peaking | 6321 Hz  | 1.01 | -4.5 dB |
| Peaking | 6345 Hz  | 2.56 | 8.7 dB  |
| Peaking | 2113 Hz  | 9.12 | -1.0 dB |
| Peaking | 4296 Hz  | 2.43 | 2.5 dB  |
| Peaking | 4455 Hz  | 6.21 | -5.2 dB |
| Peaking | 9008 Hz  | 7.56 | -3.3 dB |
| Peaking | 10165 Hz | 1.92 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20599/Sennheiser%20HD%20599.png)