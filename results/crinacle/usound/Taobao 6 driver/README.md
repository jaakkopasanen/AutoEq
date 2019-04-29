# Taobao 6 driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.2; 25 -5.4; 28 -5.8; 31 -6.1; 34 -6.3; 37 -6.6; 41 -6.8; 45 -7.1; 49 -7.3; 54 -7.6; 60 -7.8; 66 -8.2; 72 -8.6; 79 -8.9; 87 -9.3; 96 -9.7; 106 -10.1; 116 -10.4; 128 -10.7; 141 -11.0; 155 -11.1; 170 -11.2; 187 -11.2; 206 -11.1; 227 -10.9; 249 -10.7; 274 -10.4; 302 -10.0; 332 -9.5; 365 -9.0; 402 -8.3; 442 -7.7; 486 -6.9; 535 -6.1; 588 -5.2; 647 -4.3; 712 -3.5; 783 -2.9; 861 -2.6; 947 -2.7; 1042 -3.2; 1146 -4.1; 1261 -4.8; 1387 -5.1; 1526 -4.8; 1678 -4.1; 1846 -3.3; 2031 -2.9; 2234 -2.8; 2457 -3.0; 2703 -3.2; 2973 -3.0; 3270 -2.4; 3597 -1.6; 3957 -1.5; 4353 -1.1; 4788 -0.5; 5267 -1.6; 5793 -4.1; 6373 -4.6; 7010 -7.5; 7711 -9.7; 8482 -6.7; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -6.5; 18182 -7.8; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Taobao 6 driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Taobao 6 driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 183 Hz   | 0.49 | -5.6 dB |
| Peaking | 791 Hz   | 1.53 | 4.1 dB  |
| Peaking | 2863 Hz  | 0.86 | 2.8 dB  |
| Peaking | 4720 Hz  | 2.38 | 4.0 dB  |
| Peaking | 7596 Hz  | 4.81 | -5.1 dB |
| Peaking | 21 Hz    | 1.66 | 1.3 dB  |
| Peaking | 1437 Hz  | 2.84 | -1.8 dB |
| Peaking | 1846 Hz  | 1    | 1.2 dB  |
| Peaking | 2730 Hz  | 3.76 | -1.2 dB |
| Peaking | 18837 Hz | 1.25 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Taobao%206%20driver/Taobao%206%20driver.png)