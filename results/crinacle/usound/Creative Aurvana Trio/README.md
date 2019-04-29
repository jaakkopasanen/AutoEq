# Creative Aurvana Trio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.1; 28 -7.3; 31 -7.6; 34 -7.8; 37 -7.9; 41 -8.1; 45 -8.3; 49 -8.4; 54 -8.6; 60 -8.8; 66 -9.1; 72 -9.3; 79 -9.6; 87 -9.9; 96 -10.3; 106 -10.5; 116 -10.7; 128 -11.0; 141 -11.1; 155 -11.0; 170 -11.0; 187 -10.9; 206 -10.7; 227 -10.4; 249 -10.1; 274 -9.7; 302 -9.3; 332 -8.8; 365 -8.3; 402 -7.8; 442 -7.3; 486 -6.7; 535 -6.1; 588 -5.6; 647 -4.9; 712 -4.2; 783 -3.5; 861 -2.8; 947 -2.4; 1042 -2.3; 1146 -2.7; 1261 -3.1; 1387 -3.4; 1526 -3.3; 1678 -3.1; 1846 -3.2; 2031 -3.9; 2234 -4.4; 2457 -4.4; 2703 -4.2; 2973 -3.6; 3270 -1.4; 3597 -0.7; 3957 -2.7; 4353 -5.5; 4788 -5.4; 5267 -2.4; 5793 -0.6; 6373 -0.5; 7010 -3.6; 7711 -9.0; 8482 -10.3; 9330 -7.7; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Trio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Trio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 161 Hz  | 0.37 | -5.2 dB |
| Peaking | 1000 Hz | 0.71 | 4.3 dB  |
| Peaking | 3481 Hz | 4.99 | 5.0 dB  |
| Peaking | 6221 Hz | 3.35 | 6.8 dB  |
| Peaking | 8166 Hz | 3.91 | -6.2 dB |
| Peaking | 31 Hz   | 2.12 | -0.4 dB |
| Peaking | 1328 Hz | 8.23 | -0.7 dB |
| Peaking | 4611 Hz | 5.87 | -3.8 dB |
| Peaking | 4969 Hz | 2.07 | 1.9 dB  |
| Peaking | 6154 Hz | 9.13 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Creative%20Aurvana%20Trio/Creative%20Aurvana%20Trio.png)