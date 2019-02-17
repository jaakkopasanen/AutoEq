# V-Moda Crossfade LP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.8; 25 -4.5; 28 -5.5; 31 -6.3; 34 -7.1; 37 -7.8; 41 -8.5; 45 -9.0; 49 -9.3; 54 -9.6; 60 -9.7; 66 -9.8; 72 -10.3; 79 -10.6; 87 -10.4; 96 -10.9; 106 -11.2; 116 -11.5; 128 -11.7; 141 -11.9; 155 -11.9; 170 -11.7; 187 -11.7; 206 -11.3; 227 -10.4; 249 -9.3; 274 -8.3; 302 -6.6; 332 -5.0; 365 -3.9; 402 -3.2; 442 -2.3; 486 -2.3; 535 -2.6; 588 -3.2; 647 -4.4; 712 -5.6; 783 -6.0; 861 -6.3; 947 -6.5; 1042 -6.5; 1146 -6.8; 1261 -7.4; 1387 -8.2; 1526 -8.6; 1678 -8.9; 1846 -8.9; 2031 -9.2; 2234 -9.9; 2457 -9.3; 2703 -8.8; 2973 -8.0; 3270 -8.1; 3597 -6.9; 3957 -4.5; 4353 -3.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.31 | 5.0 dB  |
| Peaking | 224 Hz  | 0.71 | -6.9 dB |
| Peaking | 409 Hz  | 0.57 | 12.8 dB |
| Peaking | 593 Hz  | 0.07 | -5.5 dB |
| Peaking | 5299 Hz | 1.51 | 10.4 dB |
| Peaking | 780 Hz  | 2.47 | -2.2 dB |
| Peaking | 873 Hz  | 1.22 | 1.4 dB  |
| Peaking | 2267 Hz | 6.77 | -1.0 dB |
| Peaking | 6556 Hz | 6.57 | 2.9 dB  |
| Peaking | 7048 Hz | 2.63 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 5.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20LP/V-Moda%20Crossfade%20LP.png)