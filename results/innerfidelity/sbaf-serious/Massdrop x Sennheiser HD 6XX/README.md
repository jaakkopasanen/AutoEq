# Massdrop x Sennheiser HD 6XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.2; 49 -1.7; 54 -2.1; 60 -2.4; 66 -3.2; 72 -3.5; 79 -4.3; 87 -5.6; 96 -6.5; 106 -7.1; 116 -7.5; 128 -8.0; 141 -8.3; 155 -8.6; 170 -8.5; 187 -8.6; 206 -8.9; 227 -8.6; 249 -8.5; 274 -8.2; 302 -8.0; 332 -7.9; 365 -7.8; 402 -7.6; 442 -7.4; 486 -7.4; 535 -7.2; 588 -6.8; 647 -6.8; 712 -6.6; 783 -6.3; 861 -6.6; 947 -6.8; 1042 -6.2; 1146 -7.1; 1261 -7.2; 1387 -7.5; 1526 -7.9; 1678 -8.2; 1846 -7.9; 2031 -7.2; 2234 -6.9; 2457 -6.4; 2703 -6.1; 2973 -6.3; 3270 -6.3; 3597 -6.6; 3957 -6.0; 4353 -5.7; 4788 -5.2; 5267 -3.1; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser HD 6XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser HD 6XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.32 | 7.0 dB  |
| Peaking | 136 Hz  | 0.56 | -4.9 dB |
| Peaking | 1660 Hz | 2.98 | -1.7 dB |
| Peaking | 6186 Hz | 2.83 | 6.7 dB  |
| Peaking | 7585 Hz | 2.23 | -1.8 dB |
| Peaking | 777 Hz  | 4.68 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Sennheiser%20HD%206XX/Massdrop%20x%20Sennheiser%20HD%206XX.png)