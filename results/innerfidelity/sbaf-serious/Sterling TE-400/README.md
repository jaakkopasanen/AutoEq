# Sterling TE-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.9; 66 -3.8; 72 -5.6; 79 -7.3; 87 -8.6; 96 -10.0; 106 -10.9; 116 -10.9; 128 -10.9; 141 -10.7; 155 -10.4; 170 -9.9; 187 -9.8; 206 -9.6; 227 -9.5; 249 -9.4; 274 -9.0; 302 -8.4; 332 -8.4; 365 -8.3; 402 -8.2; 442 -8.0; 486 -8.1; 535 -7.9; 588 -6.4; 647 -2.0; 712 -0.5; 783 -0.5; 861 -2.6; 947 -5.2; 1042 -7.2; 1146 -7.7; 1261 -7.1; 1387 -6.3; 1526 -5.1; 1678 -4.1; 1846 -3.0; 2031 -1.7; 2234 -1.5; 2457 -1.7; 2703 -2.7; 2973 -3.5; 3270 -3.4; 3597 -0.9; 3957 -4.0; 4353 -10.3; 4788 -8.7; 5267 -3.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.9; 8482 -8.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sterling TE-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sterling TE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 59 Hz   | 0.24 | 27.5 dB  |
| Peaking | 94 Hz   | 0.28 | -27.4 dB |
| Peaking | 737 Hz  | 3.3  | 8.9 dB   |
| Peaking | 2309 Hz | 1.65 | 5.9 dB   |
| Peaking | 6035 Hz | 5.47 | 6.7 dB   |
| Peaking | 2981 Hz | 3.13 | -0.8 dB  |
| Peaking | 3744 Hz | 4.6  | 7.6 dB   |
| Peaking | 4350 Hz | 3.85 | -7.7 dB  |
| Peaking | 5436 Hz | 9.53 | 3.9 dB   |
| Peaking | 8304 Hz | 8.81 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sterling%20TE-400/Sterling%20TE-400.png)