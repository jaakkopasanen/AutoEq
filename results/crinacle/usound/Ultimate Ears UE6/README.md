# Ultimate Ears UE6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.2; 25 -11.2; 28 -11.2; 31 -11.2; 34 -11.1; 37 -11.1; 41 -11.0; 45 -10.9; 49 -10.8; 54 -10.7; 60 -10.6; 66 -10.6; 72 -10.6; 79 -10.6; 87 -10.7; 96 -10.7; 106 -10.6; 116 -10.6; 128 -10.6; 141 -10.5; 155 -10.4; 170 -10.2; 187 -10.0; 206 -9.7; 227 -9.4; 249 -9.1; 274 -8.8; 302 -8.5; 332 -8.2; 365 -7.9; 402 -7.7; 442 -7.4; 486 -7.1; 535 -6.8; 588 -6.5; 647 -6.2; 712 -5.9; 783 -5.5; 861 -5.1; 947 -5.1; 1042 -5.3; 1146 -6.1; 1261 -6.5; 1387 -6.4; 1526 -6.1; 1678 -5.2; 1846 -4.3; 2031 -3.5; 2234 -2.9; 2457 -2.7; 2703 -3.2; 2973 -4.6; 3270 -6.0; 3597 -4.0; 3957 -0.5; 4353 -2.7; 4788 -5.2; 5267 -6.8; 5793 -6.2; 6373 -4.0; 7010 -4.2; 7711 -6.8; 8482 -10.1; 9330 -8.0; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -9.4; 15026 -14.0; 16529 -16.1; 18182 -18.4; 20000 -18.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.21 | -4.5 dB  |
| Peaking | 166 Hz   | 0.85 | -2.3 dB  |
| Peaking | 2289 Hz  | 1.86 | 3.8 dB   |
| Peaking | 4059 Hz  | 5.38 | 5.9 dB   |
| Peaking | 18764 Hz | 0.73 | -13.6 dB |
| Peaking | 859 Hz   | 3.02 | 1.7 dB   |
| Peaking | 6865 Hz  | 3.38 | 7.1 dB   |
| Peaking | 8057 Hz  | 1.26 | -6.6 dB  |
| Peaking | 11887 Hz | 0.88 | 5.9 dB   |
| Peaking | 15185 Hz | 1.73 | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 16000 Hz | 1.41 | -11.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20UE6/Ultimate%20Ears%20UE6.png)