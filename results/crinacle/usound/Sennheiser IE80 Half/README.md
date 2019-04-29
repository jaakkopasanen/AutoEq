# Sennheiser IE80 Half
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.8; 25 -8.2; 28 -8.6; 31 -9.0; 34 -9.2; 37 -9.5; 41 -9.7; 45 -9.9; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.7; 72 -10.9; 79 -11.1; 87 -11.3; 96 -11.6; 106 -11.7; 116 -11.8; 128 -11.8; 141 -11.8; 155 -11.7; 170 -11.4; 187 -11.2; 206 -10.8; 227 -10.4; 249 -10.0; 274 -9.5; 302 -9.0; 332 -8.5; 365 -8.1; 402 -7.6; 442 -7.2; 486 -6.8; 535 -6.4; 588 -6.0; 647 -5.6; 712 -5.2; 783 -4.7; 861 -4.3; 947 -3.9; 1042 -3.8; 1146 -4.1; 1261 -4.5; 1387 -4.5; 1526 -4.0; 1678 -3.1; 1846 -2.2; 2031 -1.3; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.9; 3270 -1.4; 3597 -2.1; 3957 -3.0; 4353 -4.5; 4788 -7.6; 5267 -10.4; 5793 -6.5; 6373 -2.0; 7010 -3.2; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.8; 15026 -7.4; 16529 -6.5; 18182 -6.8; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80 Half GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80 Half ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 66 Hz    | 0.4  | -4.2 dB |
| Peaking | 177 Hz   | 0.74 | -3.6 dB |
| Peaking | 2672 Hz  | 0.83 | 5.4 dB  |
| Peaking | 5203 Hz  | 3.94 | -7.3 dB |
| Peaking | 6443 Hz  | 6.29 | 4.8 dB  |
| Peaking | 942 Hz   | 2.17 | 1.3 dB  |
| Peaking | 1406 Hz  | 3.4  | -1.3 dB |
| Peaking | 15078 Hz | 4.57 | -1.3 dB |
| Peaking | 19977 Hz | 0.38 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sennheiser%20IE80%20Half/Sennheiser%20IE80%20Half.png)