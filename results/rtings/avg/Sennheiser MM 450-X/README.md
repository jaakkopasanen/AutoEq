# Sennheiser MM 450-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.6; 34 -2.9; 37 -3.9; 41 -4.9; 45 -5.6; 49 -6.0; 54 -6.5; 60 -6.7; 66 -6.8; 72 -7.2; 79 -7.6; 87 -8.1; 96 -8.5; 106 -8.9; 116 -9.2; 128 -9.4; 141 -9.4; 155 -9.2; 170 -8.9; 187 -8.8; 206 -8.6; 227 -8.4; 249 -8.2; 274 -8.0; 302 -7.8; 332 -7.3; 365 -6.9; 402 -6.4; 442 -6.0; 486 -5.7; 535 -5.4; 588 -5.3; 647 -5.3; 712 -5.4; 783 -5.6; 861 -5.8; 947 -5.7; 1042 -5.7; 1146 -6.0; 1261 -6.5; 1387 -7.2; 1526 -8.0; 1678 -8.9; 1846 -10.3; 2031 -11.2; 2234 -12.6; 2457 -11.7; 2703 -9.7; 2973 -8.0; 3270 -5.6; 3597 -2.4; 3957 -0.5; 4353 -2.7; 4788 -3.9; 5267 -3.4; 5793 -2.9; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 450-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 450-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.39 | 6.6 dB  |
| Peaking | 135 Hz  | 0.99 | -3.1 dB |
| Peaking | 2280 Hz | 2.44 | -6.7 dB |
| Peaking | 3909 Hz | 3.63 | 6.6 dB  |
| Peaking | 6116 Hz | 3.19 | 4.1 dB  |
| Peaking | 291 Hz  | 1.33 | -1.6 dB |
| Peaking | 572 Hz  | 0.57 | 1.7 dB  |
| Peaking | 1736 Hz | 3.32 | -1.2 dB |
| Peaking | 8213 Hz | 4.88 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20MM%20450-X/Sennheiser%20MM%20450-X.png)