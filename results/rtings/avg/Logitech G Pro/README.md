# Logitech G Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.9; 25 -5.3; 28 -5.8; 31 -6.1; 34 -6.3; 37 -6.4; 41 -6.5; 45 -6.5; 49 -6.5; 54 -6.5; 60 -6.6; 66 -6.7; 72 -6.9; 79 -7.0; 87 -7.3; 96 -7.8; 106 -8.7; 116 -9.4; 128 -9.8; 141 -10.0; 155 -10.0; 170 -9.8; 187 -9.4; 206 -8.6; 227 -7.7; 249 -6.6; 274 -5.1; 302 -3.5; 332 -2.4; 365 -2.1; 402 -2.4; 442 -3.1; 486 -4.1; 535 -4.6; 588 -4.7; 647 -4.4; 712 -3.5; 783 -2.3; 861 -1.5; 947 -0.8; 1042 -0.7; 1146 -1.0; 1261 -1.5; 1387 -2.9; 1526 -3.8; 1678 -3.9; 1846 -3.6; 2031 -3.7; 2234 -3.2; 2457 -3.5; 2703 -3.2; 2973 -1.6; 3270 -1.1; 3597 -4.5; 3957 -5.2; 4353 -5.0; 4788 -5.0; 5267 -0.5; 5793 -0.8; 6373 -0.6; 7010 -3.9; 7711 -7.1; 8482 -9.3; 9330 -8.9; 10263 -5.8; 11289 -3.2; 12418 -3.1; 13660 -4.4; 15026 -5.7; 16529 -5.3; 18182 -6.3; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--1.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.35 | -5.3 dB |
| Peaking | 161 Hz   | 1.06 | -7.7 dB |
| Peaking | 588 Hz   | 3.23 | -3.5 dB |
| Peaking | 1806 Hz  | 2.09 | -2.6 dB |
| Peaking | 20003 Hz | 0.05 | -5.4 dB |
| Peaking | 347 Hz   | 6.24 | 1.6 dB  |
| Peaking | 4425 Hz  | 2.59 | -6.1 dB |
| Peaking | 5871 Hz  | 1.4  | 7.9 dB  |
| Peaking | 8679 Hz  | 1.66 | -8.3 dB |
| Peaking | 11492 Hz | 1.87 | 4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -8.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -6.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G%20Pro/Logitech%20G%20Pro.png)