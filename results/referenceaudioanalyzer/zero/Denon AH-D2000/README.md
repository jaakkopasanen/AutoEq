# Denon AH-D2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -5.2; 25 -5.9; 28 -6.6; 31 -7.1; 34 -7.4; 37 -7.5; 41 -7.6; 45 -7.5; 49 -7.5; 54 -7.5; 60 -7.5; 66 -7.5; 72 -7.4; 79 -7.2; 87 -7.0; 96 -6.8; 106 -6.6; 116 -6.5; 128 -6.2; 141 -5.9; 155 -5.4; 170 -4.8; 187 -4.6; 206 -4.6; 227 -4.6; 249 -4.9; 274 -4.9; 302 -5.0; 332 -5.4; 365 -5.8; 402 -6.3; 442 -6.6; 486 -6.8; 535 -7.1; 588 -7.7; 647 -8.1; 712 -8.0; 783 -7.6; 861 -7.8; 947 -8.2; 1042 -8.0; 1146 -7.5; 1261 -6.9; 1387 -6.4; 1526 -6.0; 1678 -5.8; 1846 -5.5; 2031 -4.8; 2234 -4.1; 2457 -2.9; 2703 -1.0; 2973 -0.5; 3270 -2.7; 3597 -6.0; 3957 -8.7; 4353 -9.5; 4788 -8.8; 5267 -8.4; 5793 -7.7; 6373 -6.4; 7010 -7.5; 7711 -8.5; 8482 -7.5; 9330 -6.4; 10263 -7.9; 11289 -10.6; 12418 -12.0; 13660 -10.3; 15026 -6.4; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 866 Hz   | 1.48 | -2.2 dB |
| Peaking | 2990 Hz  | 2.06 | 8.6 dB  |
| Peaking | 4051 Hz  | 1.64 | -5.9 dB |
| Peaking | 12408 Hz | 2.54 | -6.2 dB |
| Peaking | 19 Hz    | 1.74 | 3.7 dB  |
| Peaking | 38 Hz    | 0.33 | -1.8 dB |
| Peaking | 208 Hz   | 1.09 | 2.2 dB  |
| Peaking | 598 Hz   | 3.5  | -0.9 dB |
| Peaking | 7674 Hz  | 9.56 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-D2000/Denon%20AH-D2000.png)