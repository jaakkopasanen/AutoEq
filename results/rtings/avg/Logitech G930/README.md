# Logitech G930
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.6; 25 -7.1; 28 -7.7; 31 -8.1; 34 -8.3; 37 -8.3; 41 -8.2; 45 -8.0; 49 -7.9; 54 -7.6; 60 -7.3; 66 -7.2; 72 -7.4; 79 -7.8; 87 -8.3; 96 -8.9; 106 -9.3; 116 -9.5; 128 -9.5; 141 -9.3; 155 -8.8; 170 -8.0; 187 -6.9; 206 -5.6; 227 -3.6; 249 -1.6; 274 -0.6; 302 -2.6; 332 -5.2; 365 -7.1; 402 -8.2; 442 -8.8; 486 -9.4; 535 -9.7; 588 -9.9; 647 -10.0; 712 -9.8; 783 -9.7; 861 -9.5; 947 -9.2; 1042 -8.9; 1146 -8.1; 1261 -7.3; 1387 -6.5; 1526 -7.1; 1678 -7.5; 1846 -7.4; 2031 -7.0; 2234 -6.2; 2457 -4.9; 2703 -3.6; 2973 -2.1; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -8.9; 4788 -10.8; 5267 -8.6; 5793 -8.2; 6373 -12.3; 7010 -6.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -8.4; 15026 -7.6; 16529 -7.5; 18182 -9.7; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G930 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G930 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 136 Hz   | 0.76 | -3.1 dB  |
| Peaking | 268 Hz   | 1.93 | 10.0 dB  |
| Peaking | 513 Hz   | 0.53 | -4.3 dB  |
| Peaking | 3796 Hz  | 1.87 | 15.1 dB  |
| Peaking | 4527 Hz  | 1.74 | -12.5 dB |
| Peaking | 35 Hz    | 2.7  | -1.5 dB  |
| Peaking | 1975 Hz  | 6.07 | -1.1 dB  |
| Peaking | 6425 Hz  | 7.74 | -8.2 dB  |
| Peaking | 6668 Hz  | 2.39 | 3.6 dB   |
| Peaking | 20114 Hz | 0.61 | -5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | 5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -4.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G930/Logitech%20G930.png)