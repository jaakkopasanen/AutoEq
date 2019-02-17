# Logitech G533
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.5; 25 -6.7; 28 -6.9; 31 -7.1; 34 -7.2; 37 -7.1; 41 -7.0; 45 -6.8; 49 -6.7; 54 -6.7; 60 -6.7; 66 -6.7; 72 -6.7; 79 -6.9; 87 -7.0; 96 -7.3; 106 -7.4; 116 -7.5; 128 -7.5; 141 -7.5; 155 -7.5; 170 -7.4; 187 -7.2; 206 -7.0; 227 -6.7; 249 -6.7; 274 -7.1; 302 -7.4; 332 -7.4; 365 -6.9; 402 -6.1; 442 -5.5; 486 -5.1; 535 -4.4; 588 -3.9; 647 -3.5; 712 -3.1; 783 -2.0; 861 -1.6; 947 -2.4; 1042 -3.0; 1146 -3.3; 1261 -2.9; 1387 -1.7; 1526 -0.5; 1678 -1.1; 1846 -2.2; 2031 -2.9; 2234 -2.8; 2457 -2.2; 2703 -5.2; 2973 -5.0; 3270 -4.4; 3597 -5.6; 3957 -6.5; 4353 -7.2; 4788 -5.3; 5267 -3.4; 5793 -3.9; 6373 -5.9; 7010 -5.7; 7711 -6.1; 8482 -9.4; 9330 -9.0; 10263 -3.8; 11289 -3.1; 12418 -7.8; 13660 -10.2; 15026 -8.3; 16529 -8.2; 18182 -12.7; 20000 -18.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G533 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G533 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.38 | -3.9 dB  |
| Peaking | 147 Hz   | 0.86 | -3.6 dB  |
| Peaking | 334 Hz   | 1.86 | -3.5 dB  |
| Peaking | 18571 Hz | 0.09 | -4.2 dB  |
| Peaking | 19789 Hz | 0.95 | -11.2 dB |
| Peaking | 1585 Hz  | 3.15 | 2.8 dB   |
| Peaking | 4363 Hz  | 2.64 | -3.5 dB  |
| Peaking | 5283 Hz  | 3.57 | 3.6 dB   |
| Peaking | 8920 Hz  | 5.45 | -4.5 dB  |
| Peaking | 10819 Hz | 5.38 | 5.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -9.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G533/Logitech%20G533.png)