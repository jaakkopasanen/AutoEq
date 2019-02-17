# Sennheiser HD 280 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.0; 31 -2.5; 34 -2.8; 37 -3.1; 41 -3.4; 45 -3.7; 49 -3.8; 54 -3.7; 60 -3.2; 66 -2.3; 72 -1.3; 79 -1.0; 87 -0.9; 96 -1.2; 106 -1.5; 116 -2.0; 128 -2.2; 141 -2.5; 155 -2.7; 170 -2.9; 187 -4.6; 206 -5.4; 227 -5.7; 249 -5.9; 274 -6.2; 302 -6.3; 332 -6.4; 365 -6.4; 402 -6.4; 442 -6.3; 486 -6.5; 535 -6.5; 588 -6.3; 647 -6.3; 712 -6.5; 783 -6.4; 861 -6.6; 947 -6.7; 1042 -6.9; 1146 -7.2; 1261 -7.2; 1387 -7.5; 1526 -8.1; 1678 -9.1; 1846 -9.2; 2031 -8.7; 2234 -7.8; 2457 -5.2; 2703 -2.3; 2973 -1.1; 3270 -1.7; 3597 -2.5; 3957 -2.1; 4353 -2.8; 4788 -3.4; 5267 -1.3; 5793 -0.8; 6373 -1.3; 7010 -4.2; 7711 -6.4; 8482 -8.4; 9330 -10.1; 10263 -7.0; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  1.01 | 6.0 dB  |
| Peaking | 23 Hz   |  1.09 | 3.3 dB  |
| Peaking | 95 Hz   |  0.89 | 5.6 dB  |
| Peaking | 3221 Hz |  3.04 | 5.6 dB  |
| Peaking | 5687 Hz |  3.05 | 6.3 dB  |
| Peaking | 162 Hz  | 10.35 | 1.7 dB  |
| Peaking | 1913 Hz |  1.95 | -3.4 dB |
| Peaking | 2700 Hz |  7.03 | 2.8 dB  |
| Peaking | 5315 Hz |  0.56 | 0.7 dB  |
| Peaking | 8999 Hz |  4.54 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)