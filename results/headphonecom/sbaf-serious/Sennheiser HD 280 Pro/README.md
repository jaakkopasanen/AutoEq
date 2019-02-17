# Sennheiser HD 280 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.5; 25 -6.7; 28 -7.0; 31 -7.1; 34 -7.2; 37 -7.3; 41 -7.2; 45 -7.0; 49 -6.7; 54 -6.0; 60 -4.7; 66 -2.5; 72 -0.5; 79 -0.6; 87 -3.9; 96 -5.6; 106 -1.5; 116 -0.5; 128 -2.3; 141 -3.0; 155 -2.3; 170 -3.0; 187 -4.8; 206 -5.8; 227 -6.3; 249 -6.7; 274 -7.0; 302 -6.8; 332 -6.9; 365 -6.7; 402 -6.8; 442 -6.5; 486 -6.4; 535 -6.4; 588 -6.8; 647 -6.7; 712 -6.6; 783 -6.5; 861 -6.4; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -6.6; 1387 -6.3; 1526 -5.8; 1678 -6.7; 1846 -7.3; 2031 -7.6; 2234 -8.1; 2457 -8.3; 2703 -6.6; 2973 -3.4; 3270 -3.5; 3597 -5.1; 3957 -5.4; 4353 -4.9; 4788 -4.7; 5267 -3.2; 5793 -3.7; 6373 -5.4; 7010 -6.1; 7711 -7.7; 8482 -10.1; 9330 -12.1; 10263 -11.4; 11289 -7.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 280 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 73 Hz   |  5.03 | 5.9 dB  |
| Peaking | 126 Hz  |  2.03 | 5.1 dB  |
| Peaking | 3169 Hz |  7.93 | 3.8 dB  |
| Peaking | 5421 Hz |  2.82 | 3.7 dB  |
| Peaking | 9460 Hz |  3.03 | -6.4 dB |
| Peaking | 37 Hz   |  2.37 | -1.3 dB |
| Peaking | 164 Hz  | 10.38 | 2.8 dB  |
| Peaking | 276 Hz  |  1.46 | -0.8 dB |
| Peaking | 2308 Hz |  4.22 | -2.4 dB |
| Peaking | 7552 Hz |  0.14 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)