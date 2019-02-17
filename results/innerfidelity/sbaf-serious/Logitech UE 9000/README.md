# Logitech UE 9000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.3; 28 -7.6; 31 -7.8; 34 -8.0; 37 -8.1; 41 -8.2; 45 -8.3; 49 -8.3; 54 -8.4; 60 -8.4; 66 -8.5; 72 -8.5; 79 -8.6; 87 -8.5; 96 -8.6; 106 -8.6; 116 -9.1; 128 -10.1; 141 -9.9; 155 -9.1; 170 -8.2; 187 -8.2; 206 -8.7; 227 -8.1; 249 -7.5; 274 -6.9; 302 -6.6; 332 -6.2; 365 -5.8; 402 -5.5; 442 -5.2; 486 -5.3; 535 -5.2; 588 -4.9; 647 -5.1; 712 -5.6; 783 -5.6; 861 -5.8; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -6.5; 1387 -6.4; 1526 -6.5; 1678 -6.3; 1846 -5.4; 2031 -4.6; 2234 -3.3; 2457 -1.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -2.3; 4788 -3.0; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech UE 9000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 9000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.76 | -1.9 dB |
| Peaking | 137 Hz  | 1.82 | -3.0 dB |
| Peaking | 3111 Hz | 1.62 | 6.5 dB  |
| Peaking | 5822 Hz | 3.27 | 5.5 dB  |
| Peaking | 218 Hz  | 4.73 | -1.5 dB |
| Peaking | 565 Hz  | 0.98 | 1.7 dB  |
| Peaking | 1323 Hz | 1.08 | -1.2 dB |
| Peaking | 2507 Hz | 6.9  | 1.5 dB  |
| Peaking | 8247 Hz | 4.39 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%209000/Logitech%20UE%209000.png)