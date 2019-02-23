# Bowers & Wilkins PX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.4; 25 -6.7; 28 -7.0; 31 -7.2; 34 -7.3; 37 -7.4; 41 -7.4; 45 -7.3; 49 -7.3; 54 -7.3; 60 -7.4; 66 -7.7; 72 -8.0; 79 -8.4; 87 -8.9; 96 -9.4; 106 -9.9; 116 -10.4; 128 -10.6; 141 -10.7; 155 -10.7; 170 -10.6; 187 -10.8; 206 -11.2; 227 -11.8; 249 -12.4; 274 -12.6; 302 -12.4; 332 -11.7; 365 -10.8; 402 -9.8; 442 -8.9; 486 -8.3; 535 -7.5; 588 -6.7; 647 -5.7; 712 -4.7; 783 -3.7; 861 -2.8; 947 -2.4; 1042 -2.6; 1146 -3.4; 1261 -3.8; 1387 -3.8; 1526 -4.0; 1678 -4.6; 1846 -4.9; 2031 -5.7; 2234 -6.0; 2457 -6.0; 2703 -4.0; 2973 -0.6; 3270 -0.5; 3597 -7.5; 3957 -7.5; 4353 -6.6; 4788 -5.0; 5267 -2.1; 5793 -0.9; 6373 -2.6; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.7; 15026 -6.9; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 118 Hz   | 1.15 | -2.7 dB |
| Peaking | 294 Hz   | 0.89 | -6.9 dB |
| Peaking | 926 Hz   | 2.18 | 3.0 dB  |
| Peaking | 986 Hz   | 0.27 | 2.2 dB  |
| Peaking | 5802 Hz  | 4.49 | 5.5 dB  |
| Peaking | 2397 Hz  | 2.95 | -2.9 dB |
| Peaking | 3197 Hz  | 3.13 | 8.6 dB  |
| Peaking | 3714 Hz  | 4.01 | -7.2 dB |
| Peaking | 13972 Hz | 4.74 | -2.7 dB |
| Peaking | 15383 Hz | 2.77 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20PX/Bowers%20&%20Wilkins%20PX.png)