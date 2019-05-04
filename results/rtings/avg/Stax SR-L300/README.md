# Stax SR-L300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.5; 60 -3.0; 66 -4.3; 72 -5.5; 79 -6.7; 87 -7.4; 96 -7.6; 106 -7.5; 116 -7.2; 128 -7.1; 141 -6.8; 155 -6.7; 170 -6.6; 187 -6.3; 206 -6.1; 227 -5.9; 249 -5.7; 274 -5.6; 302 -5.8; 332 -5.9; 365 -5.9; 402 -6.0; 442 -6.1; 486 -6.3; 535 -6.5; 588 -6.2; 647 -6.2; 712 -6.2; 783 -6.3; 861 -6.4; 947 -6.6; 1042 -6.5; 1146 -6.9; 1261 -7.5; 1387 -8.0; 1526 -7.6; 1678 -6.3; 1846 -5.6; 2031 -5.8; 2234 -6.2; 2457 -6.6; 2703 -5.6; 2973 -5.2; 3270 -4.1; 3597 -3.7; 3957 -4.1; 4353 -5.1; 4788 -6.5; 5267 -7.5; 5793 -9.0; 6373 -9.2; 7010 -8.2; 7711 -8.0; 8482 -9.0; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -9.4; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 1.05 | 7.2 dB  |
| Peaking | 1386 Hz | 5.76 | -1.8 dB |
| Peaking | 3677 Hz | 2.24 | 3.2 dB  |
| Peaking | 6062 Hz | 2.84 | -3.2 dB |
| Peaking | 8619 Hz | 5.3  | -2.4 dB |
| Peaking | 33 Hz   | 1.64 | -6.6 dB |
| Peaking | 40 Hz   | 0.53 | 6.1 dB  |
| Peaking | 89 Hz   | 1.09 | -4.7 dB |
| Peaking | 284 Hz  | 1.59 | 0.8 dB  |
| Peaking | 702 Hz  | 3.48 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Stax%20SR-L300/Stax%20SR-L300.png)