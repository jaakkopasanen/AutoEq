# Logitech G433
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.5; 25 -3.9; 28 -4.4; 31 -4.9; 34 -5.3; 37 -5.7; 41 -6.0; 45 -6.1; 49 -6.2; 54 -6.2; 60 -6.2; 66 -6.3; 72 -6.3; 79 -6.3; 87 -6.6; 96 -7.1; 106 -7.9; 116 -8.6; 128 -9.0; 141 -9.0; 155 -9.1; 170 -9.0; 187 -8.7; 206 -8.0; 227 -7.3; 249 -6.7; 274 -5.9; 302 -5.1; 332 -4.4; 365 -3.9; 402 -3.9; 442 -4.5; 486 -5.4; 535 -6.4; 588 -7.3; 647 -8.0; 712 -7.9; 783 -7.1; 861 -5.7; 947 -4.6; 1042 -4.2; 1146 -4.3; 1261 -4.5; 1387 -4.7; 1526 -4.3; 1678 -4.1; 1846 -4.7; 2031 -5.5; 2234 -5.3; 2457 -4.3; 2703 -3.9; 2973 -3.7; 3270 -3.8; 3597 -5.9; 3957 -9.7; 4353 -9.2; 4788 -6.8; 5267 -5.7; 5793 -1.8; 6373 -0.5; 7010 -3.7; 7711 -6.9; 8482 -8.6; 9330 -8.2; 10263 -6.3; 11289 -4.8; 12418 -4.8; 13660 -5.4; 15026 -6.3; 16529 -7.0; 18182 -7.6; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G433 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G433 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 141 Hz   | 0.99 | -5.0 dB |
| Peaking | 674 Hz   | 3.45 | -4.0 dB |
| Peaking | 4162 Hz  | 5.85 | -5.7 dB |
| Peaking | 6199 Hz  | 6.47 | 6.6 dB  |
| Peaking | 20228 Hz | 0.06 | -2.8 dB |
| Peaking | 372 Hz   | 4.49 | 1.8 dB  |
| Peaking | 7021 Hz  | 5.42 | 1.9 dB  |
| Peaking | 8686 Hz  | 2.39 | -3.8 dB |
| Peaking | 11823 Hz | 1.69 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G433/Logitech%20G433.png)