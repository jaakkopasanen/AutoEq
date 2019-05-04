# Noontec Hammo Go
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.1; 54 -1.7; 60 -2.6; 66 -3.3; 72 -3.9; 79 -4.4; 87 -5.1; 96 -5.9; 106 -6.6; 116 -7.2; 128 -7.6; 141 -7.5; 155 -7.6; 170 -8.1; 187 -8.7; 206 -9.1; 227 -9.3; 249 -9.3; 274 -9.0; 302 -8.8; 332 -8.9; 365 -9.0; 402 -8.6; 442 -7.0; 486 -6.2; 535 -5.8; 588 -5.3; 647 -4.6; 712 -5.2; 783 -5.1; 861 -5.2; 947 -5.3; 1042 -4.6; 1146 -3.5; 1261 -2.8; 1387 -2.1; 1526 -1.8; 1678 -1.4; 1846 -1.4; 2031 -1.9; 2234 -2.6; 2457 -3.4; 2703 -3.6; 2973 -4.0; 3270 -5.6; 3597 -9.4; 3957 -7.0; 4353 -4.9; 4788 -8.8; 5267 -9.2; 5793 -9.1; 6373 -5.7; 7010 -7.4; 7711 -13.3; 8482 -14.5; 9330 -9.0; 10263 -6.5; 11289 -8.7; 12418 -8.0; 13660 -6.5; 15026 -6.5; 16529 -10.4; 18182 -14.4; 20000 -6.5
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
| Peaking | 32 Hz    | 0.61 | 6.7 dB  |
| Peaking | 220 Hz   | 0.88 | -3.3 dB |
| Peaking | 1646 Hz  | 1.17 | 5.4 dB  |
| Peaking | 8194 Hz  | 4.5  | -9.1 dB |
| Peaking | 18108 Hz | 1.94 | -8.9 dB |
| Peaking | 375 Hz   | 5.65 | -1.4 dB |
| Peaking | 609 Hz   | 3.33 | 1.7 dB  |
| Peaking | 3667 Hz  | 6.5  | -6.8 dB |
| Peaking | 4485 Hz  | 1.44 | 4.6 dB  |
| Peaking | 5076 Hz  | 3.58 | -7.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Noontec%20Hammo%20Go/Noontec%20Hammo%20Go.png)