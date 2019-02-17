# Sennheiser HD 429
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.5; 25 -6.6; 28 -6.9; 31 -7.0; 34 -7.2; 37 -7.2; 41 -7.3; 45 -7.3; 49 -7.2; 54 -7.3; 60 -7.4; 66 -7.4; 72 -7.3; 79 -7.0; 87 -6.4; 96 -5.2; 106 -5.8; 116 -7.7; 128 -8.8; 141 -8.9; 155 -8.6; 170 -8.7; 187 -9.0; 206 -8.9; 227 -8.6; 249 -8.1; 274 -7.5; 302 -6.7; 332 -5.9; 365 -6.0; 402 -6.4; 442 -6.6; 486 -6.7; 535 -7.1; 588 -7.1; 647 -7.3; 712 -7.4; 783 -7.0; 861 -6.8; 947 -6.5; 1042 -6.5; 1146 -6.8; 1261 -6.6; 1387 -7.0; 1526 -7.3; 1678 -7.1; 1846 -6.1; 2031 -4.8; 2234 -2.9; 2457 -2.4; 2703 -1.9; 2973 -1.1; 3270 -0.7; 3597 -1.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 429 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 429 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.97 | -0.6 dB |
| Peaking | 99 Hz   | 4.61 | 3.1 dB  |
| Peaking | 156 Hz  | 1.08 | -2.7 dB |
| Peaking | 1547 Hz | 2.28 | -2.4 dB |
| Peaking | 3927 Hz | 0.85 | 6.7 dB  |
| Peaking | 343 Hz  | 5.52 | 1.4 dB  |
| Peaking | 680 Hz  | 2.82 | -1.0 dB |
| Peaking | 3720 Hz | 6.92 | -1.3 dB |
| Peaking | 6341 Hz | 2.5  | 4.6 dB  |
| Peaking | 7505 Hz | 1.65 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20429/Sennheiser%20HD%20429.png)