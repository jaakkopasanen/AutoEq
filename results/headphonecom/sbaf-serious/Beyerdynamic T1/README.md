# Beyerdynamic T1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.8; 31 -2.2; 34 -2.6; 37 -2.9; 41 -3.2; 45 -3.5; 49 -3.8; 54 -4.0; 60 -4.1; 66 -3.5; 72 -4.1; 79 -5.1; 87 -5.7; 96 -6.0; 106 -6.4; 116 -6.6; 128 -6.9; 141 -7.3; 155 -7.4; 170 -7.4; 187 -7.4; 206 -7.5; 227 -7.5; 249 -7.6; 274 -7.4; 302 -7.3; 332 -7.1; 365 -6.8; 402 -6.5; 442 -6.4; 486 -6.1; 535 -5.5; 588 -5.5; 647 -5.1; 712 -4.6; 783 -4.2; 861 -4.1; 947 -4.0; 1042 -3.5; 1146 -3.1; 1261 -2.5; 1387 -2.4; 1526 -3.4; 1678 -4.9; 1846 -5.6; 2031 -5.6; 2234 -4.1; 2457 -3.4; 2703 -3.4; 2973 -4.5; 3270 -3.6; 3597 -3.2; 3957 -4.1; 4353 -4.0; 4788 -1.9; 5267 -2.3; 5793 -3.0; 6373 -0.7; 7010 -3.0; 7711 -7.4; 8482 -12.4; 9330 -12.0; 10263 -6.1; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 194 Hz  | 0.63 | -2.6 dB  |
| Peaking | 1181 Hz | 1.67 | 2.7 dB   |
| Peaking | 6994 Hz | 1.02 | 6.4 dB   |
| Peaking | 8664 Hz | 2.91 | -13.2 dB |
| Peaking | 14 Hz   | 0.44 | 5.4 dB   |
| Peaking | 66 Hz   | 4.69 | 1.4 dB   |
| Peaking | 1399 Hz | 6.31 | 1.1 dB   |
| Peaking | 1947 Hz | 3.04 | -1.9 dB  |
| Peaking | 2433 Hz | 3.99 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T1/Beyerdynamic%20T1.png)