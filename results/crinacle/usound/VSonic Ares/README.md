# VSonic Ares
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.2; 23 -13.2; 25 -13.1; 28 -13.0; 31 -12.9; 34 -12.8; 37 -12.6; 41 -12.5; 45 -12.3; 49 -12.2; 54 -12.0; 60 -11.8; 66 -11.7; 72 -11.6; 79 -11.5; 87 -11.5; 96 -11.4; 106 -11.4; 116 -11.2; 128 -11.0; 141 -10.9; 155 -10.7; 170 -10.4; 187 -10.1; 206 -9.8; 227 -9.4; 249 -9.1; 274 -8.7; 302 -8.4; 332 -8.1; 365 -7.8; 402 -7.7; 442 -7.4; 486 -7.2; 535 -7.0; 588 -6.8; 647 -6.5; 712 -6.1; 783 -5.7; 861 -5.2; 947 -5.0; 1042 -5.1; 1146 -5.5; 1261 -5.9; 1387 -6.1; 1526 -6.0; 1678 -5.6; 1846 -5.2; 2031 -5.2; 2234 -5.5; 2457 -5.7; 2703 -5.1; 2973 -3.6; 3270 -1.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.6; 5793 -6.6; 6373 -8.7; 7010 -8.8; 7711 -11.6; 8482 -8.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic Ares GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic Ares ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  0.36 | -6.3 dB |
| Peaking | 131 Hz  |  0.52 | -3.4 dB |
| Peaking | 923 Hz  |  2.19 | 1.7 dB  |
| Peaking | 4192 Hz |  1.58 | 7.3 dB  |
| Peaking | 7314 Hz |  2.45 | -5.7 dB |
| Peaking | 1904 Hz |  5.21 | 0.6 dB  |
| Peaking | 2564 Hz |  4.19 | -1.1 dB |
| Peaking | 3337 Hz |  7.43 | 1.2 dB  |
| Peaking | 6020 Hz | 13.49 | -2.1 dB |
| Peaking | 9201 Hz |  7.53 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/VSonic%20Ares/VSonic%20Ares.png)