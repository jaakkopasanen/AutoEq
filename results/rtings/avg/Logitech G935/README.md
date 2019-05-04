# Logitech G935
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.5; 25 -5.4; 28 -5.4; 31 -5.4; 34 -5.4; 37 -5.4; 41 -5.5; 45 -5.8; 49 -6.1; 54 -6.6; 60 -7.1; 66 -7.5; 72 -7.9; 79 -8.2; 87 -8.4; 96 -8.4; 106 -8.2; 116 -8.0; 128 -7.7; 141 -7.4; 155 -7.1; 170 -6.7; 187 -6.0; 206 -5.3; 227 -4.8; 249 -4.6; 274 -4.7; 302 -4.8; 332 -4.6; 365 -3.9; 402 -2.8; 442 -2.3; 486 -2.3; 535 -2.3; 588 -3.1; 647 -3.4; 712 -2.8; 783 -2.5; 861 -2.4; 947 -3.1; 1042 -3.2; 1146 -1.7; 1261 -0.5; 1387 -0.5; 1526 -2.3; 1678 -4.1; 1846 -5.2; 2031 -5.8; 2234 -6.7; 2457 -6.1; 2703 -4.5; 2973 -3.2; 3270 -2.4; 3597 -2.3; 3957 -5.2; 4353 -7.9; 4788 -6.6; 5267 -4.9; 5793 -3.9; 6373 -2.1; 7010 -4.0; 7711 -6.5; 8482 -6.6; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G935 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G935 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 93 Hz   | 0.38 | -1.1 dB |
| Peaking | 97 Hz   | 0.9  | -3.0 dB |
| Peaking | 518 Hz  | 0.97 | 2.2 dB  |
| Peaking | 1318 Hz | 3.52 | 4.1 dB  |
| Peaking | 2169 Hz | 4.05 | -2.8 dB |
| Peaking | 3509 Hz | 3.7  | 3.6 dB  |
| Peaking | 4354 Hz | 3.81 | -4.6 dB |
| Peaking | 6399 Hz | 4.7  | 2.9 dB  |
| Peaking | 7984 Hz | 5.07 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G935/Logitech%20G935.png)