# Echobox Finder X1 Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -11.9; 25 -11.8; 28 -11.8; 31 -11.7; 34 -11.5; 37 -11.4; 41 -11.3; 45 -11.1; 49 -11.0; 54 -10.8; 60 -10.6; 66 -10.5; 72 -10.4; 79 -10.3; 87 -10.2; 96 -10.0; 106 -9.8; 116 -9.4; 128 -9.2; 141 -8.9; 155 -8.5; 170 -8.1; 187 -7.7; 206 -7.2; 227 -6.6; 249 -6.1; 274 -5.6; 302 -5.0; 332 -4.5; 365 -3.9; 402 -3.4; 442 -2.8; 486 -2.4; 535 -1.9; 588 -1.3; 647 -0.9; 712 -0.9; 783 -0.5; 861 -0.7; 947 -1.0; 1042 -1.4; 1146 -1.7; 1261 -2.2; 1387 -2.8; 1526 -3.5; 1678 -4.1; 1846 -4.3; 2031 -4.4; 2234 -4.6; 2457 -4.6; 2703 -5.2; 2973 -5.9; 3270 -6.5; 3597 -6.7; 3957 -7.2; 4353 -9.0; 4788 -10.2; 5267 -11.0; 5793 -12.2; 6373 -12.6; 7010 -9.8; 7711 -8.4; 8482 -9.1; 9330 -10.9; 10263 -9.8; 11289 -5.8; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Echobox Finder X1 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.37 | -5.8 dB |
| Peaking | 113 Hz   | 0.57 | -2.9 dB |
| Peaking | 751 Hz   | 0.64 | 5.4 dB  |
| Peaking | 5800 Hz  | 1.81 | -6.9 dB |
| Peaking | 9579 Hz  | 5.01 | -4.8 dB |
| Peaking | 1693 Hz  | 5.98 | -0.5 dB |
| Peaking | 2502 Hz  | 7.08 | 0.5 dB  |
| Peaking | 11691 Hz | 5.41 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20Black%20Filter/Echobox%20Finder%20X1%20Black%20Filter.png)