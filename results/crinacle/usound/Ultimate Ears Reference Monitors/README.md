# Ultimate Ears Reference Monitors
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.0; 25 -2.2; 28 -2.6; 31 -2.9; 34 -3.1; 37 -3.3; 41 -3.6; 45 -3.8; 49 -4.0; 54 -4.3; 60 -4.6; 66 -5.0; 72 -5.4; 79 -5.8; 87 -6.3; 96 -6.8; 106 -7.2; 116 -7.6; 128 -8.0; 141 -8.4; 155 -8.7; 170 -9.0; 187 -9.2; 206 -9.4; 227 -9.5; 249 -9.6; 274 -9.6; 302 -9.6; 332 -9.6; 365 -9.6; 402 -9.5; 442 -9.5; 486 -9.3; 535 -9.2; 588 -8.9; 647 -8.5; 712 -8.0; 783 -7.5; 861 -7.0; 947 -6.6; 1042 -6.6; 1146 -7.0; 1261 -7.6; 1387 -8.0; 1526 -7.8; 1678 -7.6; 1846 -7.2; 2031 -6.6; 2234 -5.6; 2457 -4.3; 2703 -3.0; 2973 -2.3; 3270 -2.3; 3597 -2.8; 3957 -2.8; 4353 -2.7; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -11.2; 10263 -11.5; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears Reference Monitors GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears Reference Monitors ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 13 Hz    |  0.18 | 4.7 dB  |
| Peaking | 255 Hz   |  0.39 | -3.5 dB |
| Peaking | 3055 Hz  |  2.75 | 3.8 dB  |
| Peaking | 5557 Hz  |  1.85 | 6.4 dB  |
| Peaking | 9737 Hz  |  4.36 | -7.1 dB |
| Peaking | 997 Hz   |  2.25 | 2.2 dB  |
| Peaking | 1379 Hz  |  1.12 | -1.7 dB |
| Peaking | 2519 Hz  |  4.24 | 1.0 dB  |
| Peaking | 7508 Hz  | 11.9  | -1.2 dB |
| Peaking | 11467 Hz |  7.74 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20Reference%20Monitors/Ultimate%20Ears%20Reference%20Monitors.png)