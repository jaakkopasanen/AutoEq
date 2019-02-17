# V-Moda Crossfade LP2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.6; 25 -7.9; 28 -8.2; 31 -8.4; 34 -8.6; 37 -8.8; 41 -8.9; 45 -9.1; 49 -9.2; 54 -9.3; 60 -9.3; 66 -9.3; 72 -9.3; 79 -9.8; 87 -10.3; 96 -11.0; 106 -11.5; 116 -11.8; 128 -12.1; 141 -12.2; 155 -12.1; 170 -11.8; 187 -11.7; 206 -11.1; 227 -10.1; 249 -9.3; 274 -8.0; 302 -6.7; 332 -5.4; 365 -3.9; 402 -2.8; 442 -1.9; 486 -1.7; 535 -1.8; 588 -2.1; 647 -3.2; 712 -4.8; 783 -5.5; 861 -6.2; 947 -6.5; 1042 -6.5; 1146 -6.5; 1261 -6.3; 1387 -6.9; 1526 -6.5; 1678 -5.6; 1846 -4.0; 2031 -1.0; 2234 -1.6; 2457 -1.5; 2703 -1.7; 2973 -5.0; 3270 -8.3; 3597 -6.2; 3957 -2.7; 4353 -1.1; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade LP2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade LP2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.98 | -1.6 dB |
| Peaking | 152 Hz  | 0.71 | -6.1 dB |
| Peaking | 462 Hz  | 1.53 | 6.6 dB  |
| Peaking | 2260 Hz | 3.36 | 5.5 dB  |
| Peaking | 5310 Hz | 2.23 | 6.9 dB  |
| Peaking | 1227 Hz | 1.95 | -0.9 dB |
| Peaking | 2783 Hz | 5.71 | 3.8 dB  |
| Peaking | 3257 Hz | 4.22 | -5.0 dB |
| Peaking | 4137 Hz | 4.57 | 2.5 dB  |
| Peaking | 8342 Hz | 4.45 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 6.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20LP2/V-Moda%20Crossfade%20LP2.png)