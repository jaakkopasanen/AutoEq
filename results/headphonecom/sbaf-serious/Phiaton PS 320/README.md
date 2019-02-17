# Phiaton PS 320
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.5; 25 -3.5; 28 -3.3; 31 -3.2; 34 -3.4; 37 -3.7; 41 -3.8; 45 -3.9; 49 -4.2; 54 -4.2; 60 -3.4; 66 -2.8; 72 -4.2; 79 -5.4; 87 -6.2; 96 -6.8; 106 -7.2; 116 -7.0; 128 -6.8; 141 -6.4; 155 -5.6; 170 -7.4; 187 -8.8; 206 -9.5; 227 -9.6; 249 -10.4; 274 -10.9; 302 -10.5; 332 -10.1; 365 -8.9; 402 -7.6; 442 -7.0; 486 -6.2; 535 -5.0; 588 -4.2; 647 -3.7; 712 -3.9; 783 -4.3; 861 -4.7; 947 -5.6; 1042 -7.2; 1146 -8.1; 1261 -8.4; 1387 -9.2; 1526 -9.9; 1678 -10.4; 1846 -10.6; 2031 -10.8; 2234 -11.0; 2457 -9.5; 2703 -7.5; 2973 -5.8; 3270 -4.9; 3597 -4.3; 3957 -3.6; 4353 -1.8; 4788 -0.5; 5267 -0.5; 5793 -1.3; 6373 -6.7; 7010 -7.1; 7711 -7.1; 8482 -9.0; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.7; 16529 -11.4; 18182 -11.1; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 320 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.93 | 3.5 dB  |
| Peaking | 65 Hz    | 4.7  | 3.0 dB  |
| Peaking | 266 Hz   | 2.22 | -4.8 dB |
| Peaking | 1944 Hz  | 2.05 | -5.2 dB |
| Peaking | 4804 Hz  | 2.66 | 7.0 dB  |
| Peaking | 351 Hz   | 3.55 | -1.6 dB |
| Peaking | 704 Hz   | 1.52 | 3.6 dB  |
| Peaking | 1245 Hz  | 1.99 | -1.8 dB |
| Peaking | 3257 Hz  | 4.82 | 1.5 dB  |
| Peaking | 19794 Hz | 0.4  | -6.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20320/Phiaton%20PS%20320.png)