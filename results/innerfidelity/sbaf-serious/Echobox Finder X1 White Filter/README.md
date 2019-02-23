# Echobox Finder X1 White Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -11.7; 25 -11.7; 28 -11.6; 31 -11.5; 34 -11.4; 37 -11.2; 41 -11.1; 45 -10.9; 49 -10.8; 54 -10.6; 60 -10.5; 66 -10.3; 72 -10.2; 79 -10.1; 87 -10.0; 96 -9.9; 106 -9.6; 116 -9.3; 128 -9.0; 141 -8.7; 155 -8.4; 170 -8.0; 187 -7.5; 206 -7.1; 227 -6.5; 249 -6.1; 274 -5.5; 302 -4.9; 332 -4.4; 365 -3.9; 402 -3.3; 442 -2.7; 486 -2.3; 535 -1.9; 588 -1.2; 647 -0.9; 712 -0.7; 783 -0.5; 861 -0.7; 947 -1.0; 1042 -1.4; 1146 -1.8; 1261 -2.3; 1387 -3.0; 1526 -3.6; 1678 -4.1; 1846 -4.3; 2031 -4.2; 2234 -4.3; 2457 -4.2; 2703 -4.3; 2973 -4.7; 3270 -5.1; 3597 -5.8; 3957 -6.6; 4353 -8.5; 4788 -9.2; 5267 -9.3; 5793 -9.4; 6373 -9.9; 7010 -8.0; 7711 -6.0; 8482 -5.1; 9330 -5.5; 10263 -7.9; 11289 -7.8; 12418 -5.1; 13660 -5.1; 15026 -5.4; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Echobox Finder X1 White Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 White Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.43 | -6.0 dB |
| Peaking | 106 Hz   | 0.5  | -3.6 dB |
| Peaking | 728 Hz   | 0.69 | 4.8 dB  |
| Peaking | 5564 Hz  | 1.69 | -5.1 dB |
| Peaking | 21162 Hz | 1.92 | -1.1 dB |
| Peaking | 1734 Hz  | 3.48 | -0.9 dB |
| Peaking | 2900 Hz  | 1.43 | 0.7 dB  |
| Peaking | 4447 Hz  | 7.43 | -1.3 dB |
| Peaking | 8518 Hz  | 4.6  | 1.7 dB  |
| Peaking | 10695 Hz | 5.2  | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20White%20Filter/Echobox%20Finder%20X1%20White%20Filter.png)