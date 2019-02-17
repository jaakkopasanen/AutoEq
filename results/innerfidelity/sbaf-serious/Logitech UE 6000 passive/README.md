# Logitech UE 6000 passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.6; 25 -8.7; 28 -8.8; 31 -8.8; 34 -8.8; 37 -8.7; 41 -8.7; 45 -8.6; 49 -8.5; 54 -8.4; 60 -8.2; 66 -8.1; 72 -8.1; 79 -8.0; 87 -7.9; 96 -8.0; 106 -7.8; 116 -8.1; 128 -8.0; 141 -8.1; 155 -8.0; 170 -6.7; 187 -7.2; 206 -7.3; 227 -6.8; 249 -6.1; 274 -5.3; 302 -4.7; 332 -4.4; 365 -4.0; 402 -3.9; 442 -4.0; 486 -4.4; 535 -4.8; 588 -5.0; 647 -5.6; 712 -6.2; 783 -6.2; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.5; 1261 -6.0; 1387 -5.9; 1526 -5.6; 1678 -4.9; 1846 -4.0; 2031 -2.2; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech UE 6000 passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 6000 passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.66 | -2.2 dB |
| Peaking | 406 Hz   | 0.75 | 6.1 dB  |
| Peaking | 1029 Hz  | 0.11 | -4.1 dB |
| Peaking | 2844 Hz  | 0.81 | 9.7 dB  |
| Peaking | 5723 Hz  | 2.24 | 5.7 dB  |
| Peaking | 1753 Hz  | 2.33 | -1.7 dB |
| Peaking | 2268 Hz  | 1.36 | 2.1 dB  |
| Peaking | 2787 Hz  | 3.09 | -1.9 dB |
| Peaking | 7851 Hz  | 5.43 | -1.3 dB |
| Peaking | 12062 Hz | 0.52 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%206000%20passive/Logitech%20UE%206000%20passive.png)