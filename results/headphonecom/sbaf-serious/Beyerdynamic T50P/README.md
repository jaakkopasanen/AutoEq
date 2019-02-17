# Beyerdynamic T50p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.6; 37 -2.3; 41 -3.0; 45 -3.6; 49 -4.2; 54 -5.1; 60 -5.8; 66 -4.8; 72 -4.9; 79 -6.1; 87 -6.8; 96 -6.8; 106 -6.8; 116 -6.7; 128 -6.2; 141 -5.5; 155 -3.4; 170 -2.7; 187 -5.1; 206 -7.4; 227 -8.0; 249 -8.8; 274 -10.5; 302 -12.1; 332 -11.8; 365 -11.4; 402 -10.9; 442 -10.8; 486 -10.3; 535 -9.9; 588 -9.5; 647 -9.0; 712 -7.4; 783 -7.2; 861 -7.0; 947 -6.8; 1042 -6.4; 1146 -6.0; 1261 -5.7; 1387 -5.9; 1526 -6.1; 1678 -6.4; 1846 -6.3; 2031 -5.6; 2234 -4.4; 2457 -2.9; 2703 -1.9; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.4; 6373 -4.1; 7010 -4.3; 7711 -10.2; 8482 -13.4; 9330 -12.5; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -9.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 25 Hz    |  0.99 | 6.4 dB   |
| Peaking | 168 Hz   |  3.98 | 5.7 dB   |
| Peaking | 355 Hz   |  0.95 | -5.4 dB  |
| Peaking | 4320 Hz  |  0.85 | 7.1 dB   |
| Peaking | 8617 Hz  |  3.18 | -10.1 dB |
| Peaking | 93 Hz    |  4.96 | -0.8 dB  |
| Peaking | 240 Hz   | 10.87 | 1.1 dB   |
| Peaking | 1882 Hz  |  4.09 | -1.7 dB  |
| Peaking | 2819 Hz  |  3.86 | 1.2 dB   |
| Peaking | 18369 Hz |  2.31 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | 1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T50p/Beyerdynamic%20T50p.png)