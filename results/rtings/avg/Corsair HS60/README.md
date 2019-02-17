# Corsair HS60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.8; 25 -6.0; 28 -6.4; 31 -6.6; 34 -6.8; 37 -7.0; 41 -7.2; 45 -7.4; 49 -7.5; 54 -7.7; 60 -7.9; 66 -8.3; 72 -8.6; 79 -9.0; 87 -9.4; 96 -9.8; 106 -10.1; 116 -10.2; 128 -10.1; 141 -10.0; 155 -9.7; 170 -9.2; 187 -8.3; 206 -7.3; 227 -6.2; 249 -5.4; 274 -4.3; 302 -3.5; 332 -2.9; 365 -2.5; 402 -2.3; 442 -2.6; 486 -3.3; 535 -4.2; 588 -5.2; 647 -5.6; 712 -5.5; 783 -4.9; 861 -3.9; 947 -2.3; 1042 -3.2; 1146 -2.8; 1261 -2.5; 1387 -2.5; 1526 -2.3; 1678 -2.5; 1846 -3.0; 2031 -3.5; 2234 -3.5; 2457 -3.6; 2703 -4.2; 2973 -4.4; 3270 -3.7; 3597 -1.4; 3957 -1.1; 4353 -5.2; 4788 -7.6; 5267 -5.6; 5793 -4.6; 6373 -0.7; 7010 -0.5; 7711 -5.5; 8482 -12.1; 9330 -12.0; 10263 -8.5; 11289 -8.5; 12418 -9.6; 13660 -7.9; 15026 -4.8; 16529 -3.4; 18182 -4.5; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.48 | -4.2 dB |
| Peaking | 134 Hz   | 1.17 | -5.5 dB |
| Peaking | 2769 Hz  | 3.68 | -1.0 dB |
| Peaking | 8944 Hz  | 5.03 | -9.5 dB |
| Peaking | 12384 Hz | 1.87 | -6.5 dB |
| Peaking | 381 Hz   | 2.55 | 2.0 dB  |
| Peaking | 656 Hz   | 3.3  | -2.8 dB |
| Peaking | 3896 Hz  | 4.71 | 5.7 dB  |
| Peaking | 4627 Hz  | 2.37 | -5.3 dB |
| Peaking | 6684 Hz  | 6.15 | 6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20HS60/Corsair%20HS60.png)