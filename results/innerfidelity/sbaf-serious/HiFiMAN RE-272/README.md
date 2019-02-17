# HiFiMAN RE-272
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.5; 25 -1.6; 28 -1.7; 31 -1.8; 34 -1.8; 37 -1.9; 41 -2.0; 45 -2.3; 49 -2.5; 54 -2.7; 60 -3.0; 66 -3.3; 72 -3.6; 79 -4.0; 87 -4.5; 96 -5.0; 106 -5.3; 116 -5.5; 128 -5.9; 141 -6.3; 155 -6.5; 170 -6.7; 187 -6.9; 206 -7.1; 227 -7.2; 249 -7.3; 274 -7.3; 302 -7.3; 332 -7.3; 365 -7.4; 402 -7.3; 442 -7.0; 486 -7.0; 535 -6.7; 588 -6.0; 647 -5.6; 712 -5.3; 783 -5.0; 861 -5.3; 947 -5.9; 1042 -6.9; 1146 -7.9; 1261 -9.2; 1387 -10.9; 1526 -12.8; 1678 -14.4; 1846 -15.1; 2031 -13.8; 2234 -11.0; 2457 -7.1; 2703 -3.4; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -2.0; 4353 -4.4; 4788 -3.6; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN RE-272 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-272 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.81 | 4.9 dB   |
| Peaking | 59 Hz   | 1.42 | 2.3 dB   |
| Peaking | 1853 Hz | 2.16 | -10.6 dB |
| Peaking | 3166 Hz | 2.12 | 8.1 dB   |
| Peaking | 5810 Hz | 3.47 | 6.2 dB   |
| Peaking | 330 Hz  | 0.86 | -1.2 dB  |
| Peaking | 808 Hz  | 1.53 | 2.5 dB   |
| Peaking | 1524 Hz | 1.9  | -1.6 dB  |
| Peaking | 1807 Hz | 6.87 | 1.7 dB   |
| Peaking | 9179 Hz | 6.07 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-272/HiFiMAN%20RE-272.png)