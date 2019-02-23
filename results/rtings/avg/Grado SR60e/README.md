# Grado SR60e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.1; 49 -1.8; 54 -2.5; 60 -3.2; 66 -3.8; 72 -4.3; 79 -4.6; 87 -4.9; 96 -5.1; 106 -5.3; 116 -5.5; 128 -5.6; 141 -5.6; 155 -5.5; 170 -5.4; 187 -5.2; 206 -5.0; 227 -4.8; 249 -4.8; 274 -4.7; 302 -4.6; 332 -4.6; 365 -5.2; 402 -5.3; 442 -5.1; 486 -4.9; 535 -4.7; 588 -4.5; 647 -4.3; 712 -4.0; 783 -3.9; 861 -3.7; 947 -3.5; 1042 -3.4; 1146 -3.4; 1261 -3.7; 1387 -4.2; 1526 -5.0; 1678 -6.2; 1846 -9.9; 2031 -12.2; 2234 -11.3; 2457 -9.6; 2703 -8.1; 2973 -6.9; 3270 -6.5; 3597 -8.9; 3957 -10.5; 4353 -6.8; 4788 -4.2; 5267 -6.5; 5793 -7.2; 6373 -9.0; 7010 -10.8; 7711 -12.0; 8482 -14.0; 9330 -14.3; 10263 -11.1; 11289 -7.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.63 | 6.5 dB   |
| Peaking | 2133 Hz  | 2.18 | -10.2 dB |
| Peaking | 3253 Hz  | 0.17 | 5.0 dB   |
| Peaking | 3846 Hz  | 5.43 | -6.7 dB  |
| Peaking | 8551 Hz  | 1.39 | -11.9 dB |
| Peaking | 244 Hz   | 2.98 | 0.8 dB   |
| Peaking | 4768 Hz  | 7.06 | 3.3 dB   |
| Peaking | 4935 Hz  | 2.39 | -1.4 dB  |
| Peaking | 11741 Hz | 4.85 | 1.9 dB   |
| Peaking | 15557 Hz | 0.5  | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR60e/Grado%20SR60e.png)