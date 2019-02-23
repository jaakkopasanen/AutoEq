# Cyberdrive Forte Impact Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.5; 25 -13.6; 28 -13.6; 31 -13.5; 34 -13.5; 37 -13.5; 41 -13.5; 45 -13.5; 49 -13.4; 54 -13.4; 60 -13.4; 66 -13.4; 72 -13.5; 79 -13.5; 87 -13.6; 96 -13.5; 106 -13.4; 116 -13.2; 128 -13.0; 141 -12.8; 155 -12.6; 170 -12.2; 187 -11.8; 206 -11.4; 227 -10.9; 249 -10.4; 274 -9.9; 302 -9.4; 332 -8.9; 365 -8.3; 402 -7.8; 442 -7.1; 486 -6.7; 535 -6.1; 588 -5.4; 647 -5.0; 712 -4.6; 783 -4.0; 861 -3.8; 947 -3.9; 1042 -3.4; 1146 -3.1; 1261 -3.3; 1387 -3.4; 1526 -3.5; 1678 -3.3; 1846 -2.6; 2031 -1.8; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -2.3; 4353 -5.5; 4788 -7.2; 5267 -7.7; 5793 -10.5; 6373 -14.8; 7010 -11.6; 7711 -7.6; 8482 -6.5; 9330 -6.6; 10263 -8.1; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cyberdrive Forte Impact Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cyberdrive Forte Impact Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 54 Hz    | 0.13 | -7.3 dB |
| Peaking | 795 Hz   | 0.47 | 3.8 dB  |
| Peaking | 2956 Hz  | 1.31 | 6.0 dB  |
| Peaking | 6311 Hz  | 3.54 | -9.4 dB |
| Peaking | 22013 Hz | 2.02 | 0.3 dB  |
| Peaking | 3067 Hz  | 3.66 | -2.1 dB |
| Peaking | 3755 Hz  | 1.93 | 2.7 dB  |
| Peaking | 4474 Hz  | 4.44 | -3.2 dB |
| Peaking | 8230 Hz  | 7.15 | 1.2 dB  |
| Peaking | 10290 Hz | 8.58 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cyberdrive%20Forte%20Impact%20Bass/Cyberdrive%20Forte%20Impact%20Bass.png)