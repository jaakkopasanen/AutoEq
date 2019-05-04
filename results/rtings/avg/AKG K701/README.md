# AKG K701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.0; 66 -1.3; 72 -1.6; 79 -2.0; 87 -2.4; 96 -2.9; 106 -3.3; 116 -3.7; 128 -4.2; 141 -4.5; 155 -4.8; 170 -4.9; 187 -5.0; 206 -5.1; 227 -5.1; 249 -5.1; 274 -5.2; 302 -5.3; 332 -5.3; 365 -5.3; 402 -5.3; 442 -5.4; 486 -5.2; 535 -4.7; 588 -3.9; 647 -3.8; 712 -3.4; 783 -3.4; 861 -3.6; 947 -4.0; 1042 -4.5; 1146 -4.9; 1261 -5.2; 1387 -5.8; 1526 -6.3; 1678 -7.6; 1846 -9.4; 2031 -10.6; 2234 -11.8; 2457 -11.4; 2703 -10.2; 2973 -8.7; 3270 -7.5; 3597 -6.8; 3957 -6.6; 4353 -6.4; 4788 -7.4; 5267 -8.2; 5793 -9.3; 6373 -10.6; 7010 -12.0; 7711 -12.8; 8482 -11.7; 9330 -7.3; 10263 -6.7; 11289 -10.5; 12418 -9.5; 13660 -6.5; 15026 -6.5; 16529 -7.8; 18182 -12.9; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.37 | 6.3 dB  |
| Peaking | 811 Hz   | 1    | 3.2 dB  |
| Peaking | 2256 Hz  | 2.48 | -6.0 dB |
| Peaking | 7489 Hz  | 2.39 | -6.5 dB |
| Peaking | 18990 Hz | 1.23 | -7.6 dB |
| Peaking | 4135 Hz  | 2.31 | 2.6 dB  |
| Peaking | 4410 Hz  | 1.15 | -1.4 dB |
| Peaking | 9852 Hz  | 6.15 | 2.7 dB  |
| Peaking | 11685 Hz | 6.48 | -4.2 dB |
| Peaking | 22046 Hz | 1.83 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 1.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K701/AKG%20K701.png)