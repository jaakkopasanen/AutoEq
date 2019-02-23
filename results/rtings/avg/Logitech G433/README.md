# Logitech G433
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.3; 25 -3.7; 28 -4.2; 31 -4.7; 34 -5.1; 37 -5.5; 41 -5.8; 45 -5.9; 49 -6.0; 54 -6.0; 60 -6.0; 66 -6.1; 72 -6.1; 79 -6.1; 87 -6.4; 96 -6.9; 106 -7.7; 116 -8.4; 128 -8.8; 141 -8.8; 155 -8.8; 170 -8.8; 187 -8.5; 206 -7.8; 227 -7.1; 249 -6.5; 274 -5.7; 302 -4.9; 332 -4.2; 365 -3.7; 402 -3.7; 442 -4.3; 486 -5.2; 535 -6.2; 588 -7.1; 647 -7.8; 712 -7.7; 783 -6.8; 861 -5.5; 947 -4.4; 1042 -4.0; 1146 -4.1; 1261 -4.3; 1387 -4.5; 1526 -4.1; 1678 -3.9; 1846 -4.5; 2031 -5.2; 2234 -5.1; 2457 -4.1; 2703 -3.7; 2973 -3.5; 3270 -3.6; 3597 -5.7; 3957 -9.5; 4353 -9.0; 4788 -6.6; 5267 -5.5; 5793 -1.6; 6373 -0.5; 7010 -3.5; 7711 -6.7; 8482 -8.4; 9330 -8.0; 10263 -6.2; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -6.1; 16529 -6.8; 18182 -7.4; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G433 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G433 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.82 | 3.0 dB   |
| Peaking | 145 Hz  | 1.71 | -3.5 dB  |
| Peaking | 3438 Hz | 0.74 | 21.4 dB  |
| Peaking | 3939 Hz | 0.79 | -23.1 dB |
| Peaking | 6121 Hz | 3.71 | 8.6 dB   |
| Peaking | 387 Hz  | 2.61 | 2.8 dB   |
| Peaking | 705 Hz  | 1.81 | -4.4 dB  |
| Peaking | 931 Hz  | 1.31 | 2.7 dB   |
| Peaking | 2170 Hz | 4.78 | -1.5 dB  |
| Peaking | 8600 Hz | 6.7  | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G433/Logitech%20G433.png)