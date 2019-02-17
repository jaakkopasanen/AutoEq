# Beyerdynamic T50p sn16912
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.1; 45 -1.5; 49 -2.0; 54 -2.6; 60 -3.1; 66 -3.6; 72 -3.8; 79 -3.9; 87 -3.9; 96 -4.3; 106 -3.7; 116 -3.2; 128 -3.5; 141 -3.1; 155 -2.9; 170 -3.3; 187 -5.0; 206 -7.0; 227 -8.5; 249 -9.3; 274 -9.5; 302 -10.5; 332 -11.4; 365 -11.0; 402 -10.5; 442 -10.2; 486 -9.8; 535 -9.3; 588 -8.7; 647 -8.3; 712 -7.4; 783 -6.7; 861 -6.7; 947 -6.5; 1042 -6.4; 1146 -6.1; 1261 -5.9; 1387 -6.1; 1526 -6.3; 1678 -6.2; 1846 -5.5; 2031 -4.3; 2234 -2.4; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p sn16912 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sn16912 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.53 | 6.3 dB  |
| Peaking | 157 Hz  | 1.45 | 5.4 dB  |
| Peaking | 314 Hz  | 0.75 | -5.6 dB |
| Peaking | 4265 Hz | 0.67 | 7.0 dB  |
| Peaking | 8717 Hz | 2.58 | -4.6 dB |
| Peaking | 801 Hz  | 3.91 | 0.8 dB  |
| Peaking | 1786 Hz | 2.43 | -2.0 dB |
| Peaking | 2482 Hz | 2.69 | 2.9 dB  |
| Peaking | 4659 Hz | 0.74 | -1.1 dB |
| Peaking | 6151 Hz | 3.98 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | 4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sn16912/Beyerdynamic%20T50p%20sn16912.png)