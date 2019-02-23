# Logitech UE 6000 passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.6; 25 -11.7; 28 -11.8; 31 -11.8; 34 -11.8; 37 -11.7; 41 -11.7; 45 -11.6; 49 -11.5; 54 -11.3; 60 -11.2; 66 -11.1; 72 -11.1; 79 -11.0; 87 -10.9; 96 -11.0; 106 -10.8; 116 -11.0; 128 -11.0; 141 -11.1; 155 -11.0; 170 -9.7; 187 -10.2; 206 -10.3; 227 -9.7; 249 -9.1; 274 -8.3; 302 -7.7; 332 -7.4; 365 -7.0; 402 -6.9; 442 -7.0; 486 -7.4; 535 -7.8; 588 -8.0; 647 -8.6; 712 -9.2; 783 -9.2; 861 -9.4; 947 -9.4; 1042 -9.5; 1146 -9.5; 1261 -9.0; 1387 -8.9; 1526 -8.6; 1678 -7.9; 1846 -7.0; 2031 -5.2; 2234 -3.8; 2457 -2.4; 2703 -1.4; 2973 -0.5; 3270 -0.5; 3597 -1.1; 3957 -2.4; 4353 -5.3; 4788 -3.8; 5267 -2.9; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech UE 6000 passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 6000 passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.4  | -4.3 dB |
| Peaking | 134 Hz  | 1.87 | -1.8 dB |
| Peaking | 514 Hz  | 0.06 | -2.1 dB |
| Peaking | 3062 Hz | 1.79 | 8.3 dB  |
| Peaking | 6048 Hz | 3.19 | 6.6 dB  |
| Peaking | 214 Hz  | 3.67 | -1.4 dB |
| Peaking | 401 Hz  | 1.27 | 2.3 dB  |
| Peaking | 1083 Hz | 0.79 | -1.7 dB |
| Peaking | 2246 Hz | 3.76 | 1.8 dB  |
| Peaking | 7749 Hz | 7.07 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%206000%20passive/Logitech%20UE%206000%20passive.png)