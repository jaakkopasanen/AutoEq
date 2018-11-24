# Sennheiser HD 800 S sn01070

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 0.0; 23 4.4; 25 4.0; 28 3.4; 31 3.0; 34 2.6; 37 2.3; 41 1.9; 45 1.7; 49 1.5; 54 1.3; 60 1.2; 66 1.2; 72 1.1; 79 0.3; 87 -0.6; 96 -0.9; 106 -1.4; 116 -1.8; 128 -2.2; 141 -2.5; 155 -2.7; 170 -2.6; 187 -2.9; 206 -3.0; 227 -2.9; 249 -2.9; 274 -2.8; 302 -2.7; 332 -2.6; 365 -2.4; 402 -2.3; 442 -1.9; 486 -1.9; 535 -1.7; 588 -1.3; 647 -1.1; 712 -1.1; 783 -0.5; 861 -0.4; 947 -0.1; 1042 0.2; 1146 0.6; 1261 1.0; 1387 1.5; 1526 1.7; 1678 1.4; 1846 1.4; 2031 1.6; 2234 1.4; 2457 2.0; 2703 2.4; 2973 2.0; 3270 2.6; 3597 2.1; 3957 0.4; 4353 -0.3; 4788 -0.0; 5267 -0.8; 5793 -0.6; 6373 -3.4; 7010 -3.8; 7711 -2.3; 8482 -0.7; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S sn01070 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S sn01070 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 211 Hz  | 0.44 | -3.3 dB |
| Peaking | 1548 Hz | 1.38 | 1.7 dB  |
| Peaking | 3046 Hz | 2.25 | 2.4 dB  |
| Peaking | 6884 Hz | 3.89 | -4.5 dB |
| Peaking | 15 Hz   | 0.51 | 5.6 dB  |
| Peaking | 68 Hz   | 2.12 | 1.6 dB  |
| Peaking | 221 Hz  | 1.25 | 0.2 dB  |
| Peaking | 4216 Hz | 9.07 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S%20sn01070/Sennheiser%20HD%20800%20S%20sn01070.png)