# Denon AH-D2000 B2012
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.6; 25 -5.2; 28 -5.9; 31 -6.2; 34 -6.3; 37 -6.4; 41 -6.5; 45 -6.4; 49 -6.2; 54 -6.1; 60 -6.2; 66 -6.2; 72 -6.3; 79 -6.5; 87 -6.9; 96 -7.2; 106 -7.4; 116 -7.5; 128 -7.7; 141 -8.0; 155 -7.9; 170 -7.8; 187 -8.0; 206 -8.0; 227 -7.8; 249 -7.7; 274 -7.5; 302 -7.4; 332 -7.3; 365 -7.0; 402 -6.7; 442 -6.5; 486 -6.7; 535 -7.0; 588 -6.9; 647 -7.0; 712 -4.6; 783 -5.1; 861 -5.9; 947 -6.0; 1042 -5.6; 1146 -5.2; 1261 -4.7; 1387 -4.7; 1526 -4.9; 1678 -5.0; 1846 -4.7; 2031 -4.3; 2234 -4.2; 2457 -4.0; 2703 -3.8; 2973 -0.5; 3270 -1.5; 3597 -4.1; 3957 -4.6; 4353 -4.0; 4788 -2.6; 5267 -3.1; 5793 -3.4; 6373 -4.5; 7010 -5.4; 7711 -5.5; 8482 -5.7; 9330 -5.7; 10263 -7.2; 11289 -6.3; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 B2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 191 Hz   | 0.54 | -2.3 dB |
| Peaking | 1775 Hz  | 0.88 | 1.1 dB  |
| Peaking | 3073 Hz  | 5.64 | 5.0 dB  |
| Peaking | 5189 Hz  | 2.98 | 2.9 dB  |
| Peaking | 10505 Hz | 5.15 | -1.7 dB |
| Peaking | 14 Hz    | 0.64 | 3.2 dB  |
| Peaking | 32 Hz    | 1.4  | -1.9 dB |
| Peaking | 651 Hz   | 4.22 | -1.9 dB |
| Peaking | 727 Hz   | 5.5  | 2.8 dB  |
| Peaking | 898 Hz   | 5.22 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D2000%20B2012/Denon%20AH-D2000%20B2012.png)