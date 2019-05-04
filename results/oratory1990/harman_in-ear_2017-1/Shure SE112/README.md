# Shure SE112
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.4; 25 -9.5; 28 -9.6; 31 -9.7; 34 -9.8; 37 -9.9; 41 -10.0; 45 -10.1; 49 -10.3; 54 -10.5; 60 -10.7; 66 -11.0; 72 -11.2; 79 -11.5; 87 -11.8; 96 -12.2; 106 -12.5; 116 -12.7; 128 -12.9; 141 -13.0; 155 -13.0; 170 -13.0; 187 -12.9; 206 -12.7; 227 -12.4; 249 -12.1; 274 -11.8; 302 -11.3; 332 -10.8; 365 -10.2; 402 -9.8; 442 -9.3; 486 -8.7; 535 -8.2; 588 -7.6; 647 -7.1; 712 -6.6; 783 -6.2; 861 -6.0; 947 -6.1; 1042 -6.2; 1146 -6.5; 1261 -6.7; 1387 -6.7; 1526 -6.6; 1678 -6.6; 1846 -6.5; 2031 -6.3; 2234 -5.6; 2457 -4.2; 2703 -2.5; 2973 -1.2; 3270 -0.8; 3597 -1.6; 3957 -4.0; 4353 -8.5; 4788 -8.4; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.7; 15026 -10.6; 16529 -7.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE112 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE112 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.28 | -2.9 dB |
| Peaking | 147 Hz   | 0.75 | -4.5 dB |
| Peaking | 290 Hz   | 1.24 | -2.6 dB |
| Peaking | 3119 Hz  | 3.37 | 6.2 dB  |
| Peaking | 6018 Hz  | 4.85 | 6.7 dB  |
| Peaking | 843 Hz   | 3.56 | 1.1 dB  |
| Peaking | 3772 Hz  | 5.85 | 2.7 dB  |
| Peaking | 4591 Hz  | 4.86 | -5.6 dB |
| Peaking | 5352 Hz  | 8.36 | 4.0 dB  |
| Peaking | 14824 Hz | 3.45 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Shure%20SE112/Shure%20SE112.png)