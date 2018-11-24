# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.4; 37 4.9; 41 4.2; 45 3.7; 49 3.2; 54 2.8; 60 2.3; 66 1.8; 72 1.5; 79 1.2; 87 0.8; 96 0.4; 106 -0.1; 116 -0.6; 128 -1.0; 141 -1.3; 155 -1.4; 170 -1.5; 187 -1.6; 206 -1.5; 227 -1.4; 249 -1.2; 274 -1.0; 302 -0.8; 332 -0.7; 365 -0.5; 402 -0.4; 442 -0.4; 486 -0.2; 535 -0.2; 588 -0.2; 647 -0.0; 712 -0.1; 783 -0.4; 861 -0.6; 947 -0.2; 1042 -0.3; 1146 -0.5; 1261 -0.8; 1387 -1.5; 1526 -2.0; 1678 -2.2; 1846 -2.0; 2031 -1.7; 2234 -1.0; 2457 -0.7; 2703 -0.4; 2973 -0.2; 3270 0.6; 3597 1.6; 3957 1.6; 4353 1.2; 4788 1.3; 5267 3.0; 5793 5.1; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.59 | 6.2 dB  |
| Peaking | 170 Hz  | 0.94 | -2.0 dB |
| Peaking | 1743 Hz | 1.82 | -2.3 dB |
| Peaking | 3748 Hz | 4.02 | 1.7 dB  |
| Peaking | 6076 Hz | 3.95 | 6.1 dB  |
| Peaking | 85 Hz   | 3.22 | 0.1 dB  |
| Peaking | 8037 Hz | 5.36 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)