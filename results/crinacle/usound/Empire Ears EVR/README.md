# Empire Ears EVR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.5; 25 -2.8; 28 -3.2; 31 -3.5; 34 -3.8; 37 -4.0; 41 -4.2; 45 -4.5; 49 -4.7; 54 -4.9; 60 -5.3; 66 -5.7; 72 -6.0; 79 -6.4; 87 -6.8; 96 -7.3; 106 -7.7; 116 -8.1; 128 -8.5; 141 -8.8; 155 -9.1; 170 -9.3; 187 -9.5; 206 -9.5; 227 -9.6; 249 -9.6; 274 -9.5; 302 -9.5; 332 -9.4; 365 -9.2; 402 -9.1; 442 -8.9; 486 -8.7; 535 -8.4; 588 -8.2; 647 -7.8; 712 -7.4; 783 -7.0; 861 -6.7; 947 -6.6; 1042 -6.9; 1146 -7.7; 1261 -8.6; 1387 -9.0; 1526 -8.9; 1678 -8.5; 1846 -7.6; 2031 -6.1; 2234 -4.3; 2457 -2.5; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.8; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.6; 7010 -8.1; 7711 -11.7; 8482 -10.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears EVR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears EVR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.23 | 4.4 dB  |
| Peaking | 231 Hz   | 0.47 | -3.5 dB |
| Peaking | 1613 Hz  | 1.68 | -5.6 dB |
| Peaking | 3852 Hz  | 0.56 | 7.5 dB  |
| Peaking | 7831 Hz  | 3.35 | -9.6 dB |
| Peaking | 2187 Hz  | 4.24 | -0.9 dB |
| Peaking | 2696 Hz  | 2.84 | 1.1 dB  |
| Peaking | 4009 Hz  | 3.14 | -1.2 dB |
| Peaking | 5875 Hz  | 6.41 | 2.2 dB  |
| Peaking | 12503 Hz | 1.35 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20EVR/Empire%20Ears%20EVR.png)