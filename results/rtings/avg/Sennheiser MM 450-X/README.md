# Sennheiser MM 450-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.7; 34 -3.0; 37 -4.1; 41 -5.0; 45 -5.7; 49 -6.1; 54 -6.6; 60 -6.9; 66 -7.0; 72 -7.4; 79 -7.9; 87 -8.3; 96 -8.7; 106 -9.1; 116 -9.4; 128 -9.6; 141 -9.6; 155 -9.3; 170 -9.1; 187 -8.9; 206 -8.7; 227 -8.4; 249 -8.2; 274 -8.1; 302 -7.8; 332 -7.3; 365 -6.8; 402 -6.4; 442 -6.0; 486 -5.6; 535 -5.3; 588 -5.2; 647 -5.2; 712 -5.2; 783 -5.5; 861 -5.7; 947 -5.6; 1042 -5.6; 1146 -5.8; 1261 -6.3; 1387 -7.0; 1526 -7.7; 1678 -8.6; 1846 -10.1; 2031 -10.6; 2234 -11.7; 2457 -10.8; 2703 -9.1; 2973 -7.8; 3270 -5.7; 3597 -2.5; 3957 -0.6; 4353 -3.3; 4788 -3.4; 5267 -2.9; 5793 -2.9; 6373 -3.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 450-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 450-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.41 | 6.8 dB  |
| Peaking | 132 Hz  | 0.97 | -3.4 dB |
| Peaking | 2250 Hz | 2.51 | -5.8 dB |
| Peaking | 3869 Hz | 4.64 | 6.1 dB  |
| Peaking | 5715 Hz | 2.36 | 3.7 dB  |
| Peaking | 283 Hz  | 1.95 | -0.9 dB |
| Peaking | 596 Hz  | 1.22 | 1.6 dB  |
| Peaking | 1080 Hz | 2.84 | 0.8 dB  |
| Peaking | 1757 Hz | 4.46 | -1.0 dB |
| Peaking | 8503 Hz | 5.03 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20MM%20450-X/Sennheiser%20MM%20450-X.png)