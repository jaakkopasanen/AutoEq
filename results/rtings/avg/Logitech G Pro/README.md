# Logitech G Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.2; 25 -5.6; 28 -6.1; 31 -6.4; 34 -6.6; 37 -6.7; 41 -6.7; 45 -6.8; 49 -6.8; 54 -6.8; 60 -6.9; 66 -7.0; 72 -7.1; 79 -7.3; 87 -7.5; 96 -8.1; 106 -8.9; 116 -9.6; 128 -10.1; 141 -10.2; 155 -10.3; 170 -10.1; 187 -9.6; 206 -8.9; 227 -8.1; 249 -7.0; 274 -5.4; 302 -3.9; 332 -2.8; 365 -2.5; 402 -2.8; 442 -3.6; 486 -4.6; 535 -5.1; 588 -5.2; 647 -4.9; 712 -4.0; 783 -2.9; 861 -2.0; 947 -1.4; 1042 -1.3; 1146 -1.6; 1261 -2.2; 1387 -3.6; 1526 -4.6; 1678 -4.6; 1846 -4.4; 2031 -4.6; 2234 -4.6; 2457 -4.9; 2703 -4.2; 2973 -2.1; 3270 -1.5; 3597 -4.7; 3957 -5.4; 4353 -5.3; 4788 -5.4; 5267 -1.7; 5793 -0.9; 6373 -0.5; 7010 -4.4; 7711 -8.5; 8482 -9.5; 9330 -7.7; 10263 -5.6; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.8; 16529 -5.6; 18182 -6.7; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 139 Hz  | 1.23 | -5.7 dB |
| Peaking | 1005 Hz | 1.44 | 3.7 dB  |
| Peaking | 5852 Hz | 3.66 | 2.6 dB  |
| Peaking | 6320 Hz | 3.35 | 3.9 dB  |
| Peaking | 8171 Hz | 3.06 | -5.8 dB |
| Peaking | 42 Hz   | 1.43 | -1.5 dB |
| Peaking | 211 Hz  | 3.53 | -1.5 dB |
| Peaking | 349 Hz  | 3.19 | 3.5 dB  |
| Peaking | 3172 Hz | 4.47 | 6.2 dB  |
| Peaking | 3357 Hz | 1.67 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G%20Pro/Logitech%20G%20Pro.png)