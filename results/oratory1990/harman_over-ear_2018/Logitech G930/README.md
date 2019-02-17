# Logitech G930
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.8; 25 -6.5; 28 -7.4; 31 -8.0; 34 -8.5; 37 -8.9; 41 -9.1; 45 -9.2; 49 -9.1; 54 -8.9; 60 -8.1; 66 -7.0; 72 -6.3; 79 -7.3; 87 -8.7; 96 -8.8; 106 -9.9; 116 -11.2; 128 -11.7; 141 -11.8; 155 -11.4; 170 -10.5; 187 -10.1; 206 -8.7; 227 -7.3; 249 -5.7; 274 -4.7; 302 -5.2; 332 -5.5; 365 -6.0; 402 -6.2; 442 -6.4; 486 -6.4; 535 -6.5; 588 -6.6; 647 -6.7; 712 -6.7; 783 -6.3; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -7.2; 1261 -8.0; 1387 -7.7; 1526 -6.9; 1678 -6.8; 1846 -6.6; 2031 -5.6; 2234 -5.6; 2457 -5.8; 2703 -4.5; 2973 -1.7; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -9.0; 4788 -8.7; 5267 -8.2; 5793 -10.8; 6373 -10.3; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.5; 13660 -9.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G930 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G930 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 1.94 | 3.2 dB  |
| Peaking | 42 Hz    | 1.73 | -3.0 dB |
| Peaking | 137 Hz   | 2    | -5.9 dB |
| Peaking | 3590 Hz  | 2.42 | 10.6 dB |
| Peaking | 4641 Hz  | 1.59 | -6.4 dB |
| Peaking | 285 Hz   | 3.98 | 2.5 dB  |
| Peaking | 1327 Hz  | 4.31 | -1.8 dB |
| Peaking | 6160 Hz  | 7.27 | -7.4 dB |
| Peaking | 6607 Hz  | 2.63 | 4.0 dB  |
| Peaking | 13302 Hz | 6.39 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Logitech%20G930/Logitech%20G930.png)