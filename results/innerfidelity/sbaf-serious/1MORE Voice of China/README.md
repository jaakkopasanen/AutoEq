# 1MORE Voice of China
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.6; 25 -3.2; 28 -3.9; 31 -4.5; 34 -5.0; 37 -5.4; 41 -5.9; 45 -6.3; 49 -6.8; 54 -7.2; 60 -7.7; 66 -8.1; 72 -8.4; 79 -8.9; 87 -9.3; 96 -9.7; 106 -9.8; 116 -9.9; 128 -10.1; 141 -10.2; 155 -10.1; 170 -10.0; 187 -9.8; 206 -9.6; 227 -9.1; 249 -8.8; 274 -8.3; 302 -7.8; 332 -7.4; 365 -6.8; 402 -6.2; 442 -5.5; 486 -5.1; 535 -4.6; 588 -3.7; 647 -3.3; 712 -3.1; 783 -2.6; 861 -2.5; 947 -2.7; 1042 -3.0; 1146 -3.2; 1261 -3.5; 1387 -3.9; 1526 -4.4; 1678 -4.9; 1846 -5.2; 2031 -5.3; 2234 -5.8; 2457 -6.4; 2703 -6.8; 2973 -6.3; 3270 -5.4; 3597 -4.6; 3957 -5.5; 4353 -8.4; 4788 -10.5; 5267 -9.4; 5793 -4.4; 6373 -0.9; 7010 -0.5; 7711 -2.7; 8482 -3.0; 9330 -3.0; 10263 -3.4; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Voice of China GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Voice of China ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 104 Hz  | 0.58 | -6.2 dB |
| Peaking | 239 Hz  | 1.03 | -3.4 dB |
| Peaking | 2506 Hz | 1.87 | -3.4 dB |
| Peaking | 4916 Hz | 3.35 | -8.3 dB |
| Peaking | 6474 Hz | 4.07 | 4.8 dB  |
| Peaking | 18 Hz   | 2.52 | 1.8 dB  |
| Peaking | 409 Hz  | 2.53 | -0.6 dB |
| Peaking | 812 Hz  | 1.83 | 1.3 dB  |
| Peaking | 1665 Hz | 4.34 | -0.9 dB |
| Peaking | 3675 Hz | 9.48 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Voice%20of%20China/1MORE%20Voice%20of%20China.png)