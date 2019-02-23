# Nocs NS200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.3; 23 -14.0; 25 -13.8; 28 -13.5; 31 -13.3; 34 -13.0; 37 -12.8; 41 -12.5; 45 -12.2; 49 -12.1; 54 -11.9; 60 -11.7; 66 -11.6; 72 -11.6; 79 -11.5; 87 -11.4; 96 -11.3; 106 -11.2; 116 -11.1; 128 -11.0; 141 -11.0; 155 -10.9; 170 -10.7; 187 -10.5; 206 -10.2; 227 -9.9; 249 -9.5; 274 -9.1; 302 -8.6; 332 -8.1; 365 -7.5; 402 -7.0; 442 -6.6; 486 -6.1; 535 -5.5; 588 -5.0; 647 -4.5; 712 -4.0; 783 -3.8; 861 -3.9; 947 -4.1; 1042 -4.5; 1146 -4.9; 1261 -5.6; 1387 -6.2; 1526 -6.9; 1678 -7.5; 1846 -7.9; 2031 -8.2; 2234 -8.4; 2457 -8.3; 2703 -7.5; 2973 -5.4; 3270 -2.5; 3597 -0.5; 3957 -0.9; 4353 -3.1; 4788 -4.8; 5267 -5.9; 5793 -7.4; 6373 -5.7; 7010 -4.1; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.32 | -7.7 dB |
| Peaking | 154 Hz  | 0.45 | -3.9 dB |
| Peaking | 802 Hz  | 0.84 | 3.7 dB  |
| Peaking | 2391 Hz | 1.04 | -3.9 dB |
| Peaking | 3649 Hz | 2.5  | 8.2 dB  |
| Peaking | 4298 Hz | 5.32 | 0.4 dB  |
| Peaking | 5953 Hz | 4.16 | -2.0 dB |
| Peaking | 6786 Hz | 6.96 | 3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS200/Nocs%20NS200.png)