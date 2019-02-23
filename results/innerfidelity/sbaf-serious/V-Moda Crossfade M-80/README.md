# V-Moda Crossfade M-80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.9; 25 -4.3; 28 -4.8; 31 -5.2; 34 -5.5; 37 -5.8; 41 -6.1; 45 -6.4; 49 -6.6; 54 -6.9; 60 -7.3; 66 -7.6; 72 -7.9; 79 -8.2; 87 -8.4; 96 -8.9; 106 -9.1; 116 -9.0; 128 -9.0; 141 -9.3; 155 -9.5; 170 -9.2; 187 -9.1; 206 -8.8; 227 -10.5; 249 -10.3; 274 -9.5; 302 -8.6; 332 -7.6; 365 -6.7; 402 -6.1; 442 -5.7; 486 -5.2; 535 -4.3; 588 -3.3; 647 -3.1; 712 -3.5; 783 -3.8; 861 -4.7; 947 -5.6; 1042 -6.6; 1146 -7.6; 1261 -8.3; 1387 -8.7; 1526 -8.8; 1678 -8.5; 1846 -7.6; 2031 -6.4; 2234 -5.8; 2457 -5.5; 2703 -6.2; 2973 -7.2; 3270 -8.0; 3597 -7.0; 3957 -4.6; 4353 -4.1; 4788 -4.4; 5267 -0.5; 5793 -0.5; 6373 -2.9; 7010 -4.4; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade M-80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade M-80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.82 | 3.7 dB  |
| Peaking | 125 Hz  | 0.7  | -2.8 dB |
| Peaking | 248 Hz  | 3.29 | -2.9 dB |
| Peaking | 631 Hz  | 2.43 | 4.0 dB  |
| Peaking | 5595 Hz | 3.55 | 6.7 dB  |
| Peaking | 842 Hz  | 3.37 | 1.5 dB  |
| Peaking | 1502 Hz | 1.58 | -3.1 dB |
| Peaking | 2353 Hz | 2.03 | 2.1 dB  |
| Peaking | 3305 Hz | 3.06 | -2.5 dB |
| Peaking | 4068 Hz | 7.09 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20M-80/V-Moda%20Crossfade%20M-80.png)