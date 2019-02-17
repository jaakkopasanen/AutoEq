# Denon AH-C560R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.8; 25 -6.1; 28 -6.4; 31 -6.7; 34 -6.9; 37 -7.1; 41 -7.3; 45 -7.6; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.6; 72 -8.8; 79 -9.1; 87 -9.5; 96 -9.7; 106 -9.9; 116 -9.9; 128 -10.0; 141 -10.0; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.3; 227 -8.8; 249 -8.5; 274 -7.9; 302 -7.4; 332 -6.8; 365 -6.2; 402 -5.6; 442 -4.8; 486 -4.3; 535 -3.7; 588 -2.8; 647 -2.2; 712 -2.1; 783 -1.3; 861 -0.9; 947 -0.6; 1042 -0.5; 1146 -0.6; 1261 -1.0; 1387 -1.5; 1526 -2.0; 1678 -2.3; 1846 -2.3; 2031 -2.3; 2234 -2.5; 2457 -2.8; 2703 -3.7; 2973 -4.4; 3270 -4.1; 3597 -3.3; 3957 -3.6; 4353 -6.1; 4788 -8.0; 5267 -9.4; 5793 -8.6; 6373 -5.9; 7010 -4.2; 7711 -4.7; 8482 -7.2; 9330 -6.3; 10263 -0.9; 11289 -0.5; 12418 -0.5; 13660 -0.5; 15026 -0.5; 16529 -0.5; 18182 -0.5; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C560R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C560R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.28 | -6.0 dB |
| Peaking | 152 Hz   | 0.63 | -5.3 dB |
| Peaking | 317 Hz   | 1.06 | -2.8 dB |
| Peaking | 5211 Hz  | 1.42 | -8.1 dB |
| Peaking | 8818 Hz  | 6.13 | -5.8 dB |
| Peaking | 992 Hz   | 2.83 | 1.3 dB  |
| Peaking | 3014 Hz  | 1.05 | -2.0 dB |
| Peaking | 3873 Hz  | 3.61 | 3.2 dB  |
| Peaking | 10665 Hz | 6.37 | 1.4 dB  |
| Peaking | 12713 Hz | 2.02 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -8.0 dB |
| Peaking | 250 Hz   | 1.41 | -6.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.9 dB |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C560R/Denon%20AH-C560R.png)