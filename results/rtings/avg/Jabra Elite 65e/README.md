# Jabra Elite 65e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.3; 25 -8.5; 28 -8.8; 31 -8.9; 34 -9.0; 37 -9.0; 41 -9.0; 45 -9.0; 49 -8.9; 54 -8.7; 60 -8.6; 66 -8.6; 72 -8.5; 79 -8.3; 87 -8.3; 96 -8.0; 106 -7.7; 116 -7.4; 128 -7.2; 141 -6.9; 155 -6.4; 170 -6.1; 187 -5.6; 206 -5.2; 227 -5.0; 249 -4.7; 274 -4.5; 302 -4.4; 332 -4.4; 365 -4.2; 402 -4.2; 442 -3.8; 486 -3.6; 535 -3.1; 588 -2.6; 647 -2.1; 712 -1.5; 783 -1.0; 861 -0.7; 947 -0.6; 1042 -0.6; 1146 -0.5; 1261 -0.6; 1387 -1.5; 1526 -2.8; 1678 -3.7; 1846 -4.1; 2031 -3.7; 2234 -2.8; 2457 -1.6; 2703 -1.0; 2973 -1.4; 3270 -2.3; 3597 -3.6; 3957 -5.0; 4353 -5.9; 4788 -3.0; 5267 -3.3; 5793 -2.9; 6373 -5.6; 7010 -8.9; 7711 -7.7; 8482 -7.1; 9330 -10.4; 10263 -13.8; 11289 -12.4; 12418 -9.3; 13660 -8.2; 15026 -8.9; 16529 -11.6; 18182 -13.0; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.31 | -5.0 dB |
| Peaking | 1000 Hz  | 0.86 | 3.6 dB  |
| Peaking | 10389 Hz | 1.91 | -5.8 dB |
| Peaking | 10680 Hz | 3.05 | -3.0 dB |
| Peaking | 18120 Hz | 0.79 | -9.2 dB |
| Peaking | 1828 Hz  | 3.45 | -2.2 dB |
| Peaking | 2761 Hz  | 2.77 | 2.7 dB  |
| Peaking | 4200 Hz  | 6.01 | -3.3 dB |
| Peaking | 6090 Hz  | 1.72 | 3.5 dB  |
| Peaking | 6904 Hz  | 4.58 | -6.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -9.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2065e/Jabra%20Elite%2065e.png)