# RHA SA950i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.9; 25 -10.2; 28 -10.6; 31 -10.7; 34 -10.8; 37 -10.9; 41 -10.9; 45 -10.9; 49 -10.8; 54 -10.8; 60 -10.8; 66 -10.7; 72 -10.8; 79 -10.9; 87 -10.9; 96 -10.7; 106 -10.9; 116 -10.9; 128 -11.0; 141 -11.4; 155 -11.7; 170 -11.4; 187 -11.7; 206 -11.6; 227 -11.2; 249 -11.1; 274 -11.1; 302 -11.2; 332 -11.6; 365 -11.8; 402 -11.8; 442 -11.6; 486 -11.6; 535 -11.2; 588 -10.3; 647 -9.5; 712 -8.1; 783 -6.5; 861 -5.1; 947 -4.5; 1042 -4.0; 1146 -5.1; 1261 -7.1; 1387 -9.1; 1526 -9.9; 1678 -9.6; 1846 -8.1; 2031 -6.0; 2234 -4.5; 2457 -2.9; 2703 -1.6; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -6.0; 5793 -2.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA SA950i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA SA950i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 87 Hz   | 0.14 | -4.4 dB |
| Peaking | 587 Hz  | 0.76 | -4.6 dB |
| Peaking | 1009 Hz | 1.05 | 8.4 dB  |
| Peaking | 1531 Hz | 1.6  | -8.3 dB |
| Peaking | 3345 Hz | 0.92 | 6.9 dB  |
| Peaking | 90 Hz   | 4.32 | 0.3 dB  |
| Peaking | 4586 Hz | 6.84 | 2.6 dB  |
| Peaking | 5317 Hz | 4.72 | -5.6 dB |
| Peaking | 6205 Hz | 3.32 | 6.7 dB  |
| Peaking | 7430 Hz | 1.52 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -4.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20SA950i/RHA%20SA950i.png)