# Echobox Finder X1 Red Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.6; 28 -11.5; 31 -11.4; 34 -11.3; 37 -11.2; 41 -11.0; 45 -10.9; 49 -10.7; 54 -10.6; 60 -10.4; 66 -10.3; 72 -10.2; 79 -10.1; 87 -10.0; 96 -9.9; 106 -9.6; 116 -9.3; 128 -9.0; 141 -8.7; 155 -8.4; 170 -8.0; 187 -7.5; 206 -7.1; 227 -6.5; 249 -6.0; 274 -5.4; 302 -4.9; 332 -4.3; 365 -3.8; 402 -3.3; 442 -2.7; 486 -2.3; 535 -1.9; 588 -1.2; 647 -0.9; 712 -0.8; 783 -0.5; 861 -0.7; 947 -1.0; 1042 -1.5; 1146 -1.9; 1261 -2.3; 1387 -3.0; 1526 -3.7; 1678 -4.2; 1846 -4.4; 2031 -4.4; 2234 -4.6; 2457 -4.6; 2703 -5.1; 2973 -6.0; 3270 -7.1; 3597 -7.7; 3957 -7.8; 4353 -9.0; 4788 -9.5; 5267 -9.9; 5793 -11.6; 6373 -13.3; 7010 -10.6; 7711 -7.6; 8482 -5.7; 9330 -5.9; 10263 -8.6; 11289 -8.9; 12418 -5.6; 13660 -5.5; 15026 -6.2; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Echobox Finder X1 Red Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 Red Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.36 | -5.8 dB |
| Peaking | 116 Hz   | 0.62 | -2.8 dB |
| Peaking | 738 Hz   | 0.7  | 5.2 dB  |
| Peaking | 5916 Hz  | 1.57 | -6.7 dB |
| Peaking | 21430 Hz | 1.95 | -1.4 dB |
| Peaking | 1721 Hz  | 3.33 | -0.4 dB |
| Peaking | 2584 Hz  | 2.53 | 0.8 dB  |
| Peaking | 3351 Hz  | 3.52 | -1.3 dB |
| Peaking | 8632 Hz  | 4.69 | 2.7 dB  |
| Peaking | 10789 Hz | 5.55 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20Red%20Filter/Echobox%20Finder%20X1%20Red%20Filter.png)