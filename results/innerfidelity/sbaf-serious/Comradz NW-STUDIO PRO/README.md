# Comradz NW-STUDIO PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -2.1; 31 -2.9; 34 -3.6; 37 -4.2; 41 -5.0; 45 -5.7; 49 -6.2; 54 -6.8; 60 -7.4; 66 -7.8; 72 -8.2; 79 -8.6; 87 -9.0; 96 -9.3; 106 -9.5; 116 -9.6; 128 -9.8; 141 -10.0; 155 -10.2; 170 -10.4; 187 -10.4; 206 -10.6; 227 -10.6; 249 -10.7; 274 -10.6; 302 -10.4; 332 -10.2; 365 -9.7; 402 -9.4; 442 -8.9; 486 -8.5; 535 -7.9; 588 -7.0; 647 -6.2; 712 -5.3; 783 -4.3; 861 -3.9; 947 -4.9; 1042 -8.0; 1146 -11.9; 1261 -16.4; 1387 -20.4; 1526 -22.8; 1678 -22.6; 1846 -21.1; 2031 -18.9; 2234 -16.6; 2457 -13.9; 2703 -11.9; 2973 -9.1; 3270 -7.1; 3597 -6.6; 3957 -7.9; 4353 -11.1; 4788 -13.0; 5267 -12.8; 5793 -10.9; 6373 -8.2; 7010 -7.7; 7711 -11.5; 8482 -10.9; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Comradz NW-STUDIO PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Comradz NW-STUDIO PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.36 | 6.2 dB   |
| Peaking | 172 Hz   | 0.68 | -4.4 dB  |
| Peaking | 1682 Hz  | 2.24 | -18.1 dB |
| Peaking | 5180 Hz  | 2.96 | -6.1 dB  |
| Peaking | 21452 Hz | 2.36 | -2.1 dB  |
| Peaking | 870 Hz   | 2.66 | 6.1 dB   |
| Peaking | 1342 Hz  | 5.38 | -5.1 dB  |
| Peaking | 2272 Hz  | 4.57 | -3.2 dB  |
| Peaking | 3461 Hz  | 4.78 | 3.3 dB   |
| Peaking | 8087 Hz  | 7.1  | -5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -16.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.7 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Comradz%20NW-STUDIO%20PRO/Comradz%20NW-STUDIO%20PRO.png)