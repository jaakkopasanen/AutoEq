# Sennheiser IE 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.9; 25 -9.0; 28 -9.1; 31 -9.2; 34 -9.2; 37 -9.3; 41 -9.4; 45 -9.4; 49 -9.5; 54 -9.5; 60 -9.6; 66 -9.8; 72 -10.0; 79 -10.1; 87 -10.2; 96 -10.4; 106 -10.5; 116 -10.5; 128 -10.6; 141 -10.6; 155 -10.3; 170 -10.0; 187 -9.5; 206 -9.0; 227 -9.5; 249 -10.5; 274 -10.1; 302 -9.4; 332 -8.8; 365 -8.6; 402 -8.3; 442 -7.9; 486 -7.5; 535 -7.2; 588 -7.1; 647 -7.1; 712 -6.9; 783 -6.7; 861 -6.7; 947 -7.1; 1042 -7.8; 1146 -8.2; 1261 -8.3; 1387 -8.2; 1526 -8.2; 1678 -7.5; 1846 -6.3; 2031 -4.9; 2234 -3.5; 2457 -2.1; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -3.5; 5267 -6.6; 5793 -6.7; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.5; 13660 -12.5; 15026 -15.1; 16529 -13.9; 18182 -10.6; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.36 | -1.9 dB |
| Peaking | 131 Hz   | 0.66 | -2.3 dB |
| Peaking | 386 Hz   | 0.11 | -1.4 dB |
| Peaking | 3342 Hz  | 1.29 | 7.6 dB  |
| Peaking | 15790 Hz | 1.38 | -9.4 dB |
| Peaking | 271 Hz   | 4.27 | -1.5 dB |
| Peaking | 1252 Hz  | 0.55 | 2.5 dB  |
| Peaking | 1400 Hz  | 1.39 | -4.3 dB |
| Peaking | 5555 Hz  | 6.04 | -3.9 dB |
| Peaking | 6548 Hz  | 6.12 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -9.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20IE%20800%20S/Sennheiser%20IE%20800%20S.png)