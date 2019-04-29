# Ocharaku Co-Donguri Shizuku
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.2; 25 -6.5; 28 -6.7; 31 -6.9; 34 -7.0; 37 -7.0; 41 -7.1; 45 -7.2; 49 -7.3; 54 -7.4; 60 -7.5; 66 -7.7; 72 -7.8; 79 -8.0; 87 -8.2; 96 -8.4; 106 -8.5; 116 -8.5; 128 -8.6; 141 -8.7; 155 -8.6; 170 -8.5; 187 -8.2; 206 -8.0; 227 -7.6; 249 -7.2; 274 -6.8; 302 -6.3; 332 -5.8; 365 -5.3; 402 -4.9; 442 -4.5; 486 -4.0; 535 -3.6; 588 -3.2; 647 -2.7; 712 -2.3; 783 -1.9; 861 -1.6; 947 -1.6; 1042 -2.0; 1146 -2.8; 1261 -3.6; 1387 -4.2; 1526 -4.6; 1678 -5.0; 1846 -5.7; 2031 -6.2; 2234 -7.7; 2457 -11.0; 2703 -13.1; 2973 -11.7; 3270 -9.5; 3597 -8.6; 3957 -9.5; 4353 -12.4; 4788 -11.9; 5267 -5.9; 5793 -1.5; 6373 -0.5; 7010 -3.4; 7711 -6.6; 8482 -6.4; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.9; 18182 -9.4; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Co-Donguri Shizuku GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Co-Donguri Shizuku ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 889 Hz   | 1.24 | 4.7 dB  |
| Peaking | 2742 Hz  | 3.54 | -7.6 dB |
| Peaking | 4546 Hz  | 3.98 | -8.0 dB |
| Peaking | 6045 Hz  | 3.94 | 7.4 dB  |
| Peaking | 18519 Hz | 1.44 | -3.9 dB |
| Peaking | 56 Hz    | 0.55 | -0.8 dB |
| Peaking | 149 Hz   | 0.69 | -2.5 dB |
| Peaking | 458 Hz   | 1.47 | 1.2 dB  |
| Peaking | 7976 Hz  | 8.32 | -2.3 dB |
| Peaking | 12289 Hz | 0.41 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | -5.0 dB |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ocharaku%20Co-Donguri%20Shizuku/Ocharaku%20Co-Donguri%20Shizuku.png)