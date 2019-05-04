# Sennheiser HD 202 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.4; 25 -5.1; 28 -6.0; 31 -6.8; 34 -7.5; 37 -8.1; 41 -8.7; 45 -9.3; 49 -9.8; 54 -10.5; 60 -11.2; 66 -11.6; 72 -11.7; 79 -11.9; 87 -12.2; 96 -12.3; 106 -12.2; 116 -11.9; 128 -11.4; 141 -10.8; 155 -10.2; 170 -9.5; 187 -8.6; 206 -7.6; 227 -6.4; 249 -5.4; 274 -4.4; 302 -4.2; 332 -5.2; 365 -5.3; 402 -5.4; 442 -5.8; 486 -6.6; 535 -7.3; 588 -7.9; 647 -8.2; 712 -8.4; 783 -8.6; 861 -8.8; 947 -9.0; 1042 -9.4; 1146 -9.7; 1261 -10.2; 1387 -10.9; 1526 -11.2; 1678 -11.1; 1846 -10.5; 2031 -9.5; 2234 -8.8; 2457 -7.9; 2703 -6.1; 2973 -4.6; 3270 -1.6; 3597 -0.5; 3957 -0.5; 4353 -1.9; 4788 -4.6; 5267 -4.2; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -8.5; 8482 -7.3; 9330 -6.5; 10263 -6.5; 11289 -6.8; 12418 -12.1; 13660 -12.8; 15026 -10.2; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 89 Hz    |  1.04 | -6.4 dB |
| Peaking | 1580 Hz  |  1.05 | -5.1 dB |
| Peaking | 3670 Hz  |  2.4  | 7.6 dB  |
| Peaking | 6179 Hz  |  5.38 | 6.1 dB  |
| Peaking | 13555 Hz |  2.52 | -7.2 dB |
| Peaking | 17 Hz    |  1.36 | 4.3 dB  |
| Peaking | 45 Hz    |  2.26 | -1.4 dB |
| Peaking | 156 Hz   |  2.46 | -1.6 dB |
| Peaking | 291 Hz   |  2.12 | 3.3 dB  |
| Peaking | 7913 Hz  | 10.71 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20202%20II/Sennheiser%20HD%20202%20II.png)