# Westone W2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.9; 25 -4.9; 28 -5.0; 31 -5.0; 34 -5.1; 37 -5.2; 41 -5.5; 45 -5.6; 49 -5.8; 54 -6.0; 60 -6.3; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.7; 96 -8.0; 106 -8.3; 116 -8.5; 128 -8.6; 141 -8.9; 155 -9.1; 170 -9.3; 187 -9.4; 206 -9.5; 227 -9.4; 249 -9.3; 274 -9.3; 302 -9.0; 332 -8.9; 365 -8.5; 402 -8.3; 442 -8.0; 486 -7.6; 535 -7.2; 588 -6.8; 647 -6.4; 712 -6.0; 783 -5.8; 861 -5.9; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.8; 1526 -8.5; 1678 -8.9; 1846 -8.9; 2031 -8.8; 2234 -7.9; 2457 -6.1; 2703 -3.4; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.36 | 1.9 dB  |
| Peaking | 196 Hz  | 0.45 | -3.2 dB |
| Peaking | 748 Hz  | 1.61 | 1.6 dB  |
| Peaking | 1966 Hz | 1.48 | -5.9 dB |
| Peaking | 3699 Hz | 0.88 | 8.0 dB  |
| Peaking | 2401 Hz | 6.65 | -0.8 dB |
| Peaking | 2940 Hz | 5.71 | 1.8 dB  |
| Peaking | 3829 Hz | 3.28 | -1.0 dB |
| Peaking | 6284 Hz | 2.68 | 5.2 dB  |
| Peaking | 7352 Hz | 1.47 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20W2/Westone%20W2.png)