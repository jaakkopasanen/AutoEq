# Empire Ears ESR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.0; 25 -5.3; 28 -5.7; 31 -6.0; 34 -6.3; 37 -6.5; 41 -6.8; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.7; 66 -8.0; 72 -8.4; 79 -8.7; 87 -9.1; 96 -9.5; 106 -9.9; 116 -10.2; 128 -10.4; 141 -10.6; 155 -10.8; 170 -11.0; 187 -11.0; 206 -10.9; 227 -10.7; 249 -10.5; 274 -10.3; 302 -10.0; 332 -9.7; 365 -9.3; 402 -8.9; 442 -8.5; 486 -8.0; 535 -7.5; 588 -6.9; 647 -6.4; 712 -5.7; 783 -5.1; 861 -4.6; 947 -4.3; 1042 -4.4; 1146 -5.1; 1261 -5.8; 1387 -6.1; 1526 -6.0; 1678 -5.5; 1846 -4.8; 2031 -3.9; 2234 -2.9; 2457 -1.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -1.5; 5267 -0.5; 5793 -2.0; 6373 -5.8; 7010 -7.7; 7711 -11.7; 8482 -14.2; 9330 -12.7; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears ESR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears ESR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 188 Hz   | 0.55 | -4.6 dB |
| Peaking | 874 Hz   | 2.29 | 2.6 dB  |
| Peaking | 3181 Hz  | 1.29 | 6.5 dB  |
| Peaking | 5367 Hz  | 3.84 | 5.1 dB  |
| Peaking | 8433 Hz  | 3.09 | -9.2 dB |
| Peaking | 20 Hz    | 1.42 | 2.1 dB  |
| Peaking | 1519 Hz  | 2.27 | -2.2 dB |
| Peaking | 1529 Hz  | 1.2  | 1.2 dB  |
| Peaking | 9517 Hz  | 6.52 | -2.8 dB |
| Peaking | 10464 Hz | 2.73 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20ESR/Empire%20Ears%20ESR.png)