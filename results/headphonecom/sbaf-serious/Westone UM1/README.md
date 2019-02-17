# Westone UM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.1; 49 -1.6; 54 -2.1; 60 -2.7; 66 -3.2; 72 -3.7; 79 -4.2; 87 -4.6; 96 -5.1; 106 -5.5; 116 -5.8; 128 -6.0; 141 -6.6; 155 -6.8; 170 -7.0; 187 -7.1; 206 -7.2; 227 -7.3; 249 -7.3; 274 -7.3; 302 -7.2; 332 -7.0; 365 -6.9; 402 -6.7; 442 -6.7; 486 -6.6; 535 -6.4; 588 -5.9; 647 -5.7; 712 -5.6; 783 -5.7; 861 -5.9; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -7.8; 1526 -8.3; 1678 -8.3; 1846 -7.8; 2031 -7.0; 2234 -5.9; 2457 -4.3; 2703 -2.7; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.44 | 6.4 dB  |
| Peaking | 182 Hz  | 0.59 | -1.4 dB |
| Peaking | 712 Hz  | 1.89 | 1.2 dB  |
| Peaking | 1714 Hz | 1.59 | -3.7 dB |
| Peaking | 3958 Hz | 0.93 | 7.2 dB  |
| Peaking | 3019 Hz | 5.63 | 1.2 dB  |
| Peaking | 4085 Hz | 3.61 | -1.1 dB |
| Peaking | 6344 Hz | 2.51 | 5.1 dB  |
| Peaking | 7278 Hz | 1.49 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20UM1/Westone%20UM1.png)