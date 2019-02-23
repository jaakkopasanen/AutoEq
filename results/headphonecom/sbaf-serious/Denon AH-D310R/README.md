# Denon AH-D310R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.6; 25 -5.1; 28 -5.7; 31 -6.2; 34 -6.6; 37 -6.9; 41 -7.3; 45 -7.7; 49 -8.0; 54 -8.4; 60 -8.8; 66 -8.9; 72 -8.7; 79 -8.5; 87 -9.2; 96 -9.8; 106 -10.0; 116 -10.2; 128 -10.5; 141 -10.7; 155 -11.1; 170 -12.0; 187 -12.4; 206 -12.2; 227 -12.2; 249 -11.8; 274 -11.4; 302 -9.9; 332 -9.6; 365 -9.4; 402 -8.6; 442 -8.2; 486 -7.6; 535 -7.5; 588 -6.9; 647 -5.5; 712 -4.5; 783 -6.5; 861 -9.1; 947 -9.6; 1042 -9.6; 1146 -9.9; 1261 -10.2; 1387 -10.1; 1526 -3.8; 1678 -7.4; 1846 -4.4; 2031 -4.9; 2234 -6.2; 2457 -3.5; 2703 -1.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -5.3; 4788 -6.3; 5267 -2.2; 5793 -4.7; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -7.9; 9330 -11.7; 10263 -9.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D310R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D310R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 184 Hz  |  0.76 | -5.8 dB |
| Peaking | 1177 Hz |  3.07 | -4.3 dB |
| Peaking | 3228 Hz |  1.77 | 6.7 dB  |
| Peaking | 6538 Hz |  5.1  | 4.2 dB  |
| Peaking | 9410 Hz |  4.73 | -6.1 dB |
| Peaking | 19 Hz   |  1.63 | 3.0 dB  |
| Peaking | 57 Hz   |  1.97 | -1.3 dB |
| Peaking | 704 Hz  |  4.32 | 3.4 dB  |
| Peaking | 881 Hz  |  5.62 | -2.5 dB |
| Peaking | 2231 Hz | 14.18 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D310R/Denon%20AH-D310R.png)