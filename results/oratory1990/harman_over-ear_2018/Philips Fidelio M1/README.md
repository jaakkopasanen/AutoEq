# Philips Fidelio M1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.5; 25 -7.5; 28 -7.5; 31 -7.5; 34 -7.5; 37 -7.4; 41 -7.4; 45 -7.3; 49 -7.3; 54 -7.2; 60 -7.0; 66 -7.0; 72 -7.3; 79 -7.8; 87 -8.2; 96 -8.4; 106 -8.3; 116 -8.1; 128 -7.8; 141 -7.3; 155 -6.7; 170 -6.0; 187 -5.2; 206 -4.6; 227 -4.1; 249 -4.0; 274 -3.8; 302 -3.4; 332 -3.2; 365 -3.1; 402 -3.4; 442 -3.4; 486 -3.3; 535 -3.3; 588 -3.2; 647 -3.1; 712 -3.1; 783 -3.1; 861 -3.2; 947 -3.2; 1042 -3.2; 1146 -3.0; 1261 -2.8; 1387 -2.8; 1526 -2.8; 1678 -2.9; 1846 -2.9; 2031 -3.0; 2234 -3.1; 2457 -3.2; 2703 -3.3; 2973 -3.5; 3270 -3.5; 3597 -2.7; 3957 -1.5; 4353 -0.5; 4788 -1.0; 5267 -1.4; 5793 -2.3; 6373 -3.5; 7010 -2.4; 7711 -3.1; 8482 -3.4; 9330 -3.4; 10263 -3.4; 11289 -3.4; 12418 -3.8; 13660 -7.4; 15026 -7.5; 16529 -4.8; 18182 -4.1; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio M1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.4  | -4.0 dB |
| Peaking | 112 Hz   | 1.05 | -4.4 dB |
| Peaking | 291 Hz   | 0.2  | 0.6 dB  |
| Peaking | 4603 Hz  | 2.81 | 2.9 dB  |
| Peaking | 14598 Hz | 2.46 | -5.0 dB |
| Peaking | 3130 Hz  | 6.49 | -0.8 dB |
| Peaking | 11760 Hz | 5.44 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Philips%20Fidelio%20M1/Philips%20Fidelio%20M1.png)