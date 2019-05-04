# Logitech G635
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.4; 25 -5.6; 28 -5.7; 31 -5.8; 34 -5.9; 37 -5.9; 41 -6.0; 45 -6.0; 49 -6.0; 54 -6.0; 60 -6.0; 66 -6.1; 72 -6.0; 79 -5.9; 87 -5.9; 96 -6.0; 106 -6.1; 116 -6.3; 128 -6.5; 141 -6.7; 155 -6.8; 170 -6.7; 187 -6.5; 206 -6.2; 227 -6.0; 249 -5.9; 274 -5.9; 302 -5.8; 332 -5.5; 365 -4.9; 402 -4.3; 442 -4.0; 486 -4.0; 535 -4.1; 588 -4.2; 647 -4.1; 712 -3.4; 783 -3.9; 861 -3.7; 947 -2.4; 1042 -2.5; 1146 -2.2; 1261 -0.9; 1387 -0.5; 1526 -1.1; 1678 -2.9; 1846 -4.6; 2031 -5.0; 2234 -4.9; 2457 -4.5; 2703 -3.7; 2973 -3.2; 3270 -3.1; 3597 -3.4; 3957 -6.0; 4353 -7.9; 4788 -6.9; 5267 -6.0; 5793 -5.5; 6373 -4.0; 7010 -5.2; 7711 -7.6; 8482 -8.2; 9330 -4.9; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G635 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G635 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 118 Hz  | 0.39 | -1.8 dB  |
| Peaking | 1529 Hz | 0.7  | 16.0 dB  |
| Peaking | 1974 Hz | 0.58 | -16.6 dB |
| Peaking | 3139 Hz | 1.09 | 6.9 dB   |
| Peaking | 4329 Hz | 4.47 | -4.2 dB  |
| Peaking | 448 Hz  | 3.91 | 1.1 dB   |
| Peaking | 5619 Hz | 2.77 | -0.7 dB  |
| Peaking | 6450 Hz | 4.6  | 2.4 dB   |
| Peaking | 8229 Hz | 3.99 | -4.5 dB  |
| Peaking | 9342 Hz | 1.89 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G635/Logitech%20G635.png)