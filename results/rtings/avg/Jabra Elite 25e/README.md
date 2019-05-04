# Jabra Elite 25e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.8; 23 -13.9; 25 -14.1; 28 -14.3; 31 -14.4; 34 -14.4; 37 -14.4; 41 -14.4; 45 -14.3; 49 -14.3; 54 -14.2; 60 -14.1; 66 -14.0; 72 -13.9; 79 -13.8; 87 -13.7; 96 -13.6; 106 -13.4; 116 -13.3; 128 -13.0; 141 -12.7; 155 -12.3; 170 -11.8; 187 -11.4; 206 -11.1; 227 -10.6; 249 -10.1; 274 -9.4; 302 -8.7; 332 -8.0; 365 -7.3; 402 -6.6; 442 -5.8; 486 -5.0; 535 -4.1; 588 -3.2; 647 -2.3; 712 -1.5; 783 -1.1; 861 -1.1; 947 -1.2; 1042 -1.9; 1146 -2.7; 1261 -3.1; 1387 -3.3; 1526 -3.4; 1678 -3.6; 1846 -3.8; 2031 -4.0; 2234 -3.9; 2457 -3.4; 2703 -3.1; 2973 -2.5; 3270 -1.5; 3597 -0.8; 3957 -1.3; 4353 -2.2; 4788 -3.1; 5267 -2.9; 5793 -1.0; 6373 -0.5; 7010 -2.6; 7711 -5.1; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -6.8; 16529 -10.3; 18182 -12.6; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 25e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 25e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.14 | -9.2 dB |
| Peaking | 772 Hz   | 0.97 | 5.3 dB  |
| Peaking | 3613 Hz  | 2.2  | 4.0 dB  |
| Peaking | 6239 Hz  | 4.6  | 4.6 dB  |
| Peaking | 364 Hz   | 4.94 | 0.2 dB  |
| Peaking | 5718 Hz  | 7.09 | 0.6 dB  |
| Peaking | 19226 Hz | 0.83 | -9.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2025e/Jabra%20Elite%2025e.png)