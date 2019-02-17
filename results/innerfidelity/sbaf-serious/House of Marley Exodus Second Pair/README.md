# House of Marley Exodus Second Pair
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.0; 49 -1.3; 54 -1.8; 60 -2.3; 66 -2.6; 72 -2.5; 79 -3.2; 87 -3.8; 96 -4.5; 106 -4.9; 116 -5.1; 128 -5.4; 141 -5.7; 155 -5.8; 170 -5.7; 187 -5.7; 206 -5.5; 227 -7.0; 249 -6.2; 274 -5.5; 302 -5.5; 332 -5.7; 365 -5.8; 402 -5.5; 442 -5.2; 486 -5.3; 535 -5.0; 588 -4.7; 647 -5.1; 712 -5.8; 783 -6.1; 861 -6.5; 947 -6.6; 1042 -6.3; 1146 -5.5; 1261 -5.2; 1387 -4.7; 1526 -4.6; 1678 -4.2; 1846 -3.5; 2031 -3.1; 2234 -3.0; 2457 -2.9; 2703 -3.5; 2973 -4.4; 3270 -5.0; 3597 -4.8; 3957 -3.4; 4353 -2.6; 4788 -2.9; 5267 -3.1; 5793 -3.2; 6373 -5.7; 7010 -7.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Exodus Second Pair GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Exodus Second Pair ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.56 | 7.3 dB  |
| Peaking | 32 Hz   | 1.81 | -1.4 dB |
| Peaking | 528 Hz  | 2.11 | 1.5 dB  |
| Peaking | 2155 Hz | 1.54 | 3.5 dB  |
| Peaking | 4774 Hz | 2.54 | 3.8 dB  |
| Peaking | 73 Hz   | 5.11 | 0.6 dB  |
| Peaking | 294 Hz  | 7.98 | 0.6 dB  |
| Peaking | 913 Hz  | 6.07 | -0.8 dB |
| Peaking | 5944 Hz | 7.18 | 1.9 dB  |
| Peaking | 6798 Hz | 7.31 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Exodus%20Second%20Pair/House%20of%20Marley%20Exodus%20Second%20Pair.png)