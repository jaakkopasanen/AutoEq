# Sennheiser HD 598

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.5; 37 5.0; 41 4.4; 45 3.8; 49 3.4; 54 2.9; 60 2.4; 66 2.4; 72 1.7; 79 1.9; 87 1.8; 96 0.5; 106 -0.1; 116 -0.5; 128 -1.0; 141 -1.3; 155 -1.7; 170 -1.7; 187 -1.9; 206 -1.9; 227 -1.8; 249 -1.9; 274 -2.1; 302 -1.9; 332 -1.8; 365 -1.6; 402 -1.4; 442 -1.4; 486 -1.3; 535 -0.9; 588 -0.8; 647 -0.6; 712 0.4; 783 -0.3; 861 -0.3; 947 0.1; 1042 -0.1; 1146 0.1; 1261 -0.2; 1387 -0.1; 1526 0.2; 1678 1.2; 1846 1.2; 2031 0.9; 2234 0.9; 2457 1.9; 2703 0.5; 2973 0.2; 3270 -0.5; 3597 -0.2; 3957 -0.2; 4353 -3.3; 4788 -3.4; 5267 -1.1; 5793 -0.1; 6373 -0.1; 7010 0.3; 7711 0.3; 8482 -0.7; 9330 -0.6; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.2; 18182 -4.0; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.36 | 6.3 dB  |
| Peaking | 204 Hz   | 0.57 | -2.5 dB |
| Peaking | 2140 Hz  | 1.63 | 1.4 dB  |
| Peaking | 4590 Hz  | 5.68 | -4.3 dB |
| Peaking | 19287 Hz | 2.04 | -6.1 dB |
| Peaking | 83 Hz    | 7.67 | 1.1 dB  |
| Peaking | 464 Hz   | 4.81 | -0.2 dB |
| Peaking | 8456 Hz  | 2.17 | 1.0 dB  |
| Peaking | 8765 Hz  | 6.05 | -2.2 dB |
| Peaking | 15885 Hz | 3.85 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)