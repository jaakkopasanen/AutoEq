# Spider Moonlight
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.8; 25 -5.2; 28 -5.8; 31 -6.2; 34 -6.6; 37 -6.9; 41 -7.3; 45 -7.6; 49 -7.9; 54 -8.2; 60 -8.4; 66 -8.8; 72 -9.0; 79 -9.2; 87 -9.8; 96 -9.9; 106 -10.1; 116 -10.6; 128 -11.1; 141 -11.5; 155 -11.8; 170 -11.1; 187 -11.6; 206 -11.3; 227 -10.4; 249 -9.6; 274 -8.0; 302 -6.1; 332 -5.1; 365 -4.9; 402 -5.4; 442 -6.1; 486 -6.6; 535 -6.9; 588 -7.0; 647 -6.6; 712 -5.7; 783 -5.6; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -6.8; 1261 -7.1; 1387 -8.1; 1526 -9.5; 1678 -10.6; 1846 -11.4; 2031 -12.2; 2234 -12.7; 2457 -12.5; 2703 -11.5; 2973 -11.4; 3270 -11.3; 3597 -10.7; 3957 -11.4; 4353 -10.7; 4788 -7.5; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -8.1; 10263 -10.2; 11289 -8.1; 12418 -9.7; 13660 -12.0; 15026 -8.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spider Moonlight GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider Moonlight ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 142 Hz   | 1.05 | -5.5 dB |
| Peaking | 2223 Hz  | 1.79 | -6.0 dB |
| Peaking | 4313 Hz  | 1.74 | -7.8 dB |
| Peaking | 5674 Hz  | 2.26 | 11.3 dB |
| Peaking | 12813 Hz | 1.24 | -4.4 dB |
| Peaking | 20 Hz    | 1.65 | 2.4 dB  |
| Peaking | 61 Hz    | 1.9  | -1.1 dB |
| Peaking | 223 Hz   | 3.44 | -2.0 dB |
| Peaking | 345 Hz   | 2.94 | 3.0 dB  |
| Peaking | 805 Hz   | 3.18 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Spider%20Moonlight/Spider%20Moonlight.png)