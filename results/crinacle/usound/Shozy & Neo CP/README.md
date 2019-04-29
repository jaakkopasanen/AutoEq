# Shozy & Neo CP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.3; 25 -4.7; 28 -5.1; 31 -5.4; 34 -5.6; 37 -5.8; 41 -6.1; 45 -6.4; 49 -6.6; 54 -6.9; 60 -7.2; 66 -7.5; 72 -7.8; 79 -8.1; 87 -8.6; 96 -8.9; 106 -9.4; 116 -9.7; 128 -10.0; 141 -10.3; 155 -10.4; 170 -10.5; 187 -10.7; 206 -10.7; 227 -10.7; 249 -10.5; 274 -10.4; 302 -10.3; 332 -10.1; 365 -9.8; 402 -9.6; 442 -9.3; 486 -8.9; 535 -8.5; 588 -8.1; 647 -7.6; 712 -7.1; 783 -6.5; 861 -6.0; 947 -5.8; 1042 -5.9; 1146 -6.5; 1261 -7.1; 1387 -7.4; 1526 -7.2; 1678 -6.6; 1846 -5.9; 2031 -5.2; 2234 -4.4; 2457 -3.5; 2703 -2.7; 2973 -2.2; 3270 -1.8; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.8; 5793 -4.2; 6373 -3.1; 7010 -5.2; 7711 -8.2; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy & Neo CP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy & Neo CP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 14 Hz   |  0.63 | 3.4 dB  |
| Peaking | 202 Hz  |  0.53 | -4.4 dB |
| Peaking | 1522 Hz |  3.83 | -1.7 dB |
| Peaking | 4067 Hz |  0.96 | 6.2 dB  |
| Peaking | 7836 Hz |  4.39 | -3.6 dB |
| Peaking | 448 Hz  |  2.33 | -0.5 dB |
| Peaking | 896 Hz  |  3.51 | 1.3 dB  |
| Peaking | 6630 Hz | 10.79 | 2.1 dB  |
| Peaking | 8371 Hz |  1.43 | -1.4 dB |
| Peaking | 8416 Hz |  4.2  | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shozy%20&%20Neo%20CP/Shozy%20&%20Neo%20CP.png)