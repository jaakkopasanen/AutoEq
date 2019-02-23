# T-Peos H-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.1; 25 -11.8; 28 -11.4; 31 -11.0; 34 -10.6; 37 -10.3; 41 -9.8; 45 -9.5; 49 -9.2; 54 -8.8; 60 -8.5; 66 -8.3; 72 -8.1; 79 -8.0; 87 -7.8; 96 -7.8; 106 -7.5; 116 -7.2; 128 -7.1; 141 -7.0; 155 -6.8; 170 -6.5; 187 -6.3; 206 -6.1; 227 -5.7; 249 -5.5; 274 -5.2; 302 -5.0; 332 -4.7; 365 -4.5; 402 -4.3; 442 -4.1; 486 -4.0; 535 -3.9; 588 -3.7; 647 -3.7; 712 -3.9; 783 -4.0; 861 -4.5; 947 -5.2; 1042 -6.1; 1146 -6.9; 1261 -7.9; 1387 -9.2; 1526 -10.4; 1678 -11.8; 1846 -13.1; 2031 -14.2; 2234 -14.8; 2457 -13.7; 2703 -12.6; 2973 -11.5; 3270 -11.2; 3597 -6.3; 3957 -2.2; 4353 -2.7; 4788 -3.4; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.2; 9330 -12.1; 10263 -15.3; 11289 -13.2; 12418 -9.0; 13660 -6.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos H-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos H-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.58 | -5.7 dB  |
| Peaking | 2292 Hz  | 1.7  | -9.2 dB  |
| Peaking | 4036 Hz  | 6.6  | 5.2 dB   |
| Peaking | 5883 Hz  | 2.14 | 7.4 dB   |
| Peaking | 10359 Hz | 2.84 | -10.1 dB |
| Peaking | 644 Hz   | 0.7  | 3.3 dB   |
| Peaking | 1701 Hz  | 1.45 | -3.3 dB  |
| Peaking | 2350 Hz  | 1.25 | 1.9 dB   |
| Peaking | 3179 Hz  | 6.46 | -3.2 dB  |
| Peaking | 13961 Hz | 4.59 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB   |
| Peaking | 500 Hz   | 1.41 | 2.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20H-100/T-Peos%20H-100.png)