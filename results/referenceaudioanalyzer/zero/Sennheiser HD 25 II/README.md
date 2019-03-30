# Sennheiser HD 25 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -1.3; 332 -2.6; 365 -4.5; 402 -6.5; 442 -8.3; 486 -9.5; 535 -10.1; 588 -10.1; 647 -9.6; 712 -8.9; 783 -8.3; 861 -8.1; 947 -8.1; 1042 -8.1; 1146 -7.9; 1261 -7.8; 1387 -7.8; 1526 -7.9; 1678 -8.4; 1846 -9.3; 2031 -10.1; 2234 -10.5; 2457 -10.5; 2703 -10.2; 2973 -9.9; 3270 -9.8; 3597 -9.6; 3957 -8.5; 4353 -6.9; 4788 -5.6; 5267 -5.3; 5793 -5.4; 6373 -6.8; 7010 -9.3; 7711 -12.6; 8482 -14.7; 9330 -14.8; 10263 -14.0; 11289 -13.8; 12418 -14.0; 13660 -11.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 105 Hz   | 0.11 | 6.6 dB  |
| Peaking | 546 Hz   | 1.48 | -8.3 dB |
| Peaking | 3087 Hz  | 0.4  | -5.1 dB |
| Peaking | 5495 Hz  | 1.43 | 8.6 dB  |
| Peaking | 9510 Hz  | 0.97 | -8.7 dB |
| Peaking | 17 Hz    | 1.23 | 1.1 dB  |
| Peaking | 152 Hz   | 0.13 | -0.5 dB |
| Peaking | 268 Hz   | 2.32 | 2.0 dB  |
| Peaking | 12950 Hz | 3.07 | -5.1 dB |
| Peaking | 14580 Hz | 1.29 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 4.3 dB  |
| Peaking | 250 Hz   | 1.41 | 6.8 dB  |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%2025%20II/Sennheiser%20HD%2025%20II.png)