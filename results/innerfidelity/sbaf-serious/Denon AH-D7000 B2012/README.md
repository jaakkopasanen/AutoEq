# Denon AH-D7000 B2012
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.7; 25 -2.4; 28 -3.2; 31 -3.7; 34 -4.0; 37 -4.1; 41 -4.2; 45 -4.2; 49 -4.1; 54 -4.1; 60 -4.0; 66 -3.8; 72 -4.0; 79 -4.3; 87 -4.7; 96 -5.0; 106 -5.1; 116 -5.3; 128 -5.4; 141 -5.6; 155 -5.6; 170 -5.4; 187 -5.5; 206 -5.4; 227 -5.2; 249 -5.1; 274 -4.8; 302 -4.6; 332 -4.3; 365 -4.1; 402 -3.7; 442 -3.3; 486 -3.1; 535 -2.8; 588 -2.4; 647 -2.4; 712 -2.8; 783 -3.1; 861 -3.3; 947 -2.2; 1042 -2.7; 1146 -2.5; 1261 -2.2; 1387 -2.5; 1526 -3.0; 1678 -3.2; 1846 -3.3; 2031 -3.2; 2234 -2.2; 2457 -0.5; 2703 -1.4; 2973 -1.5; 3270 -1.8; 3597 -2.8; 3957 -2.6; 4353 -2.6; 4788 -2.5; 5267 -0.9; 5793 -1.7; 6373 -2.6; 7010 -3.0; 7711 -3.0; 8482 -3.3; 9330 -4.0; 10263 -3.7; 11289 -3.3; 12418 -3.3; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7000 B2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.38 | 3.9 dB  |
| Peaking | 32 Hz   | 1.03 | -1.4 dB |
| Peaking | 159 Hz  | 0.93 | -2.5 dB |
| Peaking | 2641 Hz | 2.58 | 2.4 dB  |
| Peaking | 5339 Hz | 4.69 | 2.3 dB  |
| Peaking | 283 Hz  | 2.52 | -0.5 dB |
| Peaking | 590 Hz  | 2.99 | 1.1 dB  |
| Peaking | 1232 Hz | 1.9  | 1.0 dB  |
| Peaking | 1835 Hz | 3.3  | -0.9 dB |
| Peaking | 9673 Hz | 8.99 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7000%20B2012/Denon%20AH-D7000%20B2012.png)