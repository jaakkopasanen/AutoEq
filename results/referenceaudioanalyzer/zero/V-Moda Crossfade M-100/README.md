# V-Moda Crossfade M-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.8; 41 -3.2; 45 -4.2; 49 -5.0; 54 -5.7; 60 -6.7; 66 -7.4; 72 -7.9; 79 -8.3; 87 -8.8; 96 -9.2; 106 -9.6; 116 -9.8; 128 -9.8; 141 -9.8; 155 -9.7; 170 -9.5; 187 -9.2; 206 -8.7; 227 -8.2; 249 -7.9; 274 -7.9; 302 -7.4; 332 -6.5; 365 -5.6; 402 -4.7; 442 -3.6; 486 -2.5; 535 -1.8; 588 -1.5; 647 -1.7; 712 -2.1; 783 -2.7; 861 -3.5; 947 -4.4; 1042 -5.3; 1146 -6.1; 1261 -7.0; 1387 -7.8; 1526 -8.4; 1678 -8.5; 1846 -8.4; 2031 -8.4; 2234 -8.9; 2457 -9.8; 2703 -10.5; 2973 -10.9; 3270 -11.2; 3597 -11.3; 3957 -10.5; 4353 -8.9; 4788 -7.1; 5267 -5.7; 5793 -4.7; 6373 -3.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.69 | 7.7 dB  |
| Peaking | 109 Hz  | 0.4  | -4.4 dB |
| Peaking | 601 Hz  | 1.13 | 6.3 dB  |
| Peaking | 3724 Hz | 0.65 | -5.9 dB |
| Peaking | 6040 Hz | 1.64 | 6.8 dB  |
| Peaking | 1512 Hz | 2.17 | -2.4 dB |
| Peaking | 1859 Hz | 0.99 | 1.8 dB  |
| Peaking | 3367 Hz | 1.5  | -1.0 dB |
| Peaking | 4565 Hz | 6.11 | 0.9 dB  |
| Peaking | 7849 Hz | 8.77 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 5.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/V-Moda%20Crossfade%20M-100/V-Moda%20Crossfade%20M-100.png)