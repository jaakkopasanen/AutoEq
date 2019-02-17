# V-MODA Crossfade II Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.2; 25 -7.5; 28 -7.9; 31 -8.2; 34 -8.4; 37 -8.6; 41 -8.7; 45 -8.9; 49 -9.1; 54 -9.3; 60 -9.6; 66 -9.9; 72 -10.2; 79 -10.4; 87 -10.8; 96 -11.1; 106 -11.3; 116 -11.5; 128 -11.5; 141 -11.5; 155 -11.4; 170 -11.1; 187 -10.7; 206 -10.1; 227 -9.3; 249 -8.5; 274 -6.8; 302 -5.9; 332 -5.5; 365 -4.7; 402 -4.2; 442 -4.5; 486 -4.6; 535 -4.6; 588 -4.8; 647 -5.1; 712 -5.4; 783 -5.8; 861 -6.1; 947 -6.4; 1042 -6.5; 1146 -6.5; 1261 -6.2; 1387 -5.8; 1526 -5.3; 1678 -5.1; 1846 -4.9; 2031 -4.8; 2234 -4.7; 2457 -5.2; 2703 -5.2; 2973 -6.2; 3270 -6.8; 3597 -8.1; 3957 -7.1; 4353 -3.7; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.9; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA Crossfade II Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA Crossfade II Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 107 Hz  | 0.38 | -3.2 dB |
| Peaking | 193 Hz  | 0.67 | -4.8 dB |
| Peaking | 329 Hz  | 0.65 | 5.0 dB  |
| Peaking | 377 Hz  | 1.68 | 0.9 dB  |
| Peaking | 5540 Hz | 2.72 | 7.0 dB  |
| Peaking | 1087 Hz | 1.49 | -1.8 dB |
| Peaking | 2146 Hz | 0.59 | 2.1 dB  |
| Peaking | 3711 Hz | 2.56 | -4.2 dB |
| Peaking | 4621 Hz | 7.29 | 2.9 dB  |
| Peaking | 9008 Hz | 2.04 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20Crossfade%20II%20Wireless/V-MODA%20Crossfade%20II%20Wireless.png)