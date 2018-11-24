# Sennheiser HD 569

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 4.8; 25 4.0; 28 3.0; 31 2.1; 34 1.4; 37 0.8; 41 0.1; 45 -0.4; 49 -0.9; 54 -1.3; 60 -1.7; 66 -1.9; 72 -2.0; 79 -2.0; 87 -2.1; 96 -2.1; 106 -2.2; 116 -2.5; 128 -3.3; 141 -3.9; 155 -3.3; 170 -1.3; 187 -1.8; 206 -1.1; 227 -0.0; 249 1.1; 274 2.0; 302 2.3; 332 2.3; 365 1.9; 402 1.3; 442 0.6; 486 -0.2; 535 -0.5; 588 -0.1; 647 0.1; 712 0.0; 783 0.0; 861 -0.0; 947 -0.0; 1042 0.1; 1146 0.5; 1261 0.9; 1387 1.0; 1526 0.6; 1678 0.5; 1846 0.5; 2031 0.6; 2234 0.8; 2457 2.0; 2703 2.8; 2973 2.7; 3270 0.3; 3597 0.8; 3957 2.7; 4353 3.3; 4788 4.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -1.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.3; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 569 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 569 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.47 | 6.0 dB  |
| Peaking | 148 Hz  | 0.5  | -3.7 dB |
| Peaking | 294 Hz  | 1.49 | 4.8 dB  |
| Peaking | 2705 Hz | 4.25 | 2.7 dB  |
| Peaking | 5509 Hz | 2.5  | 6.7 dB  |
| Peaking | 138 Hz  | 2.09 | 1.6 dB  |
| Peaking | 144 Hz  | 4.87 | -3.0 dB |
| Peaking | 1327 Hz | 4.04 | 1.0 dB  |
| Peaking | 6517 Hz | 9.41 | 2.0 dB  |
| Peaking | 8863 Hz | 2.75 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20569/Sennheiser%20HD%20569.png)