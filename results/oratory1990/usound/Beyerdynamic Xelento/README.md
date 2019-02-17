# Beyerdynamic Xelento
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -13.5; 25 -13.4; 28 -13.3; 31 -13.2; 34 -13.1; 37 -13.0; 41 -12.9; 45 -12.7; 49 -12.6; 54 -12.5; 60 -12.3; 66 -12.2; 72 -12.1; 79 -12.0; 87 -11.9; 96 -11.9; 106 -11.8; 116 -11.8; 128 -11.6; 141 -11.3; 155 -11.1; 170 -11.5; 187 -11.7; 206 -11.1; 227 -10.5; 249 -10.0; 274 -9.5; 302 -9.0; 332 -8.6; 365 -8.5; 402 -8.1; 442 -7.7; 486 -7.3; 535 -7.0; 588 -6.8; 647 -6.5; 712 -6.1; 783 -5.8; 861 -5.7; 947 -5.8; 1042 -6.0; 1146 -6.3; 1261 -6.9; 1387 -7.2; 1526 -7.0; 1678 -6.5; 1846 -5.9; 2031 -5.5; 2234 -5.3; 2457 -5.2; 2703 -4.8; 2973 -4.5; 3270 -4.1; 3597 -3.8; 3957 -4.2; 4353 -5.1; 4788 -7.6; 5267 -9.7; 5793 -4.6; 6373 -0.5; 7010 -3.4; 7711 -7.0; 8482 -9.2; 9330 -9.0; 10263 -7.7; 11289 -7.2; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Xelento GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Xelento ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.28 | -6.0 dB |
| Peaking | 201 Hz  | 0.9  | -2.8 dB |
| Peaking | 6472 Hz | 6.84 | 6.9 dB  |
| Peaking | 8933 Hz | 2.65 | -3.7 dB |
| Peaking | 17 Hz   | 0.9  | -2.7 dB |
| Peaking | 854 Hz  | 3.11 | 0.8 dB  |
| Peaking | 1428 Hz | 2.71 | -1.5 dB |
| Peaking | 3858 Hz | 1.07 | 2.4 dB  |
| Peaking | 5139 Hz | 5.65 | -6.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Beyerdynamic%20Xelento/Beyerdynamic%20Xelento.png)