# Sennheiser HD 280 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.8; 25 -7.2; 28 -7.6; 31 -8.0; 34 -8.2; 37 -8.2; 41 -8.1; 45 -7.8; 49 -7.5; 54 -7.0; 60 -6.4; 66 -5.8; 72 -5.2; 79 -4.7; 87 -4.4; 96 -4.3; 106 -4.1; 116 -3.7; 128 -3.2; 141 -2.3; 155 -1.5; 170 -1.3; 187 -2.3; 206 -3.9; 227 -5.2; 249 -6.1; 274 -6.9; 302 -7.4; 332 -7.7; 365 -8.1; 402 -8.6; 442 -8.5; 486 -8.1; 535 -7.8; 588 -7.5; 647 -7.1; 712 -6.8; 783 -6.6; 861 -6.2; 947 -5.6; 1042 -5.5; 1146 -5.7; 1261 -5.7; 1387 -5.6; 1526 -5.6; 1678 -5.6; 1846 -5.9; 2031 -6.2; 2234 -5.8; 2457 -4.2; 2703 -1.9; 2973 -0.5; 3270 -1.9; 3597 -3.0; 3957 -1.6; 4353 -1.1; 4788 -4.5; 5267 -4.3; 5793 -4.3; 6373 -4.0; 7010 -3.4; 7711 -5.7; 8482 -8.0; 9330 -6.4; 10263 -5.1; 11289 -6.4; 12418 -5.6; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 1.17 | -3.4 dB |
| Peaking | 166 Hz   | 1.41 | 5.4 dB  |
| Peaking | 364 Hz   | 0.68 | -4.0 dB |
| Peaking | 2953 Hz  | 5.26 | 4.8 dB  |
| Peaking | 4174 Hz  | 5.16 | 4.1 dB  |
| Peaking | 224 Hz   | 5.28 | -0.3 dB |
| Peaking | 2066 Hz  | 5.35 | -1.4 dB |
| Peaking | 6929 Hz  | 4.12 | 2.4 dB  |
| Peaking | 8421 Hz  | 4.4  | -3.4 dB |
| Peaking | 14207 Hz | 1.62 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | 3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)