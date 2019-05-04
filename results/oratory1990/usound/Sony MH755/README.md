# Sony MH755
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.4; 25 -10.1; 28 -9.6; 31 -9.3; 34 -8.9; 37 -8.5; 41 -8.1; 45 -7.6; 49 -7.2; 54 -6.9; 60 -6.5; 66 -6.2; 72 -5.9; 79 -5.7; 87 -5.5; 96 -5.3; 106 -5.2; 116 -5.0; 128 -4.9; 141 -4.8; 155 -4.6; 170 -4.3; 187 -4.1; 206 -3.8; 227 -3.6; 249 -3.3; 274 -3.1; 302 -2.8; 332 -2.6; 365 -2.3; 402 -2.1; 442 -1.9; 486 -1.8; 535 -1.6; 588 -1.4; 647 -1.1; 712 -0.9; 783 -0.7; 861 -0.5; 947 -0.6; 1042 -1.0; 1146 -1.8; 1261 -2.6; 1387 -3.2; 1526 -3.3; 1678 -3.1; 1846 -2.8; 2031 -2.8; 2234 -3.0; 2457 -3.6; 2703 -4.8; 2973 -5.5; 3270 -5.5; 3597 -4.8; 3957 -3.9; 4353 -2.8; 4788 -1.9; 5267 -1.2; 5793 -0.7; 6373 -0.8; 7010 -2.3; 7711 -3.5; 8482 -2.7; 9330 -2.7; 10263 -2.7; 11289 -2.7; 12418 -2.7; 13660 -4.4; 15026 -4.8; 16529 -3.1; 18182 -3.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.64 | -7.3 dB |
| Peaking | 83 Hz    | 0.47 | -1.9 dB |
| Peaking | 748 Hz   | 1.21 | 2.3 dB  |
| Peaking | 3150 Hz  | 2.22 | -3.2 dB |
| Peaking | 5696 Hz  | 3.17 | 2.5 dB  |
| Peaking | 1349 Hz  | 1.37 | 1.4 dB  |
| Peaking | 1425 Hz  | 2.57 | -2.5 dB |
| Peaking | 14617 Hz | 3.72 | -2.7 dB |
| Peaking | 19733 Hz | 1.19 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20MH755/Sony%20MH755.png)