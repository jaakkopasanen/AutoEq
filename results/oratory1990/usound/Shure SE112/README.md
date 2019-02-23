# Shure SE112
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.3; 25 -8.4; 28 -8.5; 31 -8.6; 34 -8.6; 37 -8.7; 41 -8.9; 45 -9.0; 49 -9.1; 54 -9.3; 60 -9.5; 66 -9.8; 72 -10.1; 79 -10.4; 87 -10.7; 96 -11.0; 106 -11.3; 116 -11.5; 128 -11.7; 141 -11.8; 155 -11.9; 170 -11.8; 187 -11.7; 206 -11.5; 227 -11.3; 249 -11.0; 274 -10.6; 302 -10.3; 332 -9.8; 365 -9.4; 402 -8.9; 442 -8.5; 486 -8.0; 535 -7.5; 588 -7.0; 647 -6.5; 712 -5.9; 783 -5.5; 861 -5.3; 947 -5.3; 1042 -5.3; 1146 -5.7; 1261 -6.2; 1387 -6.5; 1526 -6.7; 1678 -6.7; 1846 -6.7; 2031 -6.9; 2234 -6.7; 2457 -5.9; 2703 -4.6; 2973 -3.5; 3270 -3.1; 3597 -3.6; 3957 -5.6; 4353 -9.7; 4788 -9.4; 5267 -2.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE112 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE112 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 74 Hz   | 0.4  | -2.8 dB |
| Peaking | 191 Hz  | 0.79 | -4.0 dB |
| Peaking | 3352 Hz | 2.75 | 3.9 dB  |
| Peaking | 4585 Hz | 4.67 | -7.6 dB |
| Peaking | 5764 Hz | 3.15 | 7.6 dB  |
| Peaking | 20 Hz   | 1.6  | -0.6 dB |
| Peaking | 378 Hz  | 2.14 | -0.7 dB |
| Peaking | 869 Hz  | 1.72 | 1.8 dB  |
| Peaking | 1927 Hz | 2.49 | -0.9 dB |
| Peaking | 8188 Hz | 5.01 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Shure%20SE112/Shure%20SE112.png)