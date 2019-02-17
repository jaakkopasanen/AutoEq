# Logitech G930
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.1; 25 -4.6; 28 -5.2; 31 -5.6; 34 -5.8; 37 -5.8; 41 -5.7; 45 -5.5; 49 -5.4; 54 -5.2; 60 -4.8; 66 -4.8; 72 -4.9; 79 -5.3; 87 -5.8; 96 -6.4; 106 -6.8; 116 -7.0; 128 -7.0; 141 -6.8; 155 -6.3; 170 -5.5; 187 -4.5; 206 -3.1; 227 -1.1; 249 -0.5; 274 -0.5; 302 -0.6; 332 -2.7; 365 -4.6; 402 -5.8; 442 -6.3; 486 -6.9; 535 -7.3; 588 -7.4; 647 -7.5; 712 -7.3; 783 -7.2; 861 -7.0; 947 -6.7; 1042 -6.4; 1146 -5.6; 1261 -4.8; 1387 -4.0; 1526 -4.7; 1678 -5.0; 1846 -4.9; 2031 -4.6; 2234 -3.7; 2457 -2.5; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -6.4; 4788 -8.3; 5267 -6.1; 5793 -5.7; 6373 -9.8; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.3; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G930 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G930 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.65 | 3.1 dB  |
| Peaking | 64 Hz   | 3.18 | 1.8 dB  |
| Peaking | 264 Hz  | 2.53 | 7.0 dB  |
| Peaking | 2823 Hz | 2.28 | 5.7 dB  |
| Peaking | 3716 Hz | 5.71 | 4.5 dB  |
| Peaking | 126 Hz  | 3.62 | -1.2 dB |
| Peaking | 548 Hz  | 3.37 | -1.2 dB |
| Peaking | 768 Hz  | 2.19 | -1.0 dB |
| Peaking | 1376 Hz | 3.64 | 2.1 dB  |
| Peaking | 4691 Hz | 9.02 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | 6.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G930/Logitech%20G930.png)