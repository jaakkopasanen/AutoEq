# Corsair HS60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.5; 25 -5.7; 28 -6.1; 31 -6.3; 34 -6.5; 37 -6.7; 41 -6.9; 45 -7.1; 49 -7.2; 54 -7.4; 60 -7.6; 66 -8.0; 72 -8.3; 79 -8.7; 87 -9.1; 96 -9.5; 106 -9.8; 116 -9.9; 128 -9.8; 141 -9.7; 155 -9.4; 170 -8.9; 187 -8.0; 206 -7.0; 227 -5.9; 249 -5.1; 274 -4.0; 302 -3.2; 332 -2.6; 365 -2.2; 402 -2.0; 442 -2.3; 486 -3.0; 535 -3.9; 588 -4.9; 647 -5.3; 712 -5.2; 783 -4.6; 861 -3.6; 947 -2.0; 1042 -2.9; 1146 -2.5; 1261 -2.2; 1387 -2.2; 1526 -2.0; 1678 -2.2; 1846 -2.7; 2031 -3.2; 2234 -3.2; 2457 -3.3; 2703 -3.9; 2973 -4.1; 3270 -3.4; 3597 -1.1; 3957 -0.8; 4353 -4.9; 4788 -7.3; 5267 -5.3; 5793 -4.3; 6373 -0.5; 7010 -2.1; 7711 -5.5; 8482 -11.8; 9330 -11.7; 10263 -8.2; 11289 -8.2; 12418 -9.3; 13660 -7.6; 15026 -4.8; 16529 -4.7; 18182 -4.7; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 83 Hz    | 0.69 | -4.4 dB |
| Peaking | 149 Hz   | 1.48 | -4.3 dB |
| Peaking | 928 Hz   | 0.09 | 2.1 dB  |
| Peaking | 6848 Hz  | 3.35 | 9.9 dB  |
| Peaking | 8538 Hz  | 1.13 | -9.7 dB |
| Peaking | 383 Hz   | 2.64 | 1.9 dB  |
| Peaking | 656 Hz   | 3.12 | -2.9 dB |
| Peaking | 3835 Hz  | 6.66 | 4.6 dB  |
| Peaking | 4714 Hz  | 5.85 | -3.4 dB |
| Peaking | 15771 Hz | 4.76 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20HS60/Corsair%20HS60.png)