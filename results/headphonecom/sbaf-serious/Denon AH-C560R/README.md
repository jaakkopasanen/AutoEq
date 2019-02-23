# Denon AH-C560R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.7; 25 -6.1; 28 -6.5; 31 -6.9; 34 -7.2; 37 -7.5; 41 -7.8; 45 -8.1; 49 -8.4; 54 -8.6; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.1; 96 -10.4; 106 -10.4; 116 -10.5; 128 -10.6; 141 -10.6; 155 -10.6; 170 -10.5; 187 -10.3; 206 -10.0; 227 -9.6; 249 -9.2; 274 -8.7; 302 -8.1; 332 -7.4; 365 -6.7; 402 -6.0; 442 -5.3; 486 -4.6; 535 -3.9; 588 -3.2; 647 -3.2; 712 -2.3; 783 -1.7; 861 -1.4; 947 -0.8; 1042 -0.5; 1146 -0.9; 1261 -1.3; 1387 -1.7; 1526 -2.3; 1678 -2.6; 1846 -2.6; 2031 -2.5; 2234 -2.4; 2457 -2.5; 2703 -2.7; 2973 -3.0; 3270 -2.6; 3597 -2.0; 3957 -2.7; 4353 -4.9; 4788 -6.6; 5267 -8.1; 5793 -9.2; 6373 -6.8; 7010 -4.7; 7711 -5.2; 8482 -7.9; 9330 -9.0; 10263 -5.5; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C560R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 75 Hz   | 0.65 | -2.9 dB |
| Peaking | 189 Hz  | 0.61 | -4.3 dB |
| Peaking | 980 Hz  | 0.66 | 4.9 dB  |
| Peaking | 3883 Hz | 1.5  | 4.8 dB  |
| Peaking | 5170 Hz | 1.68 | -5.6 dB |
| Peaking | 1605 Hz | 5.13 | -0.5 dB |
| Peaking | 2275 Hz | 5.56 | 0.6 dB  |
| Peaking | 5930 Hz | 6.1  | -2.3 dB |
| Peaking | 7108 Hz | 2.43 | 2.6 dB  |
| Peaking | 9034 Hz | 5.22 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)