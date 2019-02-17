# Anker Soundcore Spirit X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.7; 25 -6.7; 28 -6.6; 31 -6.5; 34 -6.4; 37 -6.3; 41 -6.1; 45 -6.0; 49 -5.8; 54 -5.7; 60 -5.7; 66 -5.7; 72 -5.7; 79 -5.6; 87 -5.6; 96 -5.5; 106 -5.6; 116 -5.6; 128 -5.5; 141 -5.3; 155 -5.1; 170 -4.8; 187 -4.0; 206 -3.1; 227 -1.9; 249 -1.0; 274 -0.6; 302 -0.8; 332 -1.3; 365 -1.9; 402 -2.3; 442 -2.5; 486 -2.5; 535 -2.2; 588 -1.8; 647 -1.3; 712 -0.8; 783 -0.5; 861 -0.7; 947 -1.2; 1042 -2.0; 1146 -2.9; 1261 -3.5; 1387 -3.9; 1526 -4.1; 1678 -4.3; 1846 -4.4; 2031 -4.3; 2234 -3.6; 2457 -2.8; 2703 -2.8; 2973 -3.5; 3270 -4.4; 3597 -5.1; 3957 -5.9; 4353 -6.6; 4788 -6.9; 5267 -7.6; 5793 -8.0; 6373 -6.1; 7010 -2.4; 7711 -1.4; 8482 -3.7; 9330 -6.0; 10263 -2.5; 11289 -1.7; 12418 -1.7; 13660 -1.7; 15026 -1.7; 16529 -1.7; 18182 -1.7; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker Soundcore Spirit X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker Soundcore Spirit X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.38 | -5.0 dB |
| Peaking | 124 Hz   | 1.58 | -2.8 dB |
| Peaking | 1681 Hz  | 2.19 | -2.6 dB |
| Peaking | 5046 Hz  | 1.46 | -6.0 dB |
| Peaking | 22050 Hz | 2.14 | -1.2 dB |
| Peaking | 280 Hz   | 2.39 | 2.9 dB  |
| Peaking | 454 Hz   | 0.43 | -1.3 dB |
| Peaking | 781 Hz   | 2.18 | 2.5 dB  |
| Peaking | 7448 Hz  | 6.66 | 3.3 dB  |
| Peaking | 9190 Hz  | 6.93 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -4.4 dB |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20Soundcore%20Spirit%20X/Anker%20Soundcore%20Spirit%20X.png)