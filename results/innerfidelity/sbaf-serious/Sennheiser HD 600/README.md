# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.2; 41 4.3; 45 3.6; 49 3.0; 54 2.4; 60 1.7; 66 1.1; 72 0.8; 79 0.0; 87 -1.0; 96 -1.7; 106 -2.1; 116 -2.5; 128 -2.8; 141 -3.1; 155 -3.1; 170 -2.9; 187 -3.1; 206 -3.0; 227 -2.8; 249 -2.6; 274 -2.4; 302 -2.1; 332 -1.9; 365 -1.6; 402 -1.5; 442 -1.2; 486 -1.2; 535 -0.9; 588 -0.5; 647 -0.5; 712 -0.6; 783 -0.4; 861 -0.6; 947 -0.5; 1042 -0.1; 1146 -0.6; 1261 -1.0; 1387 -1.3; 1526 -1.9; 1678 -2.3; 1846 -1.9; 2031 -1.3; 2234 -1.4; 2457 -0.8; 2703 -1.2; 2973 -1.1; 3270 -1.6; 3597 -1.6; 3957 -0.7; 4353 -1.3; 4788 -1.5; 5267 2.1; 5793 4.1; 6373 3.9; 7010 2.5; 7711 0.3; 8482 -0.4; 9330 -0.6; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.5  | 6.6 dB  |
| Peaking | 144 Hz  |  0.53 | -4.0 dB |
| Peaking | 1683 Hz |  2.8  | -2.0 dB |
| Peaking | 5202 Hz |  1.01 | -4.0 dB |
| Peaking | 5971 Hz |  2.41 | 8.2 dB  |
| Peaking | 4661 Hz | 14.53 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)