# Sennheiser HD 229 Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.9; 25 -4.5; 28 -5.4; 31 -6.2; 34 -6.9; 37 -7.5; 41 -8.1; 45 -8.7; 49 -9.1; 54 -9.7; 60 -10.1; 66 -10.5; 72 -10.7; 79 -10.9; 87 -10.9; 96 -11.1; 106 -10.9; 116 -10.5; 128 -9.9; 141 -9.4; 155 -10.8; 170 -9.7; 187 -9.4; 206 -8.0; 227 -8.6; 249 -7.9; 274 -6.7; 302 -5.4; 332 -4.4; 365 -3.6; 402 -3.5; 442 -3.7; 486 -3.7; 535 -3.9; 588 -3.8; 647 -3.7; 712 -4.3; 783 -4.6; 861 -5.0; 947 -5.3; 1042 -5.4; 1146 -5.4; 1261 -5.2; 1387 -4.9; 1526 -4.5; 1678 -6.7; 1846 -6.4; 2031 -5.7; 2234 -5.1; 2457 -4.9; 2703 -4.9; 2973 -4.7; 3270 -4.6; 3597 -4.8; 3957 -6.2; 4353 -7.5; 4788 -7.2; 5267 -4.2; 5793 -1.6; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -9.5; 9330 -11.6; 10263 -6.4; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 229 Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 229 Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 81 Hz   | 1.09 | -5.4 dB |
| Peaking | 164 Hz  | 2.77 | -3.1 dB |
| Peaking | 6277 Hz | 4.37 | 6.3 dB  |
| Peaking | 9087 Hz | 5.24 | -6.7 dB |
| Peaking | 21 Hz   | 2.96 | 3.5 dB  |
| Peaking | 385 Hz  | 3.6  | 2.4 dB  |
| Peaking | 603 Hz  | 1.73 | 2.2 dB  |
| Peaking | 3883 Hz | 1.29 | 2.4 dB  |
| Peaking | 4374 Hz | 3.5  | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20229%20Black/Sennheiser%20HD%20229%20Black.png)