# A Audio Elite Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.0; 25 -9.1; 28 -9.2; 31 -9.3; 34 -9.3; 37 -9.3; 41 -9.3; 45 -9.3; 49 -9.3; 54 -9.2; 60 -9.2; 66 -9.1; 72 -8.9; 79 -8.9; 87 -9.3; 96 -9.4; 106 -9.6; 116 -9.5; 128 -10.1; 141 -10.5; 155 -9.9; 170 -9.0; 187 -9.2; 206 -8.2; 227 -7.0; 249 -6.2; 274 -5.7; 302 -5.3; 332 -5.2; 365 -5.2; 402 -5.6; 442 -5.9; 486 -6.5; 535 -6.8; 588 -6.3; 647 -5.9; 712 -6.5; 783 -7.4; 861 -7.5; 947 -7.3; 1042 -6.9; 1146 -6.7; 1261 -6.2; 1387 -6.0; 1526 -6.1; 1678 -6.1; 1846 -5.5; 2031 -4.5; 2234 -3.5; 2457 -2.8; 2703 -2.4; 2973 -2.6; 3270 -3.3; 3597 -3.9; 3957 -6.0; 4353 -8.0; 4788 -7.3; 5267 -4.0; 5793 -1.3; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`A Audio Elite Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `A Audio Elite Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.4  | -3.6 dB |
| Peaking | 141 Hz  | 1.72 | -3.5 dB |
| Peaking | 2813 Hz | 2.37 | 3.8 dB  |
| Peaking | 4485 Hz | 5.02 | -3.9 dB |
| Peaking | 6137 Hz | 4.15 | 6.0 dB  |
| Peaking | 167 Hz  | 3.99 | 0.6 dB  |
| Peaking | 190 Hz  | 4.21 | -1.7 dB |
| Peaking | 315 Hz  | 1.54 | 1.4 dB  |
| Peaking | 510 Hz  | 5.59 | -0.9 dB |
| Peaking | 909 Hz  | 2.04 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/A%20Audio%20Elite%20Passive/A%20Audio%20Elite%20Passive.png)