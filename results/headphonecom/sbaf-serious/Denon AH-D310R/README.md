# Denon AH-D310R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.5; 25 -2.0; 28 -2.6; 31 -3.1; 34 -3.5; 37 -3.8; 41 -4.2; 45 -4.6; 49 -4.9; 54 -5.2; 60 -5.7; 66 -5.8; 72 -5.6; 79 -5.3; 87 -6.1; 96 -6.7; 106 -6.9; 116 -7.1; 128 -7.3; 141 -7.6; 155 -8.0; 170 -8.9; 187 -9.3; 206 -9.1; 227 -9.1; 249 -8.7; 274 -8.3; 302 -6.8; 332 -6.5; 365 -6.2; 402 -5.4; 442 -5.1; 486 -4.5; 535 -4.4; 588 -3.8; 647 -2.4; 712 -1.4; 783 -3.4; 861 -6.0; 947 -6.5; 1042 -6.5; 1146 -6.7; 1261 -7.1; 1387 -7.0; 1526 -0.7; 1678 -4.3; 1846 -1.3; 2031 -1.8; 2234 -3.0; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.2; 4788 -3.2; 5267 -0.5; 5793 -1.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.6; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D310R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D310R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.13 | 5.3 dB  |
| Peaking | 677 Hz   | 4.11 | 5.0 dB  |
| Peaking | 2968 Hz  | 1.09 | 6.4 dB  |
| Peaking | 5885 Hz  | 3.46 | 4.3 dB  |
| Peaking | 22050 Hz | 2.46 | 3.5 dB  |
| Peaking | 206 Hz   | 1.61 | -3.1 dB |
| Peaking | 457 Hz   | 2.43 | 1.6 dB  |
| Peaking | 1334 Hz  | 3.26 | -3.5 dB |
| Peaking | 1528 Hz  | 7.7  | 5.5 dB  |
| Peaking | 9346 Hz  | 4.75 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D310R/Denon%20AH-D310R.png)