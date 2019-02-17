# BGVP DMG
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.8; 25 -5.1; 28 -5.6; 31 -5.9; 34 -6.2; 37 -6.5; 41 -6.8; 45 -7.0; 49 -7.3; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.4; 79 -8.7; 87 -9.0; 96 -9.2; 106 -9.4; 116 -9.6; 128 -9.7; 141 -9.7; 155 -9.6; 170 -9.4; 187 -9.1; 206 -8.8; 227 -8.4; 249 -8.0; 274 -7.5; 302 -7.0; 332 -6.5; 365 -6.0; 402 -5.4; 442 -4.9; 486 -4.3; 535 -3.8; 588 -3.2; 647 -2.7; 712 -2.1; 783 -1.6; 861 -1.3; 947 -1.0; 1042 -0.6; 1146 -0.5; 1261 -0.5; 1387 -0.7; 1526 -1.6; 1678 -2.7; 1846 -3.0; 2031 -2.9; 2234 -2.9; 2457 -3.0; 2703 -3.5; 2973 -3.8; 3270 -1.5; 3597 -3.1; 3957 -4.9; 4353 -5.3; 4788 -5.4; 5267 -6.5; 5793 -10.0; 6373 -9.6; 7010 -7.4; 7711 -7.6; 8482 -8.5; 9330 -8.8; 10263 -9.5; 11289 -9.0; 12418 -7.3; 13660 -7.7; 15026 -8.3; 16529 -5.7; 18182 -2.8; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DMG GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DMG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 67 Hz    | 0.31 | -5.9 dB |
| Peaking | 200 Hz   | 0.58 | -4.8 dB |
| Peaking | 6084 Hz  | 1.17 | -7.0 dB |
| Peaking | 10346 Hz | 1.89 | -5.3 dB |
| Peaking | 15028 Hz | 1.09 | -6.3 dB |
| Peaking | 1126 Hz  | 1.15 | 3.3 dB  |
| Peaking | 2175 Hz  | 0.34 | -2.4 dB |
| Peaking | 3355 Hz  | 7.81 | 3.1 dB  |
| Peaking | 5707 Hz  | 1.87 | 4.5 dB  |
| Peaking | 5971 Hz  | 5.78 | -5.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -9.4 dB |
| Peaking | 16000 Hz | 1.41 | -7.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/BGVP%20DMG/BGVP%20DMG.png)