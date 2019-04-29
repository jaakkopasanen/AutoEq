# Shure SE846 Black sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.3; 25 -9.4; 28 -9.4; 31 -9.5; 34 -9.5; 37 -9.5; 41 -9.6; 45 -9.6; 49 -9.6; 54 -9.6; 60 -9.6; 66 -9.7; 72 -9.8; 79 -9.9; 87 -10.1; 96 -10.2; 106 -10.3; 116 -10.3; 128 -10.3; 141 -10.3; 155 -10.3; 170 -10.1; 187 -10.0; 206 -9.9; 227 -9.7; 249 -9.5; 274 -9.4; 302 -9.3; 332 -9.2; 365 -9.1; 402 -9.1; 442 -9.0; 486 -8.9; 535 -8.7; 588 -8.4; 647 -8.1; 712 -7.6; 783 -7.1; 861 -6.7; 947 -6.4; 1042 -6.5; 1146 -7.0; 1261 -7.5; 1387 -7.5; 1526 -7.0; 1678 -6.2; 1846 -5.5; 2031 -4.8; 2234 -4.2; 2457 -3.5; 2703 -2.5; 2973 -1.7; 3270 -2.1; 3597 -3.1; 3957 -3.6; 4353 -2.9; 4788 -1.6; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.38 | -2.7 dB |
| Peaking | 115 Hz  | 0.9  | -1.5 dB |
| Peaking | 274 Hz  | 0.43 | -2.5 dB |
| Peaking | 2954 Hz | 1.93 | 4.4 dB  |
| Peaking | 5598 Hz | 2.6  | 6.2 dB  |
| Peaking | 935 Hz  | 3.78 | 1.0 dB  |
| Peaking | 1353 Hz | 4.46 | -1.3 dB |
| Peaking | 6557 Hz | 7.7  | 2.0 dB  |
| Peaking | 8057 Hz | 2.81 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shure%20SE846%20Black%20sample%202/Shure%20SE846%20Black%20sample%202.png)