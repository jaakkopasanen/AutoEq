# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.6; 31 5.0; 34 4.4; 37 3.8; 41 3.3; 45 2.8; 49 2.5; 54 2.3; 60 1.6; 66 1.2; 72 1.5; 79 0.8; 87 -0.3; 96 -1.0; 106 -1.4; 116 -1.7; 128 -2.0; 141 -2.2; 155 -2.4; 170 -2.2; 187 -2.4; 206 -2.5; 227 -2.3; 249 -2.2; 274 -2.0; 302 -1.8; 332 -1.7; 365 -1.4; 402 -1.3; 442 -1.0; 486 -1.0; 535 -1.0; 588 -0.6; 647 -0.5; 712 -0.4; 783 -0.2; 861 -0.5; 947 -0.4; 1042 -0.3; 1146 -0.8; 1261 -1.0; 1387 -1.2; 1526 -1.3; 1678 -1.6; 1846 -1.5; 2031 -0.8; 2234 -0.6; 2457 -0.2; 2703 0.0; 2973 -0.5; 3270 -1.1; 3597 -0.8; 3957 0.0; 4353 -0.1; 4788 0.7; 5267 4.6; 5793 5.6; 6373 4.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.58 | 6.2 dB  |
| Peaking | 74 Hz   | 4.04 | 1.2 dB  |
| Peaking | 164 Hz  | 0.57 | -2.8 dB |
| Peaking | 3432 Hz | 0.39 | -1.2 dB |
| Peaking | 5833 Hz | 2.97 | 7.0 dB  |
| Peaking | 830 Hz  | 1.92 | 0.4 dB  |
| Peaking | 1657 Hz | 2.42 | -0.9 dB |
| Peaking | 2714 Hz | 2.75 | 1.8 dB  |
| Peaking | 3138 Hz | 2.48 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)