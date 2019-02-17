# Sennheiser HD 229
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.7; 31 -3.5; 34 -4.3; 37 -4.9; 41 -5.7; 45 -6.3; 49 -6.9; 54 -7.5; 60 -8.1; 66 -8.6; 72 -9.1; 79 -9.5; 87 -10.0; 96 -10.5; 106 -10.7; 116 -10.6; 128 -10.5; 141 -10.3; 155 -10.9; 170 -10.3; 187 -10.0; 206 -9.3; 227 -9.0; 249 -9.3; 274 -8.4; 302 -7.2; 332 -6.3; 365 -6.0; 402 -5.6; 442 -5.2; 486 -5.7; 535 -5.6; 588 -5.3; 647 -5.4; 712 -5.9; 783 -5.9; 861 -6.1; 947 -6.4; 1042 -6.7; 1146 -6.6; 1261 -6.4; 1387 -6.2; 1526 -5.6; 1678 -7.9; 1846 -7.7; 2031 -7.1; 2234 -6.5; 2457 -5.8; 2703 -6.4; 2973 -6.2; 3270 -6.2; 3597 -5.7; 3957 -6.5; 4353 -7.9; 4788 -7.5; 5267 -4.7; 5793 -2.7; 6373 -1.7; 7010 -4.1; 7711 -6.3; 8482 -9.3; 9330 -10.5; 10263 -6.8; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 229 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 229 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.17 | 6.3 dB  |
| Peaking | 96 Hz   | 1.13 | -3.9 dB |
| Peaking | 172 Hz  | 1.88 | -2.8 dB |
| Peaking | 6313 Hz | 4.14 | 5.6 dB  |
| Peaking | 9003 Hz | 5.23 | -4.9 dB |
| Peaking | 256 Hz  | 4.1  | -1.9 dB |
| Peaking | 456 Hz  | 0.97 | 1.6 dB  |
| Peaking | 1797 Hz | 6.95 | -1.8 dB |
| Peaking | 4368 Hz | 1.65 | 1.6 dB  |
| Peaking | 4509 Hz | 4.9  | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20229/Sennheiser%20HD%20229.png)