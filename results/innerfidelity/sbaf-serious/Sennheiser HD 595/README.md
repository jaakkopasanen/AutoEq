# Sennheiser HD 595
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.7; 72 5.2; 79 4.7; 87 3.7; 96 2.8; 106 2.2; 116 1.8; 128 1.2; 141 0.8; 155 0.4; 170 0.3; 187 0.1; 206 -0.1; 227 -0.1; 249 -0.1; 274 -0.2; 302 -0.2; 332 -0.2; 365 -0.2; 402 -0.1; 442 0.0; 486 -0.1; 535 0.2; 588 0.7; 647 0.6; 712 0.4; 783 0.5; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.1; 1261 -0.5; 1387 -0.4; 1526 -0.2; 1678 0.4; 1846 1.4; 2031 1.9; 2234 1.5; 2457 1.2; 2703 0.9; 2973 1.6; 3270 2.4; 3597 3.3; 3957 4.9; 4353 4.2; 4788 3.2; 5267 3.7; 5793 5.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 595 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.58 | 6.9 dB  |
| Peaking | 649 Hz  | 3.26 | 0.4 dB  |
| Peaking | 4015 Hz | 1.88 | 4.1 dB  |
| Peaking | 6257 Hz | 3.32 | 5.6 dB  |
| Peaking | 8104 Hz | 1.74 | -1.7 dB |
| Peaking | 39 Hz   | 2.59 | -1.2 dB |
| Peaking | 71 Hz   | 1.93 | 1.5 dB  |
| Peaking | 183 Hz  | 0.89 | -0.9 dB |
| Peaking | 1394 Hz | 2.83 | -0.8 dB |
| Peaking | 2016 Hz | 4.87 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20595/Sennheiser%20HD%20595.png)