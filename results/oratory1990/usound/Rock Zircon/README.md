# Rock Zircon
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.0; 25 -3.2; 28 -3.5; 31 -3.8; 34 -4.0; 37 -4.2; 41 -4.5; 45 -4.7; 49 -4.9; 54 -5.2; 60 -5.6; 66 -6.0; 72 -6.3; 79 -6.7; 87 -7.1; 96 -7.6; 106 -7.9; 116 -8.2; 128 -8.3; 141 -8.3; 155 -8.0; 170 -6.9; 187 -8.0; 206 -8.3; 227 -7.6; 249 -6.8; 274 -6.0; 302 -5.2; 332 -4.4; 365 -3.7; 402 -3.0; 442 -2.4; 486 -1.8; 535 -1.3; 588 -1.0; 647 -0.7; 712 -0.5; 783 -0.5; 861 -0.7; 947 -1.1; 1042 -1.8; 1146 -2.6; 1261 -3.5; 1387 -4.4; 1526 -5.1; 1678 -5.5; 1846 -5.5; 2031 -5.4; 2234 -5.5; 2457 -6.2; 2703 -6.9; 2973 -7.8; 3270 -7.5; 3597 -6.6; 3957 -5.9; 4353 -6.0; 4788 -7.6; 5267 -11.4; 5793 -15.0; 6373 -13.0; 7010 -12.3; 7711 -13.4; 8482 -10.2; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -6.0; 13660 -10.9; 15026 -13.2; 16529 -13.0; 18182 -11.8; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Zircon GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Zircon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.29 | 3.5 dB  |
| Peaking | 145 Hz   | 0.66 | -3.1 dB |
| Peaking | 662 Hz   | 0.85 | 6.0 dB  |
| Peaking | 6294 Hz  | 2.17 | -8.5 dB |
| Peaking | 16748 Hz | 1.11 | -8.1 dB |
| Peaking | 3012 Hz  | 4.77 | -1.5 dB |
| Peaking | 4236 Hz  | 4.02 | 2.9 dB  |
| Peaking | 7924 Hz  | 5.85 | -5.5 dB |
| Peaking | 9850 Hz  | 0.94 | 6.6 dB  |
| Peaking | 9938 Hz  | 0.41 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Rock%20Zircon/Rock%20Zircon.png)