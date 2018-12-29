# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.4; 41 4.7; 45 4.1; 49 3.6; 54 3.6; 60 3.4; 66 1.9; 72 1.0; 79 0.5; 87 -0.1; 96 -0.5; 106 -0.9; 116 -1.1; 128 -1.5; 141 -1.4; 155 -1.7; 170 -1.8; 187 -1.6; 206 -1.6; 227 -1.4; 249 -1.4; 274 -1.1; 302 -0.8; 332 -0.6; 365 -0.3; 402 -0.0; 442 0.3; 486 0.4; 535 0.3; 588 0.5; 647 0.7; 712 0.9; 783 0.8; 861 0.5; 947 0.2; 1042 0.3; 1146 0.3; 1261 0.1; 1387 -0.3; 1526 -0.6; 1678 -0.6; 1846 -0.7; 2031 -0.7; 2234 -1.2; 2457 -1.5; 2703 -1.9; 2973 -2.5; 3270 -3.7; 3597 -4.3; 3957 -4.2; 4353 -4.5; 4788 -4.2; 5267 -1.4; 5793 2.5; 6373 1.7; 7010 1.2; 7711 0.3; 8482 -0.1; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 -0.3; 13660 -4.4; 15026 -5.4; 16529 -1.3; 18182 0.0
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.52 | 6.3 dB  |
| Peaking | 133 Hz   | 0.82 | -2.7 dB |
| Peaking | 4413 Hz  | 1.39 | -6.4 dB |
| Peaking | 5956 Hz  | 2.48 | 5.9 dB  |
| Peaking | 14643 Hz | 3.54 | -6.3 dB |
| Peaking | 266 Hz   | 1.35 | -1.3 dB |
| Peaking | 330 Hz   | 0.65 | 0.9 dB  |
| Peaking | 734 Hz   | 2.34 | 0.8 dB  |
| Peaking | 3216 Hz  | 5.4  | -0.5 dB |
| Peaking | 11584 Hz | 4.58 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)