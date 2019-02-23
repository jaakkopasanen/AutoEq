# Denon AH-D2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.1; 31 -1.8; 34 -2.4; 37 -2.7; 41 -2.9; 45 -3.1; 49 -3.3; 54 -3.2; 60 -3.2; 66 -3.4; 72 -3.7; 79 -3.9; 87 -4.1; 96 -4.4; 106 -4.5; 116 -4.6; 128 -4.9; 141 -5.1; 155 -5.2; 170 -5.2; 187 -5.1; 206 -5.3; 227 -5.4; 249 -5.3; 274 -5.4; 302 -5.4; 332 -5.6; 365 -5.8; 402 -6.1; 442 -6.5; 486 -7.2; 535 -7.8; 588 -8.0; 647 -8.4; 712 -8.9; 783 -7.3; 861 -8.5; 947 -8.8; 1042 -8.6; 1146 -8.3; 1261 -8.1; 1387 -8.1; 1526 -8.1; 1678 -7.9; 1846 -7.5; 2031 -6.9; 2234 -6.5; 2457 -5.9; 2703 -5.5; 2973 -3.3; 3270 -3.5; 3597 -6.0; 3957 -6.6; 4353 -6.5; 4788 -6.0; 5267 -5.5; 5793 -6.5; 6373 -7.4; 7010 -7.7; 7711 -7.8; 8482 -7.0; 9330 -6.7; 10263 -7.7; 11289 -7.6; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.14 | 5.3 dB  |
| Peaking | 62 Hz    | 0.61 | 2.4 dB  |
| Peaking | 333 Hz   | 0.81 | 2.5 dB  |
| Peaking | 673 Hz   | 0.48 | -2.9 dB |
| Peaking | 3066 Hz  | 4.55 | 4.2 dB  |
| Peaking | 663 Hz   | 6.51 | -0.3 dB |
| Peaking | 3942 Hz  | 6.28 | -0.5 dB |
| Peaking | 5291 Hz  | 4.55 | 1.4 dB  |
| Peaking | 7062 Hz  | 2.77 | -1.4 dB |
| Peaking | 10797 Hz | 5.26 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)