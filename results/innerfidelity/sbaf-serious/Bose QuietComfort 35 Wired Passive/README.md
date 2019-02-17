# Bose QuietComfort 35 Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.3; 28 -3.4; 31 -4.2; 34 -4.8; 37 -5.4; 41 -6.0; 45 -6.4; 49 -6.8; 54 -7.0; 60 -7.1; 66 -7.2; 72 -7.2; 79 -7.1; 87 -7.1; 96 -7.6; 106 -8.8; 116 -9.8; 128 -11.2; 141 -12.0; 155 -11.0; 170 -8.9; 187 -10.3; 206 -9.4; 227 -7.9; 249 -6.7; 274 -5.4; 302 -4.6; 332 -4.2; 365 -4.2; 402 -4.4; 442 -4.7; 486 -5.5; 535 -6.1; 588 -6.6; 647 -7.4; 712 -8.3; 783 -8.7; 861 -8.6; 947 -7.7; 1042 -6.1; 1146 -4.5; 1261 -3.1; 1387 -2.2; 1526 -1.5; 1678 -1.5; 1846 -1.7; 2031 -1.3; 2234 -1.0; 2457 -1.5; 2703 -2.2; 2973 -3.1; 3270 -5.2; 3597 -7.7; 3957 -7.0; 4353 -5.8; 4788 -3.5; 5267 -0.9; 5793 -4.3; 6373 -2.0; 7010 -4.3; 7711 -6.6; 8482 -6.8; 9330 -6.9; 10263 -6.9; 11289 -6.9; 12418 -6.9; 13660 -6.9; 15026 -6.9; 16529 -6.9; 18182 -6.9; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  1.39 | 6.6 dB  |
| Peaking | 145 Hz  |  1.64 | -4.9 dB |
| Peaking | 341 Hz  |  2.45 | 3.5 dB  |
| Peaking | 1955 Hz |  1.46 | 6.3 dB  |
| Peaking | 5453 Hz |  3.58 | 5.1 dB  |
| Peaking | 827 Hz  |  2.97 | -3.1 dB |
| Peaking | 1321 Hz |  4.06 | 2.1 dB  |
| Peaking | 2845 Hz |  4.41 | 2.0 dB  |
| Peaking | 3708 Hz |  4.66 | -3.2 dB |
| Peaking | 6569 Hz | 12.09 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wired%20Passive/Bose%20QuietComfort%2035%20Wired%20Passive.png)