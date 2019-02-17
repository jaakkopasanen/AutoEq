# Bose QuietComfort 25 Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -5.2; 25 -5.9; 28 -6.8; 31 -7.6; 34 -8.3; 37 -9.0; 41 -9.8; 45 -10.5; 49 -11.1; 54 -11.7; 60 -12.3; 66 -12.7; 72 -12.9; 79 -13.0; 87 -12.8; 96 -12.6; 106 -12.6; 116 -12.7; 128 -11.9; 141 -11.9; 155 -13.2; 170 -10.3; 187 -11.3; 206 -11.1; 227 -9.7; 249 -8.8; 274 -7.7; 302 -6.5; 332 -5.7; 365 -5.1; 402 -4.8; 442 -4.6; 486 -4.8; 535 -5.1; 588 -5.2; 647 -5.7; 712 -6.4; 783 -6.8; 861 -7.3; 947 -7.1; 1042 -6.0; 1146 -4.6; 1261 -2.9; 1387 -1.2; 1526 -0.7; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.5; 3597 -1.6; 3957 -1.5; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.7; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.89 | 3.1 dB  |
| Peaking | 72 Hz   | 0.83 | -6.4 dB |
| Peaking | 159 Hz  | 1.7  | -3.7 dB |
| Peaking | 2130 Hz | 0.94 | 6.4 dB  |
| Peaking | 5135 Hz | 1.94 | 5.1 dB  |
| Peaking | 223 Hz  | 3.39 | -1.7 dB |
| Peaking | 423 Hz  | 1.24 | 2.3 dB  |
| Peaking | 903 Hz  | 2.09 | -2.9 dB |
| Peaking | 1417 Hz | 4.36 | 2.2 dB  |
| Peaking | 8470 Hz | 3.79 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -5.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2025%20Passive/Bose%20QuietComfort%2025%20Passive.png)