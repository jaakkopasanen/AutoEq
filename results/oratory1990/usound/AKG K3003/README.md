# AKG K3003
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.0; 25 -10.1; 28 -10.1; 31 -10.1; 34 -10.0; 37 -10.0; 41 -10.1; 45 -10.3; 49 -10.4; 54 -10.6; 60 -10.7; 66 -11.0; 72 -11.2; 79 -11.6; 87 -11.9; 96 -12.2; 106 -12.5; 116 -12.7; 128 -12.9; 141 -13.0; 155 -13.1; 170 -13.1; 187 -13.0; 206 -12.9; 227 -12.7; 249 -12.4; 274 -12.1; 302 -11.8; 332 -11.4; 365 -11.0; 402 -10.5; 442 -10.1; 486 -9.6; 535 -9.1; 588 -8.6; 647 -8.1; 712 -7.6; 783 -7.1; 861 -6.7; 947 -6.5; 1042 -6.5; 1146 -6.6; 1261 -6.6; 1387 -6.7; 1526 -6.4; 1678 -5.9; 1846 -5.4; 2031 -5.1; 2234 -4.7; 2457 -3.9; 2703 -3.2; 2973 -4.0; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -6.3; 5267 -8.0; 5793 -9.3; 6373 -8.6; 7010 -10.1; 7711 -12.2; 8482 -10.2; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.4; 15026 -10.7; 16529 -6.9; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.13 | -3.1 dB |
| Peaking | 165 Hz   | 0.63 | -4.6 dB |
| Peaking | 352 Hz   | 1.07 | -2.0 dB |
| Peaking | 4040 Hz  | 1.25 | 13.3 dB |
| Peaking | 5407 Hz  | 0.88 | -9.7 dB |
| Peaking | 888 Hz   | 4.75 | 0.6 dB  |
| Peaking | 6661 Hz  | 5.13 | 3.9 dB  |
| Peaking | 7737 Hz  | 2.16 | -6.5 dB |
| Peaking | 9294 Hz  | 1.29 | 4.2 dB  |
| Peaking | 14783 Hz | 3.51 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/AKG%20K3003/AKG%20K3003.png)