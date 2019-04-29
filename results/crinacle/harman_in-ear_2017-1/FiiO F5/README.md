# FiiO F5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.2; 25 -6.3; 28 -6.5; 31 -6.6; 34 -6.7; 37 -6.8; 41 -7.0; 45 -7.1; 49 -7.2; 54 -7.4; 60 -7.6; 66 -7.8; 72 -8.1; 79 -8.4; 87 -8.7; 96 -9.1; 106 -9.5; 116 -9.7; 128 -9.9; 141 -10.0; 155 -10.2; 170 -10.1; 187 -10.0; 206 -9.8; 227 -9.6; 249 -9.5; 274 -9.3; 302 -8.8; 332 -8.4; 365 -7.9; 402 -7.5; 442 -7.0; 486 -6.5; 535 -6.0; 588 -5.6; 647 -5.0; 712 -4.3; 783 -3.9; 861 -3.5; 947 -3.4; 1042 -3.6; 1146 -4.1; 1261 -4.6; 1387 -4.8; 1526 -4.8; 1678 -4.8; 1846 -5.0; 2031 -5.2; 2234 -5.4; 2457 -5.1; 2703 -3.8; 2973 -2.1; 3270 -0.8; 3597 -0.5; 3957 -1.0; 4353 -2.6; 4788 -5.3; 5267 -7.5; 5793 -5.5; 6373 -2.5; 7010 -3.2; 7711 -5.4; 8482 -5.6; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -6.8; 15026 -9.2; 16529 -11.0; 18182 -14.7; 20000 -17.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.22 | -0.4 dB |
| Peaking | 172 Hz  | 0.51 | -4.3 dB |
| Peaking | 866 Hz  | 1.34 | 2.9 dB  |
| Peaking | 3523 Hz | 3.07 | 5.8 dB  |
| Peaking | 6658 Hz | 8.62 | 3.7 dB  |
| Peaking | 4251 Hz | 6.41 | 1.5 dB  |
| Peaking | 5239 Hz | 7.19 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -6.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FiiO%20F5/FiiO%20F5.png)