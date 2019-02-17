# Ultimate Ears UE700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.5; 25 -4.5; 28 -4.5; 31 -4.6; 34 -4.8; 37 -4.9; 41 -5.0; 45 -5.1; 49 -5.3; 54 -5.5; 60 -5.8; 66 -6.1; 72 -6.4; 79 -6.7; 87 -7.0; 96 -7.3; 106 -7.6; 116 -7.8; 128 -8.1; 141 -8.4; 155 -8.6; 170 -8.8; 187 -8.8; 206 -8.8; 227 -8.9; 249 -8.9; 274 -8.7; 302 -8.5; 332 -8.4; 365 -8.0; 402 -7.8; 442 -7.6; 486 -7.4; 535 -7.1; 588 -6.6; 647 -6.4; 712 -6.2; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -6.9; 1261 -7.2; 1387 -7.6; 1526 -8.0; 1678 -8.1; 1846 -7.7; 2031 -7.1; 2234 -6.1; 2457 -4.5; 2703 -2.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -0.9; 5793 -0.6; 6373 -2.1; 7010 -4.7; 7711 -8.6; 8482 -13.6; 9330 -14.7; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.46 | 2.1 dB   |
| Peaking | 196 Hz   | 0.63 | -2.6 dB  |
| Peaking | 3309 Hz  | 2.68 | 5.5 dB   |
| Peaking | 5573 Hz  | 1.54 | 6.2 dB   |
| Peaking | 8895 Hz  | 3.66 | -11.0 dB |
| Peaking | 777 Hz   | 1.96 | 1.0 dB   |
| Peaking | 1733 Hz  | 1.68 | -2.4 dB  |
| Peaking | 2451 Hz  | 1.82 | 0.3 dB   |
| Peaking | 2784 Hz  | 6.89 | 1.7 dB   |
| Peaking | 10809 Hz | 7.7  | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultimate%20Ears%20UE700/Ultimate%20Ears%20UE700.png)