# Sennheiser HD 219
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.7; 25 -4.3; 28 -5.1; 31 -5.8; 34 -6.4; 37 -6.9; 41 -7.5; 45 -8.1; 49 -8.5; 54 -9.0; 60 -9.4; 66 -9.8; 72 -10.0; 79 -10.2; 87 -10.2; 96 -10.4; 106 -10.4; 116 -10.2; 128 -9.8; 141 -9.0; 155 -9.0; 170 -8.9; 187 -9.1; 206 -8.4; 227 -7.5; 249 -7.3; 274 -6.5; 302 -5.3; 332 -4.2; 365 -3.7; 402 -3.4; 442 -3.4; 486 -3.6; 535 -4.0; 588 -4.4; 647 -4.3; 712 -3.4; 783 -4.0; 861 -4.6; 947 -5.1; 1042 -5.5; 1146 -5.6; 1261 -5.7; 1387 -5.6; 1526 -5.2; 1678 -6.5; 1846 -6.9; 2031 -6.6; 2234 -6.0; 2457 -5.5; 2703 -5.1; 2973 -5.0; 3270 -4.5; 3597 -3.8; 3957 -5.0; 4353 -7.2; 4788 -6.1; 5267 -3.3; 5793 -1.2; 6373 -0.5; 7010 -3.3; 7711 -6.7; 8482 -10.0; 9330 -10.1; 10263 -6.1; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -6.1; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 219 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 86 Hz   | 1.08 | -4.9 dB |
| Peaking | 176 Hz  | 3.06 | -2.2 dB |
| Peaking | 6243 Hz | 3.51 | 6.3 dB  |
| Peaking | 8767 Hz | 4.04 | -5.9 dB |
| Peaking | 21 Hz   | 2.82 | 3.5 dB  |
| Peaking | 417 Hz  | 2.37 | 2.9 dB  |
| Peaking | 731 Hz  | 3.32 | 2.1 dB  |
| Peaking | 3673 Hz | 3.37 | 2.2 dB  |
| Peaking | 4386 Hz | 5.72 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)