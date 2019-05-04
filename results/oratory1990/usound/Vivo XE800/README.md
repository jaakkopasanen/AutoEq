# Vivo XE800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.1; 25 -2.1; 28 -2.2; 31 -2.2; 34 -2.2; 37 -2.2; 41 -2.3; 45 -2.3; 49 -2.3; 54 -2.4; 60 -2.5; 66 -2.6; 72 -2.8; 79 -3.0; 87 -3.2; 96 -3.5; 106 -3.7; 116 -3.9; 128 -4.1; 141 -4.3; 155 -4.4; 170 -4.5; 187 -4.5; 206 -4.4; 227 -4.3; 249 -4.9; 274 -4.9; 302 -4.8; 332 -4.7; 365 -4.7; 402 -4.7; 442 -4.7; 486 -4.7; 535 -4.7; 588 -4.7; 647 -4.6; 712 -4.6; 783 -4.6; 861 -4.7; 947 -5.0; 1042 -5.5; 1146 -6.0; 1261 -6.4; 1387 -6.6; 1526 -6.7; 1678 -6.5; 1846 -6.2; 2031 -6.0; 2234 -5.7; 2457 -5.0; 2703 -4.0; 2973 -2.9; 3270 -1.8; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -1.3; 5267 -2.8; 5793 -4.9; 6373 -5.1; 7010 -3.9; 7711 -5.8; 8482 -9.6; 9330 -8.2; 10263 -4.6; 11289 -4.6; 12418 -6.1; 13660 -5.4; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vivo XE800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vivo XE800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.57 | 2.4 dB  |
| Peaking | 62 Hz    | 1.1  | 1.4 dB  |
| Peaking | 1645 Hz  | 1.32 | -2.4 dB |
| Peaking | 3955 Hz  | 1.95 | 4.9 dB  |
| Peaking | 8684 Hz  | 5.16 | -6.0 dB |
| Peaking | 786 Hz   | 4.16 | 0.5 dB  |
| Peaking | 4859 Hz  | 7.1  | 0.9 dB  |
| Peaking | 5931 Hz  | 7.96 | -1.8 dB |
| Peaking | 12048 Hz | 1.57 | 1.0 dB  |
| Peaking | 12851 Hz | 4.85 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Vivo%20XE800/Vivo%20XE800.png)