# Denon AH-C560R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.8; 25 -6.1; 28 -6.6; 31 -6.9; 34 -7.3; 37 -7.5; 41 -7.8; 45 -8.1; 49 -8.4; 54 -8.7; 60 -9.2; 66 -9.5; 72 -9.8; 79 -10.0; 87 -10.1; 96 -10.4; 106 -10.5; 116 -10.6; 128 -10.7; 141 -10.7; 155 -10.7; 170 -10.5; 187 -10.4; 206 -10.0; 227 -9.6; 249 -9.2; 274 -8.7; 302 -8.1; 332 -7.4; 365 -6.7; 402 -6.0; 442 -5.3; 486 -4.7; 535 -4.0; 588 -3.3; 647 -3.2; 712 -2.3; 783 -1.8; 861 -1.4; 947 -0.8; 1042 -0.5; 1146 -0.9; 1261 -1.3; 1387 -1.7; 1526 -2.3; 1678 -2.6; 1846 -2.6; 2031 -2.5; 2234 -2.4; 2457 -2.5; 2703 -2.8; 2973 -3.0; 3270 -2.6; 3597 -2.0; 3957 -2.7; 4353 -4.9; 4788 -6.7; 5267 -8.1; 5793 -9.3; 6373 -6.8; 7010 -4.8; 7711 -5.1; 8482 -7.9; 9330 -9.1; 10263 -3.6; 11289 -0.5; 12418 -0.5; 13660 -0.6; 15026 -3.3; 16529 -0.9; 18182 -0.5; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C560R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.41 | -4.9 dB |
| Peaking | 103 Hz   | 0.57 | -5.3 dB |
| Peaking | 240 Hz   | 0.63 | -6.0 dB |
| Peaking | 5539 Hz  | 1.7  | -7.9 dB |
| Peaking | 9084 Hz  | 4.74 | -8.1 dB |
| Peaking | 1055 Hz  | 1.47 | 2.7 dB  |
| Peaking | 1535 Hz  | 0.67 | -2.2 dB |
| Peaking | 3791 Hz  | 4.77 | 1.9 dB  |
| Peaking | 11429 Hz | 4.03 | 1.8 dB  |
| Peaking | 15144 Hz | 4.82 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)