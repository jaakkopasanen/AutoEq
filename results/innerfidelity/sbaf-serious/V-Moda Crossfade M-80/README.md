# V-Moda Crossfade M-80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.5; 28 -5.0; 31 -5.4; 34 -5.7; 37 -6.0; 41 -6.3; 45 -6.6; 49 -6.8; 54 -7.1; 60 -7.5; 66 -7.8; 72 -8.1; 79 -8.4; 87 -8.6; 96 -9.1; 106 -9.3; 116 -9.2; 128 -9.2; 141 -9.4; 155 -9.6; 170 -9.4; 187 -9.3; 206 -9.0; 227 -10.7; 249 -10.5; 274 -9.6; 302 -8.8; 332 -7.8; 365 -6.9; 402 -6.3; 442 -5.8; 486 -5.4; 535 -4.5; 588 -3.5; 647 -3.3; 712 -3.7; 783 -4.0; 861 -4.9; 947 -5.8; 1042 -6.8; 1146 -7.7; 1261 -8.5; 1387 -8.9; 1526 -9.0; 1678 -8.7; 1846 -7.7; 2031 -6.6; 2234 -6.0; 2457 -5.7; 2703 -6.4; 2973 -7.4; 3270 -8.2; 3597 -7.2; 3957 -4.8; 4353 -4.3; 4788 -4.6; 5267 -0.5; 5793 -0.5; 6373 -3.1; 7010 -4.6; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade M-80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade M-80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.8  | 3.6 dB  |
| Peaking | 127 Hz  | 0.64 | -2.9 dB |
| Peaking | 249 Hz  | 3.4  | -2.8 dB |
| Peaking | 629 Hz  | 2.55 | 3.9 dB  |
| Peaking | 5597 Hz | 3.78 | 6.7 dB  |
| Peaking | 836 Hz  | 3.34 | 1.6 dB  |
| Peaking | 1500 Hz | 1.57 | -3.2 dB |
| Peaking | 2343 Hz | 2.04 | 2.0 dB  |
| Peaking | 3298 Hz | 3.17 | -2.6 dB |
| Peaking | 4061 Hz | 6.97 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20M-80/V-Moda%20Crossfade%20M-80.png)