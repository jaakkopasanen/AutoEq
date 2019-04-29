# Vision Ears Erlkönig 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.4; 31 -1.9; 34 -2.3; 37 -2.6; 41 -3.1; 45 -3.5; 49 -3.9; 54 -4.3; 60 -4.8; 66 -5.3; 72 -5.8; 79 -6.3; 87 -6.8; 96 -7.3; 106 -7.8; 116 -8.2; 128 -8.6; 141 -8.9; 155 -9.1; 170 -9.3; 187 -9.4; 206 -9.5; 227 -9.5; 249 -9.3; 274 -9.2; 302 -9.1; 332 -8.9; 365 -8.7; 402 -8.4; 442 -8.1; 486 -7.8; 535 -7.4; 588 -7.0; 647 -6.6; 712 -6.0; 783 -5.5; 861 -5.1; 947 -4.8; 1042 -4.9; 1146 -5.5; 1261 -6.1; 1387 -6.3; 1526 -6.1; 1678 -5.5; 1846 -5.1; 2031 -5.0; 2234 -5.3; 2457 -5.7; 2703 -5.7; 2973 -5.1; 3270 -5.0; 3597 -5.3; 3957 -5.0; 4353 -4.6; 4788 -4.3; 5267 -3.9; 5793 -3.2; 6373 -3.5; 7010 -5.5; 7711 -6.3; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears Erlkönig 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears Erlkönig 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.55 | 6.0 dB  |
| Peaking | 60 Hz   | 0.88 | 1.2 dB  |
| Peaking | 274 Hz  | 0.32 | -4.2 dB |
| Peaking | 817 Hz  | 0.51 | 3.2 dB  |
| Peaking | 5511 Hz | 2.06 | 3.0 dB  |
| Peaking | 981 Hz  | 1.92 | 2.2 dB  |
| Peaking | 1285 Hz | 0.99 | -2.2 dB |
| Peaking | 1904 Hz | 2.86 | 1.6 dB  |
| Peaking | 3176 Hz | 3.53 | 0.9 dB  |
| Peaking | 8161 Hz | 3.87 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vision%20Ears%20Erlk%C3%B6nig%203/Vision%20Ears%20Erlk%C3%B6nig%203.png)