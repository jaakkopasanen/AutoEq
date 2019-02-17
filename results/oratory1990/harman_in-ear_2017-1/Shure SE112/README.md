# Shure SE112
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.7; 25 -9.8; 28 -9.9; 31 -10.0; 34 -10.1; 37 -10.2; 41 -10.3; 45 -10.4; 49 -10.6; 54 -10.7; 60 -11.0; 66 -11.2; 72 -11.5; 79 -11.8; 87 -12.1; 96 -12.4; 106 -12.7; 116 -13.0; 128 -13.2; 141 -13.3; 155 -13.3; 170 -13.3; 187 -13.2; 206 -13.0; 227 -12.7; 249 -12.4; 274 -12.1; 302 -11.6; 332 -11.1; 365 -10.5; 402 -10.0; 442 -9.6; 486 -9.0; 535 -8.5; 588 -7.9; 647 -7.4; 712 -6.9; 783 -6.5; 861 -6.3; 947 -6.4; 1042 -6.4; 1146 -6.8; 1261 -7.0; 1387 -7.0; 1526 -6.9; 1678 -6.8; 1846 -6.8; 2031 -6.6; 2234 -5.9; 2457 -4.5; 2703 -2.8; 2973 -1.5; 3270 -1.1; 3597 -1.9; 3957 -4.3; 4353 -8.8; 4788 -8.8; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.9; 15026 -10.9; 16529 -7.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE112 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE112 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.24 | -3.1 dB |
| Peaking | 149 Hz   | 0.69 | -4.6 dB |
| Peaking | 297 Hz   | 1.12 | -2.5 dB |
| Peaking | 3127 Hz  | 3.64 | 6.0 dB  |
| Peaking | 6026 Hz  | 4.99 | 6.8 dB  |
| Peaking | 830 Hz   | 4.36 | 1.0 dB  |
| Peaking | 3741 Hz  | 5.78 | 2.6 dB  |
| Peaking | 4557 Hz  | 5.07 | -6.0 dB |
| Peaking | 5291 Hz  | 8.04 | 4.0 dB  |
| Peaking | 14933 Hz | 3.34 | -5.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE112/Shure%20SE112.png)