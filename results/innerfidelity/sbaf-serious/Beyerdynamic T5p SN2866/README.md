# Beyerdynamic T5p sn2866
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.8; 25 -5.1; 28 -5.3; 31 -5.5; 34 -5.7; 37 -5.8; 41 -5.9; 45 -5.9; 49 -5.9; 54 -5.8; 60 -5.7; 66 -5.6; 72 -5.4; 79 -5.1; 87 -5.3; 96 -6.5; 106 -8.4; 116 -9.5; 128 -10.5; 141 -10.6; 155 -9.9; 170 -8.6; 187 -9.7; 206 -9.4; 227 -8.8; 249 -8.2; 274 -7.5; 302 -7.0; 332 -6.6; 365 -6.4; 402 -6.3; 442 -6.2; 486 -6.6; 535 -6.9; 588 -5.7; 647 -2.7; 712 -5.2; 783 -5.2; 861 -6.8; 947 -7.0; 1042 -6.2; 1146 -7.7; 1261 -9.4; 1387 -8.2; 1526 -9.9; 1678 -10.4; 1846 -10.2; 2031 -9.5; 2234 -10.4; 2457 -7.8; 2703 -5.9; 2973 -5.3; 3270 -4.3; 3597 -3.1; 3957 -1.3; 4353 -4.9; 4788 -0.5; 5267 -1.5; 5793 -5.9; 6373 -6.3; 7010 -4.3; 7711 -8.4; 8482 -11.6; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T5p sn2866 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p sn2866 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 134 Hz  | 3.66 | -4.3 dB |
| Peaking | 202 Hz  | 3.13 | -2.9 dB |
| Peaking | 1896 Hz | 1.69 | -5.0 dB |
| Peaking | 4284 Hz | 1.26 | 5.1 dB  |
| Peaking | 8480 Hz | 5.1  | -6.4 dB |
| Peaking | 13 Hz   | 0.54 | 2.5 dB  |
| Peaking | 79 Hz   | 4.03 | 1.8 dB  |
| Peaking | 402 Hz  | 0.08 | -0.2 dB |
| Peaking | 651 Hz  | 5.8  | 4.0 dB  |
| Peaking | 2811 Hz | 3.51 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T5p%20sn2866/Beyerdynamic%20T5p%20sn2866.png)