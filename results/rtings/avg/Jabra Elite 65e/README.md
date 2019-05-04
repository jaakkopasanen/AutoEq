# Jabra Elite 65e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -13.0; 25 -13.2; 28 -13.5; 31 -13.6; 34 -13.7; 37 -13.8; 41 -13.8; 45 -13.7; 49 -13.6; 54 -13.3; 60 -12.9; 66 -12.7; 72 -12.4; 79 -11.9; 87 -11.6; 96 -11.0; 106 -10.2; 116 -9.5; 128 -8.8; 141 -8.0; 155 -7.1; 170 -6.6; 187 -5.8; 206 -5.2; 227 -4.7; 249 -4.5; 274 -4.3; 302 -4.2; 332 -4.2; 365 -4.0; 402 -3.9; 442 -3.7; 486 -3.5; 535 -3.0; 588 -2.6; 647 -2.1; 712 -1.5; 783 -0.9; 861 -0.7; 947 -0.6; 1042 -0.5; 1146 -0.5; 1261 -0.6; 1387 -1.5; 1526 -2.8; 1678 -3.8; 1846 -4.2; 2031 -4.0; 2234 -3.4; 2457 -2.3; 2703 -1.4; 2973 -1.3; 3270 -2.0; 3597 -3.1; 3957 -4.7; 4353 -5.2; 4788 -3.3; 5267 -3.5; 5793 -2.7; 6373 -4.8; 7010 -8.7; 7711 -8.2; 8482 -6.6; 9330 -8.8; 10263 -13.2; 11289 -13.0; 12418 -9.2; 13660 -7.3; 15026 -8.2; 16529 -11.2; 18182 -12.6; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.39 | -10.1 dB |
| Peaking | 942 Hz   | 0.71 | 3.5 dB   |
| Peaking | 10682 Hz | 2.34 | -9.0 dB  |
| Peaking | 17955 Hz | 1.02 | -8.6 dB  |
| Peaking | 20754 Hz | 1.69 | -7.2 dB  |
| Peaking | 15 Hz    | 2.43 | -0.7 dB  |
| Peaking | 1836 Hz  | 3.81 | -2.1 dB  |
| Peaking | 2885 Hz  | 3.8  | 2.8 dB   |
| Peaking | 5936 Hz  | 4.52 | 2.9 dB   |
| Peaking | 7018 Hz  | 5.54 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB |
| Peaking | 62 Hz    | 1.41 | -7.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | -8.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2065e/Jabra%20Elite%2065e.png)