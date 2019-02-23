# Yuin G2A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -1.8; 60 -2.7; 66 -3.5; 72 -4.1; 79 -4.3; 87 -5.1; 96 -5.8; 106 -6.3; 116 -6.7; 128 -7.1; 141 -7.5; 155 -7.7; 170 -7.7; 187 -7.6; 206 -7.4; 227 -7.5; 249 -7.2; 274 -7.4; 302 -7.1; 332 -6.8; 365 -6.7; 402 -6.3; 442 -6.2; 486 -5.9; 535 -5.7; 588 -5.5; 647 -5.3; 712 -5.3; 783 -5.2; 861 -5.3; 947 -5.4; 1042 -5.6; 1146 -5.7; 1261 -6.1; 1387 -6.9; 1526 -7.4; 1678 -8.6; 1846 -9.5; 2031 -10.2; 2234 -10.0; 2457 -8.8; 2703 -6.4; 2973 -3.4; 3270 -0.9; 3597 -0.5; 3957 -3.7; 4353 -10.0; 4788 -12.2; 5267 -9.5; 5793 -3.1; 6373 -1.0; 7010 -4.0; 7711 -6.9; 8482 -10.6; 9330 -11.7; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin G2A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin G2A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.9  | 7.0 dB   |
| Peaking | 3560 Hz | 2.94 | 13.4 dB  |
| Peaking | 4899 Hz | 1.14 | -20.3 dB |
| Peaking | 6080 Hz | 1.42 | 19.0 dB  |
| Peaking | 8858 Hz | 3.07 | -7.0 dB  |
| Peaking | 67 Hz   | 0.92 | 2.8 dB   |
| Peaking | 116 Hz  | 0.38 | -2.4 dB  |
| Peaking | 919 Hz  | 0.54 | 2.2 dB   |
| Peaking | 2083 Hz | 1.79 | -3.6 dB  |
| Peaking | 2960 Hz | 5.68 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20G2A/Yuin%20G2A.png)