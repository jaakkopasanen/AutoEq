# Nuforce NE 600X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.8; 23 -17.7; 25 -17.6; 28 -17.3; 31 -17.1; 34 -16.9; 37 -16.7; 41 -16.5; 45 -16.3; 49 -16.0; 54 -15.8; 60 -15.6; 66 -15.4; 72 -15.3; 79 -15.1; 87 -14.9; 96 -14.8; 106 -14.4; 116 -14.1; 128 -13.8; 141 -13.4; 155 -13.0; 170 -12.6; 187 -12.0; 206 -11.5; 227 -10.8; 249 -10.3; 274 -9.7; 302 -9.0; 332 -8.4; 365 -7.8; 402 -7.2; 442 -6.5; 486 -6.1; 535 -5.6; 588 -4.8; 647 -4.5; 712 -4.3; 783 -3.9; 861 -4.0; 947 -4.3; 1042 -4.7; 1146 -5.0; 1261 -5.5; 1387 -6.2; 1526 -7.0; 1678 -7.7; 1846 -8.1; 2031 -8.5; 2234 -9.1; 2457 -9.5; 2703 -9.8; 2973 -9.1; 3270 -7.6; 3597 -6.0; 3957 -7.2; 4353 -10.6; 4788 -10.8; 5267 -7.6; 5793 -3.1; 6373 -0.5; 7010 -2.1; 7711 -4.3; 8482 -4.6; 9330 -5.2; 10263 -6.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -6.0; 16529 -5.4; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nuforce NE 600X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nuforce NE 600X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.19 | -12.8 dB |
| Peaking | 161 Hz   | 0.74 | -4.0 dB  |
| Peaking | 2418 Hz  | 1.64 | -5.1 dB  |
| Peaking | 4691 Hz  | 4.31 | -6.8 dB  |
| Peaking | 6387 Hz  | 4.69 | 5.7 dB   |
| Peaking | 796 Hz   | 1.99 | 1.7 dB   |
| Peaking | 1665 Hz  | 3.04 | -1.2 dB  |
| Peaking | 2188 Hz  | 4.42 | 0.6 dB   |
| Peaking | 10104 Hz | 6.42 | -2.4 dB  |
| Peaking | 11100 Hz | 3.47 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.5 dB |
| Peaking | 62 Hz    | 1.41 | -7.4 dB  |
| Peaking | 125 Hz   | 1.41 | -7.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 16000 Hz | 1.41 | -1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nuforce%20NE%20600X/Nuforce%20NE%20600X.png)