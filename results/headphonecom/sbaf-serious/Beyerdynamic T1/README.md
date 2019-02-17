# Beyerdynamic T1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.8; 31 -2.2; 34 -2.6; 37 -2.9; 41 -3.2; 45 -3.5; 49 -3.8; 54 -4.0; 60 -4.1; 66 -3.5; 72 -4.1; 79 -5.1; 87 -5.7; 96 -6.0; 106 -6.4; 116 -6.6; 128 -6.9; 141 -7.3; 155 -7.4; 170 -7.4; 187 -7.4; 206 -7.5; 227 -7.5; 249 -7.6; 274 -7.4; 302 -7.3; 332 -7.1; 365 -6.8; 402 -6.5; 442 -6.4; 486 -6.1; 535 -5.5; 588 -5.5; 647 -5.1; 712 -4.6; 783 -4.2; 861 -4.1; 947 -4.0; 1042 -3.5; 1146 -3.1; 1261 -2.5; 1387 -2.4; 1526 -3.4; 1678 -4.9; 1846 -5.6; 2031 -5.6; 2234 -4.1; 2457 -3.4; 2703 -3.4; 2973 -4.5; 3270 -3.6; 3597 -3.2; 3957 -4.1; 4353 -4.0; 4788 -1.9; 5267 -2.3; 5793 -3.0; 6373 -0.7; 7010 -2.5; 7711 -7.4; 8482 -12.4; 9330 -12.0; 10263 -5.7; 11289 -3.7; 12418 -3.7; 13660 -5.2; 15026 -5.3; 16529 -3.8; 18182 -3.7; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.55 | 4.7 dB   |
| Peaking | 206 Hz   | 0.55 | -4.1 dB  |
| Peaking | 1937 Hz  | 7.14 | -2.2 dB  |
| Peaking | 6631 Hz  | 2.17 | 4.3 dB   |
| Peaking | 8683 Hz  | 3.43 | -11.5 dB |
| Peaking | 67 Hz    | 7.25 | 0.9 dB   |
| Peaking | 454 Hz   | 2.92 | -0.5 dB  |
| Peaking | 1279 Hz  | 3.93 | 1.9 dB   |
| Peaking | 11165 Hz | 5.88 | 2.0 dB   |
| Peaking | 14602 Hz | 3.82 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T1/Beyerdynamic%20T1.png)