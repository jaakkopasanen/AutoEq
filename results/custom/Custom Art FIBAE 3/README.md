# Custom Art FIBAE 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.5; 25 -7.6; 28 -7.8; 31 -7.9; 34 -8.1; 37 -8.2; 41 -8.3; 45 -8.5; 49 -8.6; 54 -8.8; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.4; 96 -10.8; 106 -11.1; 116 -11.4; 128 -11.7; 141 -11.9; 155 -12.1; 170 -12.3; 187 -12.3; 206 -12.2; 227 -12.2; 249 -12.1; 274 -11.9; 302 -11.7; 332 -11.3; 365 -11.0; 402 -10.7; 442 -10.4; 486 -10.0; 535 -9.5; 588 -9.0; 647 -8.5; 712 -8.0; 783 -7.4; 861 -6.9; 947 -6.6; 1042 -6.4; 1146 -6.1; 1261 -5.5; 1387 -4.5; 1526 -3.4; 1678 -2.5; 1846 -2.3; 2031 -2.7; 2234 -4.1; 2457 -6.8; 2703 -8.1; 2973 -6.2; 3270 -2.2; 3597 -0.5; 3957 -1.8; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -12.6; 10263 -12.6; 11289 -6.7; 12418 -6.5; 13660 -14.3; 15026 -24.6; 16529 -23.9; 18182 -14.9; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 223 Hz   | 0.33 | -6.1 dB  |
| Peaking | 4094 Hz  | 0.14 | 3.1 dB   |
| Peaking | 5323 Hz  | 1.9  | 4.4 dB   |
| Peaking | 9597 Hz  | 5.72 | -8.1 dB  |
| Peaking | 15937 Hz | 1.61 | -22.9 dB |
| Peaking | 1948 Hz  | 2.29 | 4.1 dB   |
| Peaking | 2739 Hz  | 1.98 | -6.6 dB  |
| Peaking | 3462 Hz  | 4.14 | 5.5 dB   |
| Peaking | 12550 Hz | 4.15 | 5.8 dB   |
| Peaking | 14562 Hz | 4.79 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -20.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/my_results/Custom%20Art%20FIBAE%203/Custom%20Art%20FIBAE%203.png)