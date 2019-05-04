# Logitech G433
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.2; 25 -3.6; 28 -4.2; 31 -4.7; 34 -5.1; 37 -5.5; 41 -5.8; 45 -5.9; 49 -6.0; 54 -6.0; 60 -6.0; 66 -6.0; 72 -6.0; 79 -6.1; 87 -6.3; 96 -6.9; 106 -7.6; 116 -8.3; 128 -8.7; 141 -8.7; 155 -8.8; 170 -8.8; 187 -8.4; 206 -7.8; 227 -7.2; 249 -6.6; 274 -5.8; 302 -5.0; 332 -4.3; 365 -3.8; 402 -3.8; 442 -4.4; 486 -5.4; 535 -6.4; 588 -7.4; 647 -8.1; 712 -8.0; 783 -7.1; 861 -5.8; 947 -4.7; 1042 -4.3; 1146 -4.4; 1261 -4.6; 1387 -4.8; 1526 -4.6; 1678 -4.3; 1846 -4.9; 2031 -5.8; 2234 -6.1; 2457 -5.2; 2703 -4.4; 2973 -3.8; 3270 -3.5; 3597 -5.7; 3957 -9.3; 4353 -8.8; 4788 -7.1; 5267 -5.9; 5793 -1.6; 6373 -0.5; 7010 -3.7; 7711 -7.7; 8482 -8.2; 9330 -6.5; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.8; 18182 -7.3; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G433 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G433 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.54 | 3.2 dB   |
| Peaking | 146 Hz  | 1.84 | -3.3 dB  |
| Peaking | 3545 Hz | 0.92 | 22.2 dB  |
| Peaking | 3878 Hz | 0.96 | -23.7 dB |
| Peaking | 6151 Hz | 4.46 | 8.2 dB   |
| Peaking | 387 Hz  | 2.68 | 2.9 dB   |
| Peaking | 700 Hz  | 1.86 | -4.4 dB  |
| Peaking | 937 Hz  | 1.14 | 2.7 dB   |
| Peaking | 2209 Hz | 5.13 | -1.8 dB  |
| Peaking | 8081 Hz | 8.11 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G433/Logitech%20G433.png)