# Bose QuietComfort 25
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -6.9; 25 -6.7; 28 -6.4; 31 -6.3; 34 -6.3; 37 -6.4; 41 -6.6; 45 -6.8; 49 -6.9; 54 -7.0; 60 -7.2; 66 -7.3; 72 -7.4; 79 -7.5; 87 -7.6; 96 -7.7; 106 -7.9; 116 -8.1; 128 -8.3; 141 -8.3; 155 -8.3; 170 -8.2; 187 -8.1; 206 -7.8; 227 -7.4; 249 -7.2; 274 -7.0; 302 -6.8; 332 -6.6; 365 -6.4; 402 -6.3; 442 -6.2; 486 -6.0; 535 -5.8; 588 -5.5; 647 -5.2; 712 -4.7; 783 -4.4; 861 -4.2; 947 -4.0; 1042 -4.2; 1146 -5.1; 1261 -6.8; 1387 -8.2; 1526 -8.4; 1678 -9.7; 1846 -10.6; 2031 -10.5; 2234 -9.5; 2457 -7.8; 2703 -5.7; 2973 -4.6; 3270 -7.0; 3597 -9.8; 3957 -9.2; 4353 -6.0; 4788 -1.5; 5267 -0.5; 5793 -6.1; 6373 -12.9; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.7; 13660 -7.2; 15026 -9.0; 16529 -10.9; 18182 -11.2; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 905 Hz  |  1.93 | 3.0 dB   |
| Peaking | 1853 Hz |  2.54 | -4.9 dB  |
| Peaking | 3866 Hz |  5.12 | -5.5 dB  |
| Peaking | 5245 Hz |  2.53 | 8.4 dB   |
| Peaking | 6269 Hz |  6.04 | -10.8 dB |
| Peaking | 137 Hz  |  0.99 | -1.9 dB  |
| Peaking | 1354 Hz | 11.84 | -1.3 dB  |
| Peaking | 2238 Hz |  6.95 | -1.2 dB  |
| Peaking | 2935 Hz |  4.91 | 2.9 dB   |
| Peaking | 3450 Hz |  9.15 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -4.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)