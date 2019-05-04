# HyperX Cloud Mix
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -7.0; 25 -7.3; 28 -7.8; 31 -8.1; 34 -8.4; 37 -8.5; 41 -8.6; 45 -8.6; 49 -8.7; 54 -8.8; 60 -9.0; 66 -9.3; 72 -9.4; 79 -9.6; 87 -9.8; 96 -10.0; 106 -10.2; 116 -10.3; 128 -10.3; 141 -10.3; 155 -10.3; 170 -10.3; 187 -10.2; 206 -10.2; 227 -10.2; 249 -10.1; 274 -10.0; 302 -9.7; 332 -9.0; 365 -8.3; 402 -7.5; 442 -6.7; 486 -5.8; 535 -4.9; 588 -4.4; 647 -4.6; 712 -5.5; 783 -6.3; 861 -6.7; 947 -7.0; 1042 -6.9; 1146 -7.0; 1261 -7.5; 1387 -8.2; 1526 -8.9; 1678 -9.0; 1846 -8.6; 2031 -7.9; 2234 -6.8; 2457 -5.2; 2703 -4.0; 2973 -3.4; 3270 -2.7; 3597 -1.7; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -4.1; 7010 -6.7; 7711 -6.6; 8482 -7.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -9.1; 15026 -10.6; 16529 -7.4; 18182 -6.5; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Mix GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Mix ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 98 Hz    | 0.62 | -3.6 dB |
| Peaking | 241 Hz   | 1.88 | -2.6 dB |
| Peaking | 1696 Hz  | 2.59 | -3.5 dB |
| Peaking | 4386 Hz  | 1.39 | 6.8 dB  |
| Peaking | 14802 Hz | 2.33 | -4.5 dB |
| Peaking | 34 Hz    | 2.72 | -0.8 dB |
| Peaking | 329 Hz   | 3.93 | -1.0 dB |
| Peaking | 583 Hz   | 2.96 | 2.8 dB  |
| Peaking | 5914 Hz  | 4.63 | 5.1 dB  |
| Peaking | 6674 Hz  | 2.33 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Mix/HyperX%20Cloud%20Mix.png)