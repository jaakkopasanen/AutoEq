# Bose QuietComfort 25 Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.7; 25 -8.4; 28 -9.3; 31 -10.1; 34 -10.8; 37 -11.5; 41 -12.3; 45 -13.0; 49 -13.6; 54 -14.2; 60 -14.8; 66 -15.2; 72 -15.4; 79 -15.5; 87 -15.3; 96 -15.1; 106 -15.1; 116 -15.2; 128 -14.4; 141 -14.4; 155 -15.7; 170 -12.8; 187 -13.8; 206 -13.6; 227 -12.2; 249 -11.3; 274 -10.2; 302 -9.0; 332 -8.2; 365 -7.6; 402 -7.3; 442 -7.1; 486 -7.3; 535 -7.6; 588 -7.7; 647 -8.2; 712 -8.9; 783 -9.3; 861 -9.8; 947 -9.6; 1042 -8.5; 1146 -7.1; 1261 -5.4; 1387 -3.7; 1526 -3.2; 1678 -2.8; 1846 -2.7; 2031 -1.8; 2234 -1.0; 2457 -1.0; 2703 -1.2; 2973 -2.6; 3270 -4.0; 3597 -4.1; 3957 -4.0; 4353 -3.4; 4788 -1.1; 5267 -0.5; 5793 -2.4; 6373 -4.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 72 Hz   | 0.65 | -8.4 dB |
| Peaking | 175 Hz  | 1.23 | -4.6 dB |
| Peaking | 895 Hz  | 2.21 | -4.4 dB |
| Peaking | 2151 Hz | 1.03 | 5.5 dB  |
| Peaking | 5240 Hz | 3.77 | 5.6 dB  |
| Peaking | 21 Hz   | 2.19 | 1.6 dB  |
| Peaking | 393 Hz  | 3.79 | 0.9 dB  |
| Peaking | 2687 Hz | 4.06 | 2.1 dB  |
| Peaking | 3058 Hz | 1.51 | -1.4 dB |
| Peaking | 4598 Hz | 2.43 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -7.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2025%20Passive/Bose%20QuietComfort%2025%20Passive.png)