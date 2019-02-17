# Logitech G430
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.8; 25 -4.6; 28 -5.7; 31 -6.7; 34 -7.4; 37 -7.9; 41 -8.5; 45 -8.8; 49 -9.1; 54 -9.2; 60 -9.2; 66 -9.1; 72 -8.9; 79 -8.8; 87 -8.9; 96 -9.2; 106 -9.4; 116 -9.4; 128 -9.2; 141 -9.1; 155 -8.9; 170 -8.5; 187 -8.1; 206 -7.6; 227 -7.2; 249 -7.3; 274 -7.0; 302 -5.9; 332 -5.1; 365 -4.4; 402 -3.6; 442 -3.0; 486 -3.3; 535 -4.2; 588 -4.9; 647 -5.1; 712 -5.1; 783 -4.9; 861 -4.8; 947 -4.7; 1042 -4.5; 1146 -4.6; 1261 -4.3; 1387 -4.0; 1526 -4.8; 1678 -5.1; 1846 -5.6; 2031 -5.7; 2234 -4.6; 2457 -2.9; 2703 -1.8; 2973 -1.7; 3270 -1.3; 3597 -0.5; 3957 -1.2; 4353 -5.2; 4788 -6.0; 5267 -6.0; 5793 -7.1; 6373 -8.7; 7010 -3.4; 7711 -4.3; 8482 -4.5; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -5.2; 13660 -5.4; 15026 -5.3; 16529 -5.5; 18182 -7.0; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G430 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G430 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  1.42 | 5.2 dB  |
| Peaking | 68 Hz    |  0.22 | -5.0 dB |
| Peaking | 424 Hz   |  2.1  | 3.4 dB  |
| Peaking | 3385 Hz  |  2.79 | 4.3 dB  |
| Peaking | 5982 Hz  |  4.47 | -4.3 dB |
| Peaking | 2033 Hz  |  3.08 | -3.7 dB |
| Peaking | 2256 Hz  |  1.83 | 2.4 dB  |
| Peaking | 4611 Hz  |  7.65 | -2.2 dB |
| Peaking | 7158 Hz  | 10.17 | 2.3 dB  |
| Peaking | 20057 Hz |  0.98 | -7.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G430/Logitech%20G430.png)