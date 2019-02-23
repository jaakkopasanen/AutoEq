# Beyerdynamic T5p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.2; 25 -9.2; 28 -9.1; 31 -8.8; 34 -8.5; 37 -8.2; 41 -7.9; 45 -7.8; 49 -7.5; 54 -6.7; 60 -5.8; 66 -4.8; 72 -4.3; 79 -5.2; 87 -7.9; 96 -9.6; 106 -9.3; 116 -9.9; 128 -9.5; 141 -8.8; 155 -7.9; 170 -8.3; 187 -8.4; 206 -7.7; 227 -7.1; 249 -6.6; 274 -6.2; 302 -5.9; 332 -5.8; 365 -5.8; 402 -6.0; 442 -6.2; 486 -6.5; 535 -6.5; 588 -4.5; 647 -3.6; 712 -4.9; 783 -5.0; 861 -4.6; 947 -4.8; 1042 -6.4; 1146 -9.4; 1261 -8.2; 1387 -8.5; 1526 -8.9; 1678 -8.9; 1846 -8.8; 2031 -10.7; 2234 -10.9; 2457 -7.6; 2703 -5.2; 2973 -4.9; 3270 -6.1; 3597 -6.3; 3957 -6.1; 4353 -4.9; 4788 -3.1; 5267 -0.5; 5793 -2.5; 6373 -4.7; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.5; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.73 | -3.1 dB |
| Peaking | 121 Hz  | 2.25 | -3.6 dB |
| Peaking | 1500 Hz | 3.24 | -2.6 dB |
| Peaking | 2121 Hz | 5.85 | -5.0 dB |
| Peaking | 5328 Hz | 3.79 | 6.1 dB  |
| Peaking | 71 Hz   | 5.8  | 3.2 dB  |
| Peaking | 627 Hz  | 8.41 | 3.2 dB  |
| Peaking | 899 Hz  | 2.64 | 2.2 dB  |
| Peaking | 1162 Hz | 7.45 | -3.4 dB |
| Peaking | 2813 Hz | 7.81 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T5p/Beyerdynamic%20T5p.png)