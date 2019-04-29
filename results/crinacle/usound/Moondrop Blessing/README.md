# Moondrop Blessing
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.7; 25 -2.8; 28 -2.9; 31 -3.0; 34 -3.1; 37 -3.1; 41 -3.1; 45 -3.1; 49 -3.0; 54 -3.0; 60 -3.0; 66 -3.0; 72 -3.1; 79 -3.2; 87 -3.4; 96 -3.6; 106 -3.7; 116 -3.8; 128 -3.9; 141 -4.0; 155 -4.2; 170 -4.2; 187 -4.2; 206 -4.1; 227 -4.1; 249 -4.0; 274 -4.0; 302 -3.9; 332 -3.8; 365 -3.7; 402 -3.6; 442 -3.5; 486 -3.4; 535 -3.2; 588 -3.1; 647 -2.9; 712 -2.7; 783 -2.4; 861 -2.2; 947 -2.3; 1042 -2.7; 1146 -3.6; 1261 -4.4; 1387 -5.0; 1526 -5.0; 1678 -4.8; 1846 -4.7; 2031 -4.8; 2234 -5.2; 2457 -5.8; 2703 -6.2; 2973 -5.9; 3270 -5.1; 3597 -4.4; 3957 -4.2; 4353 -4.2; 4788 -3.9; 5267 -3.8; 5793 -2.7; 6373 -0.5; 7010 -2.9; 7711 -6.6; 8482 -5.6; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -6.5; 16529 -8.6; 18182 -9.2; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Moondrop Blessing GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Moondrop Blessing ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.49 | 1.2 dB  |
| Peaking | 830 Hz   | 1.99 | 2.0 dB  |
| Peaking | 2494 Hz  | 1.23 | -1.9 dB |
| Peaking | 6379 Hz  | 7.41 | 4.3 dB  |
| Peaking | 19682 Hz | 0.57 | -7.6 dB |
| Peaking | 1401 Hz  | 6.25 | -1.0 dB |
| Peaking | 7901 Hz  | 4.96 | -4.3 dB |
| Peaking | 8150 Hz  | 1.13 | 1.3 dB  |
| Peaking | 13810 Hz | 2.32 | 1.8 dB  |
| Peaking | 15986 Hz | 2.4  | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Moondrop%20Blessing/Moondrop%20Blessing.png)