# Sennheiser HD 429
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.5; 25 -8.7; 28 -8.9; 31 -9.1; 34 -9.2; 37 -9.3; 41 -9.4; 45 -9.4; 49 -9.3; 54 -9.4; 60 -9.4; 66 -9.5; 72 -9.4; 79 -9.1; 87 -8.4; 96 -7.3; 106 -7.9; 116 -9.8; 128 -10.9; 141 -11.0; 155 -10.6; 170 -10.8; 187 -11.1; 206 -10.9; 227 -10.6; 249 -10.1; 274 -9.5; 302 -8.8; 332 -8.0; 365 -8.1; 402 -8.5; 442 -8.6; 486 -8.8; 535 -9.2; 588 -9.1; 647 -9.4; 712 -9.5; 783 -9.1; 861 -8.9; 947 -8.6; 1042 -8.6; 1146 -8.9; 1261 -8.6; 1387 -9.0; 1526 -9.4; 1678 -9.1; 1846 -8.2; 2031 -6.8; 2234 -4.9; 2457 -4.4; 2703 -4.0; 2973 -3.2; 3270 -2.8; 3597 -3.6; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 429 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 429 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.72 | -2.9 dB |
| Peaking | 180 Hz  | 1.13 | -4.4 dB |
| Peaking | 711 Hz  | 1.04 | -2.7 dB |
| Peaking | 1558 Hz | 2.87 | -3.1 dB |
| Peaking | 4641 Hz | 1.2  | 6.6 dB  |
| Peaking | 101 Hz  | 4.49 | 4.4 dB  |
| Peaking | 105 Hz  | 2.29 | -2.5 dB |
| Peaking | 2607 Hz | 3.47 | 1.3 dB  |
| Peaking | 6296 Hz | 3.04 | 5.4 dB  |
| Peaking | 6905 Hz | 1.35 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20429/Sennheiser%20HD%20429.png)