# Ultimate Ears Reference Remastered
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.8; 25 -1.9; 28 -2.2; 31 -2.4; 34 -2.7; 37 -2.9; 41 -3.2; 45 -3.4; 49 -3.5; 54 -3.8; 60 -4.0; 66 -4.4; 72 -4.7; 79 -5.2; 87 -5.6; 96 -6.1; 106 -6.5; 116 -6.9; 128 -7.3; 141 -7.6; 155 -7.9; 170 -8.1; 187 -8.3; 206 -8.5; 227 -8.6; 249 -8.6; 274 -8.7; 302 -8.7; 332 -8.7; 365 -8.7; 402 -8.7; 442 -8.6; 486 -8.5; 535 -8.4; 588 -8.3; 647 -8.1; 712 -7.8; 783 -7.5; 861 -7.2; 947 -7.1; 1042 -7.3; 1146 -7.9; 1261 -8.9; 1387 -9.5; 1526 -9.4; 1678 -8.3; 1846 -6.8; 2031 -5.2; 2234 -4.0; 2457 -3.2; 2703 -3.0; 2973 -3.0; 3270 -2.8; 3597 -1.3; 3957 -0.5; 4353 -2.2; 4788 -4.9; 5267 -5.1; 5793 -3.6; 6373 -2.7; 7010 -4.5; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.7; 16529 -17.7; 18182 -19.8; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears Reference Remastered GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears Reference Remastered ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.9  | 4.9 dB   |
| Peaking | 2571 Hz  | 4.71 | 2.8 dB   |
| Peaking | 3881 Hz  | 2.53 | 5.8 dB   |
| Peaking | 13798 Hz | 0.75 | 6.3 dB   |
| Peaking | 17499 Hz | 0.81 | -17.2 dB |
| Peaking | 67 Hz    | 1.69 | 1.4 dB   |
| Peaking | 292 Hz   | 0.51 | -2.5 dB  |
| Peaking | 1440 Hz  | 3.81 | -3.3 dB  |
| Peaking | 6446 Hz  | 4    | 5.2 dB   |
| Peaking | 6989 Hz  | 1.62 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.8 dB   |
| Peaking | 125 Hz   | 1.41 | -0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 16000 Hz | 1.41 | -10.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ultimate%20Ears%20Reference%20Remastered/Ultimate%20Ears%20Reference%20Remastered.png)