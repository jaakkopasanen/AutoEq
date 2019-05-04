# AKG K391-NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.3; 25 -6.6; 28 -6.9; 31 -7.1; 34 -7.3; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.6; 54 -7.5; 60 -7.5; 66 -7.5; 72 -7.4; 79 -7.3; 87 -7.2; 96 -7.1; 106 -6.9; 116 -6.8; 128 -6.7; 141 -6.5; 155 -6.4; 170 -6.4; 187 -6.5; 206 -6.7; 227 -6.9; 249 -7.4; 274 -7.8; 302 -8.2; 332 -8.7; 365 -9.1; 402 -9.3; 442 -9.5; 486 -9.3; 535 -8.8; 588 -7.8; 647 -6.4; 712 -5.0; 783 -3.7; 861 -3.2; 947 -3.4; 1042 -3.8; 1146 -4.2; 1261 -4.5; 1387 -4.5; 1526 -4.4; 1678 -4.2; 1846 -4.1; 2031 -3.9; 2234 -3.3; 2457 -2.5; 2703 -2.2; 2973 -2.9; 3270 -4.6; 3597 -6.8; 3957 -8.7; 4353 -9.3; 4788 -7.9; 5267 -4.9; 5793 -1.9; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -8.9; 9330 -10.5; 10263 -8.8; 11289 -6.0; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K391-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K391-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 420 Hz  | 1.1  | -5.1 dB |
| Peaking | 2291 Hz | 0.21 | 3.1 dB  |
| Peaking | 4299 Hz | 2.86 | -7.0 dB |
| Peaking | 6257 Hz | 3.9  | 5.2 dB  |
| Peaking | 9210 Hz | 2.74 | -6.7 dB |
| Peaking | 54 Hz   | 0.7  | -1.7 dB |
| Peaking | 590 Hz  | 1.86 | -3.4 dB |
| Peaking | 778 Hz  | 0.92 | 5.2 dB  |
| Peaking | 1216 Hz | 0.79 | -3.3 dB |
| Peaking | 2677 Hz | 3.8  | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K391-NC/AKG%20K391-NC.png)