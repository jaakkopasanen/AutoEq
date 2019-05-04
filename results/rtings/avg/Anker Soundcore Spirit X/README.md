# Anker Soundcore Spirit X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.5; 25 -11.5; 28 -11.4; 31 -11.3; 34 -11.2; 37 -11.1; 41 -11.0; 45 -10.8; 49 -10.6; 54 -10.4; 60 -10.1; 66 -9.9; 72 -9.7; 79 -9.4; 87 -9.0; 96 -8.7; 106 -8.2; 116 -7.8; 128 -7.2; 141 -6.5; 155 -6.0; 170 -5.3; 187 -4.3; 206 -3.1; 227 -1.8; 249 -0.9; 274 -0.5; 302 -0.7; 332 -1.3; 365 -1.8; 402 -2.3; 442 -2.5; 486 -2.5; 535 -2.2; 588 -1.9; 647 -1.4; 712 -0.9; 783 -0.6; 861 -0.8; 947 -1.3; 1042 -2.2; 1146 -3.1; 1261 -3.7; 1387 -4.1; 1526 -4.3; 1678 -4.5; 1846 -4.7; 2031 -4.7; 2234 -4.4; 2457 -3.6; 2703 -3.3; 2973 -3.5; 3270 -4.2; 3597 -4.8; 3957 -5.5; 4353 -6.2; 4788 -7.2; 5267 -8.0; 5793 -7.8; 6373 -5.0; 7010 -2.4; 7711 -3.4; 8482 -3.7; 9330 -4.3; 10263 -3.7; 11289 -3.7; 12418 -3.7; 13660 -3.7; 15026 -3.7; 16529 -3.7; 18182 -3.7; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker Soundcore Spirit X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker Soundcore Spirit X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.37 | -5.2 dB |
| Peaking | 67 Hz   | 0.28 | -4.9 dB |
| Peaking | 267 Hz  | 1.26 | 5.5 dB  |
| Peaking | 776 Hz  | 2.22 | 3.4 dB  |
| Peaking | 5160 Hz | 2.91 | -4.6 dB |
| Peaking | 974 Hz  | 4.37 | 0.9 dB  |
| Peaking | 2065 Hz | 1.05 | -1.4 dB |
| Peaking | 2705 Hz | 3.19 | 1.8 dB  |
| Peaking | 6467 Hz | 3.96 | -1.1 dB |
| Peaking | 7146 Hz | 5.67 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20Soundcore%20Spirit%20X/Anker%20Soundcore%20Spirit%20X.png)