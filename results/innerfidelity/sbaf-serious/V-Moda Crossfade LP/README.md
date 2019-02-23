# V-Moda Crossfade LP
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.4; 25 -5.2; 28 -6.1; 31 -6.9; 34 -7.8; 37 -8.4; 41 -9.1; 45 -9.6; 49 -10.0; 54 -10.2; 60 -10.3; 66 -10.4; 72 -10.9; 79 -11.2; 87 -11.0; 96 -11.5; 106 -11.8; 116 -12.1; 128 -12.3; 141 -12.5; 155 -12.6; 170 -12.3; 187 -12.3; 206 -11.9; 227 -11.0; 249 -9.9; 274 -8.9; 302 -7.2; 332 -5.6; 365 -4.5; 402 -3.8; 442 -3.0; 486 -2.9; 535 -3.2; 588 -3.8; 647 -5.0; 712 -6.2; 783 -6.6; 861 -7.0; 947 -7.1; 1042 -7.1; 1146 -7.4; 1261 -8.0; 1387 -8.8; 1526 -9.2; 1678 -9.5; 1846 -9.5; 2031 -9.8; 2234 -10.6; 2457 -9.9; 2703 -9.4; 2973 -8.6; 3270 -8.7; 3597 -7.6; 3957 -5.1; 4353 -3.6; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade LP GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 57 Hz    | 1.51 | -1.9 dB |
| Peaking | 175 Hz   | 0.56 | -7.1 dB |
| Peaking | 435 Hz   | 1.05 | 7.1 dB  |
| Peaking | 3714 Hz  | 0.41 | -6.4 dB |
| Peaking | 5283 Hz  | 1.33 | 12.6 dB |
| Peaking | 21 Hz    | 2.63 | 3.7 dB  |
| Peaking | 4532 Hz  | 2.68 | 1.4 dB  |
| Peaking | 6232 Hz  | 1.37 | -2.5 dB |
| Peaking | 6428 Hz  | 4.68 | 3.7 dB  |
| Peaking | 12954 Hz | 1.53 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 5.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20LP/V-Moda%20Crossfade%20LP.png)