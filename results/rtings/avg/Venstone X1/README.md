# Venstone X1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -10.0; 25 -10.4; 28 -11.0; 31 -11.4; 34 -11.9; 37 -12.2; 41 -12.7; 45 -13.1; 49 -13.4; 54 -13.7; 60 -13.9; 66 -14.1; 72 -14.3; 79 -14.5; 87 -14.6; 96 -14.7; 106 -14.8; 116 -14.7; 128 -14.6; 141 -14.4; 155 -14.1; 170 -13.8; 187 -13.4; 206 -12.9; 227 -12.4; 249 -12.1; 274 -12.0; 302 -11.8; 332 -11.5; 365 -10.9; 402 -10.2; 442 -9.3; 486 -8.2; 535 -7.0; 588 -5.9; 647 -5.0; 712 -4.3; 783 -4.0; 861 -3.5; 947 -2.7; 1042 -2.1; 1146 -1.4; 1261 -0.6; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -2.0; 2703 -2.1; 2973 -1.4; 3270 -1.7; 3597 -2.8; 3957 -4.5; 4353 -5.9; 4788 -9.5; 5267 -13.6; 5793 -11.1; 6373 -4.6; 7010 -4.0; 7711 -6.3; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.7; 18182 -9.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venstone X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venstone X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 56 Hz    | 0.41 | -4.7 dB  |
| Peaking | 264 Hz   | 0.26 | -6.3 dB  |
| Peaking | 919 Hz   | 0.53 | 5.3 dB   |
| Peaking | 2116 Hz  | 0.48 | 4.6 dB   |
| Peaking | 5272 Hz  | 4.83 | -10.4 dB |
| Peaking | 909 Hz   | 6.39 | -0.5 dB  |
| Peaking | 5805 Hz  | 7.3  | -2.4 dB  |
| Peaking | 6615 Hz  | 5.47 | 4.3 dB   |
| Peaking | 8213 Hz  | 4.87 | -2.2 dB  |
| Peaking | 17721 Hz | 1.93 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Venstone%20X1/Venstone%20X1.png)