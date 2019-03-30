# Corsair HS50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.8; 25 -3.1; 28 -3.5; 31 -3.9; 34 -4.2; 37 -4.5; 41 -4.8; 45 -5.1; 49 -5.3; 54 -5.4; 60 -5.5; 66 -5.9; 72 -6.4; 79 -6.8; 87 -7.1; 96 -7.4; 106 -7.7; 116 -7.9; 128 -7.9; 141 -7.8; 155 -7.5; 170 -7.0; 187 -6.3; 206 -5.5; 227 -4.5; 249 -3.8; 274 -3.1; 302 -2.3; 332 -1.6; 365 -1.3; 402 -1.2; 442 -1.6; 486 -2.1; 535 -2.6; 588 -3.2; 647 -3.5; 712 -3.7; 783 -3.8; 861 -3.1; 947 -1.1; 1042 -1.3; 1146 -1.6; 1261 -1.0; 1387 -1.2; 1526 -1.3; 1678 -1.3; 1846 -1.5; 2031 -1.5; 2234 -1.0; 2457 -0.9; 2703 -1.2; 2973 -1.3; 3270 -1.3; 3597 -2.3; 3957 -1.4; 4353 -1.0; 4788 -2.2; 5267 -6.1; 5793 -4.3; 6373 -0.5; 7010 -0.8; 7711 -3.9; 8482 -9.9; 9330 -9.9; 10263 -6.4; 11289 -6.8; 12418 -8.7; 13660 -6.0; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 98 Hz    | 0.78 | -4.3 dB |
| Peaking | 159 Hz   | 1.58 | -3.0 dB |
| Peaking | 1284 Hz  | 0.08 | 1.8 dB  |
| Peaking | 10063 Hz | 1.34 | -6.7 dB |
| Peaking | 19804 Hz | 2.3  | -5.3 dB |
| Peaking | 716 Hz   | 3.04 | -3.2 dB |
| Peaking | 2172 Hz  | 0.19 | 0.5 dB  |
| Peaking | 5492 Hz  | 5.54 | -6.0 dB |
| Peaking | 6718 Hz  | 2.43 | 5.0 dB  |
| Peaking | 8607 Hz  | 5.78 | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20HS50/Corsair%20HS50.png)