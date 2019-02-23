# Comradz NW-STUDIO PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.5; 49 -2.0; 54 -2.6; 60 -3.2; 66 -3.6; 72 -4.0; 79 -4.4; 87 -4.8; 96 -5.1; 106 -5.3; 116 -5.4; 128 -5.6; 141 -5.8; 155 -6.0; 170 -6.2; 187 -6.2; 206 -6.4; 227 -6.4; 249 -6.5; 274 -6.4; 302 -6.2; 332 -6.0; 365 -5.5; 402 -5.2; 442 -4.7; 486 -4.3; 535 -3.7; 588 -2.8; 647 -2.0; 712 -1.1; 783 -0.5; 861 -0.5; 947 -0.8; 1042 -3.8; 1146 -7.7; 1261 -12.2; 1387 -16.2; 1526 -18.6; 1678 -18.4; 1846 -16.9; 2031 -14.7; 2234 -12.4; 2457 -9.7; 2703 -7.7; 2973 -4.9; 3270 -2.9; 3597 -2.4; 3957 -3.7; 4353 -6.9; 4788 -8.8; 5267 -8.6; 5793 -6.7; 6373 -4.0; 7010 -4.0; 7711 -7.3; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Comradz NW-STUDIO PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Comradz NW-STUDIO PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.66 | 6.5 dB   |
| Peaking | 895 Hz  | 1.09 | 15.2 dB  |
| Peaking | 1581 Hz | 0.94 | -20.9 dB |
| Peaking | 3670 Hz | 1.06 | 11.2 dB  |
| Peaking | 4721 Hz | 3.07 | -7.4 dB  |
| Peaking | 250 Hz  | 1.86 | -0.6 dB  |
| Peaking | 580 Hz  | 3.56 | 0.6 dB   |
| Peaking | 5581 Hz | 6.82 | -1.4 dB  |
| Peaking | 6746 Hz | 6.07 | 4.1 dB   |
| Peaking | 7861 Hz | 4.19 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB   |
| Peaking | 62 Hz    | 1.41 | 1.9 dB   |
| Peaking | 125 Hz   | 1.41 | 0.4 dB   |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 3.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -12.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Comradz%20NW-STUDIO%20PRO/Comradz%20NW-STUDIO%20PRO.png)