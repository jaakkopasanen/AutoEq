# Elysian Eros
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.8; 25 -6.2; 28 -6.8; 31 -7.2; 34 -7.5; 37 -7.8; 41 -8.1; 45 -8.5; 49 -8.8; 54 -9.1; 60 -9.3; 66 -9.7; 72 -10.1; 79 -10.4; 87 -10.8; 96 -11.2; 106 -11.6; 116 -11.9; 128 -12.2; 141 -12.4; 155 -12.4; 170 -12.6; 187 -12.6; 206 -12.7; 227 -12.5; 249 -12.3; 274 -12.1; 302 -11.9; 332 -11.5; 365 -11.2; 402 -10.7; 442 -10.3; 486 -9.9; 535 -9.4; 588 -8.8; 647 -8.2; 712 -7.5; 783 -6.8; 861 -6.2; 947 -5.8; 1042 -5.8; 1146 -6.2; 1261 -6.6; 1387 -6.6; 1526 -6.2; 1678 -5.4; 1846 -4.5; 2031 -3.9; 2234 -3.4; 2457 -2.8; 2703 -2.0; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -5.3; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Elysian Eros GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Elysian Eros ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 2.24 | 2.0 dB  |
| Peaking | 145 Hz  | 0.51 | -5.5 dB |
| Peaking | 338 Hz  | 1.05 | -2.4 dB |
| Peaking | 3412 Hz | 1.16 | 6.1 dB  |
| Peaking | 5608 Hz | 3.26 | 4.3 dB  |
| Peaking | 591 Hz  | 1.71 | -1.1 dB |
| Peaking | 1054 Hz | 0.97 | 2.1 dB  |
| Peaking | 1355 Hz | 2.33 | -2.3 dB |
| Peaking | 6504 Hz | 6.91 | 3.1 dB  |
| Peaking | 7257 Hz | 2.53 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Elysian%20Eros/Elysian%20Eros.png)