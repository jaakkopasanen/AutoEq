# Noontec Hammo Go
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.3; 54 -1.8; 60 -2.8; 66 -3.5; 72 -4.1; 79 -4.7; 87 -5.4; 96 -6.0; 106 -6.9; 116 -7.4; 128 -7.8; 141 -7.7; 155 -7.8; 170 -8.3; 187 -8.9; 206 -9.3; 227 -9.4; 249 -9.3; 274 -9.0; 302 -8.8; 332 -8.9; 365 -9.0; 402 -8.7; 442 -6.9; 486 -6.2; 535 -5.7; 588 -5.2; 647 -4.4; 712 -5.1; 783 -4.8; 861 -5.2; 947 -5.2; 1042 -4.4; 1146 -3.2; 1261 -2.6; 1387 -1.9; 1526 -1.6; 1678 -1.2; 1846 -1.1; 2031 -1.4; 2234 -1.8; 2457 -2.6; 2703 -3.0; 2973 -3.9; 3270 -6.0; 3597 -9.9; 3957 -7.0; 4353 -5.3; 4788 -8.5; 5267 -8.7; 5793 -9.3; 6373 -6.6; 7010 -7.5; 7711 -12.6; 8482 -14.8; 9330 -10.7; 10263 -6.5; 11289 -7.4; 12418 -7.5; 13660 -6.5; 15026 -6.5; 16529 -10.8; 18182 -14.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Hammo Go GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo Go ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.62 | 6.7 dB  |
| Peaking | 214 Hz   | 0.85 | -3.4 dB |
| Peaking | 1673 Hz  | 1.15 | 5.8 dB  |
| Peaking | 8326 Hz  | 3.98 | -9.0 dB |
| Peaking | 17975 Hz | 2.03 | -9.1 dB |
| Peaking | 374 Hz   | 5.42 | -1.5 dB |
| Peaking | 611 Hz   | 3.35 | 1.7 dB  |
| Peaking | 3634 Hz  | 6.11 | -7.3 dB |
| Peaking | 4474 Hz  | 1.26 | 4.8 dB  |
| Peaking | 5114 Hz  | 2.85 | -6.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Noontec%20Hammo%20Go/Noontec%20Hammo%20Go.png)