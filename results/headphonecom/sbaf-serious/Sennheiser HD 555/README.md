# Sennheiser HD 555

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.6; 37 5.1; 41 4.5; 45 4.1; 49 3.6; 54 3.4; 60 3.2; 66 3.4; 72 3.6; 79 2.2; 87 1.3; 96 0.8; 106 0.4; 116 0.1; 128 -0.2; 141 -0.6; 155 -0.7; 170 -0.8; 187 -1.0; 206 -1.1; 227 -1.2; 249 -1.2; 274 -1.1; 302 -1.0; 332 -0.8; 365 -0.7; 402 -0.4; 442 -0.2; 486 -0.1; 535 -0.1; 588 0.4; 647 0.3; 712 0.4; 783 0.2; 861 0.4; 947 0.1; 1042 0.0; 1146 0.2; 1261 0.6; 1387 1.1; 1526 1.5; 1678 1.7; 1846 0.8; 2031 0.6; 2234 0.4; 2457 0.5; 2703 0.9; 2973 0.3; 3270 -0.8; 3597 -0.2; 3957 1.9; 4353 2.4; 4788 -0.2; 5267 3.0; 5793 5.9; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -3.1; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 555 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 555 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.23 | 6.3 dB  |
| Peaking | 165 Hz   | 0.55 | -2.1 dB |
| Peaking | 626 Hz   | 1.83 | 0.7 dB  |
| Peaking | 1600 Hz  | 2.86 | 1.7 dB  |
| Peaking | 5950 Hz  | 4.1  | 6.2 dB  |
| Peaking | 71 Hz    | 7.42 | 1.1 dB  |
| Peaking | 2726 Hz  | 7.06 | 1.1 dB  |
| Peaking | 4083 Hz  | 2.44 | -2.2 dB |
| Peaking | 4131 Hz  | 8.1  | 5.3 dB  |
| Peaking | 19122 Hz | 2.19 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20555/Sennheiser%20HD%20555.png)